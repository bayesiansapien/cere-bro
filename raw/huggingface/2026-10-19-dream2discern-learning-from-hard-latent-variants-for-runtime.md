---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.16071
url: https://huggingface.co/papers/2610.16071
arxiv_url: https://arxiv.org/abs/2610.16071
date: 2026-10-19
---

# Dream2Discern: Learning from Hard Latent Variants for Runtime Failure Prediction in Multi-Agent Systems

Reliable deployment of LLM-based multi-agent systems calls for runtime auditors that predict terminal outcomes from observed execution prefixes. These auditors typically learn from a limited corpus of trajectories with verified outcomes. Expanding this corpus requires costly execution and verification, yet broader failure coverage alone provides no explicit criterion for identifying prefixes that the current auditor finds difficult to classify. To this end, we propose Dream2Discern, a runtime auditor trained through implicit augmentation guided by its own prediction loss. During Dream, we select perturbations of the auditor's representation operators to increase prediction loss on recorded prefixes, yielding hard latent variants. During Discern, the auditor learns to predict execution outcomes from these variants using the original labels. The variants are regenerated as the auditor learns, turning a limited corpus into a renewable source of hard examples and requiring no additional trajectory collection or outcome verification. Extensive evaluations on AFTraj-2K and StepShield show that Dream2Discern outperforms competitive failure auditors and achieves over 90% trajectory-level weighted accuracy on both benchmarks while balancing prediction accuracy and timeliness. Project page: https://zbox1005.github.io/dream2discern-project/
