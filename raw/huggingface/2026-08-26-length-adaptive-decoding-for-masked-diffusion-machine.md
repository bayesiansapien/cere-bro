---
source: farmer/huggingface
farmed: 2026-08-26T12:46:47.908232
arxiv_id: 2608.22274
url: https://huggingface.co/papers/2608.22274
arxiv_url: https://arxiv.org/abs/2608.22274
date: 2026-08-26
upvotes: 1
---

# Length-Adaptive Decoding for Masked Diffusion Machine Translation

Machine translation tests masked diffusion language models (dLLMs) because every source token must be rendered faithfully, while fixed canvas decoding must choose target length before denoising. Existing masked diffusion decoding work mainly studies token unmasking order, leaving this length decision under-explored despite its direct effect on coverage and redundancy. We introduce Entropy-Valley (EV), a training-free length selector that scores candidate target canvases by mean predictive entropy from all-mask forward passes and selects the canvas the backbone is most prepared to fill. Relative to a baseline using training corpus length statistics, EV recovers 64.9%, 65.3%, and 33.0% of the COMET-22 gain from reference target lengths on EntoZh, ZhtoEn, and EntoDe. Our diagnostics show that denoising-friendly lengths need not match reference lengths. Evaluation by three translation experts supports the EnleftrightarrowZh adequacy gains, with stronger evidence on ZhtoEn. Compared with a LLaMA-3-8B autoregressive (AR) model trained on the same fine-tuning data, the EV system ties on EntoZh and leads on ZhtoEn; an oracle-length diagnostic further shows that, in this masked diffusion MT setting, deciding which tokens to reveal first matters less than how the target length is supplied.
