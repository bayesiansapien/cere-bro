---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.15980
url: https://huggingface.co/papers/2605.15980
arxiv_url: https://arxiv.org/abs/2605.15980
date: 2026-05-18
---

# Flash-GRPO: Efficient Alignment for Video Diffusion via One-Step Policy Optimization

Group Relative Policy Optimization has emerged as essential for aligning video diffusion models with human preferences, but faces a critical computational bottleneck: training a 14B parametered model typically demands hundreds of GPU days per experiment. Existing efficiency methods reduce costs through sliding window subsampling training timesteps, but fundamentally compromise optimization, exhibiting severe instability and failing to reach full trajectory performance. We present Flash-GRPO, a single-step training framework that outperforms full trajectory training in alignment quality under low computational budgets while substantially improving training efficiency. Flash-GRPO addresses two critical challenges: iso-temporal grouping eliminates timestep-confounded variance by enforcing prompt-wise temporal consistency, decoupling policy performance from timestep difficulty; temporal gradient rectification neutralizes the time-dependent scaling factor that causes vastly inconsistent gradient magnitudes across timesteps. Experiments on 1.3B to 14B parameter models validate Flash-GRPO's effectiveness, demonstrating substantial training acceleration with consistent stability and state-of-the-art alignment quality.
