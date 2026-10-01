---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36802
url: https://huggingface.co/papers/2609.36802
arxiv_url: https://arxiv.org/abs/2609.36802
date: 2026-09-30
---

# EasyPPO: Stabilizing the Critic Is Key

A key strength of Proximal Policy Optimization (PPO) is its learned critic, which uses historical trajectories collected during reinforcement learning to estimate expected returns and reduce policy-gradient variance. However, we find that the critic is also a major source of instability in reinforcement learning for large language models (LLMs). We identify two critic failure modes that destabilize PPO. First, filtering truncated rollouts from both actor and critic shifts the policy objective to reward conditioned on completion, allowing truncation to increase even as conditional reward improves. Second, heterogeneous return noise can cause high-variance prompts to dominate critic updates in finite batches. We introduce EasyPPO to address these failures. Actor-only overlong filtering trains the critic on returns from both completed and truncated rollouts. Noise-normalized critic regression weights each prompt's critic loss by the inverse standard deviation of its sampled returns, balancing noise contributions across prompts. Moderately smaller critic mini-batches confine outlier influence to fewer rollouts during gradient clipping. Across continuous-reward coding on FrontierCS, binary-reward mathematical reasoning on AIME24, and multi-turn search on Search-R1, EasyPPO remains stable throughout the full training horizon and consistently outperforms vanilla PPO, VAPO, and HL-Gauss PPO. Its best validation scores show relative gains of 14.89%, 2.28%, and 9.47% over PPO, respectively.
