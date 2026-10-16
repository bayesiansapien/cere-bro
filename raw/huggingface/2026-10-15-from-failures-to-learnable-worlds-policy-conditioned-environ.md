---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.229238+05:30
arxiv_id: 2610.19420
url: https://huggingface.co/papers/2610.19420
arxiv_url: https://arxiv.org/abs/2610.19420
date: 2026-10-15
---

# From Failures to Learnable Worlds: Policy-Conditioned Environment Generation for Navigation Agents

Simulated environments enable scalable training data generation for embodied agents, but more data does not necessarily provide what a particular agent needs to learn. Existing environment-generation pipelines largely optimize generic properties such as realism, diversity, or task coverage, while different pretrained policies can fail for different environmental reasons. We therefore introduce WEDGE, a framework for weakness-guided navigation learning in which the failure modes of a pretrained agent guide the generation of training environments at each adaptation round. Given a pretrained policy, WEDGE uses an LLM to propose executable weakness features from contrasting successful and failed rollouts, automatically validates them on the diagnostic set, and selects the strongest validated weakness based on its success-rate gap. The validated weaknesses are then mapped to the environmental factors that control them. WEDGE varies these factors to construct environments in the difficulty regimes where the policy struggles, producing targeted training experience for adaptation. Across three navigation agents with different adaptation mechanisms, we find that policies exhibit distinct weakness profiles and benefit from different training environments. Weakness-conditioned adaptation consistently outperforms matched random and hard-example alternatives on ProcTHOR, while the resulting gains for Uni-NaVid and Gemini also extend to HM3D after ProcTHOR adaptation. Iterative re-diagnosis further shows that dominant weaknesses can persist or shift as the policy improves, providing updated guidance for subsequent environment construction. Together, these results show that policy failures are not only diagnostic signals, but actionable guidance for constructing training environments that target a policy's current weaknesses.
