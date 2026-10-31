---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.161737+00:00
arxiv_id: 2610.40362
url: https://huggingface.co/papers/2610.40362
arxiv_url: https://arxiv.org/abs/2610.40362
date: 2026-10-30
---

# Your LR Schedule May Not Be Principled: Effective Learning Rate Scheduling in Weight-Normalized Training

Weight-normalized (WN) training is emerging as a compelling alternative to conventional weight decay (WD), with recent studies reporting substantial pretraining loss gains. We show that these gains are driven primarily by the induced effective learning rate (ELR) trajectory rather than by normalization alone. Matching ELR trajectories largely collapses the training loss dynamics of WN and WD. Schedule design should therefore target ELR rather than the nominal learning rate (LR) alone. Building on this principle, we propose AIR (Affine Inverse-square-Root decay), which combines a theoretically derived 1/t decay with an affine adjustment to satisfy prescribed peak and terminal LRs over a finite training horizon. We further identify late-stage ELR scheduling as a key source of its gains, because a shared late schedule attenuates the effect of earlier LR choices. Experiments on 128 B-token Mixture-of-Experts pretraining demonstrate that AIR outperforms cosine and other candidate schedules in training loss, downstream performance, and hyperparameter robustness, reducing terminal training loss by approximately 0.01 relative to cosine at matched cumulative LR. Applying the same ELR trajectory to WD reproduces the corresponding training dynamics, showing that the benefits extend beyond fixed-norm training and establishing ELR as the principled scheduling object.
