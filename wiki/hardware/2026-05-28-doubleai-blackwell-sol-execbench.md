# DoubleAI Speed-of-Light Blackwell CUDA Kernels (SOL-ExecBench)

**Date ingested:** 2026-05-28
**Source:** r/CUDA (community-curated practitioner report)
**Links:** [doubleAI blog](https://www.doubleai.com/research/warpspeed-approaches-speed-of-light-on-blackwell) · [SOL-ExecBench](https://research.nvidia.com/benchmarks/sol-execbench) · [r/CUDA post](https://www.reddit.com/r/CUDA/comments/1tpar2n/new_ai_system_writes_speedoflight_blackwell_cuda/) · [raw](../../raw/reddit/2026-05-28-r-cuda.md)

## TL;DR

DoubleAI's AI performance-engineering system ran on NVIDIA's new SOL-ExecBench (Speed-of-Light Execution Benchmark, 235 production kernels lifted from DeepSeek, Qwen, Gemma, Kimi, scored on Blackwell B200) and topped every kernel class with 90% wins versus the optimized baseline and 2.24x average speedup. Several generated kernels reportedly reached "speed of light", the least time physically possible on the hardware, including grouped-query attention for Qwen3-14B with NVFP4 inference at 14.9x over the optimized baseline, and warp-specialized single-CTA tcgen05 NVFP4 pipelined GEMM for Qwen3-VL-32B.

## Key findings

- 90% wins vs optimized baseline on SOL-ExecBench's 235 production kernels.
- 2.24x average speedup across the full benchmark.
- Qwen3-14B GQA at 14.9x baseline using NVFP4 inference kernels.
- Multiple kernels hitting the hardware speed-of-light bound.
- Includes warp-specialized Blackwell code, e.g., single-CTA tcgen05 NVFP4 pipelined GEMM for Qwen3-VL-32B.

## How this fits prior wiki state

This is the most aggressive AI-written-kernel result so far this year and lands on the same day as a cautionary r/MachineLearning post ("AI-generated CUDA kernels silently break training and inference") showing that one of the SOL-ExecBench top submissions accumulated embedding-gradient sums in bf16 when fp32 was required, causing silent loss divergence on real-text data while passing the benchmark's verifier. The two posts together form a sharp picture: AI kernel writing now wins benchmarks at speed-of-light, while still being able to introduce silent correctness bugs that benchmarks miss.

This pattern repeats the SemiAnalysis Miscompiles story (today, via Gmail and RSS), where AI agents found hundreds of plausible LLVM bugs including atomic-store-to-non-atomic miscompiles in a single afternoon. The combined message: AI is now competitive at writing low-level code and also at finding bugs in low-level code, but the verifier gap is real.

The doubleAI result also continues the gpu-kernels concept thread, alongside AccelOpt ([[2026-04-20-accelopt-gpu-kernel-optimization]]), KernelBench ([[2026-05-09-kernelbench-x-llm-gpu-kernel-benchmark]]), AgentKernelArena ([[2026-05-19-agentkernelarena-gpu-kernel-optimization-agents-benchmark]]).

## Related pages

- [[gpu-kernels]], concept page
- [[2026-04-20-accelopt-gpu-kernel-optimization]], earlier GPU kernel optimization agent
- [[2026-05-19-agentkernelarena-gpu-kernel-optimization-agents-benchmark]], kernel-agent benchmark

## Research angle

The verifier gap is the binding constraint. SOL-ExecBench's verifier accepted a kernel that silently breaks training on real data; doubleAI's wins are real but unaudited downstream. A community-curated "correctness suite" that runs accepted kernels in actual training and inference workloads for a few thousand steps before declaring victory would catch the bf16-precision class of bugs. This is the natural next-paper from the r/ML side of today's pairing.
