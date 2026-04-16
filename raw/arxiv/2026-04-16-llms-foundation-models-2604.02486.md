---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.02486
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.02486
published: 2026-04-16
authors: Haz Sameen Shahgir, Xiaofu Chen, Yu Fu
---

# VLMs Need Words: Vision Language Models Ignore Visual Detail In Favor of Semantic Anchors

**arXiv:** https://arxiv.org/abs/2604.02486
**Authors:** Haz Sameen Shahgir, Xiaofu Chen, Yu Fu

## Abstract

arXiv:2604.02486v2 Announce Type: replace-cross  Abstract: Vision-language models (VLMs) have achieved impressive performance across a wide range of multimodal tasks. However, they often fail on tasks that require fine-grained visual perception, even when the required information is still present in their internal representations. Prior work has attributed this ``hidden-in-plain-sight'' gap to the language model, but the cause remains unexplained. In this work, we demonstrate that this gap arises from the language model's lack of semantic labels for fine-grained visual details: when visual entities can be mapped to known concepts, VLMs bypass visual comparison and reason through language; when they cannot, VLMs resort to brittle and hallucinated descriptions. We verify this across semantic correspondence, synthetic shape matching, and face matching, and find that VLMs perform much better when the relevant entities are nameable than when they are unnamable. Mechanistically, Logit Lens analysis confirms that VLMs explicitly recover semantic labels for nameable entities and surface more unique tokens compared to unnameable entities. Furthermore, we show that this limitation can be addressed: teaching completely arbitrary names for unknown entities improves performance. More importantly, task-specific finetuning yields even stronger generalization without relying on language priors, i.e. through real visual perception. Our findings suggest that current VLM failures on visual tasks reflect a learned shortcut rather than a fundamental limitation of multimodal reasoning.
