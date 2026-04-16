---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2506.23640
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2506.23640
published: 2026-04-16
authors: Ximeng Liu, Zhuoran Liu, Yingming Mao
---

# Geminet: Learning the Duality-based Iterative Process for Lightweight Traffic Engineering in Changing Topologies

**arXiv:** https://arxiv.org/abs/2506.23640
**Authors:** Ximeng Liu, Zhuoran Liu, Yingming Mao

## Abstract

arXiv:2506.23640v2 Announce Type: replace-cross  Abstract: Recently, researchers have explored ML-based Traffic Engineering (TE), leveraging neural networks to solve TE problems traditionally addressed by optimization. However, existing ML-based TE schemes remain impractical: they either fail to handle topology changes or suffer from poor scalability due to excessive computational and memory overhead. To overcome these limitations, we propose Geminet, a lightweight and scalable ML-based TE framework that can handle changing topologies. Geminet is built upon two key insights: (i) a methodology that decouples neural networks from topology by learning an iterative gradient-descent-based adjustment process, as the update rule of gradient descent is topology-agnostic, relying only on a few gradient-related quantities; (ii) shifting optimization from path-level routing weights to edge-level dual variables, reducing memory consumption by leveraging the fact that edges are far fewer than paths. Evaluations on WAN and data center datasets show that Geminet significantly improves scalability. Its neural network size is only 0.04% to 7% of existing schemes, while handling topology variations as effectively as HARP, a state-of-the-art ML-based TE approach, without performance degradation. When trained on large-scale topologies, Geminet consumes under 10 GiB of memory, more than eight times less than the 80-plus GiB required by HARP, while achieving 5.45 times faster convergence speed, demonstrating its potential for large-scale deployment.
