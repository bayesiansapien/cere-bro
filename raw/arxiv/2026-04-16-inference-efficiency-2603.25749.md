---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2603.25749
category: cs.AI
concept: inference-efficiency
url: https://arxiv.org/abs/2603.25749
published: 2026-04-16
authors: Xiaoke Yang, Long Gao, Haoyu He
---

# A Lightweight, Transferable, and Self-Adaptive Framework for Intelligent DC Arc-Fault Detection in Photovoltaic Systems

**arXiv:** https://arxiv.org/abs/2603.25749
**Authors:** Xiaoke Yang, Long Gao, Haoyu He

## Abstract

arXiv:2603.25749v2 Announce Type: replace-cross  Abstract: Arc-fault circuit interrupters (AFCIs) are essential for mitigating fire hazards in residential photovoltaic (PV) systems, yet achieving reliable DC arc-fault detection under real-world conditions remains challenging. Spectral interference from inverter switching, hardware heterogeneity, operating-condition drift, and environmental noise collectively compromise conventional AFCI solutions. This paper proposes a lightweight, transferable, and self-adaptive learning-driven framework (LD-framework) for intelligent DC arc-fault detection. At the device level, LD-Spec learns compact spectral representations enabling efficient on-device inference and near-perfect arc discrimination. Across heterogeneous inverter platforms, LD-Align performs cross-hardware representation alignment to ensure robust detection despite hardware-induced distribution shifts. To address long-term evolution, LD-Adapt introduces a cloud-edge collaborative self-adaptive updating mechanism that detects unseen operating regimes and performs controlled model evolution. Extensive experiments involving over 53,000 labeled samples demonstrate near-perfect detection, achieving 0.9999 accuracy and 0.9996 F1-score. Across diverse nuisance-trip-prone conditions, including inverter start-up, grid transitions, load switching, and harmonic disturbances, the method achieves a 0% false-trip rate. Cross-hardware transfer shows reliable adaptation using only 0.5%-1% labeled target data while preserving source performance. Field adaptation experiments demonstrate recovery of detection precision from 21% to 95% under previously unseen conditions. These results indicate that the LD-framework enables a scalable, deployment-oriented AFCI solution maintaining highly reliable detection across heterogeneous devices and long-term operation.
