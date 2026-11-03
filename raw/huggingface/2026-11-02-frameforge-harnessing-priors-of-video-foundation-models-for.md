---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.495406+05:30
arxiv_id: 2610.36545
url: https://huggingface.co/papers/2610.36545
arxiv_url: https://arxiv.org/abs/2610.36545
date: 2026-11-02
---

# FrameForge: Harnessing Priors of Video Foundation Models for Unified Image Generation

Unified conditional image generation requires a single model to preserve different aspects of a visual input while producing a target image that follows textual guidance. Pretrained video models provide a promising foundation by encoding visual transformations across time, yet existing approaches typically assign the condition and target to fixed temporal positions. We observe that condition-target relationships vary substantially across generation tasks, while video models naturally encode visual transformations at different temporal scales. This motivates us to model conditional generation through input-adaptive virtual temporal relations. We propose FrameForge, which captures two complementary aspects of such relations. Mixture of Temporal Experts (MoTE) models how far the target lies from the condition by dynamically selecting temporal RoPE experts with different virtual intervals. Chain of Temporal Reasoning (CoTR) models how the condition is transformed into the target through a latent intermediate state, with a reasoning-bottleneck attention mask encouraging information propagation through this pathway. Experiments on DreamBench, COCO2017, and GEdit-Bench show that FrameForge achieves superior performance in subject-driven generation, canny-to-image generation, and image editing among the compared methods.
