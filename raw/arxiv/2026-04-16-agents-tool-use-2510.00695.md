---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.00695
category: cs.CV
concept: agents-tool-use
url: https://arxiv.org/abs/2510.00695
published: 2026-04-16
authors: Myungkyu Koo, Daewon Choi, Taeyoung Kim
---

# HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy

**arXiv:** https://arxiv.org/abs/2510.00695
**Authors:** Myungkyu Koo, Daewon Choi, Taeyoung Kim

## Abstract

arXiv:2510.00695v3 Announce Type: replace-cross  Abstract: Inherently, robotic manipulation tasks are history-dependent: leveraging past context could be beneficial. However, most existing Vision-Language-Action models (VLAs) have been designed without considering this aspect, i.e., they rely solely on the current observation, ignoring preceding context. In this paper, we propose HAMLET, a scalable framework to adapt VLAs to attend to the historical context during action prediction. Specifically, we introduce moment tokens that compactly encode perceptual information at each timestep. Their representations are initialized with time-contrastive learning, allowing them to better capture temporally distinctive aspects. Next, we employ a lightweight memory module that integrates the moment tokens across past timesteps into memory features, which are then leveraged for action prediction. Through empirical evaluation, we show that HAMLET successfully transforms a state-of-the-art VLA into a history-aware policy, especially demonstrating significant improvements on long-horizon tasks that require historical context. In particular, on top of GR00T N1.5, HAMLET achieves an average success rate of 76.4% on history-dependent real-world tasks, surpassing the baseline performance by 47.2%. Furthermore, HAMLET pushes prior art performance from 64.1% to 66.4% on RoboCasa Kitchen (100-demo setup) and from 95.6% to 97.7% on LIBERO, highlighting its effectiveness even under generic robot-manipulation benchmarks.
