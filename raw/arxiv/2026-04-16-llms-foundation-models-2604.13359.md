---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13359
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13359
published: 2026-04-16
authors: Run Wang, Victor J. B. Jung, Philip Wiese
---

# BioTrain: Sub-MB, Sub-50mW On-Device Fine-Tuning for Edge-AI on Biosignals

**arXiv:** https://arxiv.org/abs/2604.13359
**Authors:** Run Wang, Victor J. B. Jung, Philip Wiese

## Abstract

arXiv:2604.13359v1 Announce Type: new  Abstract: Biosignals exhibit substantial cross-subject and cross-session variability, inducing severe domain shifts that degrade post-deployment performance for small, edge-oriented AI models. On-device adaptation is therefore essential to both preserve user privacy and ensure system reliability. However, existing sub-100 mW MCU-based wearable platforms can only support shallow or sparse adaptation schemes due to the prohibitive memory footprint and computational cost of full backpropagation (BP). In this paper, we propose BioTrain, a framework enabling full-network fine-tuning of state-of-the-art biosignal models under milliwatt-scale power and sub-megabyte memory constraints. We validate BioTrain using both offline and on-device benchmarks on EEG and EOG datasets, covering Day-1 new-subject calibration and longitudinal adaptation to signal drift. Experimental results show that full-network fine-tuning achieves accuracy improvements of up to 35% over non-adapted baselines and outperforms last-layer updates by approximately 7% during new-subject calibration. On the GAP9 MCU platform, BioTrain enables efficient on-device training throughput of 17 samples/s for EEG and 85 samples/s for EOG models within a power envelope below 50 mW. In addition, BioTrain's efficient memory allocator and network topology optimization enable the use of a large batch size, reducing peak memory usage. For fully on-chip BP on GAP9, BioTrain reduces the memory footprint by 8.1x, from 5.4 MB to 0.67 MB, compared to conventional full-network fine-tuning using batch normalization with batch size 8.
