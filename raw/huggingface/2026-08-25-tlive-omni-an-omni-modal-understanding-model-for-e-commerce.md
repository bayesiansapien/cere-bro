---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.20958
url: https://huggingface.co/papers/2608.20958
arxiv_url: https://arxiv.org/abs/2608.20958
date: 2026-08-25
upvotes: 28
authors: ["Yibo Hu", "Yu Qian", "Mao Gu", "Yingfan Tao", "Yuhao Chen", "Yongdong Luo", "Zhuoqun Liu", "Meiguang Jin", "Junfeng Ma"]
---

# TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming

**Upvotes:** 28
**Authors:** Yibo Hu, Yu Qian, Mao Gu, Yingfan Tao, Yuhao Chen, Yongdong Luo, Zhuoqun Liu, Meiguang Jin, Junfeng Ma

E-commerce live streaming requires omni-modal understanding of noisy, temporally extended streams, where product facts are distributed across speech, video frames, product images, overlaid text, and user queries. We present TLive-Omni, an omni-modal understanding model tailored to live-commerce scenarios. It maps image, video, audio, and text inputs into a unified representation space. For long-form live streaming analysis, we introduce Per-vGrid, a timestamped token organization that groups each video grid with its temporally corresponding audio within explicit boundary tokens to facilitate temporal alignment. We design a three-stage supervised training recipe that progressively develops live-commerce understanding, from omni-modal perception to instruction-following responses. We then propose Faithful-RFT, a reinforcement fine-tuning stage that further improves answer faithfulness and expression quality while meeting real-time demands, scoring final responses directly with task-verifiable feedback rather than optimizing for reasoning-style exploration during rollout. Moreover, TLive-Omni is supported by a scenario-oriented atomic capability taxonomy and a compact data production engine that converts live-commerce audio, image, and video streams into training signals for speech recognition, speaker analysis, product visual grounding, text recognition, temporal grounding, video dense caption, and omni-modal QA, etc. For scalable training, a synchronized length-grouped sampler reduces padding while preserving comparable workloads across workers, while a lightweight dynamic sampling strategy regenerates rollout groups with near-zero reward variance to maintain meaningful relative advantages for GRPO. Experiments on e-commerce live streaming benchmarks demonstrate strong performance across live-commerce domain tasks, together with excellent generalization on general benchmarks.
