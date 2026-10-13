---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.222449+05:30
arxiv_id: 2610.13171
url: https://huggingface.co/papers/2610.13171
arxiv_url: https://arxiv.org/abs/2610.13171
date: 2026-10-12
---

# PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling

Power sampling improves large language model (LLM) reasoning at test time by sampling from a sharpened version of the base model's distribution. Its sampler, PowerMH, is slow because its Metropolis--Hastings (MH) updates are sequential: each accept/reject decision sets the state from which the next proposal is generated. Prior work reduces this cost by changing the sampler or the model (e.g., sequential Monte Carlo, approximate lookahead, distillation). We propose Predictive SubTree Prefetching (PreSTO), which accelerates PowerMH by prefetching future proposals and provably leaves its MH transition kernel unchanged. PreSTO views future MH outcomes as a tree of accept/reject decisions: in each model call, it generates the proposals of a prefetched subtree of this tree in one batch, then follows the realized path with the original MH acceptance rule. We also observe that MH reaches only a sparse, nearly unary part of each prefetched subtree, we further design a predictive traversal rule that chooses the subtree to maximize the predicted number of completed transitions. Across seven datasets and five base LLMs, PreSTO achieves median speedups of 1.71times, 1.91times, and 2.33times on PowerMH and its follow-ups EntropyCut and MultiTryMH, respectively; on the first two, it makes a median of 3.9times fewer model calls, each only 2.1times longer. On LCB V6 with Qwen3.5-9B, the predictive traversal rule is a further 1.25times--1.37times faster than the default breadth-first traversal.
