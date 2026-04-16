---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13065
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13065
published: 2026-04-16
authors: Abinav Rao, Sujan Rachuri, Nikhil Vemuri
---

# Correct Chains, Wrong Answers: Dissociating Reasoning from Output in LLM Logic

**arXiv:** https://arxiv.org/abs/2604.13065
**Authors:** Abinav Rao, Sujan Rachuri, Nikhil Vemuri

## Abstract

arXiv:2604.13065v1 Announce Type: cross  Abstract: LLMs can execute every step of chain-of-thought reasoning correctly and still produce wrong final answers. We introduce the Novel Operator Test, a benchmark that separates operator logic from operator name, enabling rigorous distinction between genuine reasoning and pattern retrieval. By evaluating Boolean operators under unfamiliar names across depths 1-10 on five models (up to 8,100 problems each), we demonstrate a reasoning-output dissociation that existing benchmarks cannot detect. At Claude Sonnet 4's depth 7, all 31 errors have verifiably correct reasoning yet wrong declared answers; 17/19 errors in mixed-operator chains exhibit the same pattern. The benchmark reveals two failure types: strategy failures at depth 2, where models attempt terse retrieval (+62pp from scaffolding), and content failures at depth 7, where models reason fully but err systematically (+8-30pp, 0/300 errors post-intervention). A Trojan operator (XOR's truth table under a novel name) confirms name alone does not gate reasoning (p >= 0.49), while Llama's novelty gap widens to 28pp at depth 8-9 with the Trojan at 92-100%, isolating genuine difficulty with novel logic from name unfamiliarity.
