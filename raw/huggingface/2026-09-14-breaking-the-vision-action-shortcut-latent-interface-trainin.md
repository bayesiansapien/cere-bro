---
source: farmer/huggingface
farmed: 2026-09-14T06:17:21.172209+00:00
arxiv_id: 2609.12641
url: https://huggingface.co/papers/2609.12641
arxiv_url: https://arxiv.org/abs/2609.12641
date: 2026-09-14
---

# Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models

Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts. When learning to generate actions from pretrained visual representations, models may exploit task-irrelevant visual cues that correlate with demonstrated actions within the training distribution. Such vision-action shortcuts can undermine generalization when these correlations change under distribution shifts. Mitigating these shortcuts requires constraining how visual information is used for action generation while preserving task-relevant spatial information. We propose Latent Interface Training (LIT), a framework-agnostic two-stage strategy that first establishes a spatial-goal-conditioned action prior without images, then constrains visual conditioning through a pose-supervised latent interface. Stage 1 trains the action expert to generate action chunks conditioned on language, robot state, and each demonstrated chunk's terminal SE(3) end-effector pose, learning goal-directed action generation independently of visual cues. Stage 2 introduces a latent interface that aggregates visual and semantic representations and serves as the pretrained action expert's only visual conditioning pathway. The interface is supervised to reconstruct the terminal pose previously used to condition Stage 1, encouraging it to retain the goal-relevant spatial information needed for action generation. Across four vision-language-action and world-action architectures (Pi0.5, MolmoAct2, FAST-WAM, and ImageWAM), LIT improves overall LIBERO-Plus success by 3.87-10.70 percentage points while preserving or improving average LIBERO success. Real-world evaluations show 13.30-16.70 percentage-point gains in success aggregated across three tasks under unseen camera configurations, lighting variations, and distractors.
