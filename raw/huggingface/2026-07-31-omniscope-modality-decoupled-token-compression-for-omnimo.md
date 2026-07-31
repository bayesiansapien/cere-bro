---
source: farmer/huggingface
farmed: 2026-08-01T00:00:00Z
arxiv_id: 2607.23193
url: https://huggingface.co/papers/2607.23193
arxiv_url: https://arxiv.org/abs/2607.23193
date: 2026-07-31
---

# OmniScope: Modality-Decoupled Token Compression for Omnimodal Large Language Models

Existing token compression methods for omnimodal large language models typically rely on one modality to determine what to retain in the other. We show that this assumption often breaks down: for the same query, audio and video relevance often peaks at different moments. This cross-modal salience mismatch makes unidirectional guidance prone to discarding answer-critical cues under aggressive compression. We propose OmniScope, a training-free token compression framework that uses the query as a shared semantic anchor while estimating relevance separately for audio and video. OmniScope allocates modality-specific token budgets, prunes visual tokens with an anchor-delta strategy that preserves both global context and temporal changes, and merges audio tokens within each second to reduce redundancy while maintaining temporal continuity. Across four audio-video benchmarks and two Qwen2.5-Omni model scales, OmniScope achieves the best average accuracy across all compression settings. At 25% overall token retention, it delivers up to 3.53x prefill speedup and more than 15% GPU memory reduction, with only a 0.35-point drop in average accuracy. These results suggest a simple design principle for OmniLLM inference: share the query across modalities, but not the salience estimates. The code is available at https://github.com/MAC-AutoML/OmniScope.
