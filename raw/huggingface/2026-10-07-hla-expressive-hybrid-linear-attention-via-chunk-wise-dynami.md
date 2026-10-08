---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.05842
url: https://huggingface.co/papers/2610.05842
arxiv_url: https://arxiv.org/abs/2610.05842
date: 2026-10-07
---

# HLA: Expressive Hybrid Linear Attention via Chunk-Wise Dynamic Mixing

Linear attention enables efficient long-context autoregressive decoding by compressing history into recurrent states, but this compression can make selective access to sparse and distant information difficult. Existing chunk-based extensions increase memory capacity, yet learned chunk-mixing coefficients may remain fixed with respect to input content and therefore cannot adapt historical access to each query. We introduce Hybrid Linear Attention (HLA), a query-dependent chunk-level attention mechanism for Gated DeltaNet (GDN). HLA represents each completed chunk as an exact affine state transition and computes content-dependent routing gates from compact, self-attentively pooled representatives. Each gate interpolates the corresponding historical transition with the identity map, controlling both the chunk's additive memory and its transformation of earlier states. Effective-support regularization further encourages concentrated routing for sparse inference. We evaluate HLA under both pretrained adaptation and from-scratch training. Across Qwen3.5 models from 0.8B to 9B, HLA consistently improves over native GDN and fixed chunk mixing, with gains of up to 5.57 percentage points on LongBench-V2 and 3.97 points on RULER. In a controlled from-scratch 1.3B setting trained for 100B tokens with a 4K context, HLA also improves RULER performance from 4K to 32K, with gains increasing from 0.83 points at 4K to 4.22 points at 32K. These results demonstrate that query-dependent composition of recurrent memory improves long-context modeling and remains effective beyond the training context while using compact per-chunk affine summaries. Project page: https://caesarhhh.github.io/hla/
