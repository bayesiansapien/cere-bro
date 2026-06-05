---
source: farmer/huggingface
farmed: 2026-06-05T08:18:05.247595+00:00
arxiv_id: 2606.05275
url: https://huggingface.co/papers/2606.05275
arxiv_url: https://arxiv.org/abs/2606.05275
date: 2026-06-05
upvotes: 14
---

# Personal AI Agent for Camera Roll VQA

We study the personal camera roll visual question answering setting. In this setting, a conversational AI assistant can access a user's personal camera roll and retrieve relevant photos to answer queries, ranging from simple factual questions (e.g., ``Name of the food I tried yesterday?'') to more open-ended ones (e.g., ``Recommend some dishes I have never eaten before''). Given the vast nature of the personal camera roll (i.e., multiple years, hundreds to thousands of photos), a successful AI assistant needs to understand a long-horizon, highly personalized visual content stream in order to navigate and locate the correct and/or relevant information. To support this, we collect and manually annotate questions that mimic real-world usage. The final dataset, camroll, contains 50 users, 31,476 images, and 2,500 QA pairs. We further design camroll-agent, a conversational AI agent equipped with hierarchical memory and a minimal set of tools for efficient navigation over large, personalized visual memory. Experimental results show that camroll-agent outperforms numerous baselines and methods for long-context understanding AI agents system. Together, the camroll dataset and camroll-agent highlight the gap in AI agents' long-context reasoning: personalized visual memory requires different approaches from standard long-context textual memory, especially when consistency, visual details, and user-specific context are present.
