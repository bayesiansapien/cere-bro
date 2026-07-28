---
source: farmer/huggingface
farmed: 2026-07-28T03:19:32Z
arxiv_id: 2607.23822
url: https://huggingface.co/papers/2607.23822
arxiv_url: https://arxiv.org/abs/2607.23822
date: 2026-07-28
---

# DriveDNA: A Large-Scale Multimodal Naturalistic Driving Dataset and Benchmark for Driving Style Identification

Driving style captures stable, driver-specific patterns in how a vehicle is driven. In naturalistic data, however, this signal is hard to isolate because drivers are observed in different vehicles, on different roads, and under different conditions, so models may mistake vehicle- or situation-specific regularities for driver-specific style. We introduce DriveDNA, a large-scale naturalistic dataset and benchmark for personalized driving-style modeling, comprising 4,121 drives from 465 drivers across 115 vehicle models and totaling 975 hours of human-controlled driving at 10 Hz with forward video, collected from community drivers in everyday use. DriveDNA defines driving style as a consistent, driver-specific behavioral pattern in how a vehicle moves under similar conditions. The benchmark evaluates this signal through three core tasks: few-shot driver re-identification, personalized behavior prediction, and condition-matched comparison, and provides behavioral annotations plus 276,248 rule-generated maneuver events across six classes with large-scale human auditing. We evaluate baselines spanning classical descriptors, supervised and self-supervised time-series encoders, multimodal fusion, probabilistic prediction, and zero-shot foundation models under a fixed multi-seed protocol. Learned representations substantially outperform classical descriptors on unseen drivers (AUROC .935 vs. .707) and retain driver-specific information under matched driving conditions, while descriptor performance approaches chance. Video-only models achieve comparable re-identification accuracy but exhibit severe route leakage, showing that strong recognition may arise from contextual shortcuts rather than driving behavior. These findings show that reliable driving-style evaluation must assess both the behavioral value of learned representations and their robustness to vehicle, drive, and condition confounds.
