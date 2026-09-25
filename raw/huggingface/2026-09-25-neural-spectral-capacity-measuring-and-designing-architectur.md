---
source: farmer/huggingface
farmed: 2026-09-25T22:51:58.846051
arxiv_id: 2609.23087
url: https://huggingface.co/papers/2609.23087
arxiv_url: https://arxiv.org/abs/2609.23087
date: 2026-09-25
upvotes: 5
---

# Neural Spectral Capacity: Measuring and Designing Architectures from Network Specification Alone

Modern Transformer design and compression both reduce to allocating capacity under a budget. The standard scalars for these decisions, #Params and #FLOPs, capture size and compute but not architectural structure: two architectures with identical parameter budgets but different depth-width, head, or FFN allocations receive identical scores yet behave differently. We propose Neural Spectral Capacity (NSC), a closed-form scalar grounded in the singular-value spectrum of each weight matrix. Under standard random initialization, the Marchenko-Pastur law renders NSC computable from the architectural specification alone, with no model instantiation, data, or gradients. Its layer-wise additive structure admits NSC-DP, an exact dynamic-programming solver returning the architecture globally maximizing NSC under resource constraints in seconds on a CPU -- a guarantee that black-box search over existing training-free proxies cannot provide. Empirically, NSC outperforms #Params, #FLOPs, and representative training-free proxies in ranking across seven Transformer and CNN families (on FlexiBERT, τ= 0.505 on pairs differing in #Params by less than 10%, where #Params collapses to 0.082); NSC-DP discovers a Transformer-XL architecture on WikiText-103 that beats the human-designed baseline in 2 seconds; and prunes LLaMA-7B to the best 5.7B model across eight commonsense reasoning tasks without any calibration data, about 5900x faster than the strongest training-free proxy baseline.
