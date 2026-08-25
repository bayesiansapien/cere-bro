---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.16812
url: https://huggingface.co/papers/2608.16812
arxiv_url: https://arxiv.org/abs/2608.16812
date: 2026-08-25
upvotes: 41
authors: ["Long Cui", "Xiaoqian Liu", "Qi Qin", "Yi Xin", "Tao Lin", "Jianguo Li", "Linfeng Zhang"]
---

# Unlocking the Potential of Image Editing via Concept Scaling and Dense Supervision

**Upvotes:** 41
**Authors:** Long Cui, Xiaoqian Liu, Qi Qin, Yi Xin, Tao Lin, Jianguo Li, Linfeng Zhang

Existing image editing frameworks predominantly follow the training paradigm of text-to-image diffusion models. However, extending this paradigm to image editing highlights two inherent discrepancies, specifically, the insufficient attention to edit concept granularity and the training inefficiency caused by sparse supervision signals. To address these issues, we establish a comprehensive hierarchical taxonomy featuring over 1,000 fine-grained edit concepts and build ConceptEdit-12M, a massive dataset of 12 million high-quality editing pairs via an improved synthesis framework. This library-driven approach effectively rectifies the distribution collapse of generated data while ensuring high data fidelity. Furthermore, we propose a dense supervision training strategy that synthesizes multiple non-interfering concepts into single image pairs. By providing richer learning signals, this strategy significantly enhances both training efficiency and overall model performance. Training results validate our strategy, significantly outperforming prior works. Finally, we present ConceptEdit-Bench, a granular evaluation suite designed to diagnose model capabilities across a vast array of real-world scenarios.
