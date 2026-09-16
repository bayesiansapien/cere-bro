# Datacenter moratoriums are not killing the US buildout (SemiAnalysis)

**Date ingested:** 2026-09-16
**Source:** SemiAnalysis, 2026-09-15 · [essay](https://newsletter.semianalysis.com/p/everyone-says-datacenter-moratoriums)
**Raw:** [raw/rss/2026-09-15-semianalysis-everyone-says-datacenter-moratoriums-are-killing-the-us.md](../../raw/rss/2026-09-15-semianalysis-everyone-says-datacenter-moratoriums-are-killing-the-us.md) · also in [raw/gmail/2026-09-16-starred.md](../../raw/gmail/2026-09-16-starred.md)

## TL;DR

Four states acted in under two months (New York stopped issuing environmental permits for datacenters, Texas paused the next step in the ERCOT interconnection queue, Pennsylvania pulled datacenters out of fast-track permitting, Oregon froze deals on state-owned land) and more than **300 towns, cities and counties** have voted to halt datacenters in eighteen months. The narrative writes itself. SemiAnalysis went and measured it parcel by parcel and found that of roughly **20 GW sitting inside a restricted local boundary, only 1,525 MW is actually delayed**, across three projects. Total genuinely delayed capacity attributable to moratoriums and New York's executive order is about **2.3 GW**, against a forecast of **+38 GW of US datacenter IT capacity delivered in 2027**, more than double 2026.

## The methodological point, which is the real content

**Counting moratoriums is easy and measures nothing.** A moratorium only matters if it applies to a specific project, covers that project's parcel, and blocks an approval the developer still needs. Establishing that requires parcel-level, project-by-project analysis. SemiAnalysis built a moratorium database covering **400+ local instruments across 17 states**, tracked each from proposal through enactment, expiration, lifting, replacement or rejection, and mapped every active restriction onto a project pipeline of **6,000+ facilities** tracked through property records, permits, power-usage data, FOIA requests and satellite imagery.

Two distinctions carry the argument:

1. **Capacity exposed to a moratorium is not capacity delayed by one.** Most restrictions land on projects years from construction, where schedules were never firm. Even where a moratorium binds, the developer can usually relocate, redesign or challenge rather than abandon.
2. **These instruments freeze new applications rather than revoke granted approvals.** Anything under construction or fully permitted is out of reach entirely, which covers **all of 2026 and most of 2027**.

Of the **38 GW** forecast for 2027, **22 GW is under vertical construction** and the remaining 16 GW "planned" is mostly already financed and doing siteworks.

## The Texas finding is the interesting one

Texas adds perhaps three to four months of administrative delay for base-load projects in the ERCOT interconnection queue, and SemiAnalysis argues this is **offset by an acceleration of behind-the-meter demand**. For projects that never needed the grid it means nothing at all, making the restriction a **net positive for behind-the-meter developers and on-site generation suppliers**. Their June analysis projected behind-the-meter powering more than half of new US datacenter capacity from 2028, and last week they counted **75 GW of firm behind-the-meter equipment orders, more bound for Texas than any other state**. The regulatory friction is therefore accelerating the architectural shift it was meant to slow.

## Notable detail on method

SemiAnalysis states they augmented their research analyst team with **"an army of state-of-the-art research agents"** across the moratorium database and project records, systematically testing each restriction against relevant projects and validating with satellite imagery. That is a frontier-quality research firm publishing that agents did the parcel-matching work, on a question where the answer contradicts the consensus narrative. It also names, in the same essay, **"uninformed claude-coded forecasts"** as the source of an earlier bad narrative about cancelled capacity. **Agents produced both the misinformation they are debunking and the debunking.** That is worth recording exactly as stated.

## How this relates to prior wiki pages

**It is the supply-side complement to a demand-side thread the [compute economics page](compute-economics.md) has been running all month.** [SemiAnalysis's Vera Rubin agentic-inference analysis (09-15)](2026-09-15-semianalysis-vera-rubin-agentic-inference.md) put 1.4x to 3x tokens-per-TCO-dollar over GB300 at realistic interactivity, and defined the agentic workload as one whose cached-input ratio tends toward 1. That is a claim about how efficiently a rack converts power into tokens. This essay is the claim about how much power there will be to convert, and the answer is: more than the headlines suggest, arriving mostly behind the meter.

**It intersects a Kurate paper directly.** [Characterizing Job Power Elasticity for Power-Flexible AI Training](https://arxiv.org/abs/2609.11542) sits at cs.AI #15 this week, and the [09-12 digest](../daily-digest/2026-09/2026-09-12.md) predicted that an interruptible or power-flexible training SKU would be offered by a neocloud within 90 days, with the paper supplying the metric and Nvidia's capacity guarantee supplying the motive. The behind-the-meter shift this essay documents is the infrastructure precondition for that SKU: on-site generation is exactly where curtailment windows are a contractual object rather than a grid negotiation.

**And it is the counter-data point to today's market story.** [Wall Street's verdict on the AI slowdown (09-15)](../ai-industry/2026-09-15-pacing-the-frontier-debate.md) had neocloud and chip stocks falling while enterprise software rallied, on the theory that a pacing agreement would cut buildout. SemiAnalysis's forecast has not moved in twelve months despite bi-weekly updates, because construction activity keeps accelerating. **The financial market is pricing a slowdown that the satellite imagery does not show.** One of those two signals is wrong and the concrete one is harder to argue with.

## Gaps

- The forecast and the moratorium database are both SemiAnalysis products sold to subscribers, so the incentive runs toward a confident number. The methodology described is unusually checkable in principle and entirely unchecked in practice.
- The essay explicitly concedes moratoriums **could** delay the buildout and are simply not yet at scale. That is a statement about the present, and the restriction count is rising.
- The claim that developers can "relocate, redesign, or challenge" a blocked project is doing quiet work. Relocation has a schedule cost that is not in the 2.3 GW figure.
- Power availability is only one input. Nothing here addresses transformer, turbine or HBM lead times, which the same publication has elsewhere identified as binding.

## Industrial implication

The practical reading for anyone modelling compute supply: **stop tracking moratorium counts and start tracking behind-the-meter equipment orders.** The former is a political signal with almost no capacity content; the latter is 75 GW of firm orders and is where the buildout has already moved. The second-order consequence is that the regulatory leverage points are shifting too. A local board can block a grid interconnection; it has much less purchase on a campus that generates its own power. Whatever one thinks of that, it means the next two years of US compute supply is less politically contestable than it looks.
