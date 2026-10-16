---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.234677+05:30
arxiv_id: 2610.20828
url: https://huggingface.co/papers/2610.20828
arxiv_url: https://arxiv.org/abs/2610.20828
date: 2026-10-15
---

# CoTranslator: Reverse to Forward Chain-of-Thought Translator for Reasoning Distillation

Reasoning distillation requires chain-of-thought (CoT) data with correct answers, but obtaining such data efficiently remains challenging. Forward CoT generation (FCG) followed by rejection sampling (RS) produces verified, question-only responses, yet may require many teacher calls for difficult problems. Reverse CoT generation (RCG) is cheaper because it conditions on the known answer, but access to this answer can lead to post-hoc rationalization and a mismatch with the student's answer-free inference setting. We propose CoTranslator, which learns to translate reverse CoT responses toward the distribution of verified forward responses. Trained on a small set of paired reverse and rejection-sampled forward responses, it supports large-scale generation and verification of student training data. Across six student models evaluated on six mathematics benchmarks, CoTranslator improves average accuracy over semantic suppression by up to 5.82 percentage points. For two 4B students, it retains 95.0% of rejection sampling's average accuracy while using 35.9% of its estimated compute. Without retraining, the same translator transfers to a new mathematics dataset, a different teacher, and STEM problems, improving average STEM accuracy by 4.88 and 4.31 percentage points for 4B and 8B students, respectively. These results show that CoTranslator offers an efficient and transferable approach to reasoning distillation.
