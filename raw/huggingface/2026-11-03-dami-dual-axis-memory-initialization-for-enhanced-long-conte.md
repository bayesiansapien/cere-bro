---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.41994
url: https://huggingface.co/papers/2610.41994
arxiv_url: https://arxiv.org/abs/2610.41994
date: 2026-11-03
---

# DAMI: Dual-Axis Memory Initialization for Enhanced Long-Context Retrieval in Gated Linear Attention

Linear attention scales linearly with sequence length, but its finite-state memory can limit long-context retrieval. In gated linear recurrences, memory retention depends on state decay, which is shaped jointly by gate parameters A_log and dt_bias and by input activations. In controlled Gated DeltaNet (GDN) experiments, both parameters remain highly correlated with their initial values after training, highlighting the importance of initialization. Therefore, we introduce Dual-Axis Memory Initialization (DAMI), which jointly configures these parameters before training. DAMI assigns geometric timescales across heads for varied retrieval distances and a low-high-low input-sensitivity profile across layers. A small activation sample calibrates the GDN-family implementation to match both behavioral targets without adding trainable parameters. Across GDN, KDA, GDN2, Mamba-2, and RWKV-7, DAMI improves average RULER-style retrieval accuracy by 5.29 to 16.71 percentage points over the corresponding random-initialization baselines. Performance on language modeling, commonsense reasoning, and 2K real-world retrieval remains broadly comparable to those baselines. Our code is available at https://speedai.com/research/dami.
