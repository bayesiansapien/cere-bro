---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.12856
category: cs.CV
concept: agents-tool-use
url: https://arxiv.org/abs/2604.12856
published: 2026-04-16
authors: Xuan Wang, Kai Ruan, Jiayi Han
---

# PianoFlow: Music-Aware Streaming Piano Motion Generation with Bimanual Coordination

**arXiv:** https://arxiv.org/abs/2604.12856
**Authors:** Xuan Wang, Kai Ruan, Jiayi Han

## Abstract

arXiv:2604.12856v2 Announce Type: replace  Abstract: Audio-driven bimanual piano motion generation requires precise modeling of complex musical structures and dynamic cross-hand coordination. However, existing methods often rely on acoustic-only representations lacking symbolic priors, employ inflexible interaction mechanisms, and are limited to computationally expensive short-sequence generation. To address these limitations, we propose PianoFlow, a flow-matching framework for precise and coordinated bimanual piano motion synthesis. Our approach strategically leverages MIDI as a privileged modality during training, distilling these structured musical priors to achieve deep semantic understanding while maintaining audio-only inference. Furthermore, we introduce an asymmetric role-gated interaction module to explicitly capture dynamic cross-hand coordination through role-aware attention and temporal gating. To enable real-time streaming generation for arbitrarily long sequences, we design an autoregressive flow continuation scheme that ensures seamless cross-chunk temporal coherence. Extensive experiments on the PianoMotion10M dataset demonstrate that PianoFlow achieves superior quantitative and qualitative performance, while accelerating inference by over 9\times compared to previous methods.
