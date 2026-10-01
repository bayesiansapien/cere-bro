# Micron's Quarter: Revenue Up Nearly 5x, HBM Locked for 2027, and NAND Rides the KV Cache

**Sources:** [The Information](https://www.theinformation.com/briefings/revenue-quintupled-ai-memory-maker-micron) · [@StockSavvyShay on HBM](https://x.com/StockSavvyShay/status/2105417538767343651) · [@StockSavvyShay on NAND](https://x.com/StockSavvyShay/status/2105427171464683791)
**Raw:** [raw/rss/2026-09-30-the-information-revenue-quintupled-at-ai-memory-maker-micron.md](../../raw/rss/2026-09-30-the-information-revenue-quintupled-at-ai-memory-maker-micron.md) and the 2026-10-01 X feed capture

## TL;DR

Micron reported revenue of **$54.2B** for the quarter ending 2026-09-03, nearly 5x a year earlier, on demand for HBM (high-bandwidth memory, the stacked DRAM next to GPU dies). Gross margin nearly doubled to **86.8%** on price increases. Micron said HBM had been *lower* margin than conventional DRAM this cycle, but most **2027 HBM supply is already locked at much higher prices**, closing that gap. It also announced **NVHBM**, which it calls the first custom HBM4E implementation, for Nvidia's next GPUs and NVLink Fusion. The surprise line: **NAND revenue up nearly 8x to $14B in 18 months**, with data-center SSDs about 71% of it.

## Why it matters here

- **The KV cache is now a storage market.** The [memory-hierarchy](memory-hierarchy.md) page has tracked KV spilling down tiers: SGLang HiSparse fetching top-k misses from host DRAM (09-29), KVCMAS sharing caches across agents (09-30). Micron's NAND growth is the demand-side signal that the tier below DRAM (SSD-backed KV and context stores for long agent sessions) is being bought at scale.
- **HBM pricing power moves to the supplier.** Locked 2027 prices plus a custom HBM4E part for Nvidia means memory, not compute, sets a growing share of accelerator cost. Pair with SK hynix validating HBM5 on CoWoS (09-30 digest).
- **Context for the capex debate:** the same day, The Information reported banks (SocGen, SMBC, MUFG) pulling back from data-center loans and CleanSpark conceding terms to finance a Meta site. Memory makers are pricing in demand that the debt market is starting to question.

## Links

- Concepts: [Memory hierarchy](memory-hierarchy.md) · [Compute economics](compute-economics.md)
- Digest: [2026-10-01](../daily-digest/2026-10/2026-10-01.md)
