# Efficiency shorts (2026-10-09)

Short items from the 2026-10-09 window that touch inference cost, compression or GPU work but do not need their own page.

**Kernels and serving**
- **KernelAgent (Meta, PyTorchCon talk).** A multi-agent harness that feeds GPU hardware-performance counters into a closed loop for Triton kernel optimization. Across all 100 KernelBench L1 tasks: 2.02x over kernels from its earlier versions and 1.56x average over default torch.compile ([post](https://x.com/PyTorch/status/2108292066153230677)). Talk abstract, not a paper. See [GPU kernels](../hardware/gpu-kernels.md).
- **MXFP4 checkpoints for AMD.** Red Hat AI released more MXFP4 (4-bit microscaling floats, small blocks sharing one scale) checkpoints, e.g. Qwen3.8-27B, for vLLM on AMD GPUs ([model](https://huggingface.co/RedHatAI/Qwen3.8-27B-MXFP4)). Follows its expert-only NVFP4 release (10-06).
- **llama.cpp RPC across heterogeneous devices.** Georgi Gerganov highlighted ggml's RPC backend for splitting inference across mixed devices ([RT](https://x.com/huggingface/status/2108225596199149849)); 10-08 saw MiMo 2.6 Flash split across an RTX 6000 and an M5 laptop.
- **Disaggregated inference** (prefill and decode on separate hardware) got an endorsement from Cerebras CEO Andrew Feldman ([post](https://x.com/andrewdfeldman/status/2107968665219985746)); YC's next Paper Club is on inference systems ([RT](https://x.com/harjtaggar/status/2108331278315802817)).
- **Upscale AI launched Token Fabric**, scale-up networking for tightly coupled accelerators, congratulated by SambaNova ([post](https://x.com/SambaNovaAI/status/2108274251719655516)). No specs captured.

**Tokens and pricing**
- **GPT-6 uses the GPT-5 tokenizer.** Simon Willison's ttok 1.0 switched its default; an independent test found all seven GPT-5.5 to GPT-6 models count 44,794 tokens on 31 fixtures ([ttok 1.0](https://simonwillison.net/2026/Oct/9/ttok/)). Contrast Haiku 5.5's new tokenizer, which counts the same text as 25-30% more tokens (10-08). Per-token prices are only comparable within a tokenizer.
- **Byteification (Nature).** Ai2, Cambridge and Edinburgh convert subword LLMs to byte-level models with under 1% of a pretraining budget, about 49B tokens (AI Weekly Espresso). Byte models read code and DNA more precisely; the trade is longer sequences.

**Generation-side compression**
- **SemanTok (Stability AI).** Coarse-to-fine video tokens whose early tokens are made more semantic; a model using it matches or beats one over 3x its size ([blog](https://stability.ai/research/semantok-predictable-semantic-tokens-for-efficient-autoregressive-video-generation)).
- **GRACE** ([arXiv 2610.10524](https://arxiv.org/abs/2610.10524), HF 74 upvotes): generation-aware latent compression for video diffusion. Abstract only.
- **LittleBit (Samsung)** resurfaced on X: a 13B model under 1 GB, i.e. below 1 bit per weight. Accuracy cost unverified ([RT](https://x.com/ChrSzegedy/status/2108102814027448762)).

**Evaluation cost**
- **Agentic RAG evaluation budgets** ([arXiv 2610.05034](https://arxiv.org/abs/2610.05034)): at about 34M model tokens, spending on more questions lowers standard error 33% versus five reads per question and 12.6% versus three trajectories. Temperature zero cuts answer disagreement from 14.3% to 3.4%.

## Related

[KV cache](kv-cache.md) · [Quantization](quantization.md) · [GPU kernels](../hardware/gpu-kernels.md) · [Efficiency shorts 10-08](2026-10-08-efficiency-shorts.md)
