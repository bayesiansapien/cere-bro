---
source: farmer/huggingface
farmed: 2026-05-12T00:00:00Z
arxiv_id: 2605.06096
url: https://huggingface.co/papers/2605.06096
arxiv_url: https://arxiv.org/abs/2605.06096
date: 2026-05-12
---

# Uncovering Entity Identity Confusion in Multimodal Knowledge Editing

Multimodal knowledge editing (MKE) aims to correct the internal knowledge of large vision-language models after deployment, yet the behavioral patterns of post-edit models remain underexplored. In this paper, we identify a systemic failure mode in edited models, termed Entity Identity Confusion (EIC): edited models exhibit an absurd behavior where text-only queries about the original entity's identity unexpectedly return information about the new entity. To rigorously investigate EIC, we construct EC-Bench, a diagnostic benchmark that directly probes how image-entity bindings shift before and after editing. Our analysis reveals that EIC stems from existing methods failing to distinguish between Image-Entity (I-E) binding and Entity-Entity (E-E) relational knowledge in the model, causing models to overfit E-E associations as a shortcut: the image is still perceived as the original entity, with the new entity's name serving only as a spurious identity label. We further explore potential mitigation strategies, showing that constraining edits to the model's I-E processing stage encourages edits to act more faithfully across modalities.
