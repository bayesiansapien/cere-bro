---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.20430
url: https://huggingface.co/papers/2608.20430
arxiv_url: https://arxiv.org/abs/2608.20430
date: 2026-08-25
upvotes: 23
authors: ["Hongbo Lu", "Liang Yao", "Chenghao He", "Hao Han", "Fan Liu", "Wenlong Liao", "Tao He", "Pai Peng"]
---

# RISE: Adaptive Imagination for World Action Models

**Upvotes:** 23
**Authors:** Hongbo Lu, Liang Yao, Chenghao He, Hao Han, Fan Liu, Wenlong Liao, Tao He, Pai Peng

World Action Models (WAMs) improve planning by incorporating future world evolution into action generation, yet existing methods allocate a fixed imagination budget to every scene. We propose RISE (Refining Imagination through SElective Rollout), a system-level adaptive imagination framework that makes sequential Roll/Stop decisions according to the expected planning benefit of continued rollout. At each step, a Latent Evaluator estimates the risk revealed by the current prefix and how much planning could improve if imagination continues, while a Rollout Gate weighs this expected benefit against additional computation cost. Since factual driving logs expose only one realized future, we further construct CounterDrive, a counterfactual dataset with diverse outcomes and risk levels, to enrich future dynamics and provide localized risk supervision. Each retained sample undergoes expert verification and annotation of trajectory validity, incident onset, and causal category, providing a reusable resource for safety-critical world-modeling research. Experiments on NAVSIM and nuScenes show that RISE achieves the best overall planning performance while reducing unnecessary rollout, with additional transfer results supporting its plug-in generality across WAM architectures.
