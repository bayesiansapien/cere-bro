---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.505971+00:00
arxiv_id: 2610.17656
url: https://huggingface.co/papers/2610.17656
arxiv_url: https://arxiv.org/abs/2610.17656
date: 2026-10-14
---

# Open-o3-Video-v2: Seek, Ground, and Reason with Verifiable Spatio-Temporal Evidence

Reliable video reasoning requires models to produce correct answers and expose supporting visual evidence. Open-o3-Video enables verifiable reasoning by embedding timestamps and object-level bounding boxes into reasoning traces, but is restricted to frames from an initial sparse sampler. We introduce Open-o3-Video-v2, which formulates video reasoning as a unified agentic evidencegrounded process. The model identifies missing information, acquires additional observations, grounds the moments and objects supporting its reasoning, and writes this evidence into the trajectory before continuing or answering. To support this behavior, we construct STGR-v2-CoT135K, including 52K multi-turn agentic grounded reasoning trajectories, and STGR-v2-RL-13K for reinforcement learning. We further propose Clue-Seek GRPO (CS-GRPO), which tracks how tool calls change accumulated evidence, rewards clue coverage and step-wise gains, and penalizes excessive, repetitive, or uninformative retrieval. On V-STaR, Open-o3-Video-v2-4B achieves 40.4% mAM and 56.3% mLGM, outperforming its Qwen3-VL-4B backbone by 8.5% and 12.6%, respectively. It also delivers consistent gains across general video understanding, long-video reasoning, and temporal grounding benchmarks. These results show that active evidence acquisition and verifiable object-level grounding are complementary for reliable video reasoning. The code and models are released at https://msalab-pku.github.io/projects/Open-o3-Video-v2.
