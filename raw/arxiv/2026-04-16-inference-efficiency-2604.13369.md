---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13369
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13369
published: 2026-04-16
authors: Sushrut Kumar
---

# AeTHERON: Autoregressive Topology-aware Heterogeneous Graph Operator Network for Fluid-Structure Interaction

**arXiv:** https://arxiv.org/abs/2604.13369
**Authors:** Sushrut Kumar

## Abstract

arXiv:2604.13369v1 Announce Type: cross  Abstract: Surrogate modeling of body-driven fluid flows where immersed moving boundaries couple structural dynamics to chaotic, unsteady fluid phenomena remains a fundamental challenge for both computational physics and machine learning. We present AeTHERON, a heterogeneous graph neural operator whose architecture directly mirrors the structure of the sharp-interface immersed boundary method (IBM): a dual-graph representation separating fluid and structural domains, coupled through sparse cross-attention that reflects the compact support of IBM interpolation stencils. This physics-informed inductive bias enables AeTHERON to learn nonlinear fluid-structure coupling in a shared high-dimensional latent space, with continuous sinusoidal time embeddings providing temporal generalization across lead times. We evaluate AeTHERON on direct numerical simulations of a flapping flexible caudal fin, a canonical FSI benchmark featuring leading-edge vortex formation, large membrane deformation, and chaotic wake shedding across a 4x5 parameter grid of membrane thickness (h* = 0.01-0.04) and Strouhal number (St = 0.30-0.50). As a proof-of-concept, we train on the first 150 timesteps of a representative case using a 70/30 train/validation split and evaluate on the fully unseen extrapolation window t=150-200. AeTHERON captures large-scale vortex topology and wake structure with qualitative fidelity, achieving a mean extrapolation MAE of 0.168 without retraining, with error peaking near flapping half-cycle transitions where flow reorganization is most rapid -- a physically interpretable pattern consistent with the nonlinear fluid-membrane coupling. Inference requires milliseconds per timestep on a single GPU versus hours for equivalent DNS computation. This is a continuously developing preprint; results and figures will be updated in subsequent versions.
