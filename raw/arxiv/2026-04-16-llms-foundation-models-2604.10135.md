---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.10135
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.10135
published: 2026-04-16
authors: Zhichen Liu, Yongyuan Li, Yang Xu
---

# Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities

**arXiv:** https://arxiv.org/abs/2604.10135
**Authors:** Zhichen Liu, Yongyuan Li, Yang Xu

## Abstract

arXiv:2604.10135v2 Announce Type: replace-cross  Abstract: Researchers have explored different ways to improve large language models (LLMs)' capabilities via dummy token insertion in contexts. However, existing works focus solely on the dummy tokens themselves, but fail to leverage the inherent sentence-level structure of natural language. This is a critical oversight, as LLMs acquire linguistic capabilities through exposure to human-generated texts, which are inherently structured at the sentence level. Motivated by this gap, we propose an approach that inserts delimiters at sentence boundaries in LLM inputs, which not only integrates dummy tokens into the context, but also facilitates LLMs with sentence-by-sentence processing behavior during reasoning. Two concrete methods: (1). In-context learning and (2). Supervised fine-tuning are experimented using 7B models to 600B Deepseek-V3. Our results demonstrate consistent improvements across various tasks, with notable gains of up to 7.7\% on GSM8k and 12.5\% on DROP. Furthermore, the fine-tuned LLMs can incorporate sentence awareness evidenced by their internal representations. Our work establishes a simple yet effective technique for enhancing LLM's capabilities, offering promising directions for cognitive-inspired LLM enhancement paradigm.
