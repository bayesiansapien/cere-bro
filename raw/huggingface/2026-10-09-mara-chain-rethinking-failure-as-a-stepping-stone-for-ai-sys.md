---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.417622+00:00
arxiv_id: 2609.35855
url: https://huggingface.co/papers/2609.35855
arxiv_url: https://arxiv.org/abs/2609.35855
date: 2026-10-09
---

# Mara Chain: Rethinking Failure as a Stepping Stone for AI System Auto-Evolution

Optimizing deployed AI systems increasingly amounts to editing prompts, skills, harnesses, and code rather than model weights. Existing approaches commonly optimize these artifacts through propose-evaluate-select procedures, where candidate configurations are evaluated and only those meeting an acceptance criterion are selected. Yet our analysis shows that discarded candidates often contain information critical for subsequent optimization. Discarding them causes later proposals to revisit the same failure modes. We introduce Mara Chain, a refinement procedure that turns rejected candidates into stepping stones. Rather than discarding a rejected candidate, Mara Chain retains and iteratively refines it using evidence accumulated across preceding attempts. The procedure limits each refinement chain to a fixed depth and applies Pareto-filtered Top-N selection to bound the candidate pool. Across AppWorld skill optimization, TerminalBench 2.1 harness optimization, and MuSiQue retrieval-pipeline optimization, Mara Chain delivers greater task-performance gains with fewer rollouts. It outperforms GEPA, ACE, and SkillOpt-Lite by up to 20.5% in relative performance on AppWorld, reaching the target score with 65.5% fewer rollouts than GEPA. It improves the pass rate by 20.2 and 22.5 percentage points over AHE and Meta-Harness on TerminalBench 2.1, respectively, and improves MuSiQue test nDCG@10 and Recall@10 by 0.104 and 0.131 over a hand-written retrieval pipeline.
