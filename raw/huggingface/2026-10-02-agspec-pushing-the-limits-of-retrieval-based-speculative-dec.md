---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.821040+00:00
arxiv_id: 2610.01108
url: https://huggingface.co/papers/2610.01108
arxiv_url: https://arxiv.org/abs/2610.01108
date: 2026-10-02
---

# AgSpec: Pushing the Limits of Retrieval-Based Speculative Decoding in Coding Agent Pipelines

Retrieval-based speculative decoding (SD) drafts tokens by copying continuations from existing text, which suits coding agents that repeatedly reproduce code, logs, and earlier attempts. Yet existing methods fall short in agent pipelines: much of the reusable text is missing from their corpora or stored in a form that differs from what the agent emits, and their draft lengths ignore that accept length varies across agents and drifts over turns. We present AgSpec, a framework that supplies the corpus and draft-length policies that existing retrieval engines lack in coding-agent pipelines. AgSpec retrieves from session, workspace, and global corpora, retaining the ongoing session trajectory and indexing opened files in the agent's emission format. It bounds each agent's draft length with an offline-profiled cap and adapts the length online from verification feedback. On two repository-level multi-agent coding benchmarks, AgSpec outperforms five retrieval-based drafters and EAGLE-3 in most evaluated settings, raising generation throughput over autoregressive decoding up to 4.37times at batch size 1 and 4.76times at batch size 16. AgSpec also remains effective on benchmarks without a repository or a multi-agent pipeline, showing that its gains generalize to coding agents broadly.
