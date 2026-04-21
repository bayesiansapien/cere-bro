# GPU Kernels and Accelerator Optimization

How AI computations are mapped to the specific instruction sets and memory hierarchies of GPU and accelerator hardware. Kernel optimization determines how efficiently a model actually runs — the gap between theoretical peak FLOPS and real throughput.

## Current State (as of 2026-04-21)

Kernel optimization is one of the hardest bottlenecks in production AI: hardware-specific, expert-intensive, and time-consuming. The dominant paradigm has been hand-tuned kernels by specialists (CUDA experts for NVIDIA, NKI experts for AWS Trainium). AccelOpt demonstrated LLM-agent-based automation; Nemotron 3 Super now shows the architectural path forward — hybrid SSM+MoE with native FP4 training and built-in speculative decoding, compressing the throughput gains from architectural decisions rather than kernel tuning alone. The SemiAnalysis goodput framework adds the economic layer: even optimal kernel performance gets negated by poor cluster reliability.

## Key Papers

**AccelOpt (2026-04-20)** — Self-improving LLM agent for AWS Trainium kernel optimization. Maintains a memory of slow-fast kernel pairs from past iterations, uses it to guide generation of improved variants. Raises peak throughput from 49% → 61% on Trainium 1 (45% → 59% on Trainium 2). Matches Claude Sonnet 4 performance using open-source models at 26x lower cost. Introduces NKIBench, the first kernel benchmark for Trainium. → [summary](../inference-efficiency/2026-04-20-accelopt-gpu-kernel-optimization.md)

**Nemotron 3 Super (2026-04-21)** — NVIDIA's hybrid Mamba-Attention MoE: 120B total / 12B active parameters, first Nemotron pretrained in NVFP4 (25T tokens), 1M context length. 2.2x throughput over GPT-OSS-120B, 7.5x over Qwen3.5-122B. MTP layers enable native speculative decoding with no external draft model. All artifacts open-sourced. Demonstrates convergence of SSM + sparse MoE + FP4 pretraining + native speculative decoding in a single architecture. → [summary](../inference-efficiency/2026-04-21-nemotron3-super-hybrid-moe.md)

**SemiAnalysis GPU Cluster TCO / Goodput (2026-04-21)** — Comprehensive framework based on 80+ neoclouds and 150+ customer interviews. Key finding: two providers at identical GPU-hour pricing can differ by 6–21% in useful work delivered (goodput). Three-tier recovery model (checkpoint-cold, checkpoint-hot, fault-tolerant). Gold-tier neoclouds (Nebius, Fluidstack, Crusoe) 5–15% cheaper than silver tier for large pretraining at the same nominal price. No open-source zero-overhead fault-tolerant training framework exists. → [summary](2026-04-21-semianalysis-gpu-cluster-goodput.md)

## Key Concepts

- **Peak throughput utilization**: fraction of the hardware's theoretical maximum FLOPS actually achieved. A kernel at 61% throughput leaves 39% of the hardware idle or stalled.
- **NKI (Neuron Kernel Interface)**: AWS's programming model for Trainium accelerators, analogous to CUDA for NVIDIA GPUs. Writing efficient NKI code requires understanding Trainium's specific memory hierarchy (HBM, SBUF, PSUM) and compute engines.
- **Memory hierarchy**: modern AI accelerators have multiple memory tiers (high-bandwidth memory, on-chip SRAM, register files). Efficient kernels minimize data movement across tiers. This is the primary source of throughput gaps.
- **Kernel memory**: AccelOpt's key innovation — rather than trying to solve each kernel from scratch, accumulate (slow, fast) pairs and use them as few-shot examples. The quality of memory curation determines the quality of future improvements.
- **Operator fusion**: combining multiple operations (e.g., matmul + activation + normalization) into a single kernel pass to avoid intermediate memory round-trips. Expert-designed kernels like FlashAttention exploit this extensively.

## Open Problems

1. **Generalization across hardware**: AccelOpt targets Trainium; does the same LLM-agent approach transfer to new hardware (Blackwell, future accelerators) without restarting the memory from scratch?
2. **Memory curation strategy**: what's the optimal policy for deciding which slow-fast pairs to retain, forget, or summarize as the memory grows?
3. **Plateau problem**: even with memory, AccelOpt doesn't close the full throughput gap (61% peak, not 100%). The remaining gap likely requires novelty the memory can't provide — what class of optimizations is beyond the memory-based approach?
4. **Interaction with FlashAttention**: LLM workloads spend most compute in attention. How does LLM-agent kernel optimization interact with hand-designed attention kernels?

## Related Pages

- [KV Cache](../inference-efficiency/kv-cache.md)
- [AccelOpt summary](../inference-efficiency/2026-04-20-accelopt-gpu-kernel-optimization.md)
