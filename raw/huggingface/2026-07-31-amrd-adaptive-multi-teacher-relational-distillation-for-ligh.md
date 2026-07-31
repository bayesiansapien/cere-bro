---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.25289
url: https://huggingface.co/papers/2607.25289
arxiv_url: https://arxiv.org/abs/2607.25289
date: 2026-07-31
---

# AMRD: Adaptive Multi-Teacher Relational Distillation for Lightweight Speech Emotion Recognition

On-device speech emotion recognition (SER) is critical for real-time applications, yet large self-supervised models that excel at SER are too costly for edge devices. Multi-teacher knowledge distillation can compress them into a lightweight student, but two challenges remain: teacher reliability varies across batches, and logit-level distillation ignores inter-sample relational structure. We propose Adaptive Multi-teacher Relational Distillation (AMRD) to address both. A one-class SVM on each teacher's logit similarity matrix assigns per-batch weights favoring more coherent teachers. A relational distillation loss aligns teacher and student similarity matrices, capturing structure that logit matching misses. On IEMOCAP and CREMA-D datasets across four student architectures, AMRD outperforms single-teacher distillation baselines in most settings, and ablations confirm both components yield complementary gains.
