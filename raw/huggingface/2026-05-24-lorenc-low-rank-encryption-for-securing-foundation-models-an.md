---
source: farmer/huggingface
farmed: 2026-05-24T05:07:38.368292+00:00
arxiv_id: 2605.13163
url: https://huggingface.co/papers/2605.13163
arxiv_url: https://arxiv.org/abs/2605.13163
date: 2026-05-24
---

# LoREnc: Low-Rank Encryption for Securing Foundation Models and LoRA Adapters

Foundation models and low-rank adapters enable efficient on-device generative AI but raise risks such as intellectual property leakage and model recovery attacks. Existing defenses are often impractical because they require retraining or access to the original dataset. We propose LoREnc, a training-free framework that secures both FMs and adapters via spectral truncation and compensation. LoREnc suppresses dominant low-rank components of FM weights, compensates for the missing information in authorized adapters, and further applies orthogonal reparameterization to obscure structural fingerprints of the protected adapter. Unauthorized users produce structurally collapsed outputs, while authorized users recover exact performance. Experiments demonstrate that LoREnc provides strong protection against model recovery with under 1% computational overhead.
