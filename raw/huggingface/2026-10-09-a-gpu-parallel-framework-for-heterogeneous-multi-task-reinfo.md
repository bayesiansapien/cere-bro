---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.416540+00:00
arxiv_id: 2606.03335
url: https://huggingface.co/papers/2606.03335
arxiv_url: https://arxiv.org/abs/2606.03335
date: 2026-10-09
---

# A GPU-Parallel Framework for Heterogeneous Multi-Task Reinforcement Learning

GPU-parallel simulation provides abundant robot interaction, but existing benchmarks rarely combine this scale with heterogeneous manipulation tasks and standardized multi-task RL evaluation. We introduce Hebero (Heterogeneous Benchmark for Robot Learning), a GPU-parallel Isaac Lab benchmark that enables efficient joint training and evaluation of a single policy across all 40 heterogeneous tasks. Scaling experiments show that increasing parallel replicas per task improves success under a fixed wall-clock budget. To support learning with sparse rewards and limited demonstrations, we propose Demonstration-Guided Policy Optimization (DGPO), which reuses demonstrations for dense tracking rewards and asymmetric value learning. Its shared stack supports controlled comparisons of learner-specific demonstration interfaces within PPO. Within DGPO framework, we introduce IW-ABC, which uses a lightweight per-task learning progress signal to coordinate adaptive behavior cloning (ABC), relaxing demonstration guidance with task progress, and importance weighting (IW), emphasizing lagging tasks in PPO updates. With 50 demonstrations per task, IW-ABC achieves 90.1% state-input mean success, outperforming the strongest baseline FAMO-ABC by 7.8 percentage points. Its visual counterpart reaches 93.5% mean success. Real-world experiments further demonstrate that a single multi-task policy trained in simulation can successfully perform four tasks on a physical Piper robot. The project page is available at https://hebero-rl.github.io/.
