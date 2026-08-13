---
source: farmer/huggingface
farmed: 2026-08-13T03:36:17.258300+00:00
arxiv_id: 2608.06270
url: https://huggingface.co/papers/2608.06270
arxiv_url: https://arxiv.org/abs/2608.06270
date: 2026-08-13
---

# The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images

The "thinking-with-images" paradigm equips multimodal LLMs with active visual operations such as crop-and-zoom. However, models using these operations often achieve only marginal or negative gains over direct inference at substantially higher token cost. They may also repeatedly crop irrelevant regions and fail on questions that direct inference answers correctly. We ask whether the returned visual evidence causally affects the answer. To answer this question, we formulate visual tool-use as a causal graph that separates observation-mediated paths from action-induced shortcuts. We then audit it through interventions at the three levels: policy (comparing tool-use with direct inference), trajectory (corrupting all observations during rollout), and step (counterfactually replacing one individual observation under a fixed prefix). Our step-level estimand, Visual Evidence Gain, isolates the contribution of each returned observation. Across six representative models and five fine-grained perception benchmarks, we uncover policy miscalibration with two failure modes. In Calling Without Looking, returned observations have no causal effect on the answer. In Looking Without Planning, observations are informative but the call schedule is incoherent. A trajectory-level diagnostic decomposes the policy-level accuracy gain and shows that the gain is concentrated in a Calibrated minority. We term this discrepancy the illusion of visual tool-use: despite aggregate accuracy gains, visual tool-use is not causally effective across a broad range of rollouts. The code is available at https://github.com/OpenCausaLab/CauAudit.
