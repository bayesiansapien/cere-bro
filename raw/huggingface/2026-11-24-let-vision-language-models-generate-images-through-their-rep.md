---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.926375+00:00
arxiv_id: 2611.31237
url: https://huggingface.co/papers/2611.31237
arxiv_url: https://arxiv.org/abs/2611.31237
date: 2026-11-24
---

# Let Vision-Language Models Generate Images through Their Representations

Recent unified multimodal models aim to combine visual understanding and generation within a single model, yet effectively integrating the two capabilities remains challenging. Leveraging pretrained vision-language models offers a way to build on already learned multimodal knowledge, but making this knowledge effectively accessible to visual generation remains nontrivial. We find that a central challenge lies in the heterogeneous visual representations used for understanding and generation. To address this challenge, we introduce Integral, which converts a pretrained vision-language model into a unified multimodal model by constructing a shared visual representation space across the two capabilities. Integral implements this design through two complementary components. Abstraction Fusion constructs shared visual tokens by aggregating hierarchical representations from the frozen vision encoder, while Block-wise MoT introduces a lightweight generative stream that interacts with the vision-language model only at block boundaries. Our approach effectively preserves the pretrained understanding capability while extending it to strong visual generation. Controlled comparisons further demonstrate that sharing visual representations between understanding and generation substantially improves generative learning compared with using a separate visual representation space, despite comparable reconstruction fidelity. These results suggest that representations learned by pretrained vision-language models already provide an effective foundation for visual generation.
