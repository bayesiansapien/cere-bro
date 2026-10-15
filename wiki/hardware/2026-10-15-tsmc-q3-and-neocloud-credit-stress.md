# TSMC beats and adds a 3nm fab while neocloud credit cracks

**Date:** 2026-10-15 · **Sources:** The Information (TSMC 3nm fab; CoreWeave), X Following feed (TSMC Q3 figures, Bloomberg via @rohanpaul_ai, Epoch AI note, Cerebras investor post), Gary Marcus, Gmail
**Links:** [TSMC 3nm fab](https://www.theinformation.com/briefings/tsmc-add-new-3nm-fab-ai-orders-pile) · [CoreWeave co-founders](https://www.theinformation.com/articles/coreweave-co-founders-stock-sales-helping-investor-confidence) · [TSMC Q3 thread](https://x.com/StockSavvyShay/status/2110643114268647698) · [CoreWeave bonds thread](https://x.com/rohanpaul_ai/status/2110451515010023703) · [Marcus](https://garymarcus.substack.com/p/generative-ai-in-disarray)
**Raw:** `raw/rss/2026-10-15-the-information-tsmc-to-add-a-new-3nm-fab-as-ai-orders-pile-up.md`, `raw/rss/2026-10-15-the-information-coreweave-co-founders-stock-sales-aren-t-helping-invest.md`, `raw/rss/2026-10-15-marcus-on-ai-generative-ai-in-disarray.md`, X feed captures (private)

## TL;DR

The two ends of the AI hardware stack moved in opposite directions on the same US day. **TSMC Q3:** revenue **$46.7B** (+41% YoY, vs $44.9B est.), net income $23.9B, gross margin 66%, advanced nodes (7nm and below) **79% of wafer revenue**; Q4 guide **$53.3B** (vs $49.1B est.), gross margin 66%, operating margin 58%, and a steep 2nm ramp. It will build **another 3nm fab in Tainan**, producing from 1H 2028, and is reported to be discussing a Texas expansion and Musk's "Terafab" (Musk could own the building, TSMC run the fab). **Neoclouds:** CoreWeave fell ~15.5% after its unsecured 2032 bonds ($1.25B, 9.625%, sold in June) dropped **below 85 cents**, yields near 15%. Q2: net loss $626M versus net interest expense **$640M**, so the interest bill now exceeds the loss. Oracle bonds weakened; Nebius and Dell fell. Gartner is quoted predicting **over 80% of neoclouds will fold** (via ZeroHedge, secondary). The Information notes CoreWeave's CEO sold stock every week April to September.

## Key points

- **Who captures the margin.** TSMC prints 58% operating margin on the same demand that leaves a GPU lessor paying more in interest than it loses. The scarce input (leading-edge wafers, EUV, see ASML sold out to 2028 in the [10-14 digest](../daily-digest/2026-10/2026-10-14.md)) earns monopoly rent; the commodity layer (racked GPUs for rent) carries the leverage.
- **Anthropic's compute ratio** (FT via X): earns **$1.70 per $1 of compute**, putting compute near 59% of revenue, which implies its reported 85% adjusted gross margin excludes much of that spend. Q3 revenue $16.8B (+45% QoQ, down from >100%). This is the demand side the neoclouds are financing.
- **Inference silicon diversification:** Microsoft says in-house Maia becomes its primary inference system ([10-13 OCP/Maia page](2026-10-13-ocp-2026-maia-300-and-tokens-per-watt.md)); an investor post argues Cerebras' on-chip SRAM avoids scarce HBM and wins as agents make dozens of calls per task (OpenAI already buys Cerebras inference). Both are bets that agent latency, not training FLOPs, sets the next hardware margin.
- **Exposure:** Epoch AI estimates chips are 2.7x as large a share of Chinese spending as US spending ($15.2 vs $5.7 per $1,000), widening to 4.7x for Taiwan-made chips. Musk: "China will be making a LOT of RAM in 2028." Domestic producers covered 23% of China's chip demand in 2022.
- **Disaggregation:** IOWN Global Forum demo of ~40 km separation between data and GPU processing at ~1.9% penalty (photonics), a power-and-land play.

## Relation to prior wiki pages

- **Confirms** the [compute economics](compute-economics.md) 10-13 "capital wall" entry: debt-funded capacity is the fragile layer. The [10-12 inference reverse auction](../ai-industry/2026-10-12-inference-reverse-auction-and-capability-funnel.md) predicted spot GPU prices would pressure lessors; bond pricing now says the same thing.
- **Same direction as** ASML (10-14): leading-edge supply stays short through 2028, which keeps foundry and lithography margins high regardless of who rents the GPUs.

Concept pages: [Compute economics](compute-economics.md) · [Memory hierarchy](memory-hierarchy.md)
