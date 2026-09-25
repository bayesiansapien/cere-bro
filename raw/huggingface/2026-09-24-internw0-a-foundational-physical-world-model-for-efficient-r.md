---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.27656
url: https://huggingface.co/papers/2609.27656
arxiv_url: https://arxiv.org/abs/2609.27656
date: 2026-09-24
upvotes: 5
authors: ["Jisong Cai", "Yao Mu", "Ganlin Yang", "Zhe Cao", "Zhangzheng Tu", "Xing Gao", "Kailin Li", "Xinyu Zhan", "Lixin Yang", "Yangkun Zhu", "Haoxiang Ma", "Ming Zhou", "Qiaojun Yu", "Yufei Xue", "Liqun He", "Yifei Yao", "Yifan Zhu", "Long Ling", "Bingqi Jiang", "Haoyu Guo", "Xueyue Zhu", "Bowen Zhou", "Bin Zhao", "Tianfan Xue", "Chunhua Shen", "Weinan Zhang"]
---

# InternW0: A Foundational Physical World Model for Efficient Real-World Interactions

**Authors:** Jisong Cai, Yao Mu, Ganlin Yang, Zhe Cao, Zhangzheng Tu, Xing Gao, Kailin Li, Xinyu Zhan, Lixin Yang, Yangkun Zhu, Haoxiang Ma, Ming Zhou, Qiaojun Yu, Yufei Xue, Liqun He, Yifei Yao, Yifan Zhu, Long Ling, Bingqi Jiang, Haoyu Guo, Xueyue Zhu, Bowen Zhou, Bin Zhao, Tianfan Xue, Chunhua Shen, Weinan Zhang

**Upvotes:** 5

**Links:** [HuggingFace](https://huggingface.co/papers/2609.27656) · [arXiv](https://arxiv.org/abs/2609.27656)

Physical intelligence requires more than predicting how the world may evolve: predictions must remain actionable as the world continues to change. We introduce InternW0, the first instantiation of the InternW physical world model series from Shanghai AI Laboratory, built around omnimodal interfaces, asynchronous multi-frequency processing, and local physical modeling under partial observations and external influences. InternW0 jointly learns future visual dynamics and continuous robot control through an asymmetric video--action architecture with flow matching. A high-capacity video expert provides longer-horizon predictive context, while a lightweight action expert operates at a faster timescale. Instead of regenerating the future for every action update, InternW0 reuses layerwise K/V and adapts it to newly observed states through observation-conditioned context routing. Domain-specific interfaces and soft prompts support heterogeneous embodiments, while contact-aware post-training incorporates force and tactile signals for contact-rich manipulation. We train InternW0 on approximately 7,200 hours of heterogeneous robot and egocentric data, including EgoLab, a 275-hour real-laboratory egocentric dataset. Evaluation spans simulation benchmarks and real-world scientific tasks, including a 15-stage metal--organic framework synthesis workflow and 5-stage contact- and force-aware dexterous manipulation for general-purpose quantitative pipetting. These results advance scalable, asynchronous, and science-native physical world models for universal and efficient real-world interactions.
