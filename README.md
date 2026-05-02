# OutRich

AI-powered B2B outreach pipeline. Define your ICP and a target competitor's user base — OutRich handles lead discovery, AI qualification, and personalized message drafting at scale, with a full audit trail in a local database.

**Want to see output without running anything?** A complete sample run against real DataStax LinkedIn profiles is committed to this repo — 19 real profiles discovered, qualified, 3 selected, 6 messages drafted. Names are anonymized to first name + last initial to protect privacy:
**[Full report →](data/sample_run/report.md)** &nbsp;|&nbsp; **[Results CSV →](data/sample_run/results.csv)** &nbsp;|&nbsp; **[SQLite DB →](data/sample_run/outrich.db)**

> **Why 3 selected, not 10?** The Apify free tier returns 25 profiles per run. LinkedIn surfaces senior leadership first — this batch was mostly VPs of Sales, marketing, and legal, with 2 engineers and 1 former VP of Product. The pipeline correctly identified them (`not_relevant` for sales/legal, `obvious_fit` for the engineers) and selected from what qualified. A paid Apify run returning 100–200 profiles would fill all quota slots.

## Viewing the results (no setup required)

All output from a completed pipeline run is committed to this repo. No API keys, no Python, no install.

**To see each candidate and the message drafted for them:**

- **[`data/sample_run/report.md`](data/sample_run/report.md)** — The primary human-readable output. Opens directly on GitHub. For each of the 3 selected leads you'll see: full profile, AI qualifier reasoning, ScyllaDB angle, pain points, the LinkedIn connection note (with character count), and the follow-up email — including the personalization hooks the AI used, as an anti-hallucination audit trail. Rejected leads are included at the bottom with the AI's reasoning.

- **[`data/sample_run/results.csv`](data/sample_run/results.csv)** — Flat table covering all 19 leads. Each row is one candidate. For the 3 selected leads, `linkedin_invite`, `email_subject`, and `email_body` are populated. The `selected` column is `yes`/`no`. Open in Excel, Google Sheets, or any CSV viewer.

- **[`data/sample_run/outrich.db`](data/sample_run/outrich.db)** — The SQLite source-of-truth database. Query it with any SQLite viewer (e.g., [DB Browser for SQLite](https://sqlitebrowser.org/), TablePlus, or `sqlite3` in the terminal). Tables: `leads`, `qualifications`, `messages`, `send_log`.

**Quick orientation:**
- Want the narrative, with reasoning and messages formatted per person? → `report.md`
- Want to sort, filter, or export to a spreadsheet? → `results.csv`
- Want to query raw pipeline data? → `outrich.db`

## How it works

```
Discover → Qualify → Select → Personalize → Trigger → Report
 Apify     Claude    6/3/1    Claude        Dry-run    Markdown
 LinkedIn  (LLM)    Quota    (LLM)         + DB log   + SQLite
```

**Five-stage pipeline, each backed by the DB — composable and resumable:**

1. **Discover** — Pull LinkedIn profiles via Apify (live) or a committed fixture (offline). Raw profiles are saved immediately; reruns skip already-discovered leads.
2. **Qualify** — LLM evaluates each profile against your ICP, assigns a segment and a 0–100 score, identifies pain points, and writes a tailored ScyllaDB angle. Already-qualified leads are skipped on reruns.
3. **Select** — Quota-based selection: top 6 `obvious_fit` + top 3 `high_potential_low_experience` + top 1 `wild_card`.
4. **Personalize** — LLM drafts a LinkedIn connection note (≤300 chars, enforced by schema) and a follow-up email per selected lead. Every message includes a list of personalization hooks — the specific facts used, as an anti-hallucination control.
5. **Trigger** — Dry-run by default: logs every "send" to the console and the DB. Real send adapters are intentionally unimplemented; the interface is wired for a production integration.

## Segmentation rationale

Most outreach tools blast the entire ICP. OutRich segments deliberately:

| Segment | Quota | Why |
|---|---|---|
| `obvious_fit` | 6 | Proven decision-makers at confirmed Cassandra/DataStax shops — highest close probability |
| `high_potential_low_experience` | 3 | Junior engineers on the right stack; future champions who grow into authority |
| `wild_card` | 1 | Non-obvious but strategically interesting: AI leaders who could become PMs, DevRel influencers, infrastructure investors |

The AI assigns the segment — it's not hardcoded. The qualifier's reasoning is stored and surfaced in the report.

## Quickstart

### Prerequisites

- Python 3.11+
- At least one of `ANTHROPIC_API_KEY` or `GEMINI_API_KEY`

### Install

```bash
git clone https://github.com/Yoavsela33/OutRich.git
cd OutRich
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
# Fill in your API keys in .env
```

### Run offline (no Apify needed)

Uses the committed fixture of 42 AI-generated synthetic DataStax profiles (fictional people, not real employees — designed to simulate a real Apify pull for pipeline demonstration):

```bash
make run-fixture
# or:
outrich run --source fixture
```

### Run live (pulls fresh LinkedIn profiles via Apify)

```bash
# Requires APIFY_TOKEN in .env
make run-live
# or:
outrich run --source apify
```

Uses the `harvestapi/linkedin-company-employees` actor, querying DataStax's LinkedIn company page directly. Apify responses are cached to `data/cache/apify_discover.json` — subsequent runs use cached data automatically. Force a fresh pull with `--no-cache`.

> **Note:** The Apify free tier caps at 25 profiles per run. LinkedIn surfaces senior leadership first, so a free-tier run will qualify mostly executives and sales roles. Upgrade to a paid plan (or run multiple searches) to surface enough individual contributors to fill all quota slots.

### Individual stages

```bash
outrich discover --source fixture   # populate DB with leads
outrich qualify                     # AI qualification (skips already-qualified)
outrich select                      # print selected lead IDs (6/3/1 quota)
outrich personalize                 # draft messages for selected leads
outrich trigger                     # log all messages (dry-run)
outrich report                      # generate data/sample_run/report.md
outrich status                      # print pipeline stats table
```

### Run tests

```bash
make test
# or: pytest tests/ -v
```

## Configuration

All settings via `.env` (see `.env.example`):

| Variable | Required | Default | Purpose |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | one of these | — | Claude (primary LLM) |
| `GEMINI_API_KEY` | one of these | — | Gemini (fallback LLM) |
| `APIFY_TOKEN` | for `--source apify` | — | LinkedIn profile discovery |
| `CLAUDE_MODEL` | optional | `claude-sonnet-4-6` | Override Claude model |
| `GEMINI_MODEL` | optional | `gemini-2.0-flash` | Override Gemini model |

## Caching and idempotency

Every external API call is cached:

| Source | Cache location |
|---|---|
| Apify discovery | `data/cache/apify_discover.json` |
| LLM qualification | `qualifications` table (skips if row exists) |
| LLM personalization | `messages` table (skips if row exists) |

Re-running the pipeline never re-charges API credits unless you pass `--no-cache`.

## Retargeting

OutRich is not DataStax-specific. To target a different competitor:

1. Update `ICP` in `src/outrich/config.py`
2. Update the Apify search keywords in `src/outrich/sources/apify_linkedin.py`
3. Update the qualifier and personalizer system prompts in `src/outrich/ai/`
4. Replace or extend `data/fixtures/leads.json`

## Project layout

```
src/outrich/
├── cli.py              Typer CLI — all subcommands
├── config.py           Settings, ICP definition, segment quotas
├── models.py           Pydantic schemas (enforces 300-char invite, non-empty hooks, etc.)
├── pipeline.py         Stage orchestration
├── ai/
│   ├── provider.py     Claude→Gemini fallback abstraction (instructor)
│   ├── qualifier.py    Qualification agent + prompt
│   └── personalizer.py Personalization agent + prompt
├── db/
│   ├── schema.sql      SQLite schema
│   └── store.py        All DB reads and writes
├── sources/
│   ├── apify_linkedin.py  Live Apify discovery (with cache)
│   └── fixture.py         Offline fixture loader
├── trigger/
│   └── dry_run.py      Logs messages to console + send_log table
└── report/
    └── markdown.py     Generates report.md from DB
```
