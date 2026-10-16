---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.223672+05:30
arxiv_id: 2610.19975
url: https://huggingface.co/papers/2610.19975
arxiv_url: https://arxiv.org/abs/2610.19975
date: 2026-10-15
---

# LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation

Looped Mixture-of-Experts (MoE) models combine parameter reuse with sparse computation to improve performance under matched budgets. Prior work demonstrates that different loop visits can play different roles even when they share parameters. To probe the contributions of different loop visits, we learn separate residual coefficients in a model that applies a shared block twice, observing a smaller scale in the first visit. Fixed coefficient experiments show that reducing the first visit's scale preserves or improves performance, whereas the same reductions to the second hurt it. This asymmetry motivates us to explore asymmetric compute allocation. We propose LatentLoop, which compresses the first visit's sequence, retains full resolution in the second, and reallocates saved computation to increase the hidden size. We further learn how strongly the first visit updates the full sequence, and share MoE weights across visits while using separate attention parameters to accommodate their different sequence resolutions. Across 15 configurations spanning 1.3B--7B parameters, with the largest budget exceeding 10^{21} FLOPs, LatentLoop consistently lowers validation NLL. At a fitted NLL of 1.988, predicted compute savings are 19.0\% and 7.9\% relative to vanilla MoE and the looped baseline. It also improves average scores on nine benchmarks at all sizes in 0-shot and 5-shot settings. These results suggest asymmetric compute allocation is a promising direction for looped MoE models.
