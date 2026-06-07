---
source: farmer/huggingface
farmed: 2026-06-07T04:51:04Z
arxiv_id: 2606.04880
url: https://huggingface.co/papers/2606.04880
arxiv_url: https://arxiv.org/abs/2606.04880
date: 2026-06-07
---

# MAOAM: Unified Object and Material Selection with Vision-Language Models

Selection is a core operation in interactive image editing. To be practical, a user should be able to specify and disambiguate the desired selection region through either text or click-based interactions, and the system should support selecting not only objects but also other criteria, such as materials. Material-based selection is valuable for tasks like re-texturing surfaces or editing instances of a specific material. However, existing vision-language-model (VLM) based selection methods are object-centric and typically support a single interaction modality, limiting their applicability. In this work, we thus present Mask Any Object And Material (MAOAM), a unified selection framework that enables precise object and material-level selection across both text- and click-based interactions. MAOAM leverages a VLM with a segmentation head to produce pixel-accurate masks from user prompts: the VLM interprets the user's selection intent (object or material-level) and encodes visual entities, attributes, and spatial relations, while the segmentation head decodes the output token into a mask. A key challenge is the lack of material selection datasets with text annotations. We propose a scalable data generation pipeline: we collect real and synthetic images with material masks, and leverage VLMs to generate material descriptions with rich visual-semantics. We train MAOAM with a multi-task objective over click and text-based selection, along with an auxiliary VQA task derived from the material descriptions to facilitate deeper material understanding. Despite being trained with uni-modal prompts, our model exhibits an emergent improvement in selection when combining text and clicks at inference, enabling flexible image editing workflows. Experiments demonstrate accurate and coherent selections across diverse objects, materials, and interaction scenarios, highlighting robustness in practice.
