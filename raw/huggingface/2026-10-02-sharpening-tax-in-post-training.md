---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.816989+00:00
arxiv_id: 2610.01509
url: https://huggingface.co/papers/2610.01509
arxiv_url: https://arxiv.org/abs/2610.01509
date: 2026-10-02
---

# Sharpening Tax in Post-Training

An emerging hypothesis about reinforcement learning (RL) post-training of large language models (LLMs) is that it merely sharpens existing behaviors of a base model, improving single-shot accuracy at the cost of solution coverage. Although this trade-off has been observed in math and coding tasks, it need not extend to agentic tasks, where multi-turn tool use and interaction may require capabilities newly acquired during post-training. Our surprising finding is that pre-trained LLMs, equipped with a light inference harness, can serve as capable agents. Despite far lower accuracy (pass@1), they often surpass their post-trained counterparts in solution coverage (pass@K) given a sufficient test-time budget. We further analyze the underlying mechanism and show that post-training pushes tasks toward two extremes, always solved or never solved, and thereby improves sampling efficiency and consistency at the cost of solution coverage. To measure this cost, we propose Sharpening Tax, a diagnostic metric that quantifies the loss in test-time scalability after post-training. Across 14 base/post-trained model pairs from four families and three agentic benchmarks (42 cases in total), the tax is prevalent in most settings, can be estimated from a few rollouts, and correlates well with other metrics. Finally, we present posterior-tempered group sampling (PTGS), a simple plug-and-play Bayesian sampler that adapts the sampling temperature per prompt to its estimated difficulty. Applied during RL training in two agentic environments, PTGS pays a smaller tax than the fixed-temperature baseline, solving more tasks under repeated sampling while also improving single-shot accuracy.
