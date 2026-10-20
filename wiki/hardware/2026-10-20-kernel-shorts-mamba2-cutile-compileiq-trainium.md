# Kernel shorts: Mamba-2 in cuTile, CompileIQ + Helion, Deepgram on Trainium2

**Sources:** [NVIDIA Developer, Mamba-2 forward kernels in CUDA Tile](https://developer.nvidia.com/blog/accelerating-mamba-2-with-high-performance-forward-pass-kernels-in-nvidia-cuda-tile/) (2026-10-19); [PyTorch on X, CompileIQ + Helion](https://x.com/PyTorch/status/2112212326057148443); [AWS, Deepgram Nova-3 on Trainium2](https://aws.amazon.com/blogs/machine-learning/how-deepgram-optimized-voice-ai-at-scale-with-aws-trainium/); [IBM Research, Dataflow Architectures course](https://research.ibm.com/blog/coursera-dataflow-accelerator-architecture-specialization). Raw: [`raw/labs/2026-10-20-100728-labs.md`](../../raw/labs/2026-10-20-100728-labs.md), [`raw/labs/2026-10-19-180645-labs.md`](../../raw/labs/2026-10-19-180645-labs.md)

## TL;DR

- **Mamba-2 in cuTile (Jane Street + NVIDIA).** cuTile is NVIDIA's Python tile-level kernel DSL. The Mamba-2 forward pass becomes three kernels. `chunk_cumsum` stores the log-space cumulative decay once. `fwd_pass_state` jumps the hidden state across chunks with a Tensor Core matmul (h_{t+T} = exp(G_last) h_t + (exp(G_last - G) B) X^T). `compute_out` fuses the carried state, the decayed causal interaction matrix and the skip connection in registers, in TF32. Numerical safety comes free: the causal mask discards every exponential of a positive number. Tuning used latency hints, operand swaps into Tensor Memory, TMA-friendly transposed layouts and a per-shape autotuner. The post gives no headline speedup.
- **CompileIQ + Helion.** NVIDIA's CompileIQ exposes ptxas decisions (register allocation, fine scheduling) as Advanced Control Files; Helion's autotuner now searches them jointly with tile shape, warps and stages. Aimed at kernels already autotuned to the limit.
- **Deepgram Nova-3 on Trainium2.** Ported from PyTorch with TorchNeuron (torch.compile, no CPU fallbacks), NKI library fused kernels (QKV, FFN, depthwise conv), then agent-assisted kernel tuning (Neuron Agentic Development toolkit). Eight replicas per trn2.3xlarge; **11-70% more audio per dollar** than Deepgram's prior compute for offline batch transcription.
- **IBM's Dataflow Architectures course** teaches one PyTorch model across GPU, TPU, Cerebras WSE, Groq LPU and IBM Spyre: a sign that multi-target compilation is now a job skill.

## How this relates to prior wiki pages

- **Agent-written kernels are now in vendor tooling.** Meta's AMD port (10-19) used agentic CUDA-to-HIP porting; AWS ships an agentic kernel-tuning toolkit. See [gpu-kernels](gpu-kernels.md).
- **Hybrid/SSM kernels catch up:** the Mamba-2 chunked formulation (state jump + masked "linear attention" inside a chunk) is the same structure ReplaySSM (10-13) and today's ReaDy exploit. See [attention-mechanisms](../llms-foundation-models/attention-mechanisms.md).
- **Portability is the theme of the day:** TorchNeuron (one setting to target Trainium), the course, and Meta's AMD co-design all lower the cost of leaving CUDA.
