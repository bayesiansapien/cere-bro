---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.930485+00:00
arxiv_id: 2609.34972
url: https://huggingface.co/papers/2609.34972
arxiv_url: https://arxiv.org/abs/2609.34972
date: 2026-09-29
---

# Just MLPs: Efficient Visual State Reconstruction for Multimodal Language Models

Long visual token sequences often account for a substantial fraction of the computational overhead in multimodal large language models~(MLLMs). Existing approaches reduce this cost by pruning redundant visual tokens, but permanently discard visual evidence that may become useful in subsequent layers. We instead ask whether all visual tokens can be preserved while reducing the cost of repeatedly evolving the representations through the Transformer. To answer this question, we perform low-rank interventions on visual-to-text information flow. We find that, after visual-to-text attention is blocked, restoring only a few directions recovers most of the lost accuracy, suggesting the relevant visual influence is concentrated in a low-dimensional subspace. We further observe strong predictability in layer-specific visual states: lightweight MLPs approximate them with high cosine similarity and low reconstruction error. Motivated by these findings, we propose δ-Vision, which replaces repeated Transformer evolution of visual tokens with lightweight low-rank adapters that construct layer-wise visual memories while preserving all visual tokens for text retrieval. Across image and video benchmarks, δ-Vision achieves higher accuracy than visual token pruning baselines at comparable or lower computation, while delivering competitive inference efficiency without discarding visual tokens.
