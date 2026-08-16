# Compute Economics (GPU pricing, utilization, and the durability of a chip)

**Concept page.** How AI compute is priced, rented, financed, and depreciated, and what that does to who can train a model. This page exists because the wiki accumulated five separate sources on GPU price formation in under two weeks and had nowhere to put the pattern.

The one-line state of knowledge as of 2026-08-14: **compute has moved from a capacity market to a scarcity market, prices are being set by auction rather than by contract, and the incidence falls hardest on the smallest trainers.**

---

## The vendor became the lender, and the number moved twice in two days (2026-08-16)

**Nvidia is now financing the demand for its own hardware at a scale that is difficult to distinguish from vendor-financed revenue, and the size of that commitment is visibly unstable.** Within 48 hours the reported figure for OpenAI's planned Ohio datacenter campus moved from **$250 billion down to just under $120 billion** after investor pushback on the risk ([The Decoder, 08-15](https://the-decoder.com/investor-pressure-forces-nvidia-to-shrink-its-openai-bet-just-as-anthropics-numbers-defy-bubble-warnings/)), while The Information reported Nvidia **close to a deal guaranteeing around $100 billion** in credit covering roughly half the project across a two-year first phase, with a second phase of similar magnitude to follow ([08-15](https://www.theinformation.com/articles/nvidia-nears-deal-guarantee-100-billion-financing-massive-data-center)). Separately Nvidia is in talks to invest **up to $3 billion in SB Energy**, the SoftBank-backed developer of that same campus ([The Information, 08-15](https://www.theinformation.com/articles/nvidia-talks-invest-3-billion-sb-energy-part-openai-data-center-deal)).

*Why this belongs on this page rather than in an industry log.* Everything above about the auction regime describes prices set by scarcity between independent buyers and sellers. Credit support at this scale is a supplier removing the buyer's financing constraint so the buyer can keep bidding, which is the opposite mechanism. It also cuts directly against the incidence finding recorded above: **a rising spot price squeezes neolabs precisely because nobody guarantees their credit, and the largest buyer in the market just had $100 billion of its credit guaranteed by the seller.** The concentration effect the price regime produces is being amplified by the financing structure rather than offset by it.

*The counterweight, which is real.* Anthropic's quarterly revenue went from $787 million a year ago to **$4.73 billion in Q1 and $11.5 billion in Q2** ([The Information, 08-14](https://www.theinformation.com/briefings/anthropic-revenue-jumped-14-times-second-quarter)), which is the strongest available argument that the demand being financed is not imaginary. Both things are true at once: revenue is compounding at a rate that justifies aggressive buildout, and the buildout's financing is increasingly circular.

## The unit of cost is finally being measured, and it is not the token (2026-08-16)

Three items landed the same day and together they invalidate the metric this page and most of the wiki has been using.

- **A 24x dollar spread on one identical completed task.** DHH ran the same Rust rewrite of the TerminalTextEffects library across five frontier models, all working from a plan Fable 5 wrote: **$550 on Fable in 45 minutes, $55 on Grok 4.6 in 1.5 hours, $43 on GPT Sol, $23 on DeepSeek Pro V4 Max in 2.5 hours**, with DeepSeek V4 Flash and GPT Luna failing to complete ([@dhh](https://x.com/dhh/status/2088657836586807687)). The trade it exposes is time for money, and at any realistic engineer hourly rate the $527 premium does not buy back the 1.75 hours saved, so the expensive tier is rational only when a human is blocked on the result.
- **A token is not a token across vendors.** Anthropic's Tibo Sottiaux publicly put OpenAI's tokenizer at roughly **30% more efficient** per unit of text, with a circulated comparison putting the total at **34.5%** across 493 words and **53.2% on multilingual prose** ([post](https://x.com/thsottiaux/status/2088856449959276836)). Because API and usage plans bill per token, two vendors quoting the same dollars per million tokens are not quoting the same price. **Every cost comparison on this page and in the routing literature is denominated in a unit that differs by up to a third between providers, and nobody normalises for it.**
- **The instrument shipped.** Artificial Analysis launched [Optima](../ai-industry/2026-08-16-optima-cost-per-task-benchmarking.md), which benchmarks models on the user's own data by quality, **cost, and time per task** rather than by token price. The [08-14 Looking Ahead](../daily-digest/2026-08/2026-08-14.md) predicted a major leaderboard would make dollars-per-completed-task its primary metric within 60 days. It took two.

**The synthesis worth carrying forward.** A 34.5% tokenizer penalty is the same order of magnitude as the headline savings from this month's best efficiency research: Gambit's 68.5% token reduction, AutoPrune's 9.9x FLOP cut. That means a serving stack can adopt a state-of-the-art token-reduction technique and have most of the gain erased by a vendor choice that appears in none of those papers. **Cost-per-task is the only unit in which those two effects are commensurable, and until this week nobody was publishing it.**

---

## The current price regime (2026-08)

Three data points from the same week, which line up unusually cleanly:

- **Nebius held its first auction of computing capacity in Q2 2026 and cleared Blackwell-generation capacity at "15% above the highest price we ever charged before"** (CEO Arkady Volozh, earnings call, reported by [The Information, 08-13](https://www.theinformation.com/articles/nebius-coreweave-cashing-soaring-ai-compute-prices)). Nebius also said it is deliberately selling capacity *closer* to when customers need it, to capture the spot premium instead of locking it away in forward contracts. That is a supplier consciously converting a contract business into a spot business.
- **Contract durations are collapsing and volumes are being rationed.** Evan Morikawa of robotics-model startup Generalist talked to about 17 different AI cloud providers hunting compute, and reported that a year earlier he could get reasonable prices on contracts as short as one year; six months into that contract, needing roughly a thousand more chips, the market had changed ([The Information, 08-13](https://www.theinformation.com/articles/ai-compute-crunch-hitting-neolabs-especially-hard)). His line, "it's like VC currency right now to know the current price of GPUs," is a market-microstructure observation: when the price of an input becomes private information, the input is scarce.
- **Nvidia's market capitalization moved $1 trillion above Apple's over roughly two weeks**, an 18% Nvidia rise against a ~10% Apple fall. Broad macro explains part of it; chip rental prices going "through the roof" is the part that belongs on this page.

**Who pays.** The incidence is not uniform. Hyperscalers hold forward contracts and their own capacity. The hardest-hit class is what The Information calls **neolabs**: startups training their own frontier or domain models, who need hundreds to thousands of chips, have finite venture funding, and cannot outbid a hyperscaler in an auction. The structural consequence is that a rising spot price does not slow frontier training, it slows *independent* frontier training, which is a concentration effect rather than a slowdown.

---

## The other side: durability, fungibility, and why old GPUs stay valuable

The scarcity story has a counterpart that is easy to miss. Jensen Huang's argument, made in response to CoreWeave committing to Nvidia A100s through 2029 ([@JensenHuang, 08-13](https://x.com/JensenHuang/status/2087755674650603534)), is that the useful life of an Nvidia GPU is set by software, not silicon:

> CUDA gives developers and NVIDIA engineers a common platform to continually upgrade Ampere, Hopper and Blackwell throughout their useful lives. CUDA makes NVIDIA computing versatile. Versatility makes it fungible. Fungibility drives utilization and extends durability, making NVIDIA compute a productive asset: rentable, durable and financeable.

Read as an economic claim rather than marketing, this is a chain of four steps: a common software platform → versatility → fungibility → high utilization → long depreciable life → **financeable**. The last word is the point. An asset with a predictable multi-year utilization curve can be borrowed against, which is what lets a CoreWeave or a Nebius build out at scale without equity-funding every rack. The A100 fleet being "mission-capable from 2020 through 2029" is not a nostalgia claim; it is a statement about the denominator in a depreciation schedule.

This is the same argument the wiki recorded in [Nvidia and compute as an asset class (08-11)](../ai-industry/2026-08-11-nvidia-compute-asset-class.md), now with a named nine-year fleet life attached.

**The tension worth holding.** High spot prices and long asset lives are both good for the supplier and pull in opposite directions for the buyer. A nine-year-durable A100 is exactly what makes renting rational for a small trainer, and a 15%-above-record auction clear is exactly what makes it unaffordable. Whether the second-hand and older-generation market becomes the neolab's escape hatch, or whether older capacity is simply absorbed by inference demand, is the open question. Nobody in the sources has priced A100-hours against Blackwell-hours per unit of useful training work.

---

## Why this connects to inference efficiency (the Tier 1 link)

Compute price is the denominator under every efficiency result this wiki tracks, and in 2026-08 it started moving fast enough to change conclusions:

- **A quantization or KV-cache result is worth its savings times the price of the compute it saves.** When Blackwell-hour prices clear 15% above record, every efficiency paper's economic value rises by the same factor without a single new experiment.
- **Provider pricing is now an efficiency variable in its own right.** [DeepSeek repriced cache-hit tokens to roughly 6x (08-14)](../inference-efficiency/2026-08-14-deepseek-harness-kv-cache-economics.md) while introducing a peak/off-peak split with off-peak 50% below peak. That makes *when* you run as consequential as *how* you run, and no routing formulation in the wiki has a time-of-day term.
- **Token price is not task cost.** The [AlphaSense study (08-14)](../ai-industry/2026-08-14-alphasense-token-price-vs-task-cost.md) found GPT-5.6 Sol and Opus 4.8 producing better answers at *lower total cost* than Kimi K3 and GLM-5.2 on financial-document analysis, despite charging $25 to $30 per million output tokens against Kimi's $15, because a smarter model finishes the task in fewer tokens. Any compute-economics claim stated in dollars-per-token is therefore only half a claim.

---

## Open problems

1. **A published cost-per-completed-task series across GPU generations.** Everyone quotes dollars per GPU-hour and dollars per million tokens. Nobody publishes dollars per solved task on fixed hardware over time, which is the only series that would show whether efficiency research is outrunning price inflation.
2. **Does the spot premium reach inference, or only training?** All three 08-13 data points concern training capacity. Inference is the larger and stickier market, and a spot regime there would reprice every deployed product.
3. **Where the neolabs go.** If auction pricing persists for two more quarters, the falsifiable outcomes are: they move to older generations, they move to non-Nvidia silicon, they stop pre-training and start post-training only, or they get acquired. All four are observable.
4. **Whether nine-year fleet life survives an architecture break.** The CUDA-continuity argument has never been tested against a discontinuity large enough to strand a generation. Low-precision-native training would be a candidate.

---

## Sources

- [Nebius, CoreWeave cashing in on soaring AI compute prices](https://www.theinformation.com/articles/nebius-coreweave-cashing-soaring-ai-compute-prices) (The Information, 08-13) · [raw](../../raw/rss/2026-08-13-the-information-nebius-coreweave-are-cashing-in-on-soaring-ai-compute-p.md)
- [Why the AI compute crunch is hitting neolabs especially hard](https://www.theinformation.com/articles/ai-compute-crunch-hitting-neolabs-especially-hard) (The Information, 08-13) · [raw](../../raw/rss/2026-08-13-the-information-why-the-ai-compute-crunch-is-hitting-neolabs-especially.md)
- [@JensenHuang on A100 fleet durability and fungibility](https://x.com/JensenHuang/status/2087755674650603534) (08-13) · [raw](../../raw/twitter/2026-08-13-afternoon.md)
- [Nvidia and compute as an asset class (08-11)](../ai-industry/2026-08-11-nvidia-compute-asset-class.md)
- [Token price is not task cost: the AlphaSense study (08-14)](../ai-industry/2026-08-14-alphasense-token-price-vs-task-cost.md)
- [DeepSeek Harness v0.1 and the price of a cache hit (08-14)](../inference-efficiency/2026-08-14-deepseek-harness-kv-cache-economics.md)

## Related pages

- [Memory hierarchy](memory-hierarchy.md)
- [GPU kernels](gpu-kernels.md)
- [KV cache](../inference-efficiency/kv-cache.md)
- [LLM routing](../ai-routing/llm-routing.md)
