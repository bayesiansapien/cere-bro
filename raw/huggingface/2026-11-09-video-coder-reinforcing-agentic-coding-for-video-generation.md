---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.203803+00:00
arxiv_id: 2611.09894
url: https://huggingface.co/papers/2611.09894
arxiv_url: https://arxiv.org/abs/2611.09894
date: 2026-11-09
---

# Video-Coder: Reinforcing Agentic Coding for Video Generation

Recent years have witnessed remarkable progress in video generation in terms of visual quality and temporal consistency. However, generating videos with precise spatial structure, coherent motion dynamics, and controllable scene composition remains challenging. In this paper, we introduce Video-Coder, the first attempt to train a code-driven video generation agent, which autonomously writes and executes code to construct a dynamic 3D scene (Draft Video) that provides structure and motion signals to downstream video generators. To support this paradigm, we design a dedicated data pipeline and curate two high-quality datasets, Video-Coder-SFT-6k and Video-Coder-RL-2k, which contain diverse prompts and ground-truth reference videos. We further develop the Video- Coder Harness, a unified interactive environment integrating code execution, 3D scene rendering, and execution feedback for agent training and inference. We then train Video-Coder with SFT fol- lowed by harness-native agentic reinforcement learning with dual reward feedback, which combines execution-based and video-based rewards. Additionally, we design an annealing training strategy that gradually reduces the execution reward over time, allowing the model to rely more on the video reward in the later training stages. Experiments show that Video-Coder achieves significant gains, improving Minimax-H3 by approximately 7 points on PhyGenBench and 24 points on VBench-2.0. We hope this work can serve as an open foundation for coding agents in video generation, and we fully open-source our data, models, and code
