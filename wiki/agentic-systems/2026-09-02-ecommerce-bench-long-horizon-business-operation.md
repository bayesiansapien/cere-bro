# E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation

**Source:** HuggingFace Daily Papers, 2026-09-02
**Paper:** [arXiv 2608.30730](https://arxiv.org/abs/2608.30730)
**Code:** [github.com/QwenLM/E-CommerceBench](https://github.com/QwenLM/E-CommerceBench)
**Raw:** [raw/huggingface/2026-09-02-e-commerce-bench-evaluating-llm-agents-on-long-horizon-auton.md](../../raw/huggingface/2026-09-02-e-commerce-bench-evaluating-llm-agents-on-long-horizon-auton.md)

## TL;DR

E-Commerce Bench runs an LLM agent as a merchant for a simulated **365-day year**, operating several online stores at once: researching the market, negotiating with suppliers, sourcing inventory, setting sales strategy, fulfilling orders, handling returns and managing cash flow, with the objective of maximizing end-of-year assets. A calendar of promotions, natural disasters and supply-chain shocks reshapes demand throughout. Both sides of the market are **deterministic** for reproducibility: customer purchases and returns follow a fixed demand model, a negotiation kernel sets supplier pricing and concessions, and an LLM is used only to verbalize those decisions. Across 18 frontier models evaluated on seven dimensions, **no single model dominates**. GPT-5.6 Sol earns the most, growing a 100,000 opening stake to **1,431,425**, yet ranks **16th of 18 on fraud avoidance** and trails Fable5 on operational efficiency. Among open-weight models Qwen3.8-Max-Preview leads at **416,252**, 38% above GLM 5.2 (high), and shows the strongest learning over the horizon by progressively bargaining suppliers down across repeated orders.

## Why the design choices matter

Two of them are the contribution, more than the leaderboard is.

**Determinism on both sides of the market.** Long-horizon agent benchmarks usually have to choose between realism and reproducibility, because a simulated counterparty driven by an LLM makes the environment non-stationary in a way that confounds comparison. E-Commerce Bench keeps the counterparty logic deterministic and uses the language model purely as a surface layer over decisions the kernel already made. That means two runs face the same market, so a score difference is attributable to the agent.

**Seven scoring dimensions, and the top earner losing on most of them.** The single most useful result is the dissociation: the model that maximizes end-of-year assets is nearly the worst at avoiding fraud and is beaten on operational efficiency. A benchmark reporting one number would have declared GPT-5.6 Sol the winner and hidden both facts.

## How this relates to prior wiki pages

**It reproduces, in a business simulation, the finding that has been accumulating on [agent-benchmarks.md](agent-benchmarks.md) all month: single-number agent scores conceal the dimension that actually decides deployability.** The wiki already carries Microsoft's Thinkingbox (08-25), where the strongest model fell from 65.36% pass@1 to 25.25% pass^20 on stateful workflows, so reliability across attempts and headline accuracy came apart. E-Commerce Bench separates a different pair, profit and integrity, and finds them anti-correlated in the same model. **Two benchmarks, two different decompositions, one conclusion: the aggregate was hiding the trade-off.**

**The learning-over-horizon result is the part that connects to efficiency.** Qwen3.8-Max-Preview progressively bargains prices down across repeated orders, which means the agent is accumulating and exploiting counterparty-specific knowledge over a long horizon. That is the same capability [Recuris (08-26)](2026-08-26-recuris-experiential-working-memory.md) measured when one memory-evolution harness lifted ten models by different amounts, with the advantage widening with task horizon to +32.2 on the longest tasks. E-Commerce Bench provides an independent, economically-denominated version of the horizon effect: the payoff to memory is not a benchmark point, it is a purchase price.

**It sharpens the model-harness routing gap in the right currency.** [llm-routing.md](../ai-routing/llm-routing.md) has argued for two months that the routable unit is the model-harness pair and that the field measures cost in the wrong units, citing the AlphaSense study (08-14) where per-token pricing ranked models backwards because stronger models finish in fewer tokens, and Optima (08-16), which shipped quality, cost and time per task as headline metrics. E-Commerce Bench denominates outcome in **dollars of end-of-year assets**, which is the closest thing yet to the cost-per-completed-task currency that page keeps asking for, and it shows a 3.4x spread between the best closed model and the best open-weight one on that axis. A router that could pick per-task on this benchmark would have a directly interpretable objective, and nobody has built one.

## Gaps

Determinism buys reproducibility at the price of adversarial realism: a fixed negotiation kernel cannot adapt to an agent that discovers an exploit, so a high score may reflect kernel-gaming rather than commercial competence, and the paper's own fraud-avoidance dimension hints that some of this is happening. The demand model is fixed, so no agent's pricing affects the market it operates in, which removes the central feedback loop of real retail. One simulated year is a horizon in simulated time, not in tokens or wall-clock, so the compute cost per run is unstated and cannot be compared across the 18 models. And "growing 100,000 into 1,431,425" is a headline that depends entirely on the kernel's margin structure, so it is a within-benchmark comparison only.

## Related

- [agent-benchmarks](agent-benchmarks.md) — the concept page this updates
- [Recuris: experiential working memory (08-26)](2026-08-26-recuris-experiential-working-memory.md) — the horizon effect on memory
- [llm-routing](../ai-routing/llm-routing.md) — cost-per-completed-task as the routing currency
