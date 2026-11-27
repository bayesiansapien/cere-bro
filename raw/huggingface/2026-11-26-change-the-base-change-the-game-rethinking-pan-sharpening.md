---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.909694+00:00
arxiv_id: 2611.32002
url: https://huggingface.co/papers/2611.32002
arxiv_url: https://arxiv.org/abs/2611.32002
date: 2026-11-26
---

# Change the Base, Change the Game: Rethinking Pan-sharpening

Many pan-sharpening (PS) networks reconstruct high-resolution multispectral (HRMS) images by adding learned residuals to 4times-interpolated low-resolution multispectral (LRMS) inputs, incorporating panchromatic (PAN) detail only through these residual corrections. This raises a simple question: Why start with a blurry base when sharp spatial detail is already available? We propose PanBase, a sharper multispectral starting point designed for more effective residual learning. Guided by physical sensor characteristics, PanBase combines PAN spatial detail with LRMS spectral information while enforcing consistency with the LRMS observations under sensor-specific blur. We construct this base without neural network training, estimating only nine coefficients per spectral band through closed-form calibration. Our PanBase can be easily integrated into existing backbones with a global residual skip through two simple changes: (i) replacing the skip base with PanBase and (ii) concatenating it as an additional input. Using each backbone's original training recipe and matched training budgets, PanBase improves most reduced- and full-resolution metrics on WorldView-3, QuickBird, and GaoFen-2, while achieving 4.4times faster training convergence on average. In zero-shot evaluation on WorldView-2, standalone PanBase achieves competitive reconstruction without target-sensor fitting or neural refinement.
