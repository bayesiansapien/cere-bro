---
source: farmer/huggingface
farmed: 2026-05-29T09:54:41Z
arxiv_id: 2605.27891
url: https://huggingface.co/papers/2605.27891
arxiv_url: https://arxiv.org/abs/2605.27891
date: 2026-05-29
---

# SmartDirector: Keyframe-Conditioned Cinematic Video Generation with Narrative Pacing Control

The narrative quality of a video fundamentally determines its perceptual value. Although existing video generation methods can produce visually appealing content, they predominantly rely on sparse conditioning signals such as text prompts or first/last frames, which limits precise control over narrative structure and temporal pacing. In this paper, we propose SmartDirector, a framework that enhances the narrative capacity of video generation models through multiple keyframes. SmartDirector supports flexible generation scenarios including single-shot generation, multi-shot narrative synthesis, and video extension. The framework operates in two stages: Director-Gen generates a low-resolution video conditioned on the provided keyframes, and Director-SR refines the output by exploiting high-resolution keyframes as semantic anchors to recover fine-grained details. To enable robust multi-keyframe training, we construct a data pipeline that curates single-shot and multi-shot sequences from movies. Extensive experiments demonstrate that SmartDirector substantially outperforms existing state-of-the-art approaches. We will release the code to facilitate further research.
