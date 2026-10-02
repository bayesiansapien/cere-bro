---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.348889+05:30
arxiv_id: 2609.34599
url: https://huggingface.co/papers/2609.34599
arxiv_url: https://arxiv.org/abs/2609.34599
date: 2026-10-01
---

# The Low-Rank Structure of VLA Reinforcement Learning

Reinforcement learning (RL) is increasingly used to post-train vision-language-action (VLA) models, yet how RL reshapes these policies remains poorly understood. We find that RL across widely used flow-based VLA models, including π_{0.5} and GR00T~N1.5/N1.6, on LIBERO, ManiSkill, MetaWorld, and CALVIN induces substantially lower-rank parameter updates that are highly concentrated in the action expert's Timestep Modules, a small and previously overlooked component. Through systematic module-replacement experiments, we further show that these modules capture a disproportionate share of the performance gains from RL. We then characterize what is encoded in these Timestep Modules. First, we show that RL specializes them to the discrete denoising timesteps used during rollouts, and that this discrete-timestep training underlies the low-rank updates. Second, we find that among their outputs, the shift vector changes most distinctly under RL, and through probing, we show that shift update directions strongly predict task success (ROC-AUC up to 99.6%). Third, we find that the geometry of shift updates reflects task relationships, as their pairwise similarity correlates with cross-task transfer patterns. Building on these findings, we show that steering along shift update directions further improves RL-trained policies without additional RL training. Overall, we provide a systematic understanding of how RL reshapes VLA policies by studying how learned signals are encoded in parameter space, offering insights into more efficient and interpretable VLA post-training.
