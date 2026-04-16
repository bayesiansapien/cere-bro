---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13713
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13713
published: 2026-04-16
authors: Sinan Kurtyigit, Sabine Schulte im Walde, Alexander Fraser
---

# Learning the Cue or Learning the Word? Analyzing Generalization in Metaphor Detection for Verbs

**arXiv:** https://arxiv.org/abs/2604.13713
**Authors:** Sinan Kurtyigit, Sabine Schulte im Walde, Alexander Fraser

## Abstract

arXiv:2604.13713v1 Announce Type: new  Abstract: Metaphor detection models achieve strong benchmark performance, yet it remains unclear whether this reflects transferable generalization or lexical memorization. To address this, we analyze generalization in metaphor detection through RoBERTa, the shared backbone of many state-of-the-art systems, focusing on English verbs using the VU Amsterdam Metaphor Corpus. We introduce a controlled lexical hold-out setup where all instances of selected target lemmas are strictly excluded from fine-tuning, and compare predictions on these Held-out lemmas against Exposed lemmas (verbs seen during fine-tuning). While the model performs best on Exposed lemmas, it maintains robust performance on Held-out lemmas. Further analysis reveals that sentence context alone is sufficient to match full-model performance on Held-out lemmas, whereas static verb-level embeddings are not. Together, these results suggest that generalization is primarily driven by "learning the cue" (transferable contextual patterns), while "learning the word" (verb-specific memorization) provides an additive boost when lexical exposure is available.
