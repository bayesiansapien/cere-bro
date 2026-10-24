---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.887386+00:00
arxiv_id: 2610.22951
url: https://huggingface.co/papers/2610.22951
arxiv_url: https://arxiv.org/abs/2610.22951
date: 2026-10-23
---

# MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models

Vision-language-action (VLA) models have shown strong promise for generalist robotic manipulation, but their inference cost remains a major bottleneck for real-time control. This limitation is especially pronounced in flow-matching VLAs such as π_{0.5}, where the action expert is evaluated repeatedly during iterative denoising. We introduce MambaAct, an efficient Mamba action expert for flow-matching VLA policies. MambaAct retains the pretrained visual-language prefix encoder of π_{0.5}, while replacing its transformer-based action expert with a compact Mamba-based action expert. Within this expert, Mamba serves as the action mixer that models dependencies across the noisy continuous-action sequence. To preserve visual-language conditioning without repeated token-level cross-attention, MambaAct uses a lightweight Context Compressor to map Vision-language model (VLM) prefix tokens into a compact conditioning signal that gates and modulates each Mamba action block. MambaAct uses a 10times smaller action expert and reduces flow-matching denoising latency by 64.8% on LIBERO and 58.8% in real-world deployment, while improving mean LIBERO success by 1.08 percentage points across three independent fine-tuning seeds and maintaining gains on LIBERO-Plus and real-world benchmarks. Our code and model weights are publicly available at https://github.com/giakhuyendihoc/MambaAct.
