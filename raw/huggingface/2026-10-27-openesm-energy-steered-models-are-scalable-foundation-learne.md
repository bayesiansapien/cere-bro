---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33005
url: https://huggingface.co/papers/2610.33005
arxiv_url: https://arxiv.org/abs/2610.33005
date: 2026-10-27
---

# OpenESM: Energy-Steered Models Are Scalable Foundation Learners

Energy-based models have shown promising properties for domain-specific tasks but remain challenging in modeling general-purpose scenarios. To bridge this gap, we design energy-steered models (ESMs) for foundational language modeling. ESMs integrate energy steering and token generation within a single architecture to leverage the energy-guided search to refine token generation. Specifically, ESMs first optimize a latent state over the energy landscape, then leverages the refined latent state for token generation. By performing such energy-guided pre-training on large-scale corpora, ESMs learn generally effective energy landscape where favorable tokens correspond to lower energy values. To explore the scaling behavior of ESMs, we pre-train ESMs on three large-scale corpora, then evaluate across 26 downstream tasks spanning a broad range of domains. Our results demonstrate that ESMs have promising scaling behaviors with increasing model size and training data, and outperform GPTs on most downstream tasks. These findings highlight ESMs as a promising architecture for large-scale pre-training and general purpose problem solving. We fully release the model weights and training infrastructure to enable the community to completely reproduce and extend our results.
  GitHub: https://github.com/datamllab/openesm HuggingFace: https://huggingface.co/collections/guan-wang/openesm
