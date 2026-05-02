---
source: farmer/huggingface
farmed: 2026-05-02T00:00:00Z
arxiv_id: "2604.24952"
url: https://huggingface.co/papers/2604.24952
arxiv_url: https://arxiv.org/abs/2604.24952
date: 2026-05-02
---

# Learning from Noisy Preferences: A Semi-Supervised Learning Approach to Direct Preference Optimization

Human visual preferences involve multiple factors including aesthetics, detail fidelity, and semantic alignment. However, existing datasets typically provide only single holistic annotations, causing substantial label noise where images excelling in some dimensions but lacking in others are marked simply as winner or loser. The authors theoretically show that reducing multi-dimensional preferences to binary labels creates conflicting gradient signals that mislead Diffusion Direct Preference Optimization. They propose Semi-DPO, treating consistent pairs as clean data and conflicting pairs as noisy unlabeled data. The approach trains initially on a consensus-filtered clean subset, then uses the resulting model to generate pseudo-labels for iterative refinement. Results demonstrate significant improvements in aligning with complex human preferences without requiring additional annotation or explicit reward models during training, with code and models promised for release.
