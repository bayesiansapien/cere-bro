---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.02684
url: https://huggingface.co/papers/2606.02684
arxiv_url: https://arxiv.org/abs/2606.02684
date: 2026-06-04
---

# Filter, Then Reweight: Rethinking Optimization Granularity in On-Policy Distillation

On-Policy distillation (OPD) in large language models is shifting from full-trace KL supervision toward more selective training paradigms. Recent OPD methods increasingly focus on selecting which trajectories to learn from, which tokens are most informative, and which supervision signals are most reliable. Motivated by this trend, we rethink optimization granularity of OPD and propose \fireicon\ FiRe-OPD (Filter, then Reweight), which jointly adjusts supervision signals at both trajectory and token levels. In details, FiRe-OPD first filters trajectories to remove low-quality rollout samples, and then applies soft reweighting within the retained trajectories to emphasize informative tokens. Compared with hard token selection, FiRe-OPD leverages a soft-weighting mechanism to effectively mitigate information loss and enhance optimization stability, thereby achieving finer-grained OPD optimization. We validate the effectiveness of FiRe-OPD across strong-to-weak, single-teacher, and multi-teacher settings, and demonstrate its superiority over recent token-level OPD methods ( (e.g., +6.25 on AIME 2024 in strong-to-weak, +18.81 on Miner in multi-teacher). Our code is available at https://github.com/YuYingLi0/FiRe-OPD.
