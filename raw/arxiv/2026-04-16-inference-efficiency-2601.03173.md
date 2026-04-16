---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2601.03173
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2601.03173
published: 2026-04-16
authors: Sumit S. Shevtekar, Chandresh K. Maurya, Gourab Sil
---

# Predicting Time Pressure of Powered Two-Wheeler Riders for Proactive Safety Interventions

**arXiv:** https://arxiv.org/abs/2601.03173
**Authors:** Sumit S. Shevtekar, Chandresh K. Maurya, Gourab Sil

## Abstract

arXiv:2601.03173v2 Announce Type: replace  Abstract: Time pressure critically influences risky maneuvers and crash proneness among powered two-wheeler riders, yet its prediction remains underexplored in intelligent transportation systems. We present a large-scale dataset of 129,000+ labeled multivariate time-series sequences from 153 rides by 51 participants under No, Low, and High Time Pressure conditions. Each sequence captures 63 features spanning vehicle kinematics, control inputs, behavioral violations, and environmental context. Our empirical analysis shows High Time Pressure induces 48% higher speeds, 36.4% greater speed variability, 58% more risky turns at intersections, 36% more sudden braking, and 50% higher rear brake forces versus No Time Pressure. To benchmark this dataset, we propose MotoTimePressure, a deep learning model combining convolutional preprocessing, dual-stage temporal attention, and Squeeze-and-Excitation feature recalibration, achieving 91.53% accuracy and 98.93% ROC AUC, outperforming eight baselines, with only 172K parameters, 2.16 MB model size, and 0.04 ms inference on CPU. Since time pressure cannot be directly measured in real time, we demonstrate its utility in collision prediction and threshold determination. Using MTPS-predicted time pressure as a feature improves collision risk accuracy for both Informer (91.25% to 93.51%) and TimesNet (92.10% to 93.90%), approaching oracle performance (93.72% and 94.06%, respectively). Thresholded time pressure states capture rider cognitive stress and enable proactive ITS interventions, including adaptive alerts, haptic feedback, V2I signaling, and speed guidance, supporting safer two-wheeler mobility under the Safe System Approach.
