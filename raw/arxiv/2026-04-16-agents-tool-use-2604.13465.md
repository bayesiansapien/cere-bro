---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13465
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13465
published: 2026-04-16
authors: Ahmadreza Eslaminia, Kuan-Chieh Lu, Klara Nahrstedt
---

# Adaptive Unknown Fault Detection and Few-Shot Continual Learning for Condition Monitoring in Ultrasonic Metal Welding

**arXiv:** https://arxiv.org/abs/2604.13465
**Authors:** Ahmadreza Eslaminia, Kuan-Chieh Lu, Klara Nahrstedt

## Abstract

arXiv:2604.13465v1 Announce Type: new  Abstract: Ultrasonic metal welding (UMW) is widely used in industrial applications but is sensitive to tool wear, surface contamination, and material variability, which can lead to unexpected process faults and unsatisfactory weld quality. Conventional monitoring systems typically rely on supervised learning models that assume all fault types are known in advance, limiting their ability to handle previously unseen process faults. To address this challenge, this paper proposes an adaptive condition monitoring approach that enables unknown fault detection and few-shot continual learning for UMW. Unknown faults are detected by analyzing hidden-layer representations of a multilayer perceptron and leveraging a statistical thresholding strategy. Once detected, the samples from unknown fault types are incorporated into the existing model through a continual learning procedure that selectively updates only the final layers of the network, which enables the model to recognize new fault types while preserving knowledge of existing classes. To accelerate the labeling process, cosine similarity transformation combined with a clustering algorithm groups similar unknown samples, thereby reducing manual labeling effort. Experimental results using a multi-sensor UMW dataset demonstrate that the proposed method achieves 96% accuracy in detecting unseen fault conditions while maintaining reliable classification of known classes. After incorporating a new fault type using only five labeled samples, the updated model achieves 98% testing classification accuracy. These results demonstrate that the proposed approach enables adaptive monitoring with minimal retraining cost and time. The proposed approach provides a scalable solution for continual learning in condition monitoring where new process conditions may constantly emerge over time and is extensible to other manufacturing processes.
