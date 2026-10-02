---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.350322+05:30
arxiv_id: 2609.38792
url: https://huggingface.co/papers/2609.38792
arxiv_url: https://arxiv.org/abs/2609.38792
date: 2026-10-01
---

# Training LLM Judges from Language Feedback via Position-Selective Self-Distillation

We study training LLM judges from natural language feedback, especially for subjective tasks where the verdict depends strongly on which evaluation criteria the judge invokes and how it weighs them. The dominant approach, outcome-supervised RL (e.g., GRPO), credits every token in the rollout with a single scalar determined only by the accuracy of the final verdict, providing no separate credit at the criterion-choice tokens and ignoring the rich language feedback (e.g., preference rationales) that naturally accompanies preference labels. Self-Distillation (SD) is one natural way to use this language feedback: the same model, conditioned on this feedback, acts as a teacher providing dense, position-level supervision. However, not all positions carry equally useful signal. Using the per-position entropy shift between teacher and student, we identify two regimes: context sharpening, where the teacher concentrates probability on a particular feedback-aligned criterion expression, and context spreading, where the teacher distributes probability across multiple feedback-aligned alternatives. We interpret these patterns as follows: sharpening encourages memorization of a particular criterion expression, whereas spreading promotes semantic understanding by preserving these alternatives. Motivated by this asymmetry, we introduce position masking based on the entropy shift that retains the lower tail of the entropy-shift distribution. Experiments show that masking higher-entropy-shift positions improves out-of-distribution generalization over naive SD. The resulting self-distilled judges outperform judges trained with outcome-supervised RL by 2-9 percentage points on the evaluated subjective subcategories, while remaining competitive on objective ones.
