---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.905263+00:00
arxiv_id: 2611.30472
url: https://huggingface.co/papers/2611.30472
arxiv_url: https://arxiv.org/abs/2611.30472
date: 2026-11-26
---

# Target-Part Preference Optimization for Part-Aware 3D Generation

Part-aware 3D generation requires not only globally plausible objects but also complete, well-separated semantic parts, yet high-quality part decompositions remain too scarce to support large-scale supervised fine-tuning. We study whether preference fine-tuning based on Direct Preference Optimization (DPO) can adapt a pretrained part-aware generator from limited part-annotated data without architectural changes. We rank candidates generated with different random seeds against ground-truth (GT) geometric metrics, and select the (object, target-part) examples with the largest across-seed quality gap. Each selected example stores a seed pair whose two flow trajectories share one clean GT compositional latent and differ only in Gaussian noise. We derive a reference-relative target-block preference loss from FlowDPO that compares the two trajectories against a frozen reference model. GT flow-matching losses on the target block and complete part set provide absolute supervision, while only the diffusion transformer (DiT) is updated. Human-ranked controls test an alternative ordering source, and synthetic cropping provides controlled loser targets that are incomplete by construction. Among the three training-set scales, the medium-scale setting gives the strongest result on held-out Objaverse and outperforms both the pretrained generator and the reported direct supervised fine-tuning baseline on the multi-part aggregate. Further analysis shows sensitivity to pair ordering, target-part coverage, and the balance between pairwise and GT supervision. Cross-dataset experiments show less consistent gains under distribution shift.
