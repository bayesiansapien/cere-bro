---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32554
url: https://huggingface.co/papers/2611.32554
arxiv_url: https://arxiv.org/abs/2611.32554
date: 2026-11-25
---

# PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement

Segmenting a 3D object into semantically meaningful parts requires joint reasoning about geometric structure and semantic context. Pretrained 3D experts provide spatially grounded region proposals, while 2D experts provide semantic cues for identifying object parts. The challenge is to integrate these complementary capabilities into a framework that can both produce meaningful part segmentations and progressively refine them. We present PartAgent, a training-free agentic framework for 3D part segmentation built upon two complementary modules: (i) Structural-Semantic Expert Integration combines regions predicted by the 3D expert with multiview semantic evidence from the 2D expert through image-to-surface correspondences, constructing compositional part partitions at multiple granularities. (ii) Observation-Driven Closed-Loop Partition Refinement observes the current partition and its supporting evidence to select targeted inspection, evidence repair, composition, or reselection actions. It verifies proposed changes and uses the updated state and action outcomes to guide subsequent decisions. On PartObjaverse-Tiny-WT, PartAgent achieves 68.41 mIoU, outperforming the strongest competing method by 8.53 points. Across 3DCoMPaT200, PartNeXt, PartNetE, and PartObjaverse-Tiny, PartAgent achieves the highest mIoU on each dataset, averaging 69.36 across the four datasets, 7.28 points above the highest mean among competing methods.
