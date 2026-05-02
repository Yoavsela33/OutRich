# OutRich Pipeline Run — 2026-05-02 09:55 UTC

## Summary

| Metric | Count |
|--------|-------|
| Leads discovered | 19 |
| Leads qualified | 19 |
| &nbsp;&nbsp;↳ obvious_fit | 2 |
| &nbsp;&nbsp;↳ high_potential_low_experience | 0 |
| &nbsp;&nbsp;↳ wild_card | 4 |
| &nbsp;&nbsp;↳ not_relevant | 13 |
| Leads selected for outreach | 3 |
| Messages drafted | 6 |
| Messages triggered (dry-run) | 6 |

## Segmentation strategy

Leads are selected by a quota system that reflects deliberate GTM thinking:

- **6 obvious_fit** — senior technical DataStax employees: engineers, architects, and engineering leaders working directly on Cassandra, DSE, or Astra DB. Highest value as recruits, ecosystem connectors, or converted advocates.
- **3 high_potential_low_experience** — junior DataStax engineers on the right stack. Limited authority today, but they grow into senior roles and carry deep institutional knowledge of the competitive stack.
- **1 wild_card** — non-obvious but strategically interesting DataStax employees: Developer Advocates with Cassandra community reach, Technical PMs who know the product deeply, Principal Evangelists.

The qualifier AI assigns each lead to a segment and scores them 0–100. Selection then picks the top-N per quota.

## Obvious fit (2/6)

### Norton S.
**Engineering Director** at **DataStax** · United States
_Engineering Director at DataStax_

**Score:** 97/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Current Engineering Director at DataStax (~9.5 yrs). Previously Deputy Director owning DSE Graph architecture, performance, and scalability. Inventor of Titan/JanusGraph (Cassandra-backed graph DB), co-founder of Aurelius, O'Reilly author. Deep distributed systems expertise. Holds major organizational influence over engineering strategy at DataStax — textbook senior technical decision-maker with direct DSE/Cassandra ecosystem depth.

**ScyllaDB angle:** Nearly a decade owning DSE architecture means Norton knows Cassandra's operational cost firsthand. ScyllaDB's drop-in API, 10x P99 gains, and fewer nodes directly address his lived pain — ideal for a peer-level outreach.

**Pain points identified:**

- Operational complexity of DSE at enterprise scale — tuning, compaction, node management
- P99 latency in real-time transactional graph workloads on DSE
- Infrastructure cost of large Cassandra/DSE clusters
- Scaling data platforms for concurrent ML and graph workloads

**LinkedIn invite** *(dry-run)*

> Norton — you've spent a decade on DSE architecture and literally invented Titan/JanusGraph. You know Cassandra's operational costs better than most. Worth 15 min to compare P99 numbers and node economics with ScyllaDB?

*Hooks used: Engineering Director at DataStax for ~9.5 years, Inventor of Titan/JanusGraph (Cassandra-backed distributed graph DB), Previously owned DSE Graph architecture, performance, and scalability as Deputy Director*
*Characters: 218/300*

**Follow-up email** *(dry-run)*

**Subject:** DSE operational cost vs. ScyllaDB — worth a comparison

Norton,

Nearly a decade owning DSE Graph architecture gives you a sharper view of Cassandra's operational overhead than almost anyone — compaction tuning, P99 tail latency under concurrent graph and ML workloads, cluster sprawl at enterprise scale.

ScyllaDB is a drop-in Cassandra replacement built in C++ with a shard-per-core model. In head-to-head migrations, teams typically cut node count significantly while achieving 10x P99 improvements.

No pitch — I'd rather compare architectural tradeoffs directly with someone who's lived the DSE side of it. 15 minutes?

— Yoav, ScyllaDB

*Hooks used: Engineering Director at DataStax for ~9.5 years, Inventor of Titan/JanusGraph — a distributed graph DB built on Cassandra/Titan stack, Owned DSE Graph architecture, performance optimization, and scalability for real-time transactional workloads as Deputy Director, Explicitly cited pain points: P99 latency in graph workloads, operational complexity of DSE, infrastructure cost of large clusters*

---

### Makarand G.
**Head of Engineering - Unit Economics** at **DataStax** · Cupertino, California, United States
_Head of Engineering,  Unit Economics  at DataStax._

**Score:** 95/100 &nbsp;|&nbsp; **Segment:** `obvious_fit`

**Qualifier reasoning:** Gokhale is a current Head of Engineering at DataStax with 5+ years in senior roles: 3+ years owning Astra DB (serverless multi-cloud Cassandra, vector search, Cassandra 4.0/4.1/5.0 OSS contributions), now leading Unit Economics (cloud cost, bin-packing, multi-tenant optimization). He has direct organizational authority over the exact products ScyllaDB competes against. His cost-reduction mandate maps precisely to ScyllaDB's TCO advantage. Prior VMware/GemFire and Pivotal distributed data platform experience adds further depth.

**ScyllaDB angle:** Lead with ScyllaDB's 5x TCO story — his unit economics mandate is a direct hook. ScyllaDB's fewer-nodes architecture and lower cloud resource consumption directly address his bin-packing and multi-tenant cost challenges on Astra DB serverless.

**Pain points identified:**

- Cloud cost reduction and unit economics pressure on SaaS Cassandra workloads
- Multi-tenant resource optimization and bin packing complexity on Astra DB
- Operational overhead of large-scale Apache Cassandra clusters in cloud
- Balancing serverless pricing competitiveness vs. infrastructure cost
- Cassandra scalability and P99 latency constraints at enterprise scale

**LinkedIn invite** *(dry-run)*

> Makarand — you've spent 4+ years engineering Astra DB's serverless Cassandra economics. ScyllaDB's fewer-nodes architecture cuts cloud unit cost materially. Given your bin-packing mandate, a 15-min benchmark comparison seems worth your time.

*Hooks used: Head of Engineering - Unit Economics at DataStax, with an explicit mandate for bin-packing and cloud cost reduction, 3+ years as Head of Engineering - Databases owning Astra DB serverless multi-cloud Cassandra, Current focus on multi-tenant resource optimization and SaaS unit economics*
*Characters: 241/300*

**Follow-up email** *(dry-run)*

**Subject:** ScyllaDB TCO vs. Astra DB serverless cost structure

Makarand,

You built Astra DB's serverless Cassandra stack and now own the unit economics behind it — that's a precise mandate, and cloud cost per workload is the hard part.

ScyllaDB's shard-per-core architecture runs the same workloads on materially fewer nodes than Cassandra, which maps directly to your bin-packing and multi-tenant optimization problem. We have published benchmarks showing 5x throughput-per-node at comparable P99 latency targets.

Worth 15 minutes to walk through the numbers side by side?

— Yoav, ScyllaDB

*Hooks used: Head of Engineering - Unit Economics at DataStax with explicit bin-packing and cloud cost reduction charter, 3+ years leading Astra DB development, including serverless multi-cloud Cassandra and vector search, Stated focus on multi-tenant dynamic resource utilization and waste reduction on SaaS infrastructure*

---

## High potential / low experience (0/3)

## Wild card (1/1)

### Ed A.
**VP & CPO, IBM watsonx.data** at **IBM** · San Francisco, California, United States
_CPO, IBM watsonx.data_

**Score:** 72/100 &nbsp;|&nbsp; **Segment:** `wild_card`

**Qualifier reasoning:** Ed Anuff is the former CPO of DataStax (6+ years) who personally launched Astra DB and led the GenAI/vector DB strategy. Now VP & CPO at IBM watsonx.data post-acquisition. Not a hands-on engineer, but has extraordinary product depth on Cassandra/Astra DB — he shaped DataStax's entire product direction. Also founded Usergrid (Cassandra-powered) and lists Cassandra as a skill. His ecosystem influence and IBM positioning power make him a strategically interesting target, though he's a product exec rather than a technical engineer.

**ScyllaDB angle:** Anuff now shapes how IBM positions Cassandra-compatible workloads across its portfolio. Framing ScyllaDB as a higher-performance, lower-TCO path for Astra DB/DSE customers under IBM's cost pressures — with drop-in Cassandra compatibility — is a credible executive-level conversation.

**Pain points identified:**

- Managing large Cassandra/Astra DB installed base under IBM cost scrutiny
- Pressure to modernize legacy DSE deployments within IBM's portfolio
- Competing with cloud-native databases on latency and TCO post-acquisition
- Navigating IBM's complex product portfolio while retaining DataStax customers

**LinkedIn invite** *(dry-run)*

> Ed — you spent 6 years shaping DataStax's Cassandra strategy, now steering IBM watsonx.data. Worth 15 min to compare how ScyllaDB handles the TCO and latency pressures IBM's Cassandra install base is facing? — Yoav, ScyllaDB

*Hooks used: Former CPO of DataStax for 6+ years, personally led Astra DB launch, Now VP & CPO at IBM watsonx.data post-DataStax acquisition, Founded Usergrid on Cassandra; lists Cassandra as a core skill*
*Characters: 224/300*

**Follow-up email** *(dry-run)*

**Subject:** ScyllaDB + IBM's Cassandra install base — TCO angle

Ed,

You built DataStax's product direction for over six years — Astra DB, the vector DB push, the DSE installed base — and now you're holding that entire portfolio inside IBM, where cost scrutiny on infrastructure is real.

ScyllaDB is drop-in Cassandra-compatible and consistently benchmarks at 3–10x lower latency and fewer nodes for equivalent throughput. For IBM customers running DSE or Astra DB at scale, that's a credible modernization conversation.

Would a 15-minute benchmark walkthrough be useful? I can tailor it to workloads you're already thinking about.

— Yoav, ScyllaDB

*Hooks used: CPO at DataStax for 6+ years, personally drove Astra DB and DSE product strategy, Joined IBM as VP of Open Platform Strategy following DataStax acquisition in 2025, Now VP & CPO, IBM watsonx.data — owns Cassandra-compatible workload positioning across IBM portfolio, Founded Usergrid on Cassandra; deep hands-on familiarity with Cassandra-based architectures*

---

## Rejected leads (sample — qualifier said no)

**Jason M.** — Chief Marketing Officer at DataStax (Acquired by IBM)
> Jason McClelland is DataStax's CMO — a pure marketing executive with no technical depth in Cassandra, DSE, or Astra DB. His entire career spans marketing, GTM strategy, eCommerce, and growth leadership. While he led DataStax's AI pivot narrative and the IBM acquisition story, his role is entirely commercial and brand-oriented. No engineering, architecture, or hands-on database background exists. He does not fit the ICP of technical DataStax staff with Cassandra/DSE expertise.

**Mark H.** — Strategic Cloud Executive at DataStax
> Mark Hupe is a pure sales and channel/partner executive with no technical background. His entire ~10-year DataStax tenure covers Sr. Director BD, Global Lead OEM/MSP, and Strategic Cloud Executive — all commercial roles. His skills are entirely sales-oriented: channel strategy, solution selling, business development, strategic alliances. Prior career at ExactTarget, Interwoven, and Data Return is uniformly sales/alliances. No evidence of hands-on Cassandra, DSE, or Astra DB knowledge. He does not meet the ICP criteria of engineer, architect, SA, DevRel, or technical product leader.

**Monty B.** — SVP Partnerships for GSI's at Palo Alto Networks
> Monty Bhatia is a senior business executive with a 30+ year career focused entirely on partnerships, alliances, GSI channels, and IT strategy — not technical engineering. His DataStax role is a part-time Board Advisor position (since Mar 2024), which is a governance/strategic advisory role with no indication of hands-on technical work on Cassandra, DSE, or Astra DB. His entire career spans SAP ERP, cloud sales, GSI partnerships (AWS, VMware, NetApp, Deloitte), with no engineering, architecture, or database technology depth. He is firmly a non-technical exec persona.

**Dawn S.** — Global Campaign Lead at Aiven
> Dawn Schaeffer is a pure marketing professional with no engineering, architecture, or technical depth. Her ~3-year DataStax tenure was in a Senior Global Campaign and Demand Generation role — entirely on the marketing/pipeline side, not touching Cassandra, DSE, or Astra DB technically. Her broader career spans demand gen, product marketing, and campaign management at Red Hat and Aiven. No technical signals whatsoever: no engineering titles, no Cassandra/DSE hands-on work, no SA or DevRel function. She is firmly in the not-relevant bucket as a non-technical marketing leader.

**Denis D.** — VP, EMEA at DataStax
> Denis Dorval is a pure GTM/sales executive — VP EMEA at DataStax — focused entirely on revenue growth and sales team building. His full career history is in sales leadership and channel management (JumpCloud, Apigee, Alfresco, FileNet). No evidence of technical depth in Cassandra, DSE, Astra DB, or any database technology. Skills are entirely GTM/sales-oriented. He does not fit the ICP of technical DataStax staff.
