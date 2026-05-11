---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.06628
url: https://huggingface.co/papers/2605.06628
arxiv_url: https://arxiv.org/abs/2605.06628
date: 2026-05-11
---

# LiVeAction: a Lightweight, Versatile, and Asymmetric Neural Codec Design for Real-time Operation

Modern sensors generate rich, high-fidelity data, yet applications operating on wearable or remote sensing devices remain constrained by bandwidth and power budgets. Standardized codecs such as JPEG and MPEG achieve efficient trade-offs between bitrate and perceptual quality but are designed for human perception, limiting their applicability to machine-perception tasks and non-traditional modalities such as spatial audio arrays, hyperspectral images, and 3D medical images. General-purpose compression schemes based on scalar quantization or resolution reduction are broadly applicable but fail to exploit inherent signal redundancies, resulting in suboptimal rate-distortion performance. Recent generative neural codecs, or tokenizers, model complex signal dependencies but are often over-parameterized, data-hungry, and modality-specific, making them impractical for resource-constrained environments. We introduce a Lightweight, Versatile, and Asymmetric neural codec architecture (LiVeAction), that addresses these limitations through two key ideas. (1) To reduce the complexity of the encoder to meet the resource constraints of the execution environments, we impose an FFT-like structure and reduce the overall size and depth of the neural-network-based analysis transform. (2) To allow arbitrary signal modalities and simplify training, we replace adversarial and perceptual losses with a variance-based rate penalty. Our design produces codecs that deliver superior rate-distortion performance compared to state-of-the-art generative tokenizers, while remaining practical for deployment on low-power sensors.
