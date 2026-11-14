---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.530659+00:00
arxiv_id: 2611.17190
url: https://huggingface.co/papers/2611.17190
arxiv_url: https://arxiv.org/abs/2611.17190
date: 2026-11-13
---

# Consensus Capture in Reference-Based UAV Video Stabilization: A Benchmark on Dynamic Urban Scenes

Reference-frame stabilization registers every frame of a hovering-drone video onto one reference frame, keeping object positions comparable. The registration pipelines it relies on are selected on feature-matching benchmarks in which only the camera moves. Over a busy intersection, vehicles moving together supply mutually consistent correspondences that can draw the robust homography estimate toward their motion: consensus capture, which inlier statistics cannot flag. A two-part benchmark measures it and the object masking meant to prevent it. A static protocol scores ten pipelines under exactly known homographies on 4K aerial frames, tuned on a site-disjoint split at a matched resolution and feature budget. A dynamic protocol scores them at an offline and a real-time budget on hovers selected from the video alone to span the amount and coherence of moving foreground, plus a stationary control. It measures background alignment, object position error and the share of a moving group's displacement an estimate follows, against a pseudo-ground-truth reference audited with manually annotated ground control points, which also score every candidate. On static scenes, tuned AKAZE, RootSIFT, SIFT and BRISK lead, retuning the matcher thresholds raises the mean average accuracy (mAA) by at most 0.0062, and masking costs less than 0.005. Unmasked ORB is captured on 28 of 304 real-time dynamic pairs and on 6 offline; its real-time captured estimates have a median corner error of 18.8 px yet typical inlier counts and ratios. Masking removes capture for every pipeline and leaves the leading pipelines unchanged. Code, data and results are released.
