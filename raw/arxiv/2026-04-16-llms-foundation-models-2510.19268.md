---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.19268
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.19268
published: 2026-04-16
authors: Mingen Li, Houjian Yu, Yixuan Huang
---

# Hierarchical DLO Routing with Reinforcement Learning and In-Context Vision-language Models

**arXiv:** https://arxiv.org/abs/2510.19268
**Authors:** Mingen Li, Houjian Yu, Yixuan Huang

## Abstract

arXiv:2510.19268v2 Announce Type: replace-cross  Abstract: Long-horizon routing tasks of deformable linear objects (DLOs), such as cables and ropes, are common in industrial assembly lines and everyday life. These tasks are particularly challenging because they require robots to manipulate DLO with long-horizon planning and reliable skill execution. Successfully completing such tasks demands adapting to their nonlinear dynamics, decomposing abstract routing goals, and generating multi-step plans composed of multiple skills, all of which require accurate high-level reasoning during execution. In this paper, we propose a fully autonomous hierarchical framework for solving challenging DLO routing tasks. Given an implicit or explicit routing goal expressed in language, our framework leverages vision-language models~(VLMs) for in-context high-level reasoning to synthesize feasible plans, which are then executed by low-level skills trained via reinforcement learning. To improve robustness over long horizons, we further introduce a failure recovery mechanism that reorients the DLO into insertion-feasible states. Our approach generalizes to diverse scenes involving object attributes, spatial descriptions, implicit language commands, and \myred{extended 5-clip settings}. It achieves an overall success rate of 92\% across long-horizon routing scenarios. Please refer to our project page: https://icra2026-dloroute.github.io/DLORoute/
