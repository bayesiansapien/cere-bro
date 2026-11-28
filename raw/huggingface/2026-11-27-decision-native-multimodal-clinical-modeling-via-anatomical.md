---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.32993
url: https://huggingface.co/papers/2611.32993
arxiv_url: https://arxiv.org/abs/2611.32993
date: 2026-11-27
---

# Decision-Native Multimodal Clinical Modeling via Anatomical Grounding and Confidence Calibration

Structured clinical decisions from volumetric computed tomography (CT) require anatomically grounded predictions and calibrated confidence estimates. However, existing 3D medical multimodal models often suffer from uncalibrated autoregressive decoding and shortcut reliance on irrelevant anatomical regions. We introduce Radev, a decision-native multimodal model that integrates anatomy-guided visual compression, direct candidate prediction, and counterfactual confidence supervision. To bridge global context with fine-grained slice details, a frozen 3D encoder extracts reusable organ-level features, which are dynamically selected by the query to attend to 2D slice features within predicted anatomical bounds. The resulting compact visual tokens enable the language backbone to estimate candidate probabilities in a single forward pass without autoregressive decoding. We further propose Counterfactual-Calibrated Training (CCT) to compare predictions under intact and intervened organ representations. CCT encourages confidence to decrease when removing target-organ evidence degrades decision quality, while penalizing excessive confidence drops under unrelated-organ removal. To facilitate rigorous evaluation, we construct CT-Verdict, a comprehensive benchmark spanning binary finding presence, multiple-choice questions, and ordinal severity assessment across both in-distribution and external cohorts. Extensive experiments demonstrate that Radev significantly outperforms state-of-the-art methods in both decision accuracy and confidence calibration, while generalizing robustly under distribution shifts. Project page at https://juntaojianggavin.github.io/projects/Radev/
