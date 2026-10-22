---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2606.31876
url: https://huggingface.co/papers/2606.31876
arxiv_url: https://arxiv.org/abs/2606.31876
date: 2026-10-20
---

# Harnessing Textual Refusal Directions for Multimodal Safety

Safety in Multimodal Large Language Models (MLLMs) depends on unsafe multimodal data for post-training alignment or activation steering. However, such data is hard to collect, must be gathered anew for each modality, and its collection and distribution raise ethical and legal concerns. In this work, we relax this constraint and investigate whether textual refusal directions, extracted directly from the LLM backbone, generalize across modalities (i.e., image, video). Preliminary findings confirm this ability, though effectiveness is conditioned by layer selection, steering strength, and cross-modal alignment, with the latter causing safe multimodal inputs to be spuriously steered toward refusal. Building on this, we introduce Modality-Agnostic Refusal Steering (MARS), a lightweight training-free approach that injects multimodal safety without the need for multimodal safety data. MARS corrects modality misalignment via activation centering, adaptively scales steering strength within a geometrically defined trust region, and selects the optimal intervention layer, operating at the first generated token. Evaluated on five SOTA MLLMs across safety, utility, and video jailbreak, MARS achieves consistent safety gains while preserving utility up to over-refusal. MARS reveals that safety-relevant structure is shared across modalities and that textual refusal directions are a powerful and underexplored foundation for multimodal alignment.
