# X-WAM: Unified 4D World Action Modeling with Asynchronous Denoising

**Date:** 2026-04-30
**Source:** [HuggingFace](https://huggingface.co/papers/2604.26694) | [Paper](https://arxiv.org/abs/2604.26694)
**Raw:** [raw/huggingface/2026-04-30-unified-4d-world-action-modeling-video-priors-asynchronous-denoising.md](../../raw/huggingface/2026-04-30-unified-4d-world-action-modeling-video-priors-asynchronous-denoising.md)

## TL;DR

X-WAM unifies real-time robot action execution with high-fidelity 4D world synthesis (multi-view RGB-D video + 3D reconstruction) in a single framework. Uses pretrained video diffusion priors plus a lightweight depth-prediction branch (replicates final blocks of the diffusion transformer for depth). The key trick is **Asynchronous Noise Sampling (ANS)** — fewer denoising steps for actions (real-time decoding), full steps for video (high fidelity), with joint timestep distribution training to prevent inference-time distribution shift. 5,800+ hours of robotic pretraining data; 79.2% RoboCasa, 90.7% RoboTwin 2.0.

## Why Tier 4 for Amit

Robotics-heavy and 3D-spatial — outside the routing/efficiency/GPU core. Recorded for the asynchronous-denoising mechanism, which is *transferable*: any diffusion model that produces multiple outputs at different latency targets could use the same pattern. ANS is a sibling of speculative decoding's "different speeds for different parts of the same generation" — the difference is that ANS trains for the schedule rather than computing speedups at inference.

## One Sentence for the Digest

Yet another diffusion-policy world model — interesting only for the asynchronous denoising trick, which generalizes beyond robotics.
