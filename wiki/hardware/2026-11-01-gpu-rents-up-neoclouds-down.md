# GPU rents up, neoclouds down, memory is the bottleneck (2026-11-01)

**Sources:** X Following feed, 2026-10-31 US evening ([@StockSavvyShay](https://x.com/StockSavvyShay/status/2116509925606412522), [@StockSavvyShay](https://x.com/StockSavvyShay/status/2116513841911935196), [@StockSavvyShay](https://x.com/StockSavvyShay/status/2116536906339307987), [@StockSavvyShay](https://x.com/StockSavvyShay/status/2116571871831552290), [@StockSavvyShay](https://x.com/StockSavvyShay/status/2116545861790650594), [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2116470475677405254), [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2116508928985186565), [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2116582173914587300)) · [The Decoder](https://the-decoder.com/openai-raises-just-11-billion-of-its-30-billion-target-as-big-investors-lose-their-ai-appetite/) · raw: `raw/twitter/feed/2026-10-31-evening-*-ranked.json`, `raw/rss/2026-10-31-*.md`

## TL;DR

The physical market and the capital market disagree. B300 rental prices are up about 52% since May and even H100 rents are rising, while API token prices have fallen by more than half from peak. Over the same stretch neocloud stocks fell hard (CIFR -75%, IREN -65%, APLD -64%, CoreWeave -60%, Nebius -46%). Revenue per MW varies 3x (DigitalOcean about $20M, CoreWeave about $10M, Nebius about $7M). CoreWeave-style financing turns about $8M equity into $40M of GPUs by borrowing against contracted customer payments. Memory is the binding constraint: Altman met about 50 Samsung executives in Korea to deepen memory and data-center ties. Hyperscalers hold over $3T in future data-center commitments, $1.3T of it leases. Meta's capacity is modeled to reach 26GW by 2030 on about $1.2T capex, pushing annual depreciation to $171B, which is why S&P moved its outlook to negative. Inference platforms still raise: Baseten about $2B at up to $30B (run-rate revenue reportedly $200M to $600M in Q1 2026). OpenAI closed only about $11B of a $30B target at $1.25T.

## Reading

- Rents rising while token prices fall means margin sits with GPU owners, and inference software (routing, caching, quantization) is where API providers recover it.
- Equity markets price financing risk (leverage against a few customers), not utilization. These are investor-account numbers; treat as framing, not audited data.

## Relation to prior wiki pages

- Extends [compute-economics](compute-economics.md): 10-29 recorded GB300 rents rising after Q3 cloud earnings; 10-30 recorded Nvidia backstopping neocloud debt and Samsung's 783% profit jump on HBM ([summary](2026-10-30-china-export-catalogue-and-compute-finance.md)). Today's data shows the gap between physical scarcity and capital appetite widening.
- Memory-supply angle continues [memory-hierarchy](memory-hierarchy.md).
