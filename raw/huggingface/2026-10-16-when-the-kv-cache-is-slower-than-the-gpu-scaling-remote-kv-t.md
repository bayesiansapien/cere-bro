---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.21500
url: https://huggingface.co/papers/2610.21500
arxiv_url: https://arxiv.org/abs/2610.21500
date: 2026-10-16
---

# When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill

Reusing the attention KV cache across requests is a standard way to cut prefill cost in long-context LLM serving, and production systems increasingly back the per-engine cache with a remote tier shared by every engine. We study such a tier in a disaggregated deployment of GLM-5.3, an FP8 mixture-of-experts model with multi-head latent attention (MLA), on 8xB300 nodes running prefill context parallelism (PCP8). Enabling the remote tier (LMCache with a Valkey store) left median time-to-first-token unchanged but raised the 16k-token p99 from 3.96 s to 17.3 s. Replaying a production request stream on an isolated engine, we find that a remote hit took 0.88 s against 0.31 s to recompute the prompt, and that synchronous loading turned a hit-heavy stream into an unstable queue: p99 83.32 s with the GPUs 7% busy. A two-term cost model explains both: a hit pays off only if the tier delivers more than B* = sR (2.53 GB/s for this model and GPU), and a fixed per-hit engine cost (T0 ~ 0.33 s) means that hits on prompts shorter than about 17k tokens cannot beat recompute at any bandwidth. Guided by the model, we (i) shard the MLA KV store across PCP ranks, with a proof that the existing minimum-over-ranks lookup returns the longest cached prefix and a load protocol that can never desynchronize collectives; (ii) partition the remote tier by rank, one server instance per rank with no coordination, which raises GET bandwidth 6.3x to 10.76 GB/s; (iii) add asynchronous loading to the sharded store; and (iv) fix three client bugs that caused unbounded stalls. On the hit-heavy stream, with 98.5% of prompt tokens served from the remote tier, p99 falls from 83.32 s to 0.67 s. The sharded store raises prefill throughput by 14%, and by 34% together with an upstream kernel fix. All changes are submitted upstream to LMCache.
