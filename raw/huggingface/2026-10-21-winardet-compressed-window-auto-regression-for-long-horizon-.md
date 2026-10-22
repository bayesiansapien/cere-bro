---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.645568
arxiv_id: 2610.19419
url: https://huggingface.co/papers/2610.19419
arxiv_url: https://arxiv.org/abs/2610.19419
date: 2026-10-21
---

# WinARDet: Compressed Window Auto-Regression for Long-Horizon Vision-Language Grounding

MLLM-based detectors formulate vision-language grounding as autoregressive coordinate generation, yet in dense scenes, they often collapse into a box repetition loop, repeatedly emitting identical boxes until the decoding budget is exhausted. We trace this failure to historical-answer attention takeover: Under full-history autoregression, repeated coordinate tokens in the growing answer history attract disproportionate attention, crowding out the attention sinks needed to attend to new visual evidence. % To break this loop, in this paper, we propose Compressed Window Auto-Regression (WinAR). This new mechanism partitions a long answer sequence into consecutive generation windows and restricts full token-level autoregression to the current window only while compressing each previous window into a fixed set of latent tokens that condition subsequent decoding. This design reduces the repeated exposure to raw historical coordinates that triggers the attention takeover, yet preserves cross-window dependencies essential for coherent multi-object generation. On RSDense, which contains 200-2,000 objects per image, our model WinARDet improves RexOmni F1-score (IoU=0.5) from 32.16 to 39.36 over the baseline, while reducing the redundancy rate from 35.48% to 13.00%. WinARDet also generalizes across decoding strategies and output formats, including parallel box decoding and polygon generation, providing a practical paradigm for long-horizon vision-language grounding across scene densities.
