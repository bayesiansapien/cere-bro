---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.511410+00:00
arxiv_id: 2610.15965
url: https://huggingface.co/papers/2610.15965
arxiv_url: https://arxiv.org/abs/2610.15965
date: 2026-10-14
---

# Scaling Repeated-Data Pretraining: Batch Size, Regularization, and GPU-Time Tradeoffs

We study pretraining when compute is abundant but unique training data are finite, requiring repeated training on the same data. We first revisit infinite-compute pretraining (Kim et al. 2026) and show that its frontier depends critically on choices previously fixed or studied only in isolation. In particular, optimizing batch size together with epoch counts reveals a U-shaped relationship between validation loss and batch size, favoring smaller batches than typical pretraining, likely because small-batch gradient noise provides implicit regularization. We further find that training recipes, previously optimized under a single-pass assumption, can be tuned, e.g., repacking documents into new sequences every epoch, weight tying, and positive embedding weight decay.
  We then relax the infinite-compute assumption. In particular, smaller-than-typical batch sizes can require prohibitively long sequential training, motivating to treat GPUs and time as separate resources. Tighter deadlines favor larger batches, and latency-oriented parallelism can trade additional GPUs for shorter training. Nevertheless, even under a fixed time budget, a smaller batch with fewer GPUs can achieve lower validation loss than a larger batch with more GPUs, challenging the common practice of increasing data parallelism to maximize GPU utilization under a deadline. Together, our results identify underexplored factors in repeated-data training and provide concrete guidance on how training recipes and resource allocation should change from single-pass pretraining.
