---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.300201+00:00
arxiv_id: 2611.05609
url: https://huggingface.co/papers/2611.05609
arxiv_url: https://arxiv.org/abs/2611.05609
date: 2026-11-05
---

# On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation

Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) to consolidate capabilities from multiple teachers. Although prior work reports near-perfect in-distribution (IND) distillation performance, we find that this can mask incomplete capability consolidation beyond the supervised distribution. A preliminary study on synthetic reasoning shows that OPD does not fully transfer teachers' generalization capabilities. We then extend this investigation to real-world tasks, evaluating extrapolative and compositional generalization across mathematical reasoning, coding, agent, and long-context capabilities using Qwen3 models. Across extrapolative settings, OPD and MOPD reach 96.04-102.73% of their teachers' IND scores. Yet their out-of-distribution (OOD) scores remain 2.45-16.25% below the base model's. Across three compositional settings, MOPD improves IND performance over the base model, but its performance on composed tasks as OOD remains 18.19-24.34% below that of the best teachers. To understand these gaps, we examine teacher capability and data coverage as two potential bottlenecks. Jointly alleviating these bottlenecks eliminates OOD forgetting in our experiments and suggests the potential for generalization beyond the teacher. (M)OPD also reduces OOD forgetting on average relative to its reinforcement learning (RL) baselines. Analysis of the associated update geometry reveals smaller and more spectrally concentrated updates on average than those of the RL baselines, along with greater shared update structure under MOPD. Motivated by these findings, we propose geometry-based patching and base-preserving replay to improve OOD performance while largely preserving IND performance. Our findings identify a blind spot in capability consolidation via (M)OPD, highlighting the need for algorithms that explicitly support OOD retention and generalization.
