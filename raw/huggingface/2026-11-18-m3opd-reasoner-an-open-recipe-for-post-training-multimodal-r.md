---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.23034
url: https://huggingface.co/papers/2611.23034
arxiv_url: https://arxiv.org/abs/2611.23034
date: 2026-11-18
---

# M3OPD-Reasoner: An Open Recipe for Post-Training Multimodal Reasoning with Multi-Teacher On-Policy Distillation

Multi-Teacher On-Policy Distillation (MOPD) enables a single student to absorb the skills of several domain teachers by learning from its own generated responses. We present Multimodal Model Multi-Teacher On-Policy Distillation Reasoner (M3OPD-Reasoner), a fully open recipe for post-training vision-language models (VLMs) over three reasoning domains: image STEM, image perception, and video. We curate two datasets, M3OPD-SFT-1.35M for supervised fine-tuning (SFT) and M3OPD-RL-193K for reinforcement learning (RL) with verifiable rewards. On these data, we compare post-training recipes that start from Qwen3.5-9B: training one model on the mixed data of all domains (MixSFT and MixRL), and training one teacher per domain with Group Sequence Policy Optimization (GSPO), directly or after an SFT warm-up, and distilling the teachers into one student with MOPD. We evaluate on 21 image STEM, image perception, and video reasoning benchmarks after we decontaminate the training data against them. The comparison establishes MOPD of teachers trained with GSPO directly from Qwen3.5-9B as the best recipe: the student closely matches each teacher on its own domain and is on average above the mixed-training baselines on the same prompts. Since MOPD already merges the domain capabilities that MixRL would otherwise have to learn, its student is a stronger starting point for RL, and we ask whether the same data can carry the model further from there: we add MixRL on top of the MOPD student, on the same prompts and with the same settings, which, to our knowledge, no prior VLM recipe has studied. The same prompts still improve the MOPD student, with no collapse, and give our main model, M3OPD-Reasoner-9B. MOPD and MixRL can therefore work as consecutive stages that get more out of the same data. We release all data, the training code, and the checkpoints of every stage.
