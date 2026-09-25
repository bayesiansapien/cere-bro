---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.27334
url: https://huggingface.co/papers/2609.27334
arxiv_url: https://arxiv.org/abs/2609.27334
date: 2026-09-24
upvotes: 34
authors: ["Yefan Zhou", "Yang Li", "Zeyu Leo Liu", "Semih Yavuz", "Shafiq Joty"]
---

# Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents

**Authors:** Yefan Zhou, Yang Li, Zeyu Leo Liu, Semih Yavuz, Shafiq Joty

**Upvotes:** 34

**Links:** [HuggingFace](https://huggingface.co/papers/2609.27334) · [arXiv](https://arxiv.org/abs/2609.27334)

Agentic memory systems reuse past experience to improve future performance, yet most existing designs curate memory at write time: once a task is completed, its trajectory is distilled into a fixed artifact, such as a reflection, workflow, skill, or reasoning strategy, that is later retrieved by similarity. This forces the system to decide what is worth remembering before the future query is known, irreversibly discarding information and producing a query-independent summary that must serve many possible downstream tasks. Learning such a write-time curator is also difficult because the value of a storage decision may only become apparent when a relevant query arrives, potentially many tasks later, creating a long-horizon credit-assignment problem. We instead retain raw trajectories and defer curation until read time, when the current task is known. Given the retrieved traces and the new task, a memory curator synthesizes a compact, task-adaptive payload tailored to the immediate need. Because this payload is consumed on the same task, the curator can be trained directly from immediate task success, avoiding delayed utility signals and the need to artificially group related tasks. Across ALFWorld, WebShop, and τ^2-bench, our Just-in-Time Memory (JitMem) consistently outperforms no-memory agents as well as heuristic and learned write-time memory methods, improving over the strongest baseline by 16.2, 16.3, and 3.9 absolute success-rate points, respectively. Notably, even an untrained curator is already competitive with or surpasses these baselines, showing that task-adaptive read-time curation itself is a major source of the gain; training the curator further compounds the improvement.
