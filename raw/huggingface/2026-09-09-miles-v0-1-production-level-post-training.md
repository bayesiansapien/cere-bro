---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.08368
url: https://huggingface.co/papers/2609.08368
arxiv_url: https://arxiv.org/abs/2609.08368
date: 2026-09-09
---

# Miles v0.1: Production-Level Post-Training

We present Miles v0.1, a full-stack, production-ready system for frontier post-training. Building upon the clean design of slime, Miles designs each stage of the reinforcement-learning (RL) training loop around a single principle: components should be verified, clean, and customizable. With accuracy, efficiency, reliability, and scalability as first-class goals, Miles aims to make frontier-scale RL accessible to researchers and enterprises alike. This report walks through the system end to end: rollout engines built on SGLang, a trainer with a choice of two backends (NVIDIA Megatron-LM and PyTorch FSDP), and three weight-synchronization transports for different deployment topologies. Beyond full-parameter RL, Miles also supports LoRA RL, on-policy distillation, supervised fine-tuning, and true-on-policy rollout-training alignment, and extends the same architecture to diffusion models. We close with an end-to-end case study: fully asynchronous agentic RL on a GLM-5.2 744B-A40B model over terminal-use coding tasks, running on 64 NVIDIA GB300 GPUs with a median step time of 263 seconds over the first 30 measured steps. Miles is open-sourced at https://github.com/radixark/miles, with the project website at https://miles.radixark.com.
