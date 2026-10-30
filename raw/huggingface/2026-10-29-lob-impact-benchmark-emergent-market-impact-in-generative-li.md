---
source: farmer/huggingface
farmed: 2026-10-30T18:38:23.926686+05:30
arxiv_id: 2610.27100
url: https://huggingface.co/papers/2610.27100
arxiv_url: https://arxiv.org/abs/2610.27100
date: 2026-10-29
---

# LOB-Impact Benchmark: Emergent Market Impact in Generative Limit Order Book Models

Realistic market impact is essential for generative limit order book (LOB) models to serve as world models for trading agents. If a simulator misprices this mechanism, agents learn policies that are optimal in the simulator but wrong in the real market. Existing metrics assess generated streams purely through distributional comparison with historical data, leaving counterfactual response to an agent's own orders largely unexplored. Here, we show that market impact emerges naturally in neural LOB generators trained solely for next-token prediction. We inject execution-style metaorders into the generated message flow of five autoregressive models across five NASDAQ stocks and measure the response using estimators from the empirical impact literature, validated on baselines whose physics is known in advance. Our benchmark evaluates any message-level generator in three phases: free generation (reading order-flow persistence against price diffusivity); metaorder injection (yielding the impact law's exponent and amplitude); and a post-execution window (measuring relaxation). In addition, comparing each visible injection to a blind, simulator-only control isolates the model's learned response from standard book mechanics. For every model on every stock, we measure how the impact responds as a function of cumulative metaorder participation. Interestingly, we observe emergent impact in generative models of market data, with exponents in the range of 0.63 to 1.21, slightly above the traditional 0.5 of the square-root law of impact. In the family of models tested, we are so far unable to observe impact decay during relaxation. We tentatively attribute this to the still-short context windows of the models. We release the benchmark as open source to validate future generative models for market data.
