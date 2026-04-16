---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13108
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13108
published: 2026-04-16
authors: Ruoqi Jin
---

# Formal Architecture Descriptors as Navigation Primitives for AI Coding Agents

**arXiv:** https://arxiv.org/abs/2604.13108
**Authors:** Ruoqi Jin

## Abstract

arXiv:2604.13108v1 Announce Type: cross  Abstract: AI coding agents spend a substantial fraction of their tool calls on undirected codebase exploration. We investigate whether providing agents with formal architecture descriptors can reduce this navigational overhead. We present three complementary studies. First, a controlled experiment (24 code localization tasks x 4 conditions, Claude Sonnet 4.6, temperature=0) demonstrates that architecture context reduces navigation steps by 33-44% (Wilcoxon p=0.009, Cohen's d=0.92), with no significant format difference detected across S-expression, JSON, YAML, and Markdown. Second, an artifact-vs-process experiment (15 tasks x 3 conditions) demonstrates that an automatically generated descriptor achieves 100% accuracy versus 80% blind (p=0.002, d=1.04), proving direct navigational value independent of developer self-clarification. Third, an observational field study across 7,012 Claude Code sessions shows 52% reduction in agent behavioral variance. A writer-side experiment (96 generation runs, 96 error injections) reveals critical failure mode differences: JSON fails atomically, YAML silently corrupts 50% of errors, S-expressions detect all structural completeness errors. We propose intent.lisp, an S-expression architecture descriptor, and open-source the Forge toolkit.
