---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.936521+00:00
arxiv_id: 2609.16145
url: https://huggingface.co/papers/2609.16145
arxiv_url: https://arxiv.org/abs/2609.16145
date: 2026-09-29
---

# Safe Error Correction for Language Models: Frozen-Base Adjustment with Capability Preservation

We study a practical question: can a small correction module fix errors in a frozen language model's outputs without degrading its base capabilities? We propose CRN v2, a lightweight logit-level correction module (~34M trainable parameters, 0.73% of the 4.65B text module) that sits atop a fully frozen Gemma 4 E2B model. The base model is never updated; only the correction module learns, via supervised fine-tuning followed by reference-free DPO on 83,400 error-correction pairs. On a 60-question domain exam (CEHRI: Certified Human-Robot Intelligence, covering facts, arithmetic, and implicit-goal reasoning), CRN v2 corrects 53.3% of base-model errors (reworded variant: 43.3%) while showing no degradation on tested capability benchmarks (MMLU/BoolQ N=200; car-wash N=8). A LoRA baseline at the matched CRN v1 budget (6.6M params, rank 19) achieves 83.3% correction but suffers 30-75% capability loss on the same benchmarks -- the correction-capability tradeoff. An ablation shows that the KL preservation term (lambda=0.1) is critical: lowering it to 0.01 degrades correction to 35.0%. A hidden-state injection variant at earlier layers (1.6M params, SFT-only) reaches 50.0%/55.8% but does not exceed logit correction; shallower injection (layer 4) drops to 30.0%/28.3%; multi-depth logit correction (~35M) reaches only 40%; and longer training (5,000 SFT + 2,000 DPO) stays at 53.3% -- none of the alternative configurations we tested exceeded the rank-128 logit result, consistent with a best-achieved result of ~53% rather than a floor. This is a study of a design principle (frozen base + logit correction + KL anchoring), not a claim of architectural novelty. All code, main-result weights, and evaluation scripts are released (deep variant as code only -- no trained deep checkpoints).
