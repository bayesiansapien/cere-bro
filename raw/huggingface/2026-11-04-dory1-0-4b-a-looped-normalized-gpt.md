---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.363311+05:30
arxiv_id: 2611.03998
url: https://huggingface.co/papers/2611.03998
arxiv_url: https://arxiv.org/abs/2611.03998
date: 2026-11-04
---

# Dory1.0-4B: A Looped Normalized-GPT

We introduce Dory1.0-4B, a 4-billion-parameter looped (latent-recurrent) language model with elastic depth: a single checkpoint serves different inference compute budgets. Dory1.0-4B is built on a normalized Transformer (nGPT) backbone with interleaved sliding-window and full-attention layers, organized into an input block, a shared recurrent block, and an output block. At inference, the recurrent block can be applied a variable number of times. We pre-trained Dory1.0-4B on 6 trillion tokens. The first 4.5 trillion tokens were trained in NVFP4, and additional pre-training then extended the context length to 256K tokens. Next, we post-trained the model using Supervised Fine-Tuning (SFT) and Reinforcement Learning with Verifiable Rewards (RLVR), with a difficulty-aware loop curriculum that routes harder prompts to deeper loops. Increasing the loop count improves accuracy, with the largest gains on coding, agentic, and long-context benchmarks. With two or more loops, Dory1.0-4B outperforms larger models such as Qwen3.5-9B, Gemma 4 12B, and Gemma 4 26B-A4B on average across 12 benchmarks. Looping also makes Dory1.0-4B more token-efficient on agentic benchmarks: with four loops, it generates 1.3-2.5x fewer tokens than with one loop, as the extra computation is spent in latent space rather than on longer outputs. To reduce memory during looping, Dory1.0-4B caches keys and values only from the last loop, keeping its KV-cache footprint equal to that of a non-looped model at any loop count while retaining most of the accuracy gains. We open-source the BF16, MXFP8, NVFP4, and GGUF quantized checkpoints.
