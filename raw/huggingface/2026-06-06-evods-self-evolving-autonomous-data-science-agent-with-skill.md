---
source: farmer/huggingface
farmed: 2026-06-06T09:05:36Z
arxiv_id: 2606.03841
url: https://huggingface.co/papers/2606.03841
arxiv_url: https://arxiv.org/abs/2606.03841
date: 2026-06-06
---

# EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management

Recent progress in Large Language Model (LLM) agents has enabled promising advances in automated data science. However, existing approaches remain fundamentally limited by their static action sets and lack of principled long-horizon context management, hindering their ability to accumulate reusable experience across tasks and operate reliably in multi-stage, iterative data science pipelines. To address these challenges, we introduce EvoDS, a self-evolving autonomous data science agent that learns to expand its skills and adaptively managing long-term context through agentic reinforcement learning. Specifically, EvoDS introduces two key strategies: (1) Autonomous Skill Acquisition (ASA) mechanism, which enables agents to synthesize, validate, and reuse executable skills; and (2) Adaptive Context Compression (ACC) strategy, which treats context management as a learned control problem rather than passive truncation. These strategies are orchestrated within a two-stage multi-agent training scheme, enabling EvoDS to autonomously improve over time. Theoretically, we prove that EvoDS's hierarchical design reduces tool-selection error, and its optimization objective aligns with an information bottleneck principle, ensuring efficient context use. Empirically, EvoDS outperforms state-of-the-art open-source data science agents by an average of 28.9% across four diverse benchmarks while eliminating out-of-token failures. Our code and data are available at https://github.com/usail-hkust/EvoDS.
