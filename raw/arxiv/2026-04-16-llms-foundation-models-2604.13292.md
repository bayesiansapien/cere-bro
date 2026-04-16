---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13292
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13292
published: 2026-04-16
authors: Mahyar Ghazanfari, Peng Wei
---

# See&Say: Vision Language Guided Safe Zone Detection for Autonomous Package Delivery Drones

**arXiv:** https://arxiv.org/abs/2604.13292
**Authors:** Mahyar Ghazanfari, Peng Wei

## Abstract

arXiv:2604.13292v1 Announce Type: new  Abstract: Autonomous drone delivery systems are rapidly advancing, but ensuring safe and reliable package drop-offs remains highly challenging in cluttered urban and suburban environments where accurately identifying suitable package drop zones is critical. Existing approaches typically rely on either geometry-based analysis or semantic segmentation alone, but these methods lack the integrated semantic reasoning required for robust decision-making. To address this gap, we propose See&amp;Say, a novel framework that combines geometric safety cues with semantic perception, guided by a Vision-Language Model (VLM) for iterative refinement. The system fuses monocular depth gradients with open-vocabulary detection masks to produce safety maps, while the VLM dynamically adjusts object category prompts and refines hazard detection across time, enabling reliable reasoning under dynamic conditions during the final delivery phase. When the primary drop-pad is occupied or unsafe, the proposed See&amp;Say also identifies alternative candidate zones for package delivery. We curated a dataset of urban delivery scenarios with moving objects and human activities to evaluate the approach. Experimental results show that See&amp;Say outperforms all baselines, achieving the highest accuracy and IoU for safety map prediction as well as superior performance in alternative drop zone evaluation across multiple thresholds. These findings highlight the promise of VLM-guided segmentation-depth fusion for advancing safe and practical drone-based package delivery.
