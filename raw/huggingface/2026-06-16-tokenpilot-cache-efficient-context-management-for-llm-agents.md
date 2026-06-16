---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.17016
url: https://huggingface.co/papers/2606.17016
arxiv_url: https://arxiv.org/abs/2606.17016
date: 2026-06-16
---

# TokenPilot: Cache-Efficient Context Management for LLM Agents

As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, Ingestion-Aware Compaction acts as a framework harness to stabilize prompt prefixes and eliminate open-world environmental noise at the ingestion gate. Locally, Lifecycle-Aware Eviction monitors the ongoing residual utility of context segments, enforcing a conservative batch-turn schedule to offload content segments only when task relevance expires. Experiments on PinchBench and Claw-Eval under both isolated and continuous modes demonstrate that TokenPilot reduces costs by 61% and 56% in isolated mode, and 61% and 87% in continuous mode, while maintaining competitive performance compared to prior systems. TokenPilot has been integrated into LightMem2 at https://github.com/zjunlp/LightMem2.
