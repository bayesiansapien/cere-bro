---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2609.39822
url: https://huggingface.co/papers/2609.39822
arxiv_url: https://arxiv.org/abs/2609.39822
date: 2026-10-07
---

# Toward Real-Time VLAs: Stage-Aware Two-Step Flow Denoising and System-Level Evaluation

Vision-language-action (VLA) models face a timing gap between low-rate inference and high-rate robot execution. We characterize this gap through end-to-end latency measurements of model inference and the robot execution chain. Repeated Flow Matching denoising contributes substantially to inference cost, while robot-side delays mainly arise from perception acquisition, communication scheduling, and physical response. Analysis of the velocity field shows relatively stable magnitude and direction in early integration, followed by stronger directional correction near the terminal steps. Based on this stage heterogeneity, we propose two-stage non-uniform denoising, reducing the number of steps from 10 to 2 and model-inference time from 61.557 ms to 21.956 ms. We also develop a distributed real-time VLA framework with independent inference, action-publication, and robot-control rates, modular observation acquisition, and action-provenance logging. Using π0.5 as the baseline, we evaluate six real-time execution methods on a long-horizon physical garment-folding task. Legato performs best overall among training-based methods, while Temporal Smoothing leads among training-free methods; both perform strongly in task success, completion time, action continuity, and acceleration smoothness. Combining two-step denoising with representative execution methods substantially reduces inference cost with a small reduction in task performance. These results motivate joint optimization of model-inference efficiency and robot-system timing.
