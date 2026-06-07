---
source: farmer/huggingface
farmed: 2026-06-07T04:51:04Z
arxiv_id: 2606.05254
url: https://huggingface.co/papers/2606.05254
arxiv_url: https://arxiv.org/abs/2606.05254
date: 2026-06-07
---

# Flash-WAM: Modality-Aware Distillation for World Action Models

World-action models (WAMs) jointly generate future video and robot actions through iterative diffusion, achieving strong performance on manipulation benchmarks but requiring tens of denoising steps, a cost that precludes real-time control. Step distillation has emerged as the natural remedy, but off-the-shelf methods break down in the joint video-action setting because video and action streams use different SNR-shifted noise schedules and reach training with substantially different marginal noise distributions, an asymmetry that single-modality distillation methods cannot accommodate. We introduce Flash-WAM, a modality-aware step-distillation framework inspired by consistency distillation that selects the consistency function for each modality to match its noise regime: a linear-gradient-scaling parametrization for the action stream's low-noise regime, paired with a variance-preserving parametrization for the video stream's high-noise regime, grounded in a structural analysis of the consistency-function family that characterizes the achievable gradient scaling under the consistency boundary condition. Instantiated on LingBot-VA, Flash-WAM compresses inference to a single step in each modality. On RoboTwin 2.0, this reduces per-chunk latency from 8.1 seconds to 348 ms on NVIDIA L40S, a 23{times} speedup that enables real-time inference. Flash-WAM preserves task success on simulation benchmarks (85.5% RoboTwin 2.0, 95.7% LIBERO) and substantially recovers real-world performance (60% average on a Unitree G1 humanoid robot), while naive consistency distillation drops to 24% at the same step budget.
