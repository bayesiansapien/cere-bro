---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.23787
url: https://huggingface.co/papers/2610.23787
arxiv_url: https://arxiv.org/abs/2610.23787
date: 2026-10-19
---

# DLite: History-free Speculative Decoding for Agentic AI

Speculative decoding has become a mainstream technique for accelerating large language model (LLM) inference by using a lightweight draft model to generate candidate tokens that are subsequently verified by the target model. However, agentic workloads introduce long and continuously evolving contexts and frequent multi-turn interactions. Under such workloads, we observe that existing draft models suffer from up to an 80% degradation in acceptance length, while maintaining their historical KV cache introduces substantial system overhead. In this paper, we identify the growing historical context as a common source of both problems and introduce DLite, a history-free speculative decoding framework for agentic AI. DLite directly reuses contextual hidden states from the target model and performs local speculative prediction without explicitly maintaining the historical context, transforming an increasingly complex modeling problem into local simple prediction problem. A lightweight sequential head further restores intra-block causal dependencies with low overhead. To effectively train this heterogeneous history-free architecture, we introduce a tailored two-stage training strategy. Experiments on general-purpose, long-context and agentic workloads show that DLite achieves 2-6 acceptance length and outperforms the state-of-the-art speculative decoding method, DSpark, up to 70%.
