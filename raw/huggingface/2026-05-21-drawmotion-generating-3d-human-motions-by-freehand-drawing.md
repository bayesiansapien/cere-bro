---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.20955
url: https://huggingface.co/papers/2605.20955
arxiv_url: https://arxiv.org/abs/2605.20955
date: 2026-05-21
---

# DrawMotion: Generating 3D Human Motions by Freehand Drawing

Text-to-motion generation, which translates textual descriptions into human motions, faces the challenge that users often struggle to precisely convey their intended motions through text alone. To address this issue, this paper introduces DrawMotion, an efficient diffusion-based framework designed for multi-condition scenarios. DrawMotion generates motions based on both a conventional text condition and a novel hand-drawing condition, which provide semantic and spatial control over the generated motions, respectively. Specifically, we tackle the fine-grained motion generation task from three perspectives: 1) freehand drawing condition. To accurately capture users' intended motions without requiring tedious textual input, we develop an algorithm to automatically generate hand-drawn stickman sketches across different dataset formats; 2) multi-condition fusion. We propose a Multi-Condition Module (MCM) that is integrated into the diffusion process, enabling the model to exploit all possible condition combinations while reducing computational complexity compared to conventional approaches; and 3) training-free guidance. Notably, the MCM in DrawMotion ensures that its intermediate features lie in a continuous space, allowing classifier-guidance gradients to update the features and thereby aligning the generated motions with user intentions while preserving fidelity. Quantitative experiments and user studies demonstrate that the freehand drawing approach reduces user time by approximately 46.7% when generating motions aligned with their imagination. The code, demos, and relevant data are publicly available at https://github.com/InvertedForest/DrawMotion.
