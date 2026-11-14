---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.528255+00:00
arxiv_id: 2611.05984
url: https://huggingface.co/papers/2611.05984
arxiv_url: https://arxiv.org/abs/2611.05984
date: 2026-11-13
---

# On the Design of Hyper-Connections: Simplification, Stability, and Scalability

Hyper-Connections (HC) architectures are increasingly adopted in frontier language models, yet their components remain insufficiently understood and introduce non-negligible training overhead. In this work, we systematically study the HC architecture to understand its components and identify simpler, more efficient designs. We find that learned read/write gating without mixing and unconstrained mixing with fixed gates form two effective interaction groups: either alone achieves performance comparable to mHC. We also identify repeated access to the expanded residual state as a major source of training overhead, even without mixing. These findings lead to SimpleHC, which simplifies the architecture by removing residual mixing and simplifies execution through shared memory access, using the resulting additive structure and shared gate inputs. Layer-specific gates share a group-entry state, enabling batched reads and deferred writes; scalar corrections exactly preserve preceding sublayer output contributions. Our analyses support both the retained residual structure and the design of shared memory access. SimpleHC incurs only 2.4% extra end-to-end training time over a vanilla residual baseline at the largest tested scale. It maintains performance comparable to mHC when scaling from 15B to 30B MoE models, exhibits smoother gradient dynamics during standard training, and remains stable under stress. We hope SimpleHC will encourage a broader pursuit of simplicity in foundation model design, making performance gains more accessible and practical at scale.
