---
source: farmer/huggingface
farmed: 2026-06-06T09:05:36Z
arxiv_id: 2606.06416
url: https://huggingface.co/papers/2606.06416
arxiv_url: https://arxiv.org/abs/2606.06416
date: 2026-06-06
---

# Unsupervised Skill Discovery for Agentic Data Analysis

Inference-time skill augmentation provides a lightweight way to improve data-analytic agents by injecting reusable procedural knowledge without updating model parameters. However, discovering effective skills for data analysis remains challenging, as reliable supervision is expensive and success criteria vary across analytical formats. This raises the key question of how to discover reusable data-analysis skills from unlabeled exploration alone. We propose DataCOPE, an unsupervised verifier-guided skill discovery framework for data-analytic agents. DataCOPE derives verifier signals from the exploration trajectories and uses them to characterize relative quality or aggreement among trajectories. It iteratively coordinates a Data-Analytic Agent for trajectory generation, an Unsupervised Verifier for signal extraction, and a Skill Manager for contrastive skill distillation. For report-style analysis, we instantiate the verifier as an Adaptive Checklist Verifier that derives task-specific criteria, scores reports by verifiable coverage, and iteratively refines the checklist. For reasoning-style analysis, we instantiate it as an Answer Agreement Verifier that groups trajectories by answer agreement and uses self-consistency as an auxiliary signal. We evaluate DataCOPE on report-style analysis from Deep Data Research and reasoning-style analysis from DABStep. Across both settings, DataCOPE consistently improves held-out performance over baselines. Averaged across four model settings, DataCOPE improves the mean score by 9.71% and 32.30% on report-style and reasoning-style tasks respectively.
