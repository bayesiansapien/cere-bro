---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.365577+05:30
arxiv_id: 2611.03360
url: https://huggingface.co/papers/2611.03360
arxiv_url: https://arxiv.org/abs/2611.03360
date: 2026-11-04
---

# Every Pixel Is an Option: A System One Model for Medical Ultrasound Biometry

**Purpose:** Ultrasound biometry is widely used across various clinical applications, including prenatal and cardiac examinations, to obtain quantitative measurements by placing calipers at anatomical landmarks. However, these measurements remain subject to interoperator variability as they rely largely on manual caliper placement. Conventional methods often use specialized prediction heads for different ultrasound tasks, whereas vision-language models offer flexibility through text instructions. However, direct coordinate prediction does not explicitly model spatial likelihood distributions, limiting the representation of localization ambiguity.
  **Methods:** We propose Kev-Bio, a vision-language model that uses clinical measurement questions to guide ultrasound landmark detection. Inspired by System One decision models, Kev-Bio uses decision representations of the language model to generate queries for each caliper endpoint. These queries are matched against shared dense ultrasound features to produce spatial probability maps, from which landmark coordinates and clinical measurements are derived. The model is trained end-to-end using both landmark localization and clinical measurement losses.
  **Results:** On the nine-view FU/GU Biometry 2026 dataset, Kev-Bio achieves a mean radial error (MRE) of 22.50 pixels and a clinical measurement mean absolute error (MAE) of 15.38, outperforming the compared baselines in overall performance.
  **Conclusion:** These results demonstrate the effectiveness of Kev-Bio for ultrasound landmark detection and clinical measurement across different anatomical views. Our code and models are available at https://github.com/moeinheidari7829/Kev-Bio.
