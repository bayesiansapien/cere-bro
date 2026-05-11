---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.07825
url: https://huggingface.co/papers/2605.07825
arxiv_url: https://arxiv.org/abs/2605.07825
date: 2026-05-11
---

# Anisotropic Modality Align

Training multimodal large language models has long been limited by the scarcity of high-quality paired multimodal data. Recent studies show that the shared representation space of pretrained multimodal contrastive models can serve as a bridge, enabling models to perform multimodal training with unimodal data. However, the key premise of this paradigm remains insufficiently understood: can representations from different modalities be reliably interchanged? The core obstacle lies in the persistent Modality Gap in the shared space. In this work, we revisit the geometric nature of the modality gap. We find that modality representations already share compatible dominant semantic geometry. What truly hinders modality interchangeability is not a simple global shift, but an anisotropic residual structure concentrated along a small number of dominant directions. Based on this finding, we further propose the principle of anisotropic modality gap alignment: effective modality alignment should align with the target-modality distribution while preserving the semantic structure of the source modality. Guided by this principle, we propose an anisotropic geometric correction framework, AnisoAlign, for unpaired modality alignment. This framework leverages the internal geometric prior of the target modality and performs both global and local alignment to achieve high modality interchangeability.
