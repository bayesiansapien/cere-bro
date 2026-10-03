---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820697+00:00
arxiv_id: 2609.37362
url: https://huggingface.co/papers/2609.37362
arxiv_url: https://arxiv.org/abs/2609.37362
date: 2026-10-02
---

# Pretrain Once, Route Anywhere: Towards a Foundation Model for LLM Routing

Large language model (LLM) routing aims to assign each query to the most suitable model from a heterogeneous candidate pool, improving the quality--efficiency trade-off of LLM inference. Existing routers are typically learned through local fitting: a router is optimized for a particular query workload and candidate pool, and often requires additional supervision or retraining as the routing environment changes. We ask whether LLM routing can instead be approached from a foundation-model perspective, learning a reusable routing capability that generalizes across tasks, candidate models, and deployment conditions. To this end, we introduce RouteFM, which learns to characterize anonymous candidate models from behavioral context and infer their target-specific capabilities, rather than binding routing decisions to fixed model identities or a single environment. Through episodic pretraining across heterogeneous routing environments, this capability can be reused by a frozen router and adapted to new environments through context alone. Experiments demonstrate transfer across changes in domains, modalities, candidate pools, and context budgets, with the largest gains when behavioral evidence is limited. On MMR-Bench, which is excluded from pretraining, RouteFM outperforms the strongest baseline by 2.23 quality points with only eight observations per candidate. These results support moving LLM routing from repeated local fitting toward a pretrain once, route anywhere paradigm. Our code is publicly available at https://github.com/LAMDA-Model-Reuse/RouteFM.
