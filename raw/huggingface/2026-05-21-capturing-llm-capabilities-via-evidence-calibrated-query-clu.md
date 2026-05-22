---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.17110
url: https://huggingface.co/papers/2605.17110
arxiv_url: https://arxiv.org/abs/2605.17110
date: 2026-05-21
---

# Capturing LLM Capabilities via Evidence-Calibrated Query Clustering

Query clustering organizes queries into groups that reflect shared latent capability demands, enabling capability-aware LLM evaluation. Existing clustering methods, which primarily rely on semantic taxonomies or embeddings, often fail to capture such latent capability requirements due to a misalignment between surface-level semantics and actual model performance. We propose ECC, an algorithm that calibrates prior semantic embeddings using limited posterior model comparisons to bridge the gap between surface-level semantics and latent capability requirements. ECC characterizes each cluster through a capability profile parameterized by a Bradley-Terry model and uses trainable mixture weights to accommodate queries with mixed capability demands, jointly learning a flexible, capability-aware clustering structure that supports query-specific inference of LLM capabilities. Extensive quantitative and qualitative evaluations demonstrate that ECC significantly improves LLM capability ranking quality, outperforming human-labeled and embedding-based baselines by an average of 17.64 and 18.02 percentage points, respectively, and proves effective in downstream tasks such as query routing.
