---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.353484+05:30
arxiv_id: 2609.34162
url: https://huggingface.co/papers/2609.34162
arxiv_url: https://arxiv.org/abs/2609.34162
date: 2026-10-01
---

# SlideDP: Scaling Host-Resident LLM Fine-Tuning Across Multiple GPUs

Host-resident layer streaming enables full-parameter LLM fine-tuning beyond GPU memory, but data-parallel ranks compete for shared host resources. Replicated transfers amplify traffic, while strong scaling can expose host work as computation windows shrink. We present SlideDP, a synchronous data-parallel runtime for shared-host multi-GPU systems. It maintains one authoritative host state, decouples communication routes from state layout, and pipelines parameter delivery, gradient aggregation, and CPU updates across ranks and chunks. An analytical step-time model characterizes resource bottlenecks and pipeline exposure; runtime measurements guide communication, chunking, and activation policies under a GPU memory budget. In matched-batch sweeps, SlideDP achieves geometric-mean throughput ratios of 1.46-2.64times over SlideFormer, MegaTrain, and ZeRO-Offload. On four H100s, SlideDP approaches GPU-resident FSDP2 throughput for Qwen3-14B at a smaller batch size. With a larger batch, it processes over 1M tokens per step and exceeds FSDP2's measured peak throughput by 11.2%. Separately, it supports 256K-token sequences for the same model and fine-tunes Qwen2.5-72B on four RTX 4090 GPUs. Project page: https://github.com/RegiaYoung/SlideDP.
