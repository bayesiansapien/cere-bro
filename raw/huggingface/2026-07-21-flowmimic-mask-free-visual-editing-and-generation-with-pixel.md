---
source: farmer/huggingface
farmed: 2026-07-21T07:20:44Z
arxiv_id: 2607.18227
url: https://huggingface.co/papers/2607.18227
arxiv_url: https://arxiv.org/abs/2607.18227
date: 2026-07-21
---

# FlowMimic: Mask-free Visual Editing and Generation with Pixel-pair Warped Flow Field for Online Video Editing Data Generation and Modality Mimicry

In line with the prevailing direction of vision research, we explore the integration of both generation and editing capabilities for video and image modalities within a single model. Current approaches to collecting video editing data typically depend on labour-intensive, time-consuming curated procedures--involving object mask annotation, the use of error-introducing pair synthesis via I2V model and ControlNet-like guidance, and VLM-based quality filtering or refinement--and demonstrate limited task scalability. As a result, the diversity of editing tasks remains substantially narrower than that available for image editing models. We develop a pixel-pair temporal warped flow field that can directly generate corresponding video editing samples in real time from image editing samples, and we demonstrate across multiple levels of video editing tasks that a model can learn video editing using only such data. We regard the image modality as a particular form of the video modality. Accordingly, we design a modality mimic generation loss and a modality mimic editing loss to relatively align the capabilities--and thereby the output distributions--of the two modalities through mutual imitation. Moreover, language-based visual editing entails the comprehension of the editing instruction and the reference visual content, the localization of the region corresponding to that instruction within the reference visual contents, and the modification of that region alone. Existing approaches predominantly rely on external aids, such as fine-tuning an additional MLLM or explicitly supplying a mask sequence as auxiliary input during inference. In contrast, we aspire for the model to internalize this capability. To that end, we introduce sense-related tasks--for instance, referring expression segmentation--along with corresponding editing-region-aware latent-level loss and attention-level loss.
