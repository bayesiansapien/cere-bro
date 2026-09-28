# Who carries the AI buildout: financing, spreads and idle GPUs (2026-09-27 cluster)

**Sources (all surfaced via the X home feed, window of the 2026-09-28 digest; raw: `raw/twitter/feed/2026-09-27-*-ranked.json`, `raw/twitter/feed/2026-09-28-morning-ranked.json`, `raw/rss/2026-09-27-the-decoder-*.md`):**
- Brookings paper by a Columbia economist on US AI infrastructure cost, via [@alex_verem](https://x.com/alex_verem/status/2104269093256007884)
- Columbia Business School, "Financing the AI Buildout," via [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2103736651663208491)
- GPU-loan vs data-center-loan spreads, via [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2104369639828681013)
- Ed Zitron on warehoused GPUs and Oracle's force majeure notice ([@edzitron](https://x.com/edzitron/status/2103862335408419026), [newsletter](https://www.wheresyoured.at/wherere-all-the-ai-chips/))
- Goldman Sachs token-demand research via [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2103951890082087039); Goldman capex forecast via [The Decoder](https://the-decoder.com/goldman-sachs-expects-big-tech-to-spend-1-2-trillion-on-ai-infrastructure-by-2027-dwarfing-wall-street-estimates/)
- Dylan Patel on Rubin HBM ([@dylan522p](https://x.com/dylan522p/status/2103883333067485599))

## TL;DR

A cluster of finance-side posts in one US day, which together say where the buildout's risk sits. Brookings puts planned US AI infrastructure at **$10.3 trillion for 2025 to 2032**, about **3.6% of GDP a year**, above the railroad peak of about 2.2%, with **over $1.3 trillion of debt already committed** and a growing share routed through private credit and off-balance-sheet vehicles. Columbia's companion report says its central 182.7 GW scenario (about 77M GPUs in GB300 NVL72 racks) needs about **$5.5 of mature revenue per installed GPU-hour**, inside today's $6 to $10+ rental rates for high-end NVIDIA capacity. Lenders already price the difference between what lasts and what depreciates: **GPU loans rated BBB pay about 1.2 points more** than ordinary loans of that grade, while **data-center loans at BBB- or BB+ pay only about 0.2 points more**, and the GPU premium widens to about 2.5 points at B+. The bear case adds an estimated **$200 to $300 billion of GPUs sitting in warehouses** and Oracle's force majeure notice on its New Mexico data center.

## Key points

- **Lenders trust shells, not chips.** A grid connection, cooling plant and building outlive an accelerator generation and can be re-leased; the GPUs cannot. So a debt-funded non-NVIDIA cluster may cost more to finance than it saves on hardware, because resale and re-lease markets are thinner.
- **Token volume is not frontier volume.** Goldman: total token demand rose about 18x from December 2025 to September 2026, frontier-model tokens only about 8 to 9x. The marginal token is served by smaller, open or routed models.
- **Memory may set the next GPU's shape.** Patel's one-liner that Rubin's HBM spec is being cut ("despec") is unexplained so far; if confirmed, HBM supply, not compute, is binding.
- **Depreciation is the fuse.** Steve Hsu notes GPU depreciation of 4 to 6 years leaves leveraged bets exposed if adoption lags capability by a few years ([@hsu_steve](https://x.com/hsu_steve/status/2104211424616886429)).

## Relation to prior wiki pages

- **Updates [compute-economics](compute-economics.md).** [SemiAnalysis ClusterMAX 3.0 (09-24)](2026-09-24-semianalysis-clustermax-3.md) rated neoclouds on operations; today's sources rate them as credit risks.
- **Links to the offloading research.** [FreeToken (09-28)](../inference-efficiency/2026-09-28-freetoken-edge-moe-serving.md) and the [Engram offloading study (09-18)](2026-09-18-semianalysis-engram-dram-ssd-offloading.md) both move work off scarce HBM. If HBM is the binding constraint, those are the techniques that change the capex math.
- **CPU side.** [CPU shortage from agents and RL (09-25)](2026-09-25-cpu-shortage-agents-and-rl.md) is the other hardware bottleneck that offload-heavy serving leans on.

## Gaps

- Most numbers arrive second-hand via threads; the Brookings and Columbia papers were not captured in full.
- The warehouse-GPU estimate is a single analyst's and contested.
