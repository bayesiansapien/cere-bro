---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.197322+00:00
arxiv_id: 2610.27861
url: https://huggingface.co/papers/2610.27861
arxiv_url: https://arxiv.org/abs/2610.27861
date: 2026-10-22
---

# RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation

Vision-language-action (VLA) robustness is commonly summarized by aggregate task success, which obscures how individual executions change under distribution shifts and where failures emerge in long-horizon tasks. We introduce RoboCasa-Shift, a diagnostic robustness benchmark built on RoboCasa365 that combines controlled single-factor shifts, matched clean-perturbed rollouts in which each pair shares the same underlying settings and differs only in the target shift, and simulator-grounded stage-aware diagnostics. We evaluate GR00T N1.5 on four long-horizon tasks that pass a predefined clean-performance gate under four perturbation factors and three calibrated severity levels, including conditions that drive the evaluated policy to complete task failure, totaling 1,040 formal rollouts. Robustness responses vary substantially across factors and tasks, and increasing severity does not always produce monotonic degradation. For example, one camera condition yields ΔSR=0 despite 8 of 80 matched episodes changing outcome. Stage-aware analysis further shows that the same end-to-end degradation can correspond to different execution-depth profiles. Camera L_2 and Gaussian blur L_1 both yield ΔSR=0.188, yet their first-stage failure rates are 19.0\% and 36.4\%, respectively. Our findings suggest that VLA robustness should be viewed as a multi-dimensional property of execution rather than a single end-to-end performance measure, motivating evaluation protocols that jointly capture outcome degradation, paired outcome sensitivity, and failure progression. The code is publicly available at https://github.com/HaochengWang23/RoboCasa-Shift.
