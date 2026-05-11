---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.05997
url: https://huggingface.co/papers/2605.05997
arxiv_url: https://arxiv.org/abs/2605.05997
date: 2026-05-11
---

# 4DThinker: Thinking with 4D Imagery for Dynamic Spatial Understanding

Dynamic spatial reasoning from monocular video is essential for bridging visual intelligence and the physical world, yet remains challenging for vision-language models (VLMs). Prior approaches either verbalize spatial-temporal reasoning entirely as text, which is inherently verbose and imprecise for complex dynamics, or rely on external geometric modules that increase inference complexity without fostering intrinsic model capability. In this paper, we present 4DThinker, the first framework that enables VLMs to "think with 4D" through dynamic latent mental imagery, i.e., internally simulating how scenes evolve within the continuous hidden space. Specifically, we first introduce a scalable, annotation-free data generation pipeline that synthesizes 4D reasoning data from raw videos. We then propose Dynamic-Imagery Fine-Tuning (DIFT), which jointly supervises textual tokens and 4D latents to ground the model in dynamic visual semantics. Building on this, 4D Reinforcement Learning (4DRL) further tackles complex reasoning tasks via outcome-based rewards, restricting policy gradients to text tokens to ensure stable optimization. Extensive experiments across multiple dynamic spatial reasoning benchmarks demonstrate that 4DThinker consistently outperforms strong baselines and offers a new perspective toward 4D reasoning in VLMs.
