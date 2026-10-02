---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.353238+05:30
arxiv_id: 2609.36333
url: https://huggingface.co/papers/2609.36333
arxiv_url: https://arxiv.org/abs/2609.36333
date: 2026-10-01
---

# ATLAS: Aligned Transport of Latent Structure for Reliable World Model Planning

Latent world models rely on representation geometry for planning, yet regularizing the latent marginal alone does not determine the state-to-state relationships used for action selection. We show that this can cause planning-relevant novelty structure to be weakened as representations are transformed into the final latent used by the planner. We introduce Aligned Transport of Latent Structure (ATLAS), a training objective that explicitly preserves relational geometry while calibrating the global latent distribution. ATLAS transfers normalized pairwise structure from an informative encoder representation to the planning latent and uses Wasserstein embedding matching (WEMReg) to calibrate its marginal through one-dimensional Wasserstein-2 transport. Our analysis shows that relational preservation and marginal calibration impose non-redundant constraints, and connects finite-candidate planning stability to relational distortion, latent-scale mismatch, and prediction error. Instantiated in LeWM, ATLAS improves mean goal-reaching success across PushT, TwoRoom, and OGBench-Cube on both lower- and higher-novelty evaluation subsets, with the largest gain on higher-novelty TwoRoom episodes. Representation and rollout diagnostics further show stronger novelty-related structure in the planning latent, improved marginal calibration, and lower multi-step prediction error. Together, these results highlight preservation of planning-relevant latent geometry as an important ingredient for reliable world-model planning. Code is available at https://anonymous.4open.science/r/atlas-world-model-72C4/.
