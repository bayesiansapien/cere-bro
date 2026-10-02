# SlideDP: Full Fine-Tuning Beyond GPU Memory Across Several GPUs

**Source:** HuggingFace Daily Papers, listed 2026-10-01 · [arXiv 2609.34162](https://arxiv.org/abs/2609.34162) · [code](https://github.com/RegiaYoung/SlideDP)
**Raw:** [raw/huggingface/2026-10-01-slidedp-scaling-host-resident-llm-fine-tuning-across-multipl.md](../../raw/huggingface/2026-10-01-slidedp-scaling-host-resident-llm-fine-tuning-across-multipl.md)

## TL;DR

Host-resident training keeps the model's weights and optimizer state in CPU memory and streams layers to the GPU as needed, so a model bigger than GPU memory can be fully fine-tuned. With several GPUs on one host, each data-parallel rank used to pull its own copy of every layer over the same PCIe links and fight for the same CPU, so adding GPUs barely helped. **SlideDP** keeps one authoritative copy of the state on the host, separates how data travels from how it is stored, and pipelines three things across ranks and chunks: sending parameters out, gathering gradients back, and running the CPU optimizer step. An analytical step-time model picks chunk sizes and activation policy for a given GPU memory budget. Results: **1.46x to 2.64x** geometric-mean throughput over SlideFormer, MegaTrain and ZeRO-Offload; on four H100s with a large batch it processes over 1M tokens per step and beats GPU-resident FSDP2's measured peak by 11.2%; it supports 256K-token sequences on Qwen3-14B; and it fine-tunes **Qwen2.5-72B on four RTX 4090s**.

<div class="dg-title">One copy on the host, many GPUs fed in a pipeline</div>
<div class="dg-sub">The fix is to stop each GPU from fetching its own copy of every layer.</div>

```mermaid
flowchart LR
  H["Host state<br/><small>one authoritative copy</small>"] --> S["Stream layers<br/><small>chunked, pipelined</small>"]
  S --> G["GPU ranks<br/><small>forward and backward</small>"]
  G --> A["Gradient gather<br/><small>overlapped</small>"]
  A --> C["CPU optimizer<br/><small>updates host state</small>"]
  C --> H
  M["Step-time model<br/><small>picks chunk sizes</small>"] --> S
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class H input
  class S,A,C loop
  class G core
  class M exit
  linkStyle 4 stroke:#f08c00,stroke-width:2px
```

<div class="dg-legend">Blue is host memory, amber is the pipelined loop, purple is GPU compute, green is the planner.</div>

## How it relates to prior wiki pages

- **Cost lens for the OPD wave.** Every distillation recipe on [10-01](2026-10-01-opd-scaling-laws-saki-kl-free.md) and [10-02](2026-10-02-opd-wave-ride-lsd-oasis.md) tests at 1.7B to 8B because full fine-tuning of larger students needs a cluster. A 72B full fine-tune on four consumer GPUs moves that ceiling.
- **Memory hierarchy thread.** Same logic as SSD-tier KV caches ([memory hierarchy](../hardware/memory-hierarchy.md)): put capacity in cheap memory and hide the transfer with pipelining.

## Gaps

- Throughput for the 4x4090 72B run is not given in the abstract; it may be slow enough to matter only for small datasets.
- Beating FSDP2's "measured peak" uses a larger batch than FSDP2 could fit, so it is not a like-for-like comparison.

Related: [GPU kernels](../hardware/gpu-kernels.md) · [Memory hierarchy](../hardware/memory-hierarchy.md)
