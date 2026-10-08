---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.00864
url: https://huggingface.co/papers/2610.00864
arxiv_url: https://arxiv.org/abs/2610.00864
date: 2026-10-07
---

# Kinematic MeanFlow: One-Step Action Generation Policy for Robotic Foundation Models

In this paper, we study how to achieve one-step action generation in Robotic Foundation Models (RFMs), aiming to overcome the high inference latency of multi-step flow matching. MeanFlow provides a promising framework for this goal, yet its direct application leads to performance collapse. We discover that this stems from two distinctive dynamics exhibited in the RFM velocity field: (1) the ``local acceleration" exhibits stability early on, but surges sharply towards the end of the denoising process, and (2) the spread of its magnitudes across samples widens as denoising progresses. To address these issues, we introduce Kinematic MeanFlow (K-MF), a novel one-step action policy tailored for RFMs. Specifically, grounded in a kinematic identity, K-MF decouples the time derivative term in the MeanFlow formulation into two sub-interval terms separated by an intermediate point. This decoupled formulation enables the two terms to capture early-stage and late-stage denoising dynamics, respectively, while mitigating the error amplification across the process. As a result, our K-MF empowers RFMs to achieve one-step action generation in both training from scratch and fine-tuning paradigms across diverse tasks, while outperforming multi-step flow matching in most settings. In terms of inference efficiency, K-MF reduces action-head latency of GR00T-N1.6 by 67.5%~74.4% across L40 and Jetson Orin in eager and compiled modes, yielding end-to-end latency reductions of 30.3%~54.9%. Code will be available at https://github.com/IntelChina-AI/K-MF.
