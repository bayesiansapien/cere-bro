---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32639
url: https://huggingface.co/papers/2611.32639
arxiv_url: https://arxiv.org/abs/2611.32639
date: 2026-11-25
---

# ReFocus: Progress-Guided Adaptive Practice for Long-Horizon Robotic Manipulation Reinforcement Learning

Online reinforcement learning (RL) enables vision-language-action policies to improve through environmental interaction. However, in long-horizon manipulation, sparse success/failure feedback provides little information about where policies encounter bottlenecks. Moreover, repeated full-task rollouts also leave these bottlenecks weakly analyzed and insufficiently practiced. To this end, we introduce ReFocus, a progress-guided multi-round RL framework that alternates between Global and Local RL to identify task-specific bottlenecks and allocate additional practice to them. Specifically, during Global RL, we decompose each task into a Directed Acyclic Graph (DAG) of subtasks. Then a DAG-based Progress Reward is leveraged for both policy training and bottleneck diagnosis. Based on the identified bottlenecks, ReFocus selects Adaptive Practice Windows, defining task segments from an entry stage to a target stage. It allocates additional interaction to these segments during Local RL while updating the entire policy. After that, it evaluates the policy to perform the full task for the next round of RL, forming an iteration between Global and Local RL. Experiments on LIBERO-Long and RoboCasa365 show that ReFocus achieves success rates of 97.8% and 51.3%, respectively, compared with 90.6% and 39.3% for the π_{0.5} baseline. Furthermore, we evaluate a real-world adaptation on three long-horizon tasks. On BreadBaker, ReFocus achieves 95% success, compared with 30% for the π_{0.5}. Project page: https://refocus-robotics.github.io.
