---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.142122+00:00
arxiv_id: 2611.19200
url: https://huggingface.co/papers/2611.19200
arxiv_url: https://arxiv.org/abs/2611.19200
date: 2026-11-19
---

# LogT: Logically Think with Images for Visual Search

Thinking with images empowers vision-language models (VLMs) to use an external Zoom-in tool for fine-grained visual search. Recent works employ supervised fine-tuning (SFT) and reinforcement learning (RL) with tool-specific designs to enable such capabilities. However, achieving logical reasoning alongside accurate and efficient tool use remains a significant challenge. To address this, we shift the focus away from increasing RL complexity and instead identify SFT data quality as a key bottleneck. We then propose LogT (short for Logically Think with Images), a fully automated SFT data engine that explicitly enforces logic-chain-guided reasoning. LogT generates an SFT dataset featuring challenging, visually grounded questions and structured tool-use traces with human-like logic. We validate our approach by fine-tuning two base models, Qwen2.5-VL-7B and InternVL3.5-8B, on the dataset and evaluating them across seven benchmark test sets. We show that LogT-SFT based on Qwen2.5-VL-7B outperforms the state-of-the-art trained with both SFT and RL, despite using 3.1times less data and >120times fewer GPU hours. Furthermore, applying a simple RL recipe without tool-specific design on LogT-SFT yields a model that surpasses prior methods with complex RL setups by a substantial 9.59-point margin. In addition to strong performance gains, our model exhibits higher tool-use accuracy and efficiency, as well as more structured and logically consistent reasoning traces, directly validating the effectiveness of our approach.
