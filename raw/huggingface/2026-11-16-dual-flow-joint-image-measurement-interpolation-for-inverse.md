---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.003875+00:00
arxiv_id: 2611.05843
url: https://huggingface.co/papers/2611.05843
arxiv_url: https://arxiv.org/abs/2611.05843
date: 2026-11-16
---

# Dual Flow: Joint Image-Measurement Interpolation for Inverse Problems

Generative model-based approaches to linear inverse problems typically use the acquired noisy measurement to condition or guide sampling in the image domain. In this work, we introduce Dual Flow, a novel joint-flow model for solving linear inverse problems by jointly estimating the clean image and corresponding noise-free measurement from the observation. Specifically, Dual Flow formulates image reconstruction and measurement denoising as a coupled estimation problem, using coupled flows in the image and measurement domains. The acquired noisy measurement is used only to initialize the measurement state; thereafter, image and measurement states are jointly updated based on their current values. By construction, the final image and measurement estimates are guaranteed to satisfy the underlying forward model. We derive the sampling updates for the joint-flow which involves the conditional mean of the clean image given the joint state. We further derive a closed-form expression for a sufficient statistic of the joint state and show that the required conditional mean can be obtained by solving an image-domain Gaussian denoising problem involving operator-dependent, correlated noise. We train a velocity-prediction network using this formulation to estimate the conditional mean from the derived sufficient statistic. Extensive experiments across various linear inverse problems and image datasets demonstrate state-of-the-art performance in both distortion metrics and perceptual quality. Dual Flow requires no hyperparameter tuning beyond the number of inference steps and achieves shorter reconstruction times than competing methods. Additional analyses assess robustness to model mismatch, as well as the ability to generate diverse plausible reconstructions and characterize reconstruction uncertainty.
