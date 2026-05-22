---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.19833
url: https://huggingface.co/papers/2605.19833
arxiv_url: https://arxiv.org/abs/2605.19833
date: 2026-05-21
---

# Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation

Despite rapid advances in automatic speech recognition (ASR) and large audio-language models, robust recognition in real-world environments remains limited by an "acoustic robustness bottleneck": models often lose acoustic grounding and produce omissions or hallucinations under severe, compositional distortions. We propose Mega-ASR, a unified ASR-in-the-wild framework that combines scalable compound-data construction with progressive acoustic-to-semantic optimization. We introduce Voices-in-the-Wild-2M, covering 7 classic acoustic phenomena and 54 physically plausible compound scenarios, and train Mega-ASR with Acoustic-to-Semantic Progressive Supervised Fine-Tuning and Dual-Granularity WER-Gated Policy Optimization. Extensive experiments demonstrate that Mega-ASR achieves significant advantages over prior state-of-the-art systems on adverse-condition ASR benchmarks (45.69% vs. 54.01% on VOiCES R4-B-F, and 21.49% vs. 29.34% on NOIZEUS Sta-0). On complex compositional acoustic scenarios, Mega-ASR further delivers over 30% relative WER reduction against strong open- and closed-source baselines, establishing a scalable paradigm for robust ASR in-the-wild.
