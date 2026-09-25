---
source: farmer/huggingface
farmed: 2026-09-25T22:51:58.846051
arxiv_id: 2609.28416
url: https://huggingface.co/papers/2609.28416
arxiv_url: https://arxiv.org/abs/2609.28416
date: 2026-09-25
upvotes: 13
---

# Agent-Editing World Model: Rethinking World Modeling for LLM Agents

Recent advances in large language models (LLMs) have enabled agents to tackle long-horizon tasks across diverse environments. To further improve agent performance, existing language world models typically predict environment observations, yet reconstructing high-entropy, execution-dependent tool responses offers limited value when real feedback is available. Meanwhile, agents suffer from task-state contamination, where unsupported assumptions and outdated plans persist in history and distort subsequent decisions. We propose the Agent-Editing World Model (AEWM), which models how reasoning and actions shape future task progress rather than simulating tool responses. AEWM combines Action Judge to distinguish Critical, Exploratory, and Noisy decisions with State Revision to edit noisy reasoning--action continuations from the same observed history. EditAct integrates these capabilities with real execution, directly changing the state underlying subsequent decisions rather than merely providing critiques. We train AEWM across Search, Terminal, and Software Engineering through mid-training and supervised fine-tuning. AEWM achieves 70.5\% macro-F1 on our Action Judge benchmark, exceeding the strongest frontier baseline by 10.6 points. Across six benchmarks and three agent backbones, EditAct improves average scores by 3.2--6.7 points over the strongest baseline. Furthermore, rejection sampling fine-tuning on verified EditAct trajectories, termed AEWM-RFT, improves over Self-RFT by 2.2--2.6 points across three domains without online AEWM guidance.
