---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2603.11875
category: cs.AI
concept: inference-efficiency
url: https://arxiv.org/abs/2603.11875
published: 2026-04-16
authors: J Alex Corll
---

# The Mirror Design Pattern: Strict Data Geometry over Model Scale for Prompt Injection Detection

**arXiv:** https://arxiv.org/abs/2603.11875
**Authors:** J Alex Corll

## Abstract

arXiv:2603.11875v2 Announce Type: replace-cross  Abstract: Prompt injection defenses are often framed as semantic understanding problems and delegated to increasingly large neural detectors. For the first screening layer, however, the requirements are different: the detector runs on every request and therefore must be fast, deterministic, non-promptable, and auditable. We introduce Mirror, a data-curation design pattern that organizes prompt injection corpora into matched positive and negative cells so that a classifier learns control-plane attack mechanics rather than incidental corpus shortcuts. Using 5,000 strictly curated open-source samples -- the largest corpus supportable under our public-data validity contract -- we define a 32-cell mirror topology, fill 31 of those cells with public data, train a sparse character n-gram linear SVM, compile its weights into a static Rust artifact, and obtain 95.97\% recall and 92.07\% F1 on a 524-case holdout at sub-millisecond latency with no external model runtime dependencies. On the same holdout, our next line of defense, a 22-million-parameter Prompt Guard~2 model reaches 44.35\% recall and 59.14\% F1 at 49\,ms median and 324\,ms p95 latency. Linear models still leave residual semantic ambiguities such as use-versus-mention for later pipeline layers, but within that scope our results show that for L1 prompt injection screening, strict data geometry can matter more than model scale.
