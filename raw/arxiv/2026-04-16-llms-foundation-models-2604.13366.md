---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13366
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13366
published: 2026-04-16
authors: Angelo Moroncelli, Matteo Rufolo, Gunes Cagin Aydin
---

# Diffusion Sequence Models for Generative In-Context Meta-Learning of Robot Dynamics

**arXiv:** https://arxiv.org/abs/2604.13366
**Authors:** Angelo Moroncelli, Matteo Rufolo, Gunes Cagin Aydin

## Abstract

arXiv:2604.13366v1 Announce Type: new  Abstract: Accurate modeling of robot dynamics is essential for model-based control, yet remains challenging under distributional shifts and real-time constraints. In this work, we formulate system identification as an in-context meta-learning problem and compare deterministic and generative sequence models for forward dynamics prediction. We take a Transformer-based meta-model, as a strong deterministic baseline, and introduce to this setting two complementary diffusion-based approaches: (i) inpainting diffusion (Diffuser), which learns the joint input-observation distribution, and (ii) conditioned diffusion models (CNN and Transformer), which generate future observations conditioned on control inputs. Through large-scale randomized simulations, we analyze performance across in-distribution and out-of-distribution regimes, as well as computational trade-offs relevant for control. We show that diffusion models significantly improve robustness under distribution shift, with inpainting diffusion achieving the best performance in our experiments. Finally, we demonstrate that warm-started sampling enables diffusion models to operate within real-time constraints, making them viable for control applications. These results highlight generative meta-models as a promising direction for robust system identification in robotics.
