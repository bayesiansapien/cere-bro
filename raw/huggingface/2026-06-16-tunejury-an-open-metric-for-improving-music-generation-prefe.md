---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.17006
url: https://huggingface.co/papers/2606.17006
arxiv_url: https://arxiv.org/abs/2606.17006
date: 2026-06-16
---

# TuneJury: An Open Metric for Improving Music Generation Preference Alignment

We introduce TuneJury, an open, instance-level pairwise reward model for text-to-music that predicts a music preference score from a text prompt and an audio clip. The released checkpoint is trained on publicly available human-preference labels covering arena-style (A vs. B) votes, metric-alignment preference pairs, crowdsourced pairwise comparisons, and expert aesthetic ratings. The predicted score margin between two clips is well calibrated on our held-out test split, supporting data filtering via a simple score threshold. TuneJury generalizes to both held-out test pairs and out-of-distribution benchmarks, remaining competitive with prior baselines on the latter. For generators released after training, we introduce anchor calibration, a post-hoc, per-system Bradley-Terry calibration that recovers agreement at substantially better data efficiency than from-scratch retraining. The same frozen reward drives consistent reward-axis gains across three downstream applications: inference-time best-of-N selection, DITTO-style latent optimization, and expert-iteration post-training. TuneJury is available at https://github.com/yonghyunk1m/TuneJury.
