---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.08777
url: https://huggingface.co/papers/2610.08777
arxiv_url: https://arxiv.org/abs/2610.08777
date: 2026-10-07
---

# CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching

Interactive video world models need to generate each video chunk efficiently while responding faithfully to user controls. Many systems use chunk-wise autoregressive generation with few-step denoising, but each chunk still requires several costly denoising iterations. Training-free caching can reduce this cost, yet existing policies make reuse decisions primarily from model-internal denoising dynamics and do not explicitly account for control transitions. Actually, interactive generation explicitly exposes a signal they do not use: the controls for a chunk arrive before it is denoised, so a schedule derived from them costs no forward pass. To this end, we analyze adjacent chunks under different control regimes and find that structural similarity drops around action changes, while low-frequency structure remains more persistent than high-frequency detail. Motivated by these observations, we propose CtrlCache, a training-free control-aware caching framework that adapts computation to the current control sequence. Specifically, the action-aware scheduling and refresh policy detects action changes across and within chunks, and labels each chunk as initial, transition, turning, or steady state. At one selected interior denoising step, initial and transition chunks retain full computation, while turning and steady chunks reuse the transformer residual from the most recent fully computed step in the same chunk. To exploit the persistence of low-frequency structure during steady interaction, we further introduce a frequency-mixed history prior guidance that incorporates complementary information from the preceding clean latent without an additional DiT forward pass. Evaluated on Matrix-Game 2.0 and LingBot-World v1/v2, CtrlCache achieves 1.21x to 1.41x DiT-backbone speedups without model retraining while improving WBench Overall scores over original inference across all three models.
