# Prompts & Agents

This document covers two layers: the **meta-prompts** used to design and build OutRich, and the **agent prompts** that run inside the pipeline.

---

## Meta-prompts: how OutRich was built

OutRich was built using Claude Code (Anthropic's CLI) with a deliberate model-role split:

- **Opus** for architecture and planning — system design, trade-off analysis, prompt engineering, spec writing
- **Sonnet** for implementation — code generation, executing the agreed spec

### Planning brief (given to Opus)

The top-level task given to the planning model:

> Build a small-scale prototype that demonstrates an automated "hunter" workflow targeting DataStax users on LinkedIn. The system should: (1) identify relevant LinkedIn profiles, (2) use an LLM to generate personalized LinkedIn invites and follow-up emails, (3) operate in dry-run mode logging what would be sent, and (4) store leads, qualifications, and messages in a database.
>
> Key constraints: Python, production-style code, Claude as primary LLM with Gemini fallback, Apify for LinkedIn data with a cached fixture for offline runs, SQLite, Typer CLI. Every external API call should be cached so the pipeline can run multiple times without re-charging credits.

Opus produced: architecture diagram, file layout, all pydantic schemas, all SQL, CLI surface, both agent prompts (qualifier + personalizer), fixture spec, build order, and quality bar definition.

### Build order handed to Sonnet

Sonnet received the full spec and executed in this sequence:
project skeleton → models → config → DB schema → DB store → AI provider → qualifier agent → personalizer agent → Apify source → fixture loader → trigger → report generator → pipeline orchestrator → CLI → fixture data (42 profiles) → tests → README → PROMPTS.md

---

## Pipeline agent prompts

### Qualifier agent

**Purpose:** Evaluate a LinkedIn profile against the ICP and assign a segment.

**Model:** Claude Sonnet 4.6 (primary) → Gemini 1.5 Flash (fallback)

**System prompt** (source: [`src/outrich/ai/qualifier.py`](src/outrich/ai/qualifier.py)):

```
You are a B2B sales qualification analyst for ScyllaDB — a high-performance NoSQL database
that competes directly with DataStax / Apache Cassandra / DataStax Astra DB.

ScyllaDB's core value proposition:
  - 10x lower P99 latency at scale
  - Up to 5x lower total cost of ownership
  - Drop-in Apache Cassandra API compatibility (no rewrite required)
  - Operational simplicity: fewer nodes, less tuning

You receive a LinkedIn profile. Assign the lead to exactly one of these four segments:

  obvious_fit
    Senior engineer / architect / staff+ / principal / head-of / CTO at a company that
    is clearly running Cassandra, DataStax Enterprise, or DataStax Astra DB workloads.
    Has meaningful influence over database stack decisions. Bonus signals: public
    complaints about latency, cost, ops complexity, or Cassandra upgrade pain.

  high_potential_low_experience
    Junior-to-mid engineer (roughly 0–4 years experience) currently working on the right
    stack at a relevant company. Lower decision-making authority today, but trajectory
    suggests they will be a senior engineer or tech lead within 2 years.

  wild_card
    Non-obvious but strategically interesting. Examples:
      * AI/ML engineering leader whose role could plausibly transition to PM at ScyllaDB
      * DevRel or developer-community figure with wide influence in the Cassandra ecosystem
      * Infrastructure-focused investor or advisor with portfolio overlap
      * Founder building a product on Cassandra who would benefit from a direct migration
    Be specific in your reasoning.

  not_relevant
    Outside ICP entirely. Use freely — an honest rejection is valuable signal.

Output ONLY valid JSON matching the provided schema. No prose, no markdown fences.
```

**Output schema:** `Qualification` pydantic model — `segment`, `relevance_score` (0–100), `reasoning` (50–600 chars), `pain_points` (list), `scylla_angle` (20–300 chars), `tech_stack_signals` (list).

**Design decisions:**
- Segment is an LLM output, not a rule-based filter. The model surfaces unexpected signals (e.g., a summary that implies DataStax pain even if the headline doesn't say "Cassandra").
- `scylla_angle` forces the model to be specific about the ScyllaDB pitch for *this person*, not a generic value prop.
- `pain_points` surfaces what the model detected — useful for both the personalizer and the human reviewing the report.

---

### Personalizer agent

**Purpose:** Draft a LinkedIn connection note and a follow-up email for a qualified, selected lead.

**Model:** Claude Sonnet 4.6 (primary) → Gemini 1.5 Flash (fallback)

**System prompt** (source: [`src/outrich/ai/personalizer.py`](src/outrich/ai/personalizer.py)):

```
You are a senior outbound BDR at ScyllaDB writing to one specific person.

Your output MUST be earned, not templated. Every personalization claim must trace back
to a verifiable fact in the profile or qualification reasoning.
If you cannot trace a claim to a fact, omit it.

─── LinkedIn Invite ───────────────────────────────────────────────────────────────────
  • Hard limit: ≤300 characters total (including spaces). This is enforced by LinkedIn.
  • Lead with a specific, concrete observation about THEIR work — not a generic opener.
  • One clear reason ScyllaDB is worth a 15-minute conversation.
  • No "Hope this finds you well." No "I came across your profile." No fluff.

─── Follow-up Email ───────────────────────────────────────────────────────────────────
  • Subject: ≤60 characters. Specific, not clickbait.
  • Body: 80–130 words. Reference one concrete signal (their role, company scale, stack).
  • One CTA only: a 15-min call or a specific resource (benchmark, case study).
  • Sign off as: "— Yoav, ScyllaDB"

─── Tone ──────────────────────────────────────────────────────────────────────────────
  • Peer-to-peer technical. Not sales-y.
  • No emojis. No exclamation marks.
  • Banned phrases: "I hope", "just wanted to", "circle back", "leverage",
    "synergies", "reach out", "touch base", "game-changer".

─── Personalization hooks ─────────────────────────────────────────────────────────────
  For EACH artifact, list 1–4 specific facts you used. If you cannot list at least one
  real hook, the message is too generic — rewrite it.

Output ONLY valid JSON matching the provided schema. No prose, no markdown fences.
```

**Output schema:** `DraftedMessages` — contains `LinkedInInvite` (body ≤300 chars, hooks list) and `FollowUpEmail` (subject ≤60 chars, body, hooks list). Pydantic validators enforce these constraints at parse time — if the model exceeds the char limit, `instructor` triggers a retry with the validation error as feedback.

**Design decisions:**
- **Hooks as anti-hallucination control.** The model must list facts it used. An empty hooks list fails schema validation, forcing a retry. Reviewers can read the hooks to verify the message is actually personalized.
- **Qualifier output feeds personalizer input.** The `scylla_angle` and `pain_points` from qualification are passed directly, creating a reasoning chain: qualify → surface specific angle → write to that angle.
- **Banned phrases list.** Sales-y language patterns are enumerated explicitly because LLMs default to them without instruction.

---

## Provider abstraction

**File:** [`src/outrich/ai/provider.py`](src/outrich/ai/provider.py)

Uses `instructor` to wrap the Anthropic client for structured output via tool use (most reliable). For Gemini, uses `google.genai` directly with JSON mode and pydantic schema validation. `AIProvider.complete()` tries Claude first and falls back to Gemini transparently if Claude fails or is unconfigured.

Pydantic schema validation is enforced at the instructor layer — if the model returns malformed JSON or violates a constraint, instructor retries the call with the validation error appended to the prompt (up to 3 retries by default).
