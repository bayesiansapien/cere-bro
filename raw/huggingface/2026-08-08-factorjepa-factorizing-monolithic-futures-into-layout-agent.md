---
source: farmer/huggingface
farmed: 2026-08-08T22:00:12.430322
arxiv_id: 2608.01049
url: https://huggingface.co/papers/2608.01049
arxiv_url: https://arxiv.org/abs/2608.01049
upvotes: 5
date: 2026-08-08
---

# FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channels for Crowded and Chaotic Global South Urban Worlds

World models have attracted significant attention for their ability to capture and predict the structure and dynamics of the physical world. In this emerging landscape, Joint Embedding Predictive Architectures (JEPA) offer a particularly compelling direction.
  We study a largely unexplored regime: populous, crowded, and chaotic Global South urban environments, which we call DENSEWORLD. Unlike the lower-density, lane-structured settings that dominate existing evaluations, these scenes exhibit soft spatial boundaries, extreme agent heterogeneity, persistent occlusion, and rapid social negotiation under mixed traffic. We introduce the first large-scale dataset for this regime: 1,000 hours of drive-through, walk-through, and aerial video across 22 cities. Existing JEPA formulations struggle to preserve dense interaction dynamics under heterogeneity and partial observability.
  We introduce FactorJEPA, which makes world structure a first-class predictive primitive. Rather than encoding the future in a monolithic latent, it composes layout, entities, and interactions, using a visibility gate and separated subspaces to preserve partially observed agents and discourage cross-factor shortcuts. FactorJEPA improves (i) future-latent accuracy (Future-frame L1), (ii) intervention-sensitive prediction (Causal L1), and (iii) robustness to reduced visual evidence (Mask-ratio slope), while exposing (iv) a reproducible motion-information trade-off (Motion cosine). Method rankings replicate across 2B and 1B V-JEPA 2.1 backbones, with rho = 0.895 to 0.978.
  We publicly release the DENSEWORLD-115k dataset (https://huggingface.co/datasets/anonymousML123/denseworld-115k) and the surgery-trained FactorJEPA checkpoints (https://huggingface.co/datasets/anonymousML123/factorjepa-outputs/tree/main/outputs/full/vjepa_2_1_vitg_1B/train/m09c_surgery_3stage_DI_diheavy_encoder).
