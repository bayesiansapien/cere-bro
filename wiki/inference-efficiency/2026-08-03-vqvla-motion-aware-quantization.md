# VQVLA: Motion-Aware Vector Quantization with Centroid Reuse for VLA Inference

**arxiv:** [2607.24148](https://arxiv.org/abs/2607.24148) · **Source:** [Kurate cs.AI weekly leaderboard #14, 2026-08-03](../../raw/kurate/2026-08-03-cs-ai.md) (score 1377, ai_rating 6.0/10) · **Authors:** Zhuoran Song, Haozhe Jiang, Chunyu Qi, Minnan Pei, Gang Li, Xiaoyao Liang, Haibing Guan

## TL;DR

Vision-Language-Action models drive robots by mapping camera input and an instruction to a motor command, and their problem is latency: a control loop cannot wait for a large transformer. Prior accelerators such as Dadu-Corki improved the schedule but kept the model at full precision. VQVLA is an algorithm-hardware co-design that attacks precision and redundant compute together, and its interesting move is making the quantization **state-dependent**.

**MotionVQ** varies vector-quantization precision according to the robot's current execution state. Coarse approach motion tolerates aggressive quantization; fine contact-adjacent motion does not. The precision schedule follows the trajectory rather than the tensor statistics, which is a different conditioning variable from anything on the [KV cache page](kv-cache.md) or the quantization literature generally.

**Merged-centroid vectorized GEMM** is the compute half. Once weights are vector-quantized, they are codebook indices, and matrix multiplication over indices can skip multiplications entirely by aggregating spatially and reusing centroids temporally. The accelerator is designed to support dynamic precision selection and centroid reuse directly. Reported speedups: **6.5x over an A100, 2.8x over Dadu-Corki, 1.9x over LUT-DLA, 3.3x over CodeGEMM, 4.3x over ShiftAddLLM**, with negligible accuracy loss.

## Why it is logged here despite being a robotics paper

Two transferable ideas.

**Execution state as a quantization schedule.** Every quantization method in this wiki conditions on the data: activation outliers, weight distributions, per-channel scales. [MXAttention (08-01)](2026-08-01-mxattention-mxfp4-attention-quantization.md) derived a distribution-*independent* optimal scaling boundary at Qmax = 7.25 precisely by getting away from data conditioning. VQVLA conditions on neither the data nor the format but on **where the agent is in its task**, which is a control-flow signal from outside the model. The same instinct would apply directly to an LLM agent: an exploratory search step and a final answer-composition step do not need the same numerical precision, and nobody has built that.

**Centroid reuse is the compute-side dual of KV reuse.** Skipping multiplications because the same centroid recurs spatially and temporally is structurally the same argument as skipping attention reads because the same keys recur, which is what [MotionCache (05-05)](2026-05-05-motion-aware-caching-video.md) did on the video-denoising axis using inter-frame differences to decide which pixels need full recomputation. Both papers even use motion as the reuse signal. The pattern across the two: **when the input stream is temporally smooth, the reuse opportunity is in the intermediate representation, not the cache.**

## Gaps

The comparison set is a mix of GPUs and prior accelerators, and a 6.5x over an A100 from a custom accelerator is not an apples-to-apples number, since much of it is the accelerator rather than MotionVQ. There is no ablation separating the quantization contribution from the GEMM contribution from the hardware contribution, which is the number a reader would actually want. "Negligible accuracy degradation" is reported as task success rate, which is a coarse metric that can hide degraded motion smoothness. And the execution-state signal that drives precision selection is not described in the abstract as learned or hand-specified, which decides whether this transfers to a new robot or has to be re-tuned per platform.

## Related pages

- [KV Cache](kv-cache.md)
- [MXAttention (08-01)](2026-08-01-mxattention-mxfp4-attention-quantization.md)
- [MotionCache (05-05)](2026-05-05-motion-aware-caching-video.md)
- [GPU Kernels](../hardware/gpu-kernels.md)
