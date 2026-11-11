---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.328099+00:00
arxiv_id: 2611.09987
url: https://huggingface.co/papers/2611.09987
arxiv_url: https://arxiv.org/abs/2611.09987
date: 2026-11-10
---

# Stochastic Deep Supervision for Gallery-Consistent Early-Exit Face Recognition

Vision Transformers (ViTs) perform strongly in face recognition (FR), yet their fixed-depth inference limits deployment in resource-constrained settings. We propose SD-ViT, a training framework that gives a usable exit at every block depth by making every depth produce discriminative embeddings, for budget-selected fixed-depth exits. Standard ViTs supervise intermediate layers only through backpropagation, so their intermediate representations are not directly optimized to form usable identity embeddings. SD-ViT adds a stochastic auxiliary signal: at each iteration a randomly selected intermediate block is passed through the same embedding head as the final layer and trained with a weighted margin-penalty softmax loss. The objective is thus stochastically sampled deep supervision through a shared classifier. Because both loss terms share that head and classifier, intermediate tokens are trained to map into the same embedding space as final-layer tokens. This matters for FR, where matching is by similarity: a probe processed at an early exit can be compared directly against full-depth gallery embeddings, with no gallery recomputation or adaptation layers. On established benchmarks, SD-ViT stays within 0.4 IJB-C points of the same backbone trained conventionally at full depth, while its early-exit probes recover over 96% of their own full-depth performance at 50% of the computational cost without modifying the reference gallery. A single verification threshold calibrated at full depth remains usable from quarter depth onward.
