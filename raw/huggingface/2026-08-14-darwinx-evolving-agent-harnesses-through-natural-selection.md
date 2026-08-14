---
source: farmer/huggingface
farmed: 2026-08-14T11:17:27.766803
arxiv_id: 2608.07545
url: https://huggingface.co/papers/2608.07545
arxiv_url: https://arxiv.org/abs/2608.07545
date: 2026-08-14
---

# DarwinX: Evolving Agent Harnesses Through Natural Selection

An LLM agent's capability depends not only on model weights but on its harness: prompts, tools, skills, and control flow. Self-improvement loops already edit harnesses, yet single-lineage search is path-dependent and local wins often regress other tasks. We introduce DarwinX, which treats self-evolution as selection over a population of harnesses with the model frozen: a preserve-and-extend contract admits only variants that extend coverage without regressing, an archive keeps alternative lineages for recombination, and failure-, teacher-, and self-derived evidence share one edit interface. Fitness comes from each benchmark's own verifier: no gold solutions, no hand-picked winners. Across four benchmarks that progressively separate the evolution signal from the test, one loop adds about 17 points on average: Terminal-Bench 2.1 rises +7.7 to 83.2% on a matched base and to the verified frontier at 84.7% on a stronger one; TerminalWorld's held-out split reaches 68.3%, ahead of every off-the-shelf agent; WebArena-Infinity real-task pass@1 rises from 43.5% to 93.0% audit-clean; and a Terminal-Bench 2.1 harness transfers unchanged to SWE-bench Verified. What evolves is general agent competence, not benchmark-specific patches, so it survives changes of task, verifier, and base model. A frozen model need not be a fixed agent: harness selection turns evaluation compute into durable capability.
