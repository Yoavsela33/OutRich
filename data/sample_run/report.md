# OutRich Pipeline Run — 2026-04-30 18:48 UTC

## Summary

| Metric | Count |
|--------|-------|
| Leads discovered | 41 |
| Leads qualified | 41 |
| &nbsp;&nbsp;↳ obvious_fit | 13 |
| &nbsp;&nbsp;↳ high_potential_low_experience | 9 |
| &nbsp;&nbsp;↳ wild_card | 4 |
| &nbsp;&nbsp;↳ not_relevant | 15 |
| Leads selected for outreach | 10 |
| Messages drafted | 20 |
| Messages triggered (dry-run) | 20 |

## Segmentation strategy

Leads are selected by a quota system that reflects deliberate GTM thinking:

- **6 obvious_fit** — proven decision-makers at confirmed Cassandra/DataStax shops. Highest close probability.
- **3 high_potential_low_experience** — junior engineers at the right companies. Lower authority today, but future champions who influence stack decisions as they grow.
- **1 wild_card** — non-obvious but strategically interesting: AI leaders who could become PMs, DevRel figures with community reach, infrastructure investors.

The qualifier AI assigns each lead to a segment and scores them 0–100. Selection then picks the top-N per quota.

## Obvious fit (6/6)

### Marcus Chen
**Staff Software Engineer** at **Netflix** · San Jose, CA
_Staff Software Engineer · Cassandra Platform · Netflix_

**Score:** 97/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Marcus Chen is a Staff SWE explicitly owning Netflix's Cassandra platform — 300+ node clusters at 100M+ DAU scale. He is actively migrating from DSE to OSS Cassandra while maintaining tight latency SLOs, a textbook ScyllaDB pain point. Staff level means real architectural influence. Prior LinkedIn distributed storage experience adds depth. Every ScyllaDB value prop (P99 latency, node-count TCO reduction, drop-in Cassandra API) maps directly to his current operational reality.

**ScyllaDB angle:** Position ScyllaDB as the natural next step in his DSE→OSS Cassandra migration: same CQL API (zero rewrite), far fewer nodes at 300+ node scale (direct TCO win for Netflix), and P99 latency gains that make SLO maintenance dramatically easier during and after migration.

**Pain points identified:**

- Maintaining latency SLOs during DSE-to-OSS Cassandra migration
- Operational complexity of managing 300+ node clusters
- Cost of running large Cassandra clusters at Netflix scale
- Risk of latency degradation at 100M+ DAU serving scale

**LinkedIn invite** *(dry-run)*

> Managing 300+ node Cassandra clusters mid-DSE migration while holding P99 SLOs is a brutal constraint. ScyllaDB offers the same CQL API but typically cuts node counts 3-5x — worth 15 min?

*Hooks used: Netflix Cassandra platform owner with 300+ node clusters, Actively migrating from DSE to OSS Cassandra, Explicitly focused on maintaining tight latency SLOs during migration*
*Characters: 187/300*

**Follow-up email** *(dry-run)*

**Subject:** DSE → OSS Cassandra migration at Netflix scale

Marcus — your summary mentions migrating Netflix's 300+ node DSE clusters to OSS Cassandra while keeping latency SLOs intact. That's a hard problem: OSS Cassandra's P99 tail latency tends to widen exactly when you can least afford it at 100M+ DAU.

ScyllaDB is a drop-in CQL replacement that typically consolidates 300 Cassandra nodes to 60-100, and its shard-per-core architecture directly attacks P99 variance — the thing that makes SLO maintenance painful during a migration.

Worth a 15-min call to walk through how Disney+ and Comcast handled comparable migrations?

— Yoav, ScyllaDB

*Hooks used: Netflix Cassandra platform, 300+ node clusters at 100M+ DAU, Active DSE-to-OSS Cassandra migration in progress, Explicit SLO maintenance constraint during migration, Staff-level ownership means architectural decision influence*

---

### Sarah Okonkwo
**Principal Database Architect** at **Uber** · San Francisco, CA
_Principal Database Architect · Uber · Distributed Data Systems_

**Score:** 97/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Principal DB Architect at Uber (hyperscale DSE/Cassandra user), 12 years exp, clear stack authority. Explicitly leading a 40% TCO reduction initiative after cloud costs spiraled — a direct ScyllaDB pain match. Prior Senior DBA at Twitter (heavy Cassandra shop) adds depth. Data+AI Summit 2023 speaker signals broad community influence. Seniority, decision power, active cost pain, and confirmed DSE usage all align perfectly with ICP.

**ScyllaDB angle:** Lead with TCO: ScyllaDB's Cassandra-compatible API means no rewrite risk, while delivering 40–80% infra cost reduction — matching Sarah's stated 40% goal. Propose a benchmarking PoC on Uber's DSE workloads.

**Pain points identified:**

- Cloud cost spiral on DataStax Enterprise — targeting 40% TCO cut
- Operational complexity of Cassandra at Uber's hyperscale
- P99 latency pressure on ride/delivery matching
- Cassandra upgrade and maintenance burden at scale

**LinkedIn invite** *(dry-run)*

> Sarah — leading a 40% DSE TCO cut at Uber's scale is a hard problem. ScyllaDB is Cassandra-compatible (no rewrite) and has delivered 40–80% infra cost reductions for similar workloads. Worth 15 minutes?

*Hooks used: Sarah is leading a 40% TCO reduction initiative on DataStax Enterprise at Uber, ScyllaDB's Cassandra-compatible API eliminates rewrite risk — directly addressing her constraint, Uber operates at hyperscale across rides, eats, and freight workloads*
*Characters: 202/300*

**Follow-up email** *(dry-run)*

**Subject:** Uber's DSE TCO goal — ScyllaDB PoC worth a look

Sarah,

You mentioned leading a 40% Cassandra TCO reduction after cloud costs spiraled at Uber. That's exactly the problem ScyllaDB was built for — Cassandra-compatible API, so there's no rewrite risk, but the architecture eliminates the JVM overhead and compaction bottlenecks that drive DSE costs at hyperscale.

Operators running comparable DSE workloads have landed 40–80% infra cost reductions. Given your timeline and scale across rides, eats, and freight, a focused benchmarking PoC on your actual workloads would give you concrete data fast.

Worth a 15-minute call to see if the numbers hold for Uber's profile?

— Yoav, ScyllaDB

*Hooks used: Explicitly leading a 40% TCO reduction initiative on DataStax Enterprise at Uber, Cloud cost spiral called out directly in her LinkedIn summary, Uber's multi-product hyperscale footprint (rides, eats, freight) signals broad DSE operational surface, Data+AI Summit 2023 speaker — technically credible, peer-to-peer tone appropriate*

---

### Dmitri Volkov
**Senior Infrastructure Engineer** at **Apple** · Cupertino, CA
_Senior Infrastructure Engineer · Storage Systems · Apple_

**Score:** 97/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Dmitri is a Senior Infrastructure Engineer at Apple running one of the world's largest Cassandra deployments on the iCloud storage layer. 10 years of experience, clearly senior and technically influential. His focus on multi-DC replication and cross-region failover maps directly to ScyllaDB strengths. His Cassandra Summit 2022 talk on petabyte-scale compaction signals deep expertise and community visibility. Apple's iCloud scale virtually guarantees latency, cost, and compaction pain points ScyllaDB directly solves.

**ScyllaDB angle:** Open with ScyllaDB's compaction performance at petabyte scale — tied directly to his Summit talk. Emphasize 10x P99 latency gains, node-count reduction cutting Apple's operational footprint, and drop-in Cassandra API compatibility eliminating rewrite risk for a mission-critical iCloud deployment.

**Pain points identified:**

- Compaction overhead and strategy tuning at petabyte scale
- Multi-DC replication complexity and cross-region failover reliability
- Operational cost and node sprawl at iCloud scale
- P99 latency management under massive iCloud traffic
- Cassandra upgrade and maintenance burden at extreme scale

**LinkedIn invite** *(dry-run)*

> Your Cassandra Summit 2022 talk on petabyte-scale compaction caught my attention. At ScyllaDB we've cut compaction overhead and P99 latency by 10x on comparable deployments — with full Cassandra API compatibility. Worth 15 minutes?

*Hooks used: Presented at Cassandra Summit 2022 on compaction strategies at petabyte scale, Runs one of the world's largest Cassandra deployments on iCloud, ScyllaDB's drop-in Cassandra API compatibility eliminates rewrite risk*
*Characters: 231/300*

**Follow-up email** *(dry-run)*

**Subject:** Compaction at petabyte scale — ScyllaDB vs Cassandra

Dmitri,

Your Cassandra Summit 2022 talk on compaction strategies at petabyte scale is exactly the problem space ScyllaDB was built for. Operators running iCloud-scale Cassandra clusters consistently hit the same ceiling: compaction amplification, P99 spikes under heavy traffic, and node sprawl that inflates operational cost.

ScyllaDB's shard-per-core architecture and incremental compaction typically cut P99 latency 10x and reduce node count significantly — with a drop-in Cassandra API, so nothing in your replication topology needs to change.

Worth a 15-minute technical call to compare notes?

— Yoav, ScyllaDB

*Hooks used: Presented at Cassandra Summit 2022 on compaction strategies at petabyte scale, Runs one of the world's largest Cassandra deployments on the iCloud storage layer, Focused on multi-DC replication and cross-region failover — maps directly to ScyllaDB strengths, Pain points around compaction overhead, P99 latency, and node sprawl at iCloud scale*

---

### Priya Ramanujan
**Engineering Manager, Data Infrastructure** at **Discord** · San Francisco, CA
_Engineering Manager, Data Infrastructure · Discord_

**Score:** 97/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Priya manages Data Infrastructure at Discord, one of the most documented large-scale Cassandra deployments (500M+ users). She led the 2022 DSE → OSS Cassandra migration and explicitly cites tail latency at scale as a "constant challenge" — a direct, self-declared pain point. Senior decision-maker, confirmed Cassandra operator, and clear alignment with ScyllaDB's P99 latency and TCO value props. Prior Twitch infra experience adds further signal. Virtually no qualification gaps.

**ScyllaDB angle:** Lead with ScyllaDB's P99 latency advantages at Discord-scale, referencing drop-in Cassandra API compatibility (zero rewrite risk post-DSE migration). Secondary hook: node consolidation reducing operational overhead and TCO on large clusters.

**Pain points identified:**

- Tail latency (P99) at scale — self-described as a 'constant challenge'
- Recent DSE → OSS Cassandra migration complexity and ongoing ops burden
- Scaling message storage for 500M+ registered users
- Operational overhead of managing large Cassandra clusters

**LinkedIn invite** *(dry-run)*

> Priya — managing Cassandra at Discord scale with P99 tail latency as a "constant challenge" is exactly where ScyllaDB's architecture tends to move the needle. Drop-in Cassandra API, no rewrite risk. Worth 15 min?

*Hooks used: Discord's 500M+ user Cassandra deployment, Self-described P99 tail latency as a 'constant challenge', Drop-in Cassandra API compatibility — no rewrite risk after DSE migration*
*Characters: 212/300*

**Follow-up email** *(dry-run)*

**Subject:** P99 latency at Discord's Cassandra scale

Priya,

You called out tail latency at scale as a "constant challenge" — that's not a tuning problem, it's a JVM-and-shared-nothing architecture problem that OSS Cassandra doesn't fully escape.

ScyllaDB is a drop-in Cassandra replacement (same CQL/drivers, no rewrite) built on a thread-per-core model that consistently cuts P99s by 10x in comparable deployments. Given you just completed the DSE migration, compatibility risk is near zero.

If it's useful, I can send Discord-relevant benchmark data or find 15 minutes to walk through the latency specifics.

— Yoav, ScyllaDB

*Hooks used: Discord runs Cassandra for 500M+ registered user message storage, Priya self-declared P99 tail latency as a 'constant challenge', Led the 2022 DSE to OSS Cassandra migration — drop-in compatibility directly lowers switching risk, OSS Cassandra's JVM architecture as the root cause of tail latency at their scale*

---

### James Whitfield
**Principal Data Engineer** at **JPMorgan Chase** · New York, NY
_Principal Data Engineer · Real-Time Analytics · JPMorgan Chase_

**Score:** 97/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** James is a Principal Data Engineer at JPMC with 13 years experience, explicitly running DataStax Enterprise in production for trade surveillance at 200k ops/sec with sub-10ms read SLAs. He has seniority to influence or drive database vendor decisions. Critical buying signal: DSE contract is up for renewal and he is actively evaluating alternatives — a live, time-sensitive opportunity. ScyllaDB's drop-in DSE compatibility, 10x P99 latency gains, and TCO reduction directly address his evaluation criteria.

**ScyllaDB angle:** Lead with drop-in DSE compatibility (zero rewrite risk) and P99 latency benchmarks at 200k+ ops/sec to address his sub-10ms SLA. Frame TCO savings as a contract-renewal lever — JPMC pays enterprise DSE pricing. Engage now while his evaluation window is open.

**Pain points identified:**

- DSE contract renewal cost pressure — actively seeking alternatives
- Sub-10ms P99 latency SLA under 200k ops/sec is hard to sustain on DSE at scale
- Operational complexity of DataStax Enterprise at JPMC scale
- Vendor lock-in risk with DataStax licensing model

**LinkedIn invite** *(dry-run)*

> James — sub-10ms P99 at 200k ops/sec on DSE is a hard SLA to hold. With your contract up for renewal, worth knowing ScyllaDB is drop-in DSE-compatible and consistently beats those latencies. 15 min to share benchmarks at your scale?

*Hooks used: Explicitly running DSE in production for trade surveillance at JPMC, Sub-10ms P99 read SLA at 200k ops/sec stated in profile, DSE contract actively up for renewal — live evaluation window*
*Characters: 232/300*

**Follow-up email** *(dry-run)*

**Subject:** DSE renewal at JPMC — ScyllaDB benchmarks at 200k ops/sec

James,

You mentioned evaluating DSE alternatives as your contract comes up. ScyllaDB is wire-compatible with DSE — no rewrite, no migration risk — and in production deployments at comparable ops/sec we routinely see P99 latencies cut by half or more against your sub-10ms target.

For a trade surveillance workload where a blown SLA has real consequences, that headroom matters. JPMC's DSE licensing spend is also the kind of cost center where our TCO numbers tend to resonate.

Worth 15 minutes to walk through benchmarks at your exact load profile?

— Yoav, ScyllaDB

*Hooks used: DSE in production for trade surveillance at JPMC — explicitly stated, Sub-10ms P99 read SLA at 200k ops/sec — concrete workload detail from profile, DSE contract renewal actively in progress — time-sensitive buying signal, JPMC-scale enterprise DSE pricing as TCO lever*

---

### Aisha Muhammad
**Staff Engineer** at **eBay** · San Jose, CA
_Staff Engineer · Distributed Databases · eBay_

**Score:** 97/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Aisha is a Staff Engineer at eBay directly owning Cassandra-based infrastructure at massive scale (1.5B listings). She has clear decision-making authority over the database stack as a capacity planning and reliability owner. 10 years of experience confirms seniority. She is publicly vocal about Cassandra's operational burden on Twitter — a textbook pain signal. eBay's scale virtually guarantees latency, cost, and operational complexity pain points that ScyllaDB directly addresses.

**ScyllaDB angle:** Drop-in Cassandra replacement eliminating the operational burden she publicly complains about — fewer nodes, 10x lower P99 latency at 1.5B-listing scale, up to 5x TCO reduction, no API rewrite required.

**Pain points identified:**

- Cassandra operational burden (publicly stated on Twitter)
- Capacity planning complexity at 1.5B listing scale
- Reliability overhead for product catalog, recommendations, and inventory workloads
- High infrastructure cost at eBay's hyperscale
- Cassandra upgrade and tuning complexity

**LinkedIn invite** *(dry-run)*

> You've been vocal about Cassandra's operational burden — owning that stack for 1.5B eBay listings, I'd imagine tuning and capacity planning alone is a second job. ScyllaDB is a drop-in replacement that's cut P99 latency 10x and TCO by 5x at comparable scale. Worth 15 minutes?

*Hooks used: Owns Cassandra-based infrastructure at eBay powering 1.5B listings, Publicly vocal about Cassandra's operational burden on Twitter, Responsible for capacity planning and reliability at hyperscale*
*Characters: 276/300*

**Follow-up email** *(dry-run)*

**Subject:** Cassandra ops burden at 1.5B-listing scale — ScyllaDB

Aisha,

You mentioned Cassandra's operational overhead publicly — and running that stack for eBay's product catalog, recommendations, and inventory at 1.5B listings, I'd expect capacity planning alone consumes a disproportionate share of your team's time.

ScyllaDB is a wire-compatible Cassandra replacement. No API rewrite. In production at comparable hyperscale deployments, teams see 10x lower P99 latency, 5x TCO reduction, and a significantly thinner ops footprint.

Worth a 15-minute call to walk through what the migration path looks like at your scale?

— Yoav, ScyllaDB

*Hooks used: Owns Cassandra infrastructure at eBay supporting 1.5B listings, Publicly vocal about Cassandra operational burden on Twitter, Directly responsible for capacity planning and reliability across catalog, recommendations, and inventory workloads, eBay hyperscale makes latency, cost, and ops complexity pain points concrete and addressable*

---

## High potential / low experience (3/3)

### Jake Morrison
**Software Engineer II** at **Netflix** · Los Gatos, CA
_Software Engineer II · Cassandra Platform · Netflix_

**Score:** 72/100 &nbsp;|&nbsp; **Segment:** `high_potential_low_experience`

**Qualifier reasoning:** Jake is a Software Engineer II (~2 years) on Netflix's dedicated Cassandra Platform team — one of the most sophisticated Cassandra deployments globally. He's deeply embedded in internals: SSTable compaction, schema management, capacity automation. Decision-making authority is limited today, but his Stanford CS background, steep trajectory, and explicit "growing toward senior" signal suggest tech lead status within 1–2 years. Platform team engineers at Netflix frequently become internal champions — early cultivation is high value here.

**ScyllaDB angle:** Engage Jake on compaction and latency internals — where ScyllaDB's preemptive scheduling and faster compaction directly map to his expertise. Position ScyllaDB as a drop-in Cassandra evolution with operational wins his platform team would own.

**Pain points identified:**

- SSTable compaction complexity and tuning overhead
- Capacity automation challenges at Netflix's Cassandra scale
- Schema management friction in large multi-tenant deployments
- Operational complexity of maintaining a large Cassandra fleet

**LinkedIn invite** *(dry-run)*

> Your internal talk on SSTable compaction strategies caught my attention — that's exactly where ScyllaDB's preemptive scheduling eliminates the tuning overhead Cassandra forces on platform teams. Worth 15 min to compare notes?

*Hooks used: Jake authored an internal tech talk on SSTable compaction strategies, He works on Netflix's Cassandra Platform team handling capacity automation and schema management, Compaction tuning overhead is a direct pain point ScyllaDB's architecture addresses*
*Characters: 225/300*

**Follow-up email** *(dry-run)*

**Subject:** SSTable compaction overhead — how Netflix could reclaim it

Jake,

Your work on compaction strategies at Netflix's Cassandra scale is the kind of internals depth that makes the ScyllaDB architecture worth a direct look. Our preemptive scheduler treats compaction as a first-class latency concern — no more manual tuning to stop compaction from starving reads.

For a platform team running capacity automation at Netflix's scale, the operational delta is meaningful: fewer knobs, more predictable throughput, same CQL interface your tooling already speaks.

Happy to walk through a compaction benchmark side-by-side — 15 min if you're curious.

— Yoav, ScyllaDB

*Hooks used: Jake is on Netflix's dedicated Cassandra Platform team — one of the largest Cassandra deployments globally, He authored an internal tech talk on SSTable compaction strategies, signaling deep internals interest, His team owns capacity automation, directly mapping to ScyllaDB's operational efficiency advantages, ScyllaDB's CQL compatibility positions it as a drop-in evolution his platform tooling can adopt without rewrites*

---

### Devon Williams
**Backend Engineer** at **Riot Games** · Los Angeles, CA
_Backend Engineer · Game Infrastructure · Riot Games_

**Score:** 72/100 &nbsp;|&nbsp; **Segment:** `high_potential_low_experience`

**Qualifier reasoning:** Devon is 2 years in at Riot Games, directly owning production Cassandra workloads for leaderboard and player-state services — a textbook ScyllaDB use case. Gaming is notorious for extreme write throughput and latency sensitivity at peak events, and Devon explicitly flags latency spikes as a pain point. Decision-making authority is limited at this seniority level, but the trajectory is strong (EA intern → Riot infra ownership in 2 years). Engineers with hands-on production pain often become the most credible internal champions for stack changes.

**ScyllaDB angle:** Drop-in Cassandra compatibility = zero rewrite risk for Devon's leaderboard/player-state services. Lead with P99 latency improvements that directly address the peak-event spikes Devon already feels. Position ScyllaDB as an upgrade Devon can champion internally without asking the team to start over.

**Pain points identified:**

- Cassandra P99 latency spikes during peak gaming events (tournaments, ranked resets)
- Scaling Cassandra for high-concurrency leaderboard and player-state workloads
- Operational complexity of Cassandra at gaming scale

**LinkedIn invite** *(dry-run)*

> Leaderboard and player-state on Cassandra at Riot scale — peak-event latency spikes are a known pain. ScyllaDB is CQL-compatible and cuts P99s significantly with no rewrite. Worth 15 min?

*Hooks used: Devon owns production Cassandra leaderboard and player-state services at Riot Games, Explicitly flagged peak-event latency spikes as a pain point, Drop-in Cassandra compatibility means zero rewrite risk for his existing services*
*Characters: 187/300*

**Follow-up email** *(dry-run)*

**Subject:** Cassandra P99 spikes on Riot leaderboards

Devon,

Running leaderboards and player-state on Cassandra at Riot's scale is already a hard problem — ranked resets and tournament spikes make it harder. You flagged peak-event latency as a real pain point, and that's exactly where Cassandra tends to fall apart at high concurrency.

ScyllaDB is CQL-compatible, so your existing Go services and data model carry over without a rewrite. Engineers in similar gaming infra roles have seen P99 latency drop significantly after migration.

Worth a 15-min call to walk through what that looks like at your workload scale?

— Yoav, ScyllaDB

*Hooks used: Devon owns production Cassandra leaderboard and player-state services at Riot Games, Explicitly cited latency spikes during peak gaming events as a current pain point, Uses Go for backend services — directly compatible with ScyllaDB driver ecosystem, Drop-in Cassandra CQL compatibility = no rewrite required for his existing services*

---

### Fatima Al-Rashidi
**Site Reliability Engineer** at **Discord** · Remote
_Site Reliability Engineer · Discord · Infrastructure_

**Score:** 72/100 &nbsp;|&nbsp; **Segment:** `high_potential_low_experience`

**Qualifier reasoning:** Fatima is a 2-year SRE at Discord, directly owning Cassandra availability and performance for Discord's massive message-storage fleet — on-call rotations and runbooks included. She lacks seniority for purchase authority today, but her daily immersion in Cassandra ops pain (latency, GC, node sprawl) at one of the industry's most-watched Cassandra deployments makes her a strong future champion. Trajectory to Staff/Senior SRE or tech lead is realistic within 1–2 years. Prior DevOps role at Canonical reinforces infrastructure depth.

**ScyllaDB angle:** Engage as a technical peer on Discord's Cassandra ops pain (GC pressure, tail latency, node sprawl). ScyllaDB's drop-in Cassandra compatibility means no rewrite — just less on-call pain. Nurture now; she's rapidly building institutional knowledge and decision influence.

**Pain points identified:**

- High on-call burden managing large-scale Cassandra fleet
- Operational complexity of Cassandra at Discord's traffic scale
- P99 latency pressure on message-storage workloads
- Cassandra GC pauses and tuning overhead at extreme scale

**LinkedIn invite** *(dry-run)*

> Fatima — owning Cassandra on-call at Discord's scale is no small thing. GC pressure and tail latency at that message volume are brutal. ScyllaDB is a drop-in replacement that cuts most of that pain. Worth 15 min?

*Hooks used: Owns Cassandra availability and on-call rotations at Discord, Discord's Cassandra fleet is one of the most-watched in the industry, Qualification flags GC pressure and P99 tail latency as active pain points, ScyllaDB's drop-in Cassandra compatibility is directly relevant*
*Characters: 212/300*

**Follow-up email** *(dry-run)*

**Subject:** Discord's Cassandra on-call load — a data point

Fatima,

Managing on-call rotations for Discord's message-storage Cassandra fleet means you're absorbing some of the worst GC pause and tail latency problems in the industry at that traffic scale.

ScyllaDB is a drop-in Cassandra replacement — same CQL, same drivers — built on a shard-per-core architecture that eliminates JVM GC entirely. Teams running comparable write-heavy workloads have cut node counts significantly and reduced P99 latency without a rewrite.

Happy to share Discord-relevant benchmarks if that's useful, or just talk Cassandra ops for 15 minutes.

— Yoav, ScyllaDB

*Hooks used: Owns on-call rotations for Discord's Cassandra message-storage fleet, GC pauses and P99 tail latency are explicitly identified pain points at Discord's scale, ScyllaDB's drop-in Cassandra compatibility means no rewrite — directly addresses her operational context, Discord's Cassandra deployment is noted as one of the most-watched in the industry*

---

## Wild card (1/1)

### Dr. Rebecca Torres
**Director of AI/ML Engineering** at **PayPal** · San Jose, CA
_Director of AI/ML Engineering · PayPal · Real-Time Decisioning_

**Score:** 82/100 &nbsp;|&nbsp; **Segment:** `wild_card`

**Qualifier reasoning:** Dr. Torres owns PayPal's real-time ML decisioning platform with explicit sub-5ms Cassandra feature store SLAs for fraud and risk — a textbook high-stakes Cassandra workload. However, she is not a pure infra/database owner, so she's not obvious_fit. The wild_card is earned because she's exploring PM/product roles, making her a strong ScyllaDB product hire candidate, and her AI Infra Summit keynote gives her broad ecosystem influence bridging ML and data infrastructure.

**ScyllaDB angle:** Dual approach: (1) Sales — ScyllaDB's P99 latency advantage is directly measurable ROI against her sub-5ms fraud/risk SLA on Cassandra at PayPal scale. (2) Talent/Strategic — her PM transition interest and AI infra credibility make her a compelling ScyllaDB product leader candidate.

**Pain points identified:**

- Sub-5ms feature lookup SLAs on Cassandra at PayPal's transaction scale — P99 latency tail risk directly impacts fraud/risk model quality
- Operational complexity of maintaining a large Cassandra cluster as a real-time ML feature store
- High TCO of low-latency Cassandra fleet at PayPal's volume
- Career transition signals openness to product/PM roles at companies like ScyllaDB

**LinkedIn invite** *(dry-run)*

> Your AI Infra Summit keynote on sub-5ms Cassandra feature lookups for PayPal's fraud decisioning caught my attention. ScyllaDB cuts P99 tail latency significantly vs. Cassandra at that scale — worth 15 minutes?

*Hooks used: AI Infrastructure Summit 2024 keynote, sub-5ms Cassandra feature store SLA for fraud/risk at PayPal*
*Characters: 210/300*

**Follow-up email** *(dry-run)*

**Subject:** PayPal fraud feature store — P99 tail latency on Cassandra

Dr. Torres,

Running fraud and risk decisioning at PayPal's transaction volume with a sub-5ms feature lookup SLA is one of the harder Cassandra problems in production today. P99 tail latency is where those SLAs break — and it gets worse as the cluster grows.

ScyllaDB is a Cassandra-compatible replacement built in C++ with a shard-per-core architecture that consistently cuts P99 by 3–5x at equivalent throughput. Several financial-scale workloads have moved their feature stores for exactly this reason.

Worth a 15-minute call to see if the numbers are relevant to your stack?

— Yoav, ScyllaDB

*Hooks used: Sub-5ms feature lookup SLA on Cassandra at PayPal for fraud and risk models, Director of AI/ML Engineering owning the real-time ML decisioning platform, PayPal transaction scale amplifies Cassandra P99 tail risk, AI Infrastructure Summit 2024 keynote signals ecosystem visibility and technical credibility*

---

## Rejected leads (sample — qualifier said no)

**Yara Nasser** — Senior Data Scientist at Careem
> Yara Nasser is a Senior Data Scientist at Careem focused on demand forecasting, route optimization, and computer vision — all ML/AI work. Her stack is Python, PyTorch, and Apache Spark. She explicitly states that the data infra team handles databases and that she has no involvement in Cassandra or NoSQL infrastructure decisions. While Careem as a company may use NoSQL at scale, Yara has zero proximity to those decisions. Her prior role at Noon is also ML-focused. No database, infrastructure, or backend engineering signals present.

**Raj Kumar** — Backend Engineer at Razorpay
> Raj Kumar is a Backend Engineer at Razorpay working exclusively on Django + PostgreSQL + Redis — a purely relational/cache stack with zero signals of Cassandra, DataStax, or distributed NoSQL involvement. His profile explicitly states "no Cassandra or distributed NoSQL in sight." With ~4 years of total experience and no adjacency to the NoSQL ecosystem, he falls entirely outside the ICP. Even Razorpay as a company does not surface any public Cassandra usage signals. No latency, cost, or ops complexity pain points relevant to ScyllaDB are detectable.

**Chris Taylor** — DevOps Engineer at Grubhub
> Chris Taylor is a DevOps Engineer at Grubhub focused entirely on Kubernetes, Redis, PostgreSQL, Terraform, and CI/CD. His own summary explicitly states "No experience with Cassandra or column-family databases in our current stack." No signals of Cassandra/DataStax/Astra DB usage exist, and his prior Systems Admin role at Morningstar confirms a traditional infrastructure background with zero NoSQL wide-column overlap. No adjacency to ScyllaDB's ICP from any angle.

**Jessica Brown** — Senior Frontend Engineer at Netflix
> Jessica is a Senior Frontend Engineer at Netflix focused exclusively on consumer-facing UI with React, TypeScript, and CSS. Her profile explicitly states "no involvement in backend or data infrastructure." Her entire skill set is frontend-oriented with zero signals of database, backend, or NoSQL exposure. While Netflix is a known Cassandra user at scale, Jessica has no proximity to those systems or any database decision-making authority. Prior role at Hulu is similarly frontend-only. She is entirely outside the ICP.

**Linda Zhao** — Senior Product Manager at Airbnb
> Linda Zhao is a Senior Product Manager at Airbnb focused entirely on consumer growth, guest discovery, and recommendations. Her own summary explicitly states "no involvement in infrastructure or data systems." Her skill set (A/B Testing, Growth, Roadmapping) and career history (PM at Pinterest) are purely product/consumer-facing. There are no signals of Cassandra, NoSQL, or database infrastructure exposure whatsoever. She falls completely outside ScyllaDB's ICP — neither an engineer/architect, nor an AI/ML leader, nor a DevRel or infrastructure investor.
