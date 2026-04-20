# GPU Kernels and Accelerator Optimization

How AI computations are mapped to the specific instruction sets and memory hierarchies of GPU and accelerator hardware. Kernel optimization determines how efficiently a model actually runs — the gap between theoretical peak FLOPS and real throughput.

## Current State (as of 2026-04-20)

Kernel optimization is one of the hardest bottlenecks in production AI: hardware-specific, expert-intensive, and time-consuming. The dominant paradigm has been hand-tuned kernels by specialists (CUDA experts for NVIDIA, NKI experts for AWS Trainium). AccelOpt is the first paper in the wiki to demonstrate that an LLM agent can automate this process without expert-provided knowledge.

## Key Papers

**AccelOpt (2026-04-20)** — Self-improving LLM agent for AWS Trainium kernel optimization. Maintains a memory of slow-fast kernel pairs from past iterations, uses it to guide generation of improved variants. Raises peak throughput from 49% → 61% on Trainium 1 (45% → 59% on Trainium 2). Matches Claude Sonnet 4 performance using open-source models at 26x lower cost. Introduces NKIBench, the first kernel benchmark for Trainium. → [summary](../inference-efficiency/2026-04-20-accelopt-gpu-kernel-optimization.md)

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
