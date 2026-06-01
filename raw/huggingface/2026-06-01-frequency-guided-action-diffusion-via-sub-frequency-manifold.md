---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.27919
url: https://huggingface.co/papers/2605.27919
arxiv_url: https://arxiv.org/abs/2605.27919
date: 2026-06-01
---

# Frequency-Guided Action Diffusion via Sub-Frequency Manifold Traversal

Learning visuomotor policies via behavior cloning typically involves mimicking expert demonstrations collected by human operators. However, natural human demonstrations inherently contain high-frequency noise, such as intermittent jerks, pauses, and action jitter. Training policies to directly imitate these raw trajectories inevitably causes the model to inherit these suboptimal behaviors. This pathology is particularly pronounced in diffusion-based policies, where iterative denoising steps can inadvertently amplify high-frequency artifacts at the expense of meaningful fine-grained details. To address these limitations, we present a novel frequency-based algorithm that enables implicit spectral maneuvering and smooth action generation. Our method, Frequency Guidance Operator (FGO), steers the generation process of diffusion polices by progressively driving the noisy samples through intermediate sub-frequency manifolds with expanding spectral bands. Validated on 15 robotic manipulation tasks from 5 benchmarks, FGO achieves superior performance in enhancing action smoothness and temporal consistency while preserving the details necessary for successful task execution.
