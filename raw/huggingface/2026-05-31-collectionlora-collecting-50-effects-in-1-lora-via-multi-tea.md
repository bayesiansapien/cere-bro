---
source: farmer/huggingface
farmed: 2026-05-31T09:25:04Z
arxiv_id: 2605.25378
url: https://huggingface.co/papers/2605.25378
arxiv_url: https://arxiv.org/abs/2605.25378
date: 2026-05-31
---

# CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation

Customized image editing aims to equip pre-trained diffusion models with specific visual effects using limited paired data, typically via Low-Rank Adaptation (LoRA). As the number of desired effects grows, storing and dynamically loading numerous these effect LoRAs significantly increases deployment overhead. Furthermore, current pipelines typically cascade these effect LoRAs with acceleration modules for fast generation, which triggers severe parameter interference and results in concept bleeding and style degradation. We propose CollectionLoRA, a multi-teacher on-policy distillation framework capable of distilling the concepts of up to 50 different effect LoRAs along with few-step generation capabilities into a single LoRA. This fundamentally resolves the feature interference issue and significantly reduces deployment costs. Specifically, the method introduces (i) a Probabilistic Dual-Stream Routing mechanism that enables the model to randomly switch between data sources during training, effectively enhancing its generalization in unseen scenarios; (ii) an Asymmetric Orthogonal Prompting strategy to achieve concept isolation within the prompt space; (iii) a Coarse-to-Fine Distillation Objective to mitigate the distribution gap between the teacher and student models. Extensive evaluations show that CollectionLoRA distills all customized effects and few-step generation into a single LoRA, reducing deployment overhead while achieving concept fidelity comparable to or better than independently trained teacher models.
