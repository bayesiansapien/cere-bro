---
source: farmer/huggingface
farmed: 2026-04-21T00:00:00Z
arxiv_id: "2604.17338"
url: https://huggingface.co/papers/2604.17338
arxiv_url: https://arxiv.org/abs/2604.17338
date: 2026-04-21
---

# Precise Debugging Benchmark: Is Your Model Debugging or Regenerating?

Unlike code completion, debugging requires localizing faults and applying targeted edits. We observe that frontier LLMs often regenerate correct but over-edited solutions during debugging. To evaluate how far LLMs are from precise debugging, we introduce the Precise Debugging Benchmarking (PDB) framework, which automatically converts any coding dataset into a debugging benchmark with precision-aware evaluation. PDB generates buggy programs by synthesizing verified atomic bugs and composing them into multi-bug programs. We define two novel metrics, edit-level precision and bug-level recall, which measures how many necessary edits are made and how many bugs are resolved. We release two evaluation benchmarks: PDB-Single-Hard on single-line bugs, and PDB-Multi on multi-line bugs. Experiments show that frontier models, such as GPT-5.1-Codex and DeepSeek-V3.2-Thinking, achieve unit-test pass rates above 76% but exhibit precision below 45%, even when explicitly instructed to perform minimal debugging. Finally, we show that iterative and agentic debugging strategies do not substantially improve precision or recall, highlighting the need to rethink post-training pipelines for coding models.

**Authors:** Wang Bill Zhu, Miaosen Chai, Shangshang Wang, Yejia Liu, Song Bian, Honghua Dong, Willie Neiswanger, Robin Jia (University of Southern California; Microsoft; University of Wisconsin-Madison; University of Toronto)
