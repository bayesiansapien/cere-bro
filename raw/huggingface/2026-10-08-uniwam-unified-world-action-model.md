---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.303037+05:30
arxiv_id: 2610.02054
url: https://huggingface.co/papers/2610.02054
arxiv_url: https://arxiv.org/abs/2610.02054
date: 2026-10-08
---

# UniWAM: Unified World-Action Model

Vision-language-action models benefit from the understanding and reasoning capabilities of pretrained vision-language models, but action-only supervision provides limited grounding in world dynamics. Conversely, world-action models inherit spatiotemporal priors from video generation models, yet remain limited in semantic understanding and reasoning under distribution shifts. We introduce UniWAM, a unified architecture that integrates a physical reasoner, a world generator, and an action predictor to jointly learn semantic understanding of the physical world, visual generation, and action prediction. To ensure the quality of the training data, we developed a rigorous data cleaning and annotation pipeline for both human egocentric data and robot data. To adapt the vision-language component to embodied tasks while preserving its inherited language capabilities, we represent low-level actions in natural language and introduce a pre-training recipe that assigns complementary supervision from visual question answering (VQA) data, human egocentric data, and robot demonstrations to the appropriate model components. During post-training, future visual noise augmentation reduces reliance on precise future predictions, while history-conditioned flow matching uses encoded action history to initialize action generation. Together, these designs significantly reduce denoising steps while maintaining performance. UniWAM achieves state-of-the-art (SOTA) performance across multiple evaluations, including in-distribution performance, robustness, generalization, instruction following, and long-horizon task execution. Furthermore, we uncover a log-linear scaling law of unified human-robot co-training, demonstrating the effectiveness of large-scale pre-training on a mixture of human and robot data.
