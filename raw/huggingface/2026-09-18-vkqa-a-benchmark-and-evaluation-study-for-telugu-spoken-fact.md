---
source: farmer/huggingface
farmed: 2026-09-18T16:13:44.923131+00:00
arxiv_id: 2609.19879
url: https://huggingface.co/papers/2609.19879
arxiv_url: https://arxiv.org/abs/2609.19879
date: 2026-09-18
---

# VākQA: A Benchmark and Evaluation Study for Telugu Spoken Factoid Question Answering

Question answering has advanced rapidly with large language models, but predominantly for high-resource languages, in both text and spoken settings. Spoken question answering (SQA) benchmark for Telugu remains unexplored, and the reliability of automatic evaluation in this setting remains unquantified. We introduce VākQA, a Telugu SQA benchmark of 2,001 factoid question-answer pairs across six domains, with 2.53 hours of speech audio, bilingual transcriptions, and human-verified reference answers. We first validate evaluation methods against human judgements: Gemini-as-a-judge best approximates human ratings but is non-uniformly strict, while open-weight judges systematically penalize correct Telugu answers that differ in surface form from the reference. Using this validated setup, we benchmark proprietary and open-weight models across input modality, language, and domain. We observe that Telugu phrasing retains cultural specificity that is lost in translation, speech input introduces phonetic confusions that alter question meaning, and cascaded ASR-MT errors compound progressively. VākQA is publicly released.
