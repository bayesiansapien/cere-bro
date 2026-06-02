---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2606.00660
url: https://huggingface.co/papers/2606.00660
arxiv_url: https://arxiv.org/abs/2606.00660
date: 2026-06-02
---

# FineVerify: Scaling Test-Time Compute with Fine-Grained Self-Verification for Agentic Search

Agentic search requires language model agents to explore many sources and answer complex information-seeking questions. Scaling test-time compute is a promising way to improve these agents, but current approaches can fail, because correct answers are often sparse and score-based selection depends on model calibration. We propose FineVerify, a fine-grained self-verification framework that decomposes each question into checkable sub-questions, verifies sampled candidates against each sub-question, and selects the candidate with the highest aggregated score. This per-check structure turns selection into simpler local judgments and produces scores under the same explicit criteria. Across four agentic search benchmarks and two models, FineVerify consistently outperforms standard scaling baselines. With only four sampled trajectories, it improves GPT-5-mini by 8.2 accuracy points and Gemini-3-flash by 5.6% on average. With 12 samples, FineVerify enables GPT-5-mini to surpass frontier GPT-5 on BrowseComp-Plus. Beyond accuracy, FineVerify produces interpretable verification traces that help audit benchmark errors, suggesting broader applications for inspecting agentic search systems. Code and data are available at https://github.com/XuZhao0/fineverify
