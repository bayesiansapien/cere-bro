---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13687
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13687
published: 2026-04-16
authors: Tiago Fernandes, Francesco Di Renzo, Antonio Onofre
---

# VIGILant: an automatic classification pipeline for glitches in the Virgo detector

**arXiv:** https://arxiv.org/abs/2604.13687
**Authors:** Tiago Fernandes, Francesco Di Renzo, Antonio Onofre

## Abstract

arXiv:2604.13687v1 Announce Type: cross  Abstract: Glitches frequently contaminate data in gravitational-wave detectors, complicating the observation and analysis of astrophysical signals. This work introduces VIGILant, an automatic pipeline for classification and visualization of glitches in the Virgo detector. Using a curated dataset of Virgo O3b glitches, two machine learning approaches are evaluated: tree-based models (Decision Tree, Random Forest and XGBoost) using structured Omicron parameters, and Convolutional Neural Networks (ResNet) trained on spectrogram images. While tree-based models offer higher interpretability and fast training, the ResNet34 model achieved superior performance, reaching a F1 score of 0.9772 and accuracy of 0.9833 in the testing set, with inference times of tens of milliseconds per glitch. The pipeline has been deployed for daily operation at the Virgo site since observing run O4c, providing the Virgo collaboration with an interactive dashboard to monitor glitch populations and detector behavior. This allows to identify low-confidence predictions, highlighting glitches requiring further attention.
