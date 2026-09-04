---
source: farmer/huggingface
farmed: 2026-09-04T10:50:04.492861
arxiv_id: 2609.04098
url: https://huggingface.co/papers/2609.04098
arxiv_url: https://arxiv.org/abs/2609.04098
date: 2026-09-04
---

# Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM

Hybrid LLMs pair softmax attention with linear-attention layers such as Gated DeltaNet (GDN), whose recurrent state summarizes the context in fixed size. Early community 4-bit quantizations of Qwen3.8-27B (48 GDN layers, 16 attention layers) left the GDN block in 8- or 16-bit precision -- especially its decay and write-strength gates -- on the intuition that errors in a recurrence accumulate over long contexts. We test that intuition by building Minima: NVFP4 W4A4 on all 496 linear layers, GDN included. Across perplexity at 4K/32K, MMLU-Pro, GSM8K, AIME'25, GPQA-Diamond, LiveCodeBench, and RULER retrieval to 64K, Minima matches BF16 within seed noise (5-task average -0.52) while being the smallest (17.5 GiB) and fastest-prefill (+14-19%) recipe we compare, and its 32K perplexity gap shrinks with position. A four-part mechanism study explains why: (i) NVFP4's 16-element block scaling localizes the residual stream's extreme outliers, equalizing activation error across layer roles; (ii) the supposedly fragile gate projections are the least sensitive -- softplus/exponential and sigmoid parameterizations compress ~11% GEMM error to ~2% output error; (iii) the delta-rule recurrence holds injected noise at a flat plateau over 32K tokens and forgets a state impulse within hundreds of steps, because each write overwrites the state along the current key direction; (iv) the per-token quantization cost washes out with context instead of compounding. We also repair a global-scale mismatch that arises when per-module-calibrated NVFP4 checkpoints are served by kernels that fuse those modules into one GEMM, and show calibrated FP8 KV-cache scales are performance-free. The result: a practical recipe -- quantize everything, ship KV scales -- and a mechanistic account of why the recurrent half of a hybrid LLM is the easy half to quantize. Checkpoint: https://huggingface.co/minima-ai/mnma_qwen3.8_27b_nvfp4
