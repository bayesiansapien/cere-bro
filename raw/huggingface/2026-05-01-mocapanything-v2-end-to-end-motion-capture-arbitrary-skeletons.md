---
source: farmer/huggingface
farmed: 2026-05-01T00:00:00Z
arxiv_id: "2604.28130"
url: https://huggingface.co/papers/2604.28130
arxiv_url: https://arxiv.org/abs/2604.28130
date: 2026-05-01
---

# MoCapAnything V2: End-to-End Motion Capture for Arbitrary Skeletons

A fully end-to-end framework for arbitrary-skeleton motion capture from monocular video that jointly optimizes video-to-pose and pose-to-rotation prediction while addressing rotation ambiguity through reference pose-rotation pairs and skeleton-aware attention mechanisms. Recent methods follow a factorized pipeline where a Video-to-Pose network predicts joint positions and an analytical inverse-kinematics (IK) stage recovers joint rotations. While effective, this design is inherently limited, since joint positions do not fully determine rotations and leave degrees of freedom such as bone-axis twist ambiguous, and the non-differentiable IK stage prevents the system from adapting to noisy predictions or optimizing for the final animation objective. In this work, we present the first fully end-to-end framework in which both Video-to-Pose and Pose-to-Rotation are learnable and jointly optimized. We observe that the ambiguity in pose-to-rotation mapping arises from missing coordinate system information: the same joint positions can correspond to different rotations under different rest poses and local axis conventions. To resolve this, we introduce a reference pose-rotation pair from the target asset, which, together with the rest pose, not only anchors the mapping but also defines the underlying rotation coordinate system. This formulation turns rotation prediction into a well-constrained conditional problem and enables effective learning. In addition, our model predicts joint positions directly from video without relying on mesh intermediates, improving both robustness and efficiency. Both stages share a skeleton-aware Global-Local Graph-guided Multi-Head Attention (GL-GMHA) module for joint-level local reasoning and global coordination. Experiments on Truebones Zoo and Objaverse show that our method reduces rotation error from ~17 degrees to ~10 degrees, and to 6.54 degrees on unseen skeletons, while achieving ~20x faster inference than mesh-based pipelines.
