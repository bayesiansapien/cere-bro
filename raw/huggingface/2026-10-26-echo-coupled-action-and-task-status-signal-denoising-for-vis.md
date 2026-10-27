---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.801180+00:00
arxiv_id: 2610.31569
url: https://huggingface.co/papers/2610.31569
arxiv_url: https://arxiv.org/abs/2610.31569
date: 2026-10-26
---

# Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models

Recognizing task completion and failure enables robots to stop upon success and initiate recovery or replanning after failure. Existing methods augment Vision Language Action (VLA) policies with task status signal prediction to support these execution decisions. However, learning and integrating these signals can require fine-grained supervision, external monitoring models, or complex architectural designs. Moreover, the potential of task status signals to directly guide action generation remains underexplored. We present Echo, a framework that combines task status signal learning without frame-level progress annotations with a compact design for status prediction and action generation within a single VLA. Specifically, Echo represents task status with stop and failure signals, added as two dimensions of each action chunk and denoised together with robot actions. Their combination distinguishes ongoing execution, successful completion, and failure. To learn these signals without fine-grained progress annotations, Echo constructs successful, failed, and recovery trajectories with complementary supervision properties. To enable status signal-guided action generation, Echo controls interactions between the signals and actions and denoises the signals faster than the actions. These allow later action denoising steps to condition on cleaner status estimates while preserving accurate signal prediction. Extensive real-world manipulation experiments show that Echo accurately predicts task status and consistently improves policy performance.
