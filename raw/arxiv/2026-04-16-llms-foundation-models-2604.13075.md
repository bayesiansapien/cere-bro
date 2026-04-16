---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13075
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13075
published: 2026-04-16
authors: Md Hasebul Hasan, Krity Haque Charu, Eshwara Prasad Sridhar
---

# DeEscalWild: A Real-World Benchmark for Automated De-Escalation Training with SLMs

**arXiv:** https://arxiv.org/abs/2604.13075
**Authors:** Md Hasebul Hasan, Krity Haque Charu, Eshwara Prasad Sridhar

## Abstract

arXiv:2604.13075v1 Announce Type: cross  Abstract: Effective de-escalation is critical for law enforcement safety and community trust, yet traditional training methods lack scalability and realism. While Large Language Models (LLMs) enable dynamic, open-ended simulations, their substantial computational footprint renders them impractical for deployment on the lightweight, portable hardware required for immersive field training. Small Language Models (SLMs) offer a viable real-time alternative but suffer from a critical scarcity of high-quality, domain-specific training data. To bridge this gap, we present DeEscalWild, a novel benchmark dataset curated from a multi-stage pipeline of in-the-wild police-civilian interactions extracted from open-source video repositories. Starting with 5,000 raw inputs, we employed a rigorous hybrid filtering process - combining human-in-the-loop verification with LLM-as-a-Judge evaluation - to distill 1,500 high-fidelity scenarios. The resulting corpus comprises 285,887 dialogue turns, totaling approximately 4.7 million tokens. Extensive experiments demonstrate that SLMs fine-tuned on this data significantly outperform their base counterparts across ROUGE-L, BLEU-4, METEOR, and BERTScore metrics. Notably, our fine-tuned Qwen 2.5 (3B-Instruct) surpasses the general-purpose Gemini 2.5 Flash model, demonstrating that domain-optimized SLMs can achieve superior performance with a fraction of the computational cost. This work establishes the foundational infrastructure for accessible, low-latency, and privacy-preserving officer training systems at the edge.
