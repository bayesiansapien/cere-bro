---
source: farmer/huggingface
farmed: 2026-06-09T11:13:01Z
arxiv_id: 2606.07297
url: https://huggingface.co/papers/2606.07297
arxiv_url: https://arxiv.org/abs/2606.07297
date: 2026-06-09
---

# SWE-Explore: Benchmarking How Coding Agents Explore Repositories

Repository-level coding benchmarks such as SWE-bench have driven a rapid surge in the capabilities of coding agents. Yet they usually treat coding tasks as a holistic, binary prediction problem (e.g., resolved or unresolved), neglecting fine-grained agent capabilities such as repository understanding, context retrieval, code localization, and bug diagnosis. In this paper, we introduce SWE-Explore, a benchmark that isolates the evaluation of repository exploration, a critical capability of coding agents. Given a repository and an issue, SWE-Explore asks an explorer to return a ranked list of relevant code regions under a fixed line budget. SWE-Explore covers 848 issues across 10 programming languages and 203 open-source repositories. For each instance, we derive line-level ground truth from independent agent trajectories that successfully solved the same issue, distilling the specific code regions their solution paths actually consulted. We evaluate exploration along coverage, ranking, and context-efficiency dimensions, showing that these metrics strongly track downstream repair behavior. Across a broad set of retrieval methods, general coding agents, and specialized localizers, we find that agentic explorers form a clear tier above classical retrieval. While file-level localization is already strong for modern methods, line-level coverage and efficient ranking remain the key axes differentiating state-of-the-art explorers.
