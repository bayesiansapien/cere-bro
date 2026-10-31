---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.161283+00:00
arxiv_id: 2610.39663
url: https://huggingface.co/papers/2610.39663
arxiv_url: https://arxiv.org/abs/2610.39663
date: 2026-10-30
---

# AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers

Video diffusion transformers generate high-quality videos, but the quadratic cost of 3D full attention dominates their inference. Dynamic block-sparse attention reduces this cost by computing exact attention only on key/value blocks selected from current activations. However, its fidelity degrades under aggressive sparsity: blocks are scored from coarse summaries or formed by costly global clustering, pruned blocks vanish from the softmax, and whole tiles are kept or dropped even when only a few of their keys matter. To address these limitations, we propose Accurate Block Attention (AB-Attention), a training-free method that accurately approximates dense attention at high sparsity. Its Intra-Block Clustering Selector (IBCS) estimates block importance faithfully yet cheaply by clustering queries only within each query block, without permuting tokens. Sampling with Inclusion-Probability Weighting (SIP) then samples blocks in proportion to these estimates and reweights them by inverse inclusion probability, so that one pass estimates dense attention rather than truncating it. Finally, its kernel gathers key/value blocks much smaller than a tile into full tensor-core tiles, refining selection at no extra tensor-core cost. On Wan2.1 and HunyuanVideo, AB-Attention skips 89--92\% of attention, whereas the baselines compute 1.8--3.6times as much, yet it still improves PSNR by up to 4.4~dB over the strongest baseline and achieves up to 2.23times end-to-end speedup. Our code is available at https://github.com/InfRec-Cardinal/AB-Attention.
