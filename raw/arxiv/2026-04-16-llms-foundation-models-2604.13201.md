---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13201
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13201
published: 2026-04-16
authors: Oliver Bentham, Vivek Srikumar
---

# InfiniteScienceGym: An Unbounded, Procedurally-Generated Benchmark for Scientific Analysis

**arXiv:** https://arxiv.org/abs/2604.13201
**Authors:** Oliver Bentham, Vivek Srikumar

## Abstract

arXiv:2604.13201v1 Announce Type: cross  Abstract: Large language models are emerging as scientific assistants, but evaluating their ability to reason from empirical data remains challenging. Benchmarks derived from published studies and human annotations inherit publication bias, known-knowledge bias, label noise, and substantial storage requirements. We present InfiniteScienceGym, a procedurally generated benchmark of scientific repositories paired with a verifiable question-answering task. From a seed, the simulator deterministically generates a self-contained repository with realistic directory structure, files, and tabular data, and a privileged QA generator produces both answerable and unanswerable questions with exact ground truth. This makes it possible to evaluate evidence-grounded reasoning, abstention, and tool-mediated analysis in a controlled setting without distributing a large static corpus. InfiniteScienceGym complements real scientific benchmarks by targeting blind spots and failure modes that are hard to evaluate using published datasets alone. Evaluating both proprietary and open-weight models, we find that none achieve more than 45% accuracy overall, that recognizing unanswerable questions remains a major weakness, and that stronger models tend to use tools more effectively rather than simply consuming more tokens.
