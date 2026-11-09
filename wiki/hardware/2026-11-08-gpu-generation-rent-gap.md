---
title: "GPU generation sets the rent: GB300 at ~$13/hr vs H100 at ~$3.50"
date: 2026-11-08
source: https://x.com/StockSavvyShay/status/2119051898930319409
raw: ../../raw/twitter/feed/2026-11-07-evening-231654-ranked.json
tags: [compute-economics, gpu-rental, h100, gb300, datacenter-finance]
---

# GPU generation, not GPU count, sets what capacity is worth

**TL;DR.** Several items in the 11-07 US day point the same way. Deutsche Bank estimates SpaceX could exit 2026 with $77B ARR from contracted AI compute across 893K NVIDIA GPUs and 1.6GW, about $11B a year from Google alone, with GB300 capacity estimated at ~$13/hour versus ~$3.50 for H100. Microsoft is switching off H100-era servers it rented from Oracle after declining to renew a 2023 Bing contract, and asked IREN to upgrade its GB300 network ([@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2118783864177148059), [@StockSavvyShay](https://x.com/StockSavvyShay/status/2118762700515983749)). A Dutch bank is trying to offload about $500M of data center loans, some tied to Stargate and CyrusOne ([The Information](https://www.theinformation.com/articles/will-democrats-crush-data-centers)). The market is pricing a GPU-hour by generation: a GB300 hour rents for roughly 3.7x an H100 hour.

No architecture diagram: this is a market note.

## Why generation dominates

- **Memory per NVLink domain.** Large MoE models (mixture-of-experts, where each token visits a few expert sub-networks) serve best when all experts sit in one fast NVLink domain. An 8-GPU H100 node holds 640GB of HBM. A GB300 NVL72 rack holds tens of terabytes in one domain. The [MoE routing page](../inference-efficiency/2026-11-07-moe-routing-strategies-for-serving.md) showed cross-GPU expert traffic, not FLOPs, sets MoE latency, so older nodes lose value on exactly the models now in demand.
- **Renewal risk.** Contracts signed on H100s reprice at renewal. IREN re-contracted some H100s at double (11-09 digest), but Microsoft walked away from Oracle's. The spread depends on who the buyer is.
- **Financing reacts.** Loan sales and a delayed CME GPU rental futures market (pushed 60 days into January, 11-07) both say the market lacks a price curve for aging GPUs.

## Relation to prior wiki pages

- Extends [compute-economics](compute-economics.md): the 11-07 note on Microsoft-Oracle framed it as a contract story. The DB estimate adds a price ratio.
- Tension with efficiency research: drafters like DSpine (Tencent, 2.7-3.8x agent throughput on a 27B model) make old GPUs more productive, but the market is discounting them anyway, because memory capacity, not compute, is the binding limit for frontier MoE serving.
