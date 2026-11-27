---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.908938+00:00
arxiv_id: 2611.21155
url: https://huggingface.co/papers/2611.21155
arxiv_url: https://arxiv.org/abs/2611.21155
date: 2026-11-26
---

# Edit Recommendation: Can LLMs Anticipate Edit Requests from Users, and When?

After a large language model (LLM) agent generates an artifact, users often send edit requests for it. This paper studies whether an LLM can anticipate these requests before they are sent. Such anticipation is useful in practice because it reduces the effort of user review and feedback. We formalize this task as edit recommendation and build EditRecBench, a benchmark for evaluating the performance of LLMs on this task, from real-world conversation logs in WildChat-4.8M. Through benchmarking and failure analysis, we identify a practical challenge that some cases are inherently difficult to predict in real-world settings. To address this, we introduce decision model-based gating to filter out cases where predictions are unlikely to be correct before they are presented to the user. Our trained model outperforms existing decision models and raises pass@5 among shown suggestions by 12--25 points at a gating threshold. Our code is available at https://github.com/ntt-dkiku/llm-edit-recommendation.
