---
source: farmer/huggingface
farmed: 2026-04-21T00:00:00Z
arxiv_id: "2604.17972"
url: https://huggingface.co/papers/2604.17972
arxiv_url: https://arxiv.org/abs/2604.17972
date: 2026-04-21
---

# Modeling Multiple Support Strategies within a Single Turn for Emotional Support Conversations

Emotional Support Conversation (ESC) aims to assist individuals experiencing distress by generating empathetic and supportive dialogue. While prior work typically assumes that each supporter turn corresponds to a single strategy, real-world supportive communication often involves multiple strategies within a single utterance. In this paper, we revisit the ESC task by formulating it as multi-strategy utterance generation, where each utterance may contain one or more strategy-response pairs. We propose two generation methods: All-in-One, which predicts all strategy-response pairs in a single decoding step, and One-by-One, which iteratively generates strategy-response pairs until completion. Both methods are further enhanced with cognitive reasoning guided by reinforcement learning to improve strategy selection and response composition. We evaluate our models on the ESConv dataset under both utterance-level and dialogue-level settings. Experimental results show that our methods effectively model multi-strategy utterances and lead to improved supportive quality and dialogue success. To our knowledge, this work provides the first systematic empirical evidence that allowing multiple support strategies within a single utterance is both feasible and beneficial for emotional support conversations.

**Authors:** Jie Zhu, Huaixia Dou, Junhui Li, Lifan Guo, Feng Chen, Jinsong Su, Chi Zhang, Fang Kong (Qwen DianJin / Alibaba)

**Code:** https://github.com/aliyun/qwen-dianjin
