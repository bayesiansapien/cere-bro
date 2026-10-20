---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.22306
url: https://huggingface.co/papers/2610.22306
arxiv_url: https://arxiv.org/abs/2610.22306
date: 2026-10-19
---

# ARC-SORT: Adaptive, Robust, Compensated Multi-Object Tracking with Interacting Multiple Models

Multi-object tracking in sports broadcasts is hard for two reasons: athletes move fast and change direction abruptly, and the camera pans and zooms at the same time. We present ARC-SORT (Adaptive, Robust, Compensated SORT), a tracking-by-detection tracker that trains nothing and runs in real time. Its design rule: the tracker measures its own uncertainty, and that measurement decides how it acts. An Interacting Multiple Model (IMM) Kalman filter gives every track a predictive covariance, and we turn it into a per-track search region: the less reliable the motion prediction, the larger the region in which a detection may match (uncertainty-adaptive Expansion IoU, EIoU). On identical inputs, this continuous coupling is what matters: the same covariance used as a hard Mahalanobis gate hurts at every threshold we swept, and richer covariance summaries add nothing measurable. When two tracks cross, the assignment cost itself reports whether the decision was close. ARC-SORT keeps such pairs under review and applies at most one corrective identity swap once post-crossing appearance evidence shows the first decision was wrong; this adds +1.0 HOTA (higher order tracking accuracy) on both the SportsMOT and DanceTrack test sets at under a millisecond per frame. For players who leave the frame for seconds, motion extrapolation carries no information, so our offline re-identification drops the usual motion gate and links tracklets by appearance alone. ARC-SORT reaches 81.82 HOTA on the SportsMOT test set with the fewest identity switches of the 69 leaderboard entries as of August 2026 and tied-third multi-object tracking accuracy (MOTA, 97.09), and 62.1 HOTA on DanceTrack test with the same association settings. On Deep-EIoU's public detections and embeddings it reaches 80.31 HOTA, +3.1 over Deep-EIoU. It runs at about 50 frames per second on a laptop RTX 3060 GPU. Code will be released.
