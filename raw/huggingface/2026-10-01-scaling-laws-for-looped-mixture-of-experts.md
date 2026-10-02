---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.348755+05:30
arxiv_id: 2609.40316
url: https://huggingface.co/papers/2609.40316
arxiv_url: https://arxiv.org/abs/2609.40316
date: 2026-10-01
---

# Scaling Laws for Looped Mixture of Experts

Looped transformers and Mixture-of-Experts (MoE) offer complementary routes to efficient scaling: recurrence increases computational depth at fixed parameters, while MoE sparsity expands total capacity at fixed active compute. Yet existing scaling laws model recurrence or sparsity in isolation. In this work, we introduce Loop Scaling Laws, the first scaling law to jointly model recurrence and sparsity alongside model size and data. At its core is a bounded, sparsity-conditional recurrence mapping that characterizes the effective-parameter gain from looping and how sparsity raises this gain. The laws predict the held-out loss of looped models more accurately than prior alternatives, and recover the standard dense and MoE scaling laws as special cases. Beyond prediction, the fitted laws provide a principled foundation for designing looped MoE models under compute and memory constraints. Downstream evaluations further demonstrate the complementary benefits of the two axes: sparsity delivers ~3x active-parameter efficiency, recurrence yields ~2x total-parameter efficiency on reasoning, and joint scaling further advances the performance frontier. As a practical extension, we show these gains hold at trillion-token scale: at matched training compute, a looped MoE with law-derived recurrence matches a ~2x larger non-looped MoE on the reasoning benchmarks, while enabling test-time scaling through recurrence.
