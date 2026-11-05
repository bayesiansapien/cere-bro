---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.363612+05:30
arxiv_id: 2611.04449
url: https://huggingface.co/papers/2611.04449
arxiv_url: https://arxiv.org/abs/2611.04449
date: 2026-11-04
---

# Near-Zero Token Embeddings Silently Stall Training in Gated Sequence Models

Among 291 surveyed open-weight language model repositories (280 distinct embedding tables), 52.6% of untied gated and hybrid checkpoints (20/38) contain reachable input embeddings with norms below 10^{-6}, compared with 0% of weight-tied models. Such near-zero rows can arise during pretraining when unseen rare or template tokens receive zero input gradients while AdamW weight decay shrinks untied embeddings. In tested Transformer configurations, non-initial positions or a BOS token prevent this failure mode. In gated sequence models (Mamba, Gated DeltaNet, xLSTM), a near-zero token can amplify input-embedding gradients by more than 30 orders of magnitude (up to 35). At zero input, current-token readout factors (SiLU gates or linear queries) vanish, suppressing historical-state readout. Residual RMS values can then fall below the square root of the RMSNorm floor across consecutive layers, causing Pre-RMSNorm to amplify backward gradients by up to 10^3 per layer. When a gradient entry exceeds 1.84 times 10^{19}, FP32 global-norm clipping in PyTorch, Hugging Face Trainer, and FSDP2 can overflow to infinity and zero the current batch's gradients. In Telugu continual pretraining of Nemotron-3-Nano-4B, this discards updates on approximately 20% of steps and leaves triggered rows frozen. We propose two remedies. For released checkpoints, GroupClip decouples input-embedding clipping using a 64-bit or rescaled norm; its rescaled implementation eliminates update loss and heals triggered rows in one step with negligible measured end-to-end overhead. For pretraining, GateFloor (SiLU(z) + δ, δin [0.01, 0.1]) keeps the gate positive at zero input, reducing near-zero gradients by 28 orders of magnitude in experiments up to 370M parameters, with perplexity comparable to the baseline.
