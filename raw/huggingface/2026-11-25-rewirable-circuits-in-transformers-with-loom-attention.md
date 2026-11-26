---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.30634
url: https://huggingface.co/papers/2611.30634
arxiv_url: https://arxiv.org/abs/2611.30634
date: 2026-11-25
---

# Rewirable Circuits in Transformers with Loom Attention

We propose loom attention, which allows a Transformer to dynamically rewire its circuits at every token by interweaving a head's vertical attention over the outputs of earlier heads (to obtain its query, key and value) with its horizontal attention over tokens. We instantiate vertical attention efficiently with normalized and gated linear attention over a per-token matrix memory, which stores the compressed head outputs and serves as a second residual stream. This yields LoomFormer, a dual-stream architecture that splits control and content between the vector and matrix streams. Across model sizes and training token budgets in language modeling and downstream tasks, LoomFormer matches Transformers trained with over 3x compute and recent residual-stream baselines (HC/mHC, MUDDFormer, AttnRes) trained with ~1.7-2.8x. For example, trained on the same 300B tokens with only 2% extra FLOPs, LoomPythia-2.8B achieves ~1.6x the average downstream gain of mHC-Pythia-2.8B over Pythia-2.8B, and matches (0-shot) or surpasses (5-shot) Pythia-12B. Code is available at https://github.com/Caiyun-AI/LoomFormer
