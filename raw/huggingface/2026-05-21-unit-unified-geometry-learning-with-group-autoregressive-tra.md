---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.21131
url: https://huggingface.co/papers/2605.21131
arxiv_url: https://arxiv.org/abs/2605.21131
date: 2026-05-21
---

# UniT: Unified Geometry Learning with Group Autoregressive Transformer

Recent feed-forward models have significantly advanced geometry perception for inferring dense 3D structure from sensor observations. However, its essential capabilities remain fragmented across multiple incompatible paradigms, including online perception, offline reconstruction, multi-modal integration, long-horizon scalability, and metric-scale estimation. We present UniT, a unified model built upon a novel Group Autoregressive Transformer, which reformulates these seemingly disparate capabilities within a single framework. The key idea is to treat groups of sensor observations as the basic autoregressive units and predict the corresponding point maps in an anchor-free and scale-adaptive manner. More specifically, diverse view configurations in both online and offline settings are naturally unified within a single group autoregression process. By varying the group size, online mode operates over multiple autoregressive steps with single-frame groups, whereas offline mode aggregates a multi-frame group in a single forward pass. Meanwhile, a queue-style KV caching mechanism ensures bounded autoregressive memory over long horizons. This is enabled by reducing long-range dependencies on early frames through anchor-free relational modeling, thereby allowing outdated memory to be discarded on the fly. To improve metric-scale generalization across scenes, a scale-adaptive geometry loss is further introduced within this framework. It couples relative geometric constraints with a partial absolute scale term, implicitly regularizing global scale and inducing a progressive transition from scale-invariant geometry to metric-scale solutions. Together with a dedicated modal attention module for integrating auxiliary modalities, UniT achieves state-of-the-art performance in unified geometry perception, as validated on ten benchmarks spanning seven representative tasks.
