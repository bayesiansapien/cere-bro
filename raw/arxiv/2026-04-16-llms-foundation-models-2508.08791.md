---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2508.08791
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2508.08791
published: 2026-04-16
authors: Junjie Ye, Changhao Jiang, Zhengyin Du
---

# Feedback-Driven Tool-Use Improvements in Large Language Models via Automated Build Environments

**arXiv:** https://arxiv.org/abs/2508.08791
**Authors:** Junjie Ye, Changhao Jiang, Zhengyin Du

## Abstract

arXiv:2508.08791v3 Announce Type: replace-cross  Abstract: Effective tool use is essential for large language models (LLMs) to interact with their environment. However, progress is limited by the lack of efficient reinforcement learning (RL) frameworks specifically designed for tool use, due to challenges in constructing stable training environments and designing verifiable reward mechanisms. To address this, we propose an automated environment construction pipeline, incorporating scenario decomposition, document generation, function integration, complexity scaling, and localized deployment. This enables the creation of high-quality training environments that provide detailed and measurable feedback without relying on external tools. Additionally, we introduce a verifiable reward mechanism that evaluates both the precision of tool use and the completeness of task execution. When combined with trajectory data collected from the constructed environments, this mechanism integrates seamlessly with standard RL algorithms to facilitate feedback-driven model training. Experiments on LLMs of varying scales demonstrate that our approach significantly enhances the models' tool-use performance without degrading their general capabilities. Our analysis suggests that these gains result from improved context understanding and reasoning, driven by updates to the lower-layer MLP parameters in models. Code and data are available at https://github.com/bytedance/FTRL.
