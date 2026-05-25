# BitCPM-CANN: native 1.58-bit training outside the CUDA ecosystem

**Source:** r/LocalLLaMA post by u/Aaaaaaaaaeeeee, paper at [OpenBMB/MiniCPM/docs/BitCPM_CANN.pdf](https://github.com/OpenBMB/MiniCPM/blob/main/docs/BitCPM_CANN.pdf) · **Date:** 2026-05-24
**Raw:** [r/LocalLLaMA digest](../../raw/reddit/2026-05-25-r-localllama.md)

## TL;DR

A systematic family-level study of 1.58-bit (ternary) quantization-aware training on the Huawei Ascend NPU platform. Models from 0.5B to 8B trained end-to-end in 1.58-bit, strictly aligned with their full-precision MiniCPM4 counterparts. Across 11 benchmarks covering commonsense, domain knowledge, and math/reasoning, the 1B/3B/8B variants retain 95.7-97.2 percent of full-precision performance, with 3B variant achieving parity on BBH and 3B/8B variants recovering nearly all of GSM8K. The 0.5B variant retains 90.1 percent. QAT integration adds only 4.5 percent throughput overhead (148 vs 155 TFLOP/s/NPU) and yields 8x weight memory reduction at inference.

```
End-to-end 1.58-bit training pipeline on Huawei Ascend:

  full-precision ─► ┌───────────────────────────────┐ ─► ternary weights
  forward / back    │ QAT: weights ∈ {-1, 0, +1}    │    (1.58 bits)
                    │ scaling factors per channel   │
                    │ straight-through estimator    │
                    └───────────────┬───────────────┘
                                    │
              CANN + MindSpeed + Megatron-LM on Ascend NPU
                                    │
                                    ▼
   Retention @ 11 benchmarks vs full-precision MiniCPM4:
     0.5B : 90.1 pct   ◄── Shannon-capacity floor (math/reasoning gap)
     1B   : 95.7 pct
     3B   : 97.2 pct   parity on BBH
     8B   : 97.0 pct   recovers GSM8K
   Cost: 4.5 pct throughput overhead, 8x weight memory reduction
```

## Key claims

- First end-to-end 1.58-bit training pipeline natively outside the CUDA ecosystem. The pipeline is ported to CANN, MindSpeed, and Megatron-LM on Ascend hardware.
- 95.7-97.2 percent of full-precision performance retained at 1B, 3B, 8B scales. The 3B variant matches full-precision on BBH; 3B and 8B recover nearly all of GSM8K.
- The 0.5B retention drops to 90.1 percent, and the residual gap concentrates on math and reasoning. The authors argue capacity, not quantization, is the bottleneck at sub-billion scales.
- Throughput cost of QAT is 4.5 percent: 148 vs 155 TFLOP/s per NPU.
- Weight memory reduction is 8x (approximately 6x end-to-end including scaling factors).

## Relation to prior wiki content

This is the second concrete data point in May for breaking the CUDA monoculture on training. The first was Alibaba's Qwen3.7-Max running autonomously for 35 hours optimizing kernels for its own custom chip (covered in [yesterday's digest](../daily-digest/2026-05/2026-05-24.md), 05-24). Huawei's BitCPM-CANN now shows that end-to-end 1.58-bit training is viable on Ascend with negligible throughput overhead. The combined signal is that the field is, slowly but visibly, building production-ready training pipelines outside Nvidia.

It also connects to the [Shannon Scaling Law](../llms-foundation-models/2026-05-25-shannon-scaling-law-noisy-channel.md) paper from the same day. The 0.5B model retaining only 90.1 percent while the 1B+ models retain 95.7-97.2 percent is exactly what the Shannon channel framing predicts: smaller models hit their information capacity faster under noise injection, and 1.58-bit quantization is a noise-injection process. The capacity bottleneck the BitCPM authors flag is the SNR-bandwidth tradeoff in Shannon Scaling, observed empirically before the theory paper had even been read.

It extends the quantization-aware training thread that ran through April with [TurboQuant](2026-04-22-turbo-quant-kv-cache-quantization.md) and similar works on KV cache quantization. Those papers attacked the inference-time cache; BitCPM-CANN attacks the training-time weights. Together they cover both sides of the precision ladder.

## Research angle

The single most consequential question is whether 1.58-bit training on Ascend matches Nvidia in absolute time-to-loss, not just retention rate. The paper reports a 4.5 percent throughput overhead on Ascend; the relevant comparison is full-precision Nvidia versus 1.58-bit Ascend at end-to-end cost, including hardware availability and price. If the Huawei pipeline is genuinely competitive after the 6x memory reduction, the production economics flip.

Second: does 1.58-bit QAT compose with MoE? The cs.LG #14 Kurate paper [MoE muP scaling](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md) gave us a clean parameterization for scaling MoE. Combining MoE with 1.58-bit weights is the obvious next step and would make the memory advantage compound.

The 0.5B retention gap is the most useful diagnostic in the paper. It says the field needs a separate research program for sub-billion-scale ternary training, not a single recipe that scales down from 8B. The follow-up question is whether selectively keeping higher precision for the smallest-scale layers recovers the missing 5 percent at 0.5B.
