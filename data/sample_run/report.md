# OutRich Pipeline Run — 2026-05-02 08:10 UTC

## Summary

| Metric | Count |
|--------|-------|
| Leads discovered | 42 |
| Leads qualified | 42 |
| &nbsp;&nbsp;↳ obvious_fit | 12 |
| &nbsp;&nbsp;↳ high_potential_low_experience | 8 |
| &nbsp;&nbsp;↳ wild_card | 6 |
| &nbsp;&nbsp;↳ not_relevant | 16 |
| Leads selected for outreach | 10 |
| Messages drafted | 20 |
| Messages triggered (dry-run) | 20 |

## Segmentation strategy

Leads are selected by a quota system that reflects deliberate GTM thinking:

- **6 obvious_fit** — senior technical DataStax employees: engineers, architects, and engineering leaders working directly on Cassandra, DSE, or Astra DB. Highest value as recruits, ecosystem connectors, or converted advocates.
- **3 high_potential_low_experience** — junior DataStax engineers on the right stack. Limited authority today, but they grow into senior roles and carry deep institutional knowledge of the competitive stack.
- **1 wild_card** — non-obvious but strategically interesting DataStax employees: Developer Advocates with Cassandra community reach, Technical PMs who know the product deeply, Principal Evangelists.

The qualifier AI assigns each lead to a segment and scores them 0–100. Selection then picks the top-N per quota.

## Obvious fit (6/6)

### Elena Marchetti
**Principal Engineer, Cassandra Core** at **DataStax** · Santa Clara, CA
_Principal Engineer, Cassandra Core · DataStax_

**Score:** 99/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Principal Engineer at DataStax, 8 years in Cassandra Core, leading storage engine modernization on compaction and write-path latency. 400+ OSS commits, Cassandra Summit 2023 speaker on high-concurrency write-path limits. SSTable, LSM Trees, compaction skills align precisely with ScyllaDB's core advantages. Strong influence, OSS visibility, candid about Cassandra's rough edges — textbook recruit and peer engagement target.

**ScyllaDB angle:** Peer outreach on storage engine design: ScyllaDB's shard-per-core model and compaction solve the exact latency and compaction gaps she's tackling. Her candor about Cassandra's limits is a ready-made entry point.

**Pain points identified:**

- Compaction inefficiency and latency gaps in Cassandra's storage engine
- High-concurrency write-path bottlenecks (Cassandra Summit 2023 talk)
- Storage engine modernization complexity within legacy Cassandra architecture
- P99 latency instability under production workloads

**LinkedIn invite** *(dry-run)*

> Elena — 8 years on Cassandra Core and a Summit talk on write-path limits under concurrency: you know the compaction and P99 problems better than almost anyone. Worth 15 min to compare notes on how ScyllaDB's shard-per-core model approaches the same constraints?

*Hooks used: Principal Engineer, Cassandra Core at DataStax, 8 years at DataStax on Cassandra Core, Cassandra Summit 2023 speaker on high-concurrency write-path limits, Leading storage engine modernization focused on compaction and latency gaps*
*Characters: 261/300*

**Follow-up email** *(dry-run)*

**Subject:** Cassandra compaction gaps vs. ScyllaDB's storage model

Elena,

You presented at Cassandra Summit 2023 on write-path limits under high concurrency — the exact problem ScyllaDB's shard-per-core architecture was designed to eliminate. With 8 years leading Cassandra Core work and a current focus on storage engine modernization, you have sharper context on these trade-offs than most.

I'm not here to sell you. I'd like a 15-minute technical conversation — compaction scheduling, P99 under concurrent writes, and where the LSM design decisions diverge between the two engines.

Worth a call?

— Yoav, ScyllaDB

*Hooks used: Principal Engineer, Cassandra Core at DataStax, 8 years at DataStax on Cassandra Core, Cassandra Summit 2023 talk on high-concurrency write-path limits, Current focus on storage engine modernization targeting compaction and latency gaps*

---

### Mei Zhang
**VP Engineering, Astra DB** at **DataStax** · San Francisco, CA
_VP Engineering, Astra DB · DataStax_

**Score:** 98/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** VP Engineering for Astra DB, leading 80+ engineers on DataStax's core managed Cassandra product. Google Bigtable Staff Engineer background adds deep distributed systems credibility. Explicitly tracks P99 latency, SLA breach rates, and cost per GB — ScyllaDB's primary competitive levers. Her public debate on Cassandra compatibility vs. storage differentiation signals architectural uncertainty at the top of Astra DB engineering.

**ScyllaDB angle:** Engage on P99 latency and cost-per-GB — metrics she already owns. ScyllaDB's 10x latency and 5x TCO story hits her hyperscaler pressure directly. Cassandra API compatibility removes migration risk, sidestepping her storage-layer debate.

**Pain points identified:**

- Hyperscaler competition pressuring Astra DB on price and performance
- Internal debate on Cassandra compatibility vs. storage layer differentiation
- P99 latency and SLA breach rate management at scale
- Cost per GB efficiency on a large managed cloud product

**LinkedIn invite** *(dry-run)*

> Mei — VP Engineering on Astra DB, ex-Bigtable: you know this space cold. The Cassandra-compatibility-vs-storage-layer debate is exactly where ScyllaDB's architecture is relevant. Worth 15 min to compare P99 and cost-per-GB numbers directly? — Yoav

*Hooks used: VP Engineering for Astra DB at DataStax, Ex-Google Bigtable Staff Engineer background, Explicitly tracks P99 latency and cost per GB, Internal debate on Cassandra compatibility vs. storage layer differentiation*
*Characters: 247/300*

**Follow-up email** *(dry-run)*

**Subject:** Astra DB P99 and cost-per-GB vs. ScyllaDB

Mei,

You run engineering for Astra DB and you're already tracking the metrics that matter most in this comparison: P99 latency distributions, SLA breach rates, and cost per GB under hyperscaler pressure.

The storage-layer debate you're navigating internally is one ScyllaDB has a direct answer to — a C++-native, shard-per-core architecture that keeps full Cassandra API compatibility while materially moving those numbers.

I'd rather show you a benchmark head-to-head than describe it. Can we put 15 minutes on the calendar to walk through the data?

— Yoav, ScyllaDB

*Hooks used: VP Engineering for Astra DB overseeing 80+ engineers on DataStax's core managed Cassandra product, Explicitly tracks P99 latency distributions, SLA breach rates, and cost per GB, Internal architectural debate on Cassandra compatibility vs. storage layer differentiation, Hyperscaler competition cited as direct pressure on Astra DB*

---

### Kwame Asante
**Staff Engineer, Astra DB** at **DataStax** · Austin, TX
_Staff Engineer, Astra DB · DataStax_

**Score:** 97/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Staff Engineer, 7 years at DataStax, last 4 focused entirely on Astra DB's multi-region replication layer. Personally designed the cross-region consistency protocol at 2M+ writes/sec — deep architectural authority. Critically, he self-identifies pain with Astra DB's cost-per-query model at scale and the gap between promises and production reality. These are exactly the pain points ScyllaDB's TCO and performance story addresses. Textbook senior technical target with insider knowledge and latent dissatisfaction.

**ScyllaDB angle:** Lead with ScyllaDB's 5x TCO advantage and predictable pricing — targeting his stated cost-per-query frustration. Reinforce with P99 latency benchmarks at his write scale (2M+ writes/sec). Cassandra API compatibility eliminates rewrite risk and is a natural conversation opener.

**Pain points identified:**

- Cost-per-query model painful at scale (self-identified)
- Gap between Astra DB production promises and real-world delivery
- Multi-region replication complexity at 2M+ writes/sec

**LinkedIn invite** *(dry-run)*

> Kwame — seven years on Astra DB's replication layer, including the cross-region consistency protocol at 2M+ writes/sec, is serious depth. Given your stated friction with Astra's cost-per-query model at scale, ScyllaDB's TCO story is worth 15 minutes.

*Hooks used: Staff Engineer on Astra DB's multi-region replication layer at DataStax, Personally designed cross-region consistency protocol at 2M+ writes/sec, Self-identified frustration with Astra DB's cost-per-query model at scale*
*Characters: 250/300*

**Follow-up email** *(dry-run)*

**Subject:** Cost-per-query pain at 2M writes/sec — ScyllaDB TCO

Kwame,

You've spent four years on Astra DB's replication layer and personally designed the cross-region consistency protocol running at 2M+ writes/sec. You also know firsthand where the cost-per-query model breaks down at that scale.

ScyllaDB runs the same Cassandra-compatible workloads with a flat, predictable cost model and consistent P99 latencies at your write volumes — no cold-start surprises, no per-query tax that compounds at scale.

Worth a 15-minute call to walk through the benchmark numbers side-by-side?

— Yoav, ScyllaDB

*Hooks used: Staff Engineer on Astra DB's multi-region replication layer, DataStax, Designed cross-region consistency protocol at 2M+ writes/sec in production, Self-identified pain with Astra DB's cost-per-query model at scale, Seven years at DataStax with four focused entirely on Astra DB architecture*

---

### Priya Nair
**Director of Engineering, DSE Platform** at **DataStax** · New York, NY
_Director of Engineering, DSE Platform · DataStax_

**Score:** 97/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Director of Engineering leading 35 engineers across DSE Platform (storage, query, search) — the core of DataStax's Cassandra enterprise product. Former Principal Engineer on DSE's Solr-on-Cassandra integration gives her deep technical roots. She explicitly flags the DSE-vs-Astra internal tension and the pain of keeping legacy customers happy under shifting investment. Senior title, large org ownership, hands-on technical history, and visible strategic frustration make her a textbook ScyllaDB outreach target.

**ScyllaDB angle:** Lead with DSE platform pain: ScyllaDB is a drop-in Cassandra-compatible alternative that cuts nodes, latency, and maintenance overhead — letting her team do more with less. The DSE-vs-Astra investment tension she navigates quarterly is exactly the opening ScyllaDB exploits.

**Pain points identified:**

- Strategic tension between DSE enterprise commitments and DataStax's shift toward Astra DB
- Managing a deprioritized 35-engineer legacy platform org
- Keeping DSE customers satisfied as internal investment migrates to cloud-native
- Complexity of maintaining DSE storage, query, and Solr/search integration on Cassandra

**LinkedIn invite** *(dry-run)*

> Priya — you know DSE's internals better than almost anyone. With DataStax investment shifting to Astra, curious if you'd spare 15 min to compare notes on how ScyllaDB handles the enterprise Cassandra workloads your platform team owns.

*Hooks used: Director of Engineering, DSE Platform at DataStax, Former Principal Engineer on DSE Solr-on-Cassandra integration, Publicly acknowledged DSE-vs-Astra investment tension*
*Characters: 234/300*

**Follow-up email** *(dry-run)*

**Subject:** ScyllaDB vs DSE — worth 15 min of your time?

Priya,

You've spent years at the core of DSE — first as Principal Engineer on the Solr-on-Cassandra stack, now directing 35 engineers across storage, query, and search. You understand the platform's strengths and its ceiling better than most.

The DSE-vs-Astra investment split you navigate quarterly is exactly where ScyllaDB tends to surface as a credible path: Cassandra-compatible, fewer nodes, lower p99 latency, less operational overhead for your enterprise customers.

Worth a 15-min technical comparison call to see if the numbers are relevant to what your team is dealing with?

— Yoav, ScyllaDB

*Hooks used: Director of Engineering leading 35 engineers across DSE Platform (storage, query, search), Former Principal Engineer on DSE Solr-on-Cassandra integration, Explicitly navigates DSE-vs-Astra internal investment tension quarterly, 13 years of experience with deep hands-on Cassandra and distributed systems background*

---

### Rodrigo Santana
**Principal Solutions Architect** at **DataStax** · Miami, FL
_Principal Solutions Architect · DataStax_

**Score:** 97/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Rodrigo is a Principal SA at DataStax with 6 years of tenure — a textbook target. He is explicitly customer-facing, working with Fortune 500 banks, telcos, and retail on Cassandra and Astra DB at extreme scale. He personally witnesses tail latency and data modeling failures, and presented "Cassandra Anti-Patterns in Production" at ApacheCon 2022 — confirming deep expertise and ecosystem authority. Prior 7 years as DBA at Accenture and IBM further reinforces database depth. He knows the pain points cold and talks to affected customers daily.

**ScyllaDB angle:** Engage as a technical peer: Rodrigo personally experiences the P99 latency and data modeling pain ScyllaDB solves. Drop-in Cassandra API compatibility means zero rewrite for his customers. His ApacheCon platform and customer reach make him a top recruit and ecosystem connector candidate.

**Pain points identified:**

- P99 / tail latency issues in Cassandra production — named explicitly in his summary
- Data modeling constraints at extreme scale causing Fortune 500 customer friction
- Operational complexity of Cassandra at telco, banking, and retail scale
- Recurring Cassandra anti-patterns in production — his own ApacheCon 2022 talk topic

**LinkedIn invite** *(dry-run)*

> Rodrigo — you know Cassandra's tail latency and data modeling limits better than most, given 6 years of Fortune 500 SAs at DataStax. Worth 15 min to compare how ScyllaDB's architecture handles the P99 problems you present about at ApacheCon?

*Hooks used: Principal SA at DataStax for 6 years, Customer-facing work with Fortune 500 banks, telcos, and retail on Cassandra/Astra DB, Presented 'Cassandra Anti-Patterns in Production' at ApacheCon 2022, Explicitly names P99 tail latency and data modeling constraints in his summary*
*Characters: 241/300*

**Follow-up email** *(dry-run)*

**Subject:** Cassandra P99 tail latency — ScyllaDB's take

Rodrigo,

You've spent 6 years as a Principal SA at DataStax watching Fortune 500 banks and telcos hit the same walls: P99 latency spikes and data modeling constraints at extreme scale. You literally presented on Cassandra anti-patterns in production at ApacheCon 2022 — you know these failure modes cold.

ScyllaDB is a drop-in Cassandra API replacement built in C++ with a shard-per-core architecture that directly targets the tail latency problem. No rewrite for your customers' existing CQL schemas.

Worth a 15-min technical comparison call?

— Yoav, ScyllaDB

*Hooks used: Principal SA at DataStax for 6 years, Customer-facing Fortune 500 work in banking, telco, and retail on Cassandra and Astra DB, Presented 'Cassandra Anti-Patterns in Production' at ApacheCon 2022, Explicitly cites P99 tail latency and data modeling constraints as recurring customer pain in his summary*

---

### Tobias Gruber
**Staff SRE, Cassandra Infrastructure** at **DataStax** · Berlin, Germany
_Staff SRE, Cassandra Infrastructure · DataStax_

**Score:** 97/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Tobias is a Staff SRE owning Cassandra Infrastructure at DataStax — a textbook senior technical target. 7 years of deep Cassandra ops experience, personally authored the split-brain recovery runbook (triggered 11x in production), and tunes compaction and repair weekly. Staff SRE title carries real organizational influence. His pain points map precisely to ScyllaDB's differentiators, and his own framing — "very concrete opinions about what's hard versus what should be easier" — signals openness to alternatives.

**ScyllaDB angle:** Lead with ScyllaDB's reduced repair and compaction overhead. His split-brain, repair scheduling, and JVM tuning pain points map directly to ScyllaDB's shard-per-core architecture and self-managed compaction — fewer runbooks, fewer nodes, less tuning.

**Pain points identified:**

- Split-brain recovery complexity (authored runbook, triggered 11x in prod)
- Repair scheduling overhead at scale
- Compaction tuning burden
- JVM tuning for large Cassandra clusters
- Operational complexity of globally managed Cassandra infrastructure

**LinkedIn invite** *(dry-run)*

> Tobias — Staff SRE on Cassandra infra at DataStax, 7 years deep in repair scheduling and compaction tuning. You know exactly what's hard. Worth 15 min to compare how ScyllaDB's shard-per-core handles compaction vs. what you're tuning today?

*Hooks used: Staff SRE, Cassandra Infrastructure at DataStax, 7 years of Cassandra ops experience, Weekly compaction tuning and repair scheduling work noted in profile*
*Characters: 240/300*

**Follow-up email** *(dry-run)*

**Subject:** Cassandra repair overhead vs. ScyllaDB — 15 min?

Tobias,

You authored DataStax's split-brain recovery runbook — triggered 11 times in production. That's not a documentation exercise, that's a signal about operational ceiling.

The repair scheduling and compaction burden you're managing weekly at global scale maps directly to where ScyllaDB's shard-per-core architecture makes different tradeoffs. Fewer tuning knobs, no JVM, self-managed compaction.

Given your 7 years running this at DataStax, I'd value a direct technical conversation — not a pitch. Would you be open to 15 minutes comparing operational models?

— Yoav, ScyllaDB

*Hooks used: Authored DataStax internal split-brain recovery runbook, triggered 11x in production, Staff SRE owning globally distributed Cassandra infrastructure, Weekly repair scheduling and compaction tuning responsibilities, 7 years of Cassandra operational experience at DataStax, JVM tuning listed as core skill — maps to ScyllaDB's no-JVM differentiator*

---

## High potential / low experience (3/3)

### Dakarai Moyo
**Junior Software Engineer, DSE** at **DataStax** · Johannesburg, South Africa
_Junior Software Engineer, DSE · DataStax_

**Score:** 72/100 &nbsp;|&nbsp; **Segment:** `high_potential_low_experience`

**Qualifier reasoning:** Junior SE with ~2.5 years on DSE platform team, working on enterprise features: search integration (Solr) and node management tooling. Developing deep operational Cassandra knowledge — cluster failure/recovery at scale — and self-studying LSM-tree internals on personal time. Title and tenure place them squarely in high_potential_low_experience: no organizational authority today, but strong technical trajectory toward a senior distributed storage role in 1–2 years. Solid CS degree from UCT and hands-on DSE/Cassandra stack experience.

**ScyllaDB angle:** Dakarai's LSM-tree self-study and cluster failure/recovery focus maps directly to ScyllaDB's core strengths. Nurture with ScyllaDB compaction deep-dives and shard-per-core architecture content; position ScyllaDB as the natural next step in their distributed storage career.

**Pain points identified:**

- Operational complexity of large DSE enterprise clusters
- Cluster failure and recovery challenges at scale
- Self-studying LSM-tree internals suggests DSE tooling lacks sufficient low-level transparency

**LinkedIn invite** *(dry-run)*

> Dakarai — you're deep in DSE internals and self-studying LSM-trees. ScyllaDB's compaction and shard-per-core architecture would directly answer questions you're already asking. Worth 15 minutes to compare notes?

*Hooks used: Junior SE on the DSE platform team at DataStax, Self-studying LSM-tree internals on personal time, Focused on cluster failure/recovery at scale*
*Characters: 211/300*

**Follow-up email** *(dry-run)*

**Subject:** LSM-tree internals: Scylla vs DSE compaction design

Dakarai,

Two and a half years on the DSE platform team gives you a real operational view of Cassandra at scale — cluster failure modes, recovery paths, the limits of what the tooling exposes.

You're already reading LSM-tree internals on your own time. ScyllaDB's compaction strategies and shard-per-core architecture are a direct answer to the questions that work probably keeps raising.

If you're building toward senior distributed storage work, the design tradeoffs are worth understanding firsthand — not just from docs.

15 minutes to walk through the architecture differences?

— Yoav, ScyllaDB

*Hooks used: 2.5 years on the DSE platform team at DataStax, Self-studying LSM-tree internals on personal time, Focus on cluster failure and recovery at enterprise scale, Building toward a senior distributed storage role*

---

### Chen Wei
**Software Engineer II, DSE Query** at **DataStax** · Singapore
_Software Engineer II, DSE Query · DataStax_

**Score:** 72/100 &nbsp;|&nbsp; **Segment:** `high_potential_low_experience`

**Qualifier reasoning:** SWE II on DSE Query team, ~4 years total. Deep technical focus: CQL parsing, query planning, secondary indexes, execution engine. Fixed a P99 latency bug on the range query path for wide partitions — exactly ScyllaDB's competitive differentiator. No organizational authority yet, but trajectory toward query-layer domain expertise is clear. Strong long-game nurture; likely senior within 1-2 years.

**ScyllaDB angle:** Chen Wei has direct hands-on experience with P99 latency in DSE range queries and wide partitions — ScyllaDB's core differentiator. Outreach framing around execution engine architecture and latency trade-offs would land precisely on their stated technical interests.

**Pain points identified:**

- P99 latency degradation with wide partitions in DSE range queries
- Secondary index limitations at scale in Cassandra/DSE
- Complexity of DSE query execution layer tuning

**LinkedIn invite** *(dry-run)*

> Chen Wei — you fixed P99 latency on DSE's range query path for wide partitions. That's exactly where ScyllaDB's execution engine makes different trade-offs. 15 min to compare architecture notes?

*Hooks used: Software Engineer II on the DSE Query team at DataStax, Fixed a long-standing P99 latency bug on the range query path affecting wide partitions*
*Characters: 194/300*

**Follow-up email** *(dry-run)*

**Subject:** DSE vs Scylla: range query latency on wide partitions

Chen Wei,

Three years deep on DSE's query execution layer — CQL parsing, query planning, secondary indexes — puts you in a rare position to evaluate these trade-offs seriously.

The P99 bug you fixed on the range query path for wide partitions is a known pain point in the Cassandra execution model. ScyllaDB's shard-per-core architecture handles that path differently, with measurable impact on tail latency at scale.

I'm not pitching a migration. I'd rather compare execution engine design notes with someone who actually works at that layer.

15 minutes — worth it?

— Yoav, ScyllaDB

*Hooks used: Software Engineer II on the DSE Query team at DataStax, Three years on the DSE query team focused on CQL parsing, query planning, and secondary indexes, Fixed a long-standing P99 latency bug on the range query path for wide partitions, Stated goal of becoming a domain expert on the query execution layer*

---

### James Osei
**Software Engineer II, Astra DB** at **DataStax** · Toronto, Canada
_Software Engineer II, Astra DB · DataStax_

**Score:** 62/100 &nbsp;|&nbsp; **Segment:** `high_potential_low_experience`

**Qualifier reasoning:** James is a Software Engineer II at DataStax with ~3 years total experience (2 at DataStax), placing him in the junior-to-mid range. He works directly on the Astra DB backend — tenant isolation, billing integration, multi-tenancy, resource quotas, and the CQL execution path. Two merged OSS Cassandra commits signal growing ecosystem engagement. His stated goal to specialize in storage-layer work points to a clear trajectory toward senior technical influence within 1–2 years. Limited authority today, but strong technical foundation and growth vector make him a solid long-game nurture.

**ScyllaDB angle:** Engage on CQL execution path and multi-tenancy challenges — ScyllaDB's thread-per-core architecture offers compelling contrasts to Astra DB's tenant isolation model. Seed awareness now; revisit as he moves into storage-layer specialization.

**Pain points identified:**

- Multi-tenancy complexity and resource quota enforcement at scale
- CQL execution path performance and latency predictability
- Storage layer limitations in managed Cassandra environments
- Operational overhead of Astra DB's distributed backend

**LinkedIn invite** *(dry-run)*

> James — you're working the CQL execution path and tenant isolation at DataStax, so you've seen these tradeoffs firsthand. Worth 15 min to compare notes on how ScyllaDB's thread-per-core model handles multi-tenancy at the storage layer?

*Hooks used: Software Engineer II on Astra DB backend at DataStax, Works on tenant isolation layer and CQL execution path, Stated interest in specializing in storage-layer work*
*Characters: 235/300*

**Follow-up email** *(dry-run)*

**Subject:** Multi-tenancy at the storage layer — ScyllaDB vs Astra DB

James,

Two years on the Astra DB backend working tenant isolation and CQL execution puts you closer to these tradeoffs than most. ScyllaDB's thread-per-core architecture handles multi-tenancy and resource quota enforcement in a fundamentally different way than managed Cassandra — no JVM, predictable per-shard scheduling, hard latency isolation between tenants.

Given your trajectory toward storage-layer specialization, the architectural contrast is worth understanding directly rather than from docs.

Would a 15-min technical comparison call be useful?

— Yoav, ScyllaDB

*Hooks used: 2 years on Astra DB backend team at DataStax, Works on tenant isolation layer and resource quota enforcement, CQL execution path experience, Stated goal to specialize in storage-layer work*

---

## Wild card (1/1)

### Patrick Dubois
**Lead Developer Advocate, Apache Cassandra** at **DataStax** · Paris, France
_Lead Developer Advocate, Apache Cassandra · DataStax_

**Score:** 82/100 &nbsp;|&nbsp; **Segment:** `wild_card`

**Qualifier reasoning:** Patrick is DataStax's Lead Cassandra DevRel — technically credible with 5 years of hands-on Cassandra ops at OVHcloud before DevRel. He runs a 28K-subscriber YouTube channel, hosts live coding sessions, and speaks at 10–15 conferences/year. His InfoQ-picked Cassandra-vs-alternatives comparison shows he already engages the narrative ScyllaDB competes in. He shapes community perception at scale and has the technical depth to evaluate ScyllaDB honestly — making him a high-value ecosystem connector and potential recruit.

**ScyllaDB angle:** Engage as a technical peer on Cassandra ops pain (GC pauses, node sprawl, P99 latency) he experienced firsthand. Pitch a ScyllaDB benchmark deep-dive for content collaboration — his "no sugarcoating" credibility aligns with ScyllaDB's transparent performance story.

**Pain points identified:**

- GC pause unpredictability in Cassandra ops — lived experience at OVHcloud
- Cluster sprawl and node count overhead to hit SLA targets
- P99 latency variance in production Cassandra deployments
- Audience trust pressure: community expects honest Cassandra limitation coverage

**LinkedIn invite** *(dry-run)*

> Patrick — you ran Cassandra ops at OVHcloud for 5 years, so GC pauses and P99 variance aren't abstractions for you. Your InfoQ comparison piece caught my attention. Worth 15 min to dig into ScyllaDB's shard-per-core architecture and what it does to those numbers?

*Hooks used: 5 years as Cassandra ops engineer at OVHcloud — GC and P99 pain is firsthand experience, InfoQ-picked Cassandra-vs-alternatives comparison shows he already engages this narrative, Lead Developer Advocate for Apache Cassandra at DataStax — technically credible peer*
*Characters: 263/300*

**Follow-up email** *(dry-run)*

**Subject:** ScyllaDB vs Cassandra — a benchmark conversation

Patrick,

You spent 5 years running Cassandra in production at OVHcloud before moving to DevRel — you know exactly where the GC pause and P99 latency stories get uncomfortable. Your InfoQ comparison piece showed you don't shy away from that.

ScyllaDB's shard-per-core, userspace I/O model eliminates JVM GC entirely. The tail latency and node-count-reduction numbers are documented and reproducible. Given the "no sugarcoating" standard your 28K-subscriber community holds you to, I think a benchmark deep-dive is worth your time.

15 minutes to walk through the data?

— Yoav, ScyllaDB

*Hooks used: 5 years Cassandra ops at OVHcloud — GC pauses and P99 variance are lived experience, not theory, InfoQ-picked Cassandra-vs-alternatives comparison confirms he already covers this competitive space, Lead Developer Advocate, Apache Cassandra at DataStax — shapes community perception at scale, 28K-subscriber YouTube channel with explicit 'no sugarcoating' credibility standard*

---

## Rejected leads (sample — qualifier said no)

**Caroline Hu** — Senior Product Marketing Manager at DataStax
> Caroline Hu is a Senior PMM at DataStax focused on GTM, messaging, positioning, and analyst relations for Astra DB. Her role is firmly in marketing — not engineering, architecture, DevRel, or technical product management. Her background (B.S. Marketing, 4 years at Confluent in PMM, 3 years at DataStax in PMM) confirms a pure marketing trajectory with no technical engineering depth. She does not meet the ICP of technical staff working on DSE, Astra DB infrastructure, or the Cassandra ecosystem.

**Diana Fox** — Customer Success Manager at DataStax
> Diana Fox is a Customer Success Manager at DataStax with a background in SaaS CS (Gainsight). Her own summary explicitly states she does not go deep on Cassandra internals and escalates technical issues to engineering. Her skills are entirely non-technical: account management, renewals, churn prevention, QBRs. She holds a B.A. in Business and has no engineering, architecture, or technical product background. Despite managing 30 Astra DB and DSE enterprise accounts, her role is purely commercial/relationship-focused with zero technical depth relevant to ScyllaDB's value proposition.

**Derek Morrison** — Enterprise Account Executive at DataStax
> Derek Morrison is a pure enterprise sales professional — an Account Executive at DataStax focused on quota attainment, pipeline management, and executive relationships in financial services accounts. He explicitly states he leaves technical conversations to SAs. His background is entirely in sales (Oracle AE, MongoDB SDR) with a marketing degree. He has zero technical depth in Cassandra, DSE, or Astra DB. He does not meet any criterion of the ICP, which specifically targets technical employees. There is no angle for ScyllaDB outreach as a technical peer, recruit, or ecosystem connector.

**Ashley Burns** — Sales Development Representative at DataStax
> Ashley Burns is a Sales Development Representative at DataStax focused on outbound prospecting for Astra DB in mid-market segments. This is a pure sales role with no technical depth — skills listed are entirely sales-oriented (Outbound Prospecting, Salesforce, Outreach.io, Cold Calling). Prior role was also a BDR at Zscaler. There is zero engineering, architecture, or technical product involvement. Despite touching Astra DB as a product name in their prospecting work, they have no meaningful technical knowledge of the stack. Entirely outside ScyllaDB's ICP.

**Nina Petrov** — Senior Financial Analyst at DataStax
> Nina Petrov is a Senior Financial Analyst in FP&A at DataStax, supporting the CFO with financial modeling, board reporting, and budget management. Her skills are entirely finance-oriented (Excel, Tableau, ARR Modeling, SaaS Metrics) with no technical depth in databases, Cassandra, Astra DB, or DSE. Her background is in venture capital finance (Bessemer) and SaaS unit economics — entirely outside the ICP. She has zero engineering, architecture, or product influence relevant to ScyllaDB's competitive positioning.
