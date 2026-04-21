---
source: farmer/huggingface
farmed: 2026-04-21T00:00:00Z
arxiv_id: "2604.16893"
url: https://huggingface.co/papers/2604.16893
arxiv_url: https://arxiv.org/abs/2604.16893
date: 2026-04-21
---

# EasyVideoR1: Easier RL for Video Understanding

Reinforcement learning from verifiable rewards (RLVR) has demonstrated remarkable effectiveness in improving the reasoning capabilities of large language models. As models evolve into natively multimodal architectures, extending RLVR to video understanding becomes increasingly important yet remains largely unexplored, due to the diversity of video task types, the computational overhead of repeatedly decoding and preprocessing high-dimensional visual inputs, and the difficulty of reproducible evaluation across numerous sensitive hyperparameters. Existing open-source RL training frameworks provide solid infrastructure for text and image scenarios but lack systematic optimizations tailored for video modality. In this work, we present EasyVideoR1, a complete and efficient reinforcement learning framework specifically designed for training large vision-language models on video understanding tasks. EasyVideoR1 makes the following contributions: (1) a full video RL training pipeline with offline preprocessing and tensor caching that eliminates redundant video decoding and yields a 1.47x throughput improvement; (2) a comprehensive, task-aware reward system covering 11 distinct video and image problem types with unified routing and modular extension; (3) a mixed offline-online data training paradigm that combines curated high-quality trajectories with on-policy exploration, benefiting the learning of more challenging tasks; (4) joint image-video training to prevent catastrophic forgetting.

**Authors:** Institute of Information Engineering, Chinese Academy of Sciences; School of Cyber Security, University of Chinese Academy of Sciences; JD.COM

**Code:** https://github.com/cyuQ1n/EasyVideoR1
