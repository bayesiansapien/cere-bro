---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.04451
url: https://huggingface.co/papers/2605.04451
arxiv_url: https://arxiv.org/abs/2605.04451
date: 2026-05-09
---

# RemoteZero: Geospatial Reasoning with Zero Human Annotations

Geospatial reasoning requires models to resolve complex spatial semantics and user intent into precise target locations for Earth observation. We introduce RemoteZero, a box-supervision-free framework for geospatial reasoning. RemoteZero replaces geometric supervision with intrinsic semantic verification and enables GRPO training without box annotations, motivated by the observation that an MLLM is typically better at verifying whether a region satisfies a query than at directly generating precise coordinates. The resulting framework further supports iterative self-evolution, allowing the model to improve from unlabeled remote sensing imagery through its own verification signal. RemoteZero achieves 71.29% test Acc@0.5, outperforming the strongest supervised baseline RemoteReasoner by 3.18 percentage points.
