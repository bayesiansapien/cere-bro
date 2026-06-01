---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.30407
url: https://huggingface.co/papers/2605.30407
arxiv_url: https://arxiv.org/abs/2605.30407
date: 2026-06-01
---

# Exploring Autonomous Agentic Data Engineering for Model Specialization

Large Language Models (LLMs) have demonstrated strong performance on general tasks, while often struggling to adapt to specialized domains without high-quality domain-specific data. Existing LLM-based data curation methods primarily rely on human-designed workflows, leaving it unexamined whether LLMs can autonomously execute an end-to-end data engineering pipeline for model specialization. We formalize Autonomous Agentic Data Engineering, a novel task designed to evaluate LLMs as autonomous data engineers that drive model specialization through end-to-end data curation. We frame data as an optimizable component and study agents that plan, generate, and iteratively optimize training data across multiple domains, guided by post-training performance improvement. Experiments show that autonomous LLM data engineers yield substantial gains, as GPT-5.2 constructs a training curriculum that improves a student model by 57.29%, entirely through iterative, agent-driven data adaptation.
