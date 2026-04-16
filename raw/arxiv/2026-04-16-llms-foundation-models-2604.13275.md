---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13275
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13275
published: 2026-04-16
authors: Dikshant Kukreja (IIIT Delhi, India), Kshitij Sah (IIIT Delhi
---

# Better and Worse with Scale: How Contextual Entrainment Diverges with Model Size

**arXiv:** https://arxiv.org/abs/2604.13275
**Authors:** Dikshant Kukreja (IIIT Delhi, India), Kshitij Sah (IIIT Delhi

## Abstract

arXiv:2604.13275v1 Announce Type: cross  Abstract: Larger language models become simultaneously better and worse at handling contextual information -- better at ignoring false claims, worse at ignoring irrelevant tokens. We formalize this apparent paradox through the first scaling laws for contextual entrainment, the tendency of models to favor tokens that appeared in context regardless of relevance. Analyzing the Cerebras-GPT (111M-13B) and Pythia (410M-12B) model families, we find entrainment follows predictable power-law scaling, but with opposite trends depending on context type: semantic contexts show decreasing entrainment with scale, while non-semantic contexts show increasing entrainment. Concretely, the largest models are four times more resistant to counterfactual misinformation than the smallest, yet simultaneously twice as prone to copying arbitrary tokens. These diverging trends, which replicate across model families, suggest that semantic filtering and mechanical copying are functionally distinct behaviors that scale in opposition -- scaling alone does not resolve context sensitivity, it reshapes it.
