# r/MachineLearning | 2026-05-28 IST | sort=top
> Scraped 2026-05-28 09:02 IST | lookback=24h | tier_default=2
> Filter to [R]/[P]/Research/Project flair only — drops the [D] discussion noise. Generic news is excluded.

### AI-generated CUDA kernels silently break training and inference [R]

**Meta:** score=157 · comments=14 · tier=2 · flair=Research · posted=2026-05-27 16:35Z
**Author:** u/laginimaineb
**Reddit:** [https://www.reddit.com/r/MachineLearning/comments/1tpaw6x/aigenerated_cuda_kernels_silently_break_training/](https://www.reddit.com/r/MachineLearning/comments/1tpaw6x/aigenerated_cuda_kernels_silently_break_training/)

Last month NVIDIA released [SOL-ExecBench](https://research.nvidia.com/benchmarks/sol-execbench), a new benchmark of 235 production CUDA kernels lifted from DeepSeek, Qwen, Gemma, and Kimi. We took several top-ranked AI-generated submissions and tried using them in production workloads. Many of them broke, sometimes in surprising ways.

One of those kernels is the fused embedding-gradient + RMSNorm backward pass, which runs at the end of every transformer training step. We took the fastest submission on the benchmark for it, and dropped it into the training loop of a small transformer. The kernel had passed the benchmark's verifier with room to spare. But in our training run, the loss diverged and never recovered.

We started debugging. Replace the dataset distribution with uniformly sampled tokens, the divergence vanishes. Swap SGD for AdamW, also vanishes.

This is the worst kind of bug for research. Symptoms and masks both look exactly like "the idea didn't work". It's the type of bug that can make researchers spend a long time debugging without knowing what's at fault: the dataset? the research idea? the architecture? or the implementation itself?

Turns out, the actual bug is that the embedding-gradient half of the kernel accumulates in bf16 instead of fp32. Embedding backward sums many small gradient contributions into each token's row of the embedding matrix. With uniform random tokens the contributions spread evenly and bf16 precision is enough. In real text, a handfu

[…truncated, see permalink]

---
