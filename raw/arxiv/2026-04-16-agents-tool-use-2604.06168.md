---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.06168
category: cs.CV
concept: agents-tool-use
url: https://arxiv.org/abs/2604.06168
published: 2026-04-16
authors: Haoyu Zhen, Zixian Gao, Qiao Sun
---

# Action Images: End-to-End Policy Learning via Multiview Video Generation

**arXiv:** https://arxiv.org/abs/2604.06168
**Authors:** Haoyu Zhen, Zixian Gao, Qiao Sun

## Abstract

arXiv:2604.06168v2 Announce Type: replace  Abstract: World action models (WAMs) have emerged as a promising direction for robot policy learning, as they can leverage powerful video backbones to model the future states. However, existing approaches often rely on separate action modules, or use action representations that are not pixel-grounded, making it difficult to fully exploit the pretrained knowledge of video models and limiting transfer across viewpoints and environments. In this work, we present Action Images, a unified world action model that formulates policy learning as multiview video generation. Instead of encoding control as low-dimensional tokens, we translate 7-DoF robot actions into interpretable action images: multi-view action videos that are grounded in 2D pixels and explicitly track robot-arm motion. This pixel-grounded action representation allows the video backbone itself to act as a zero-shot policy, without a separate policy head or action module. Beyond control, the same unified model supports video-action joint generation, action-conditioned video generation, and action labeling under a shared representation. On RLBench and real-world evaluations, our model achieves the strongest zero-shot success rates and improves video-action joint generation quality over prior video-space world models, suggesting that interpretable action images are a promising route to policy learning.
