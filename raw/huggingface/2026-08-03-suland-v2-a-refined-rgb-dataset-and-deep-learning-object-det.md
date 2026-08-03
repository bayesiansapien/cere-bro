---
source: farmer/huggingface
farmed: 2026-08-03T12:36:11.005337+05:30
arxiv_id: 2607.28996
url: https://huggingface.co/papers/2607.28996
arxiv_url: https://arxiv.org/abs/2607.28996
date: 2026-08-03
---

# SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark for UAV/UGV-Based SUrface LANDmine Detection Under Domain Shift

RGB imagery offers a practical, low-cost option for Unmanned Aerial/Ground Vehicle (UAV/UGV) survey support in surface-landmine detection, but object detectors remain underexplored in this safety-critical domain. Limited cross-architecture benchmarking and insufficient out-of-distribution (OOD) analysis obscure whether detectors generalize across deployment conditions. This challenge is amplified by the scarcity of public RGB landmine datasets, making SULAND a key benchmark for PFM-1 and PMA-2 detection. However, inspection reveals missing/false annotations, localization errors, inconsistent visibility criteria, visual artifacts, temporal labeling inconsistencies, and an inverted OOD class-ID convention in SULAND. We present SULAND_v2, a refined RGB surface-landmine dataset and benchmark. Preserving original images and splits, we manually revise annotations to ensure completeness, precise localization, label validity, and class consistency. SULAND_v2 contains 33,771 images and 12,433 bounding boxes. We benchmark 35 detector configurations across nine families. Annotation refinement improves YOLOv8 in-distribution (IID) test mAP@50 by 14.6-19.6 percentage points, while fixing the OOD class-ID convention increases mean YOLOv8 OOD mAP@50 by ~25 percentage points. On SULAND_v2, YOLOv12-Small achieves the highest IID mAP@50 (0.908), while RF-DETR-Large yields the strongest OOD performance (0.799 mAP@50, 0.675 recall). Our results demonstrate that high IID accuracy does not guarantee operational readiness. SULAND_v2 provides a reliable benchmark for evaluating domain-shift robustness in RGB-based mine-action survey support.
