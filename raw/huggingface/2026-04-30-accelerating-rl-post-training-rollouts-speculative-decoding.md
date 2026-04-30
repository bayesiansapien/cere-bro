---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00Z
arxiv_id: 2604.26779
url: https://huggingface.co/papers/2604.26779
arxiv_url: https://arxiv.org/abs/2604.26779
date: 2026-04-30
---

# Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding

**Authors:** Tiyasa Mitra, Sudipta Mondal, Rasoul Shafipour, Venmugil Elango, Terry Kong, Yuki Huang, Seonjin Na, Izzy Putterman, Benjamin Chislett, Maor Ashkenazi, Joseph Guman, Gerald Shen, Tugrul Konuk, Ashwath Aithal, Ritika Borkar, Ran Zilberstein, Bita Rouhani (NVIDIA)

RL post-training of frontier language models is increasingly bottlenecked by autoregressive rollout generation, making rollout acceleration a central systems challenge. Many existing efficiency methods improve throughput by changing the rollout or optimization regime, for example, through off-policy execution, replay, or lower-precision generation. We study speculative decoding as a lossless acceleration primitive for RL rollouts that preserves the target model's output distribution. We implement speculative decoding in NeMo-RL with a vLLM backend, supporting both synchronous and asynchronous pipelines and enabling speculation during RL rollouts. This benefit is realizable across speculation mechanisms, such as pretrained MTP heads, small external draft models or even techniques such as Eagle3, which are traditionally applied after RL phase. This yields a deployment path for state-of-the-art speculative decoding inside RL training. In a reasoning post-training workload at 8B scale under synchronous RL, speculative decoding improves rollout throughput by 1.8x. Using a high-fidelity performance simulator, we project that combining speculative decoding with asynchronous RL yields up to 2.5x end-to-end training speedup at 235B scale.

## Key findings

- **Rollout bottleneck**: Generation accounts for 65–72% of RL step time; log-prob recomputation + training account for the rest (unchanged by speculation).
- **EAGLE-3 results at 8B**: 1.77x generation speedup (RL-Zero), 1.53x (RL-Think); 1.41x overall step speedup — no change in validation accuracy (AIME-2024).
- **Draft length sweet spot**: k=3 optimal; k=5 and k=7 slower than autoregressive on RL-Think despite higher acceptance lengths. More speculative work erases the benefit.
- **Draft initialization matters**: DAPO-initialized draft (1.77x) vs UltraChat chat draft (1.51x) at same k=3. Alignment with the rollout distribution is the key driver.
- **Online adaptation**: Helps weaker initialization but provides negligible gain when draft already well-aligned.
- **n-gram drafting**: Slower than autoregressive despite non-trivial acceptance (2.47 tokens) — positive acceptance alone is insufficient.
- **Async RL interaction**: Speculation reduces exposed generation from 10.4s to 0.6s per step even in async regime (1.24x step speedup).
- **Scale projection (235B, 2048 GB200s)**: ~3.5x rollout speedup, ~2.5x end-to-end training speedup projected.
- **Weight synchronization**: Critical system requirement — draft must stay aligned with moving policy. Log-probs and policy loss computed against verifier (target) policy, not the draft.
