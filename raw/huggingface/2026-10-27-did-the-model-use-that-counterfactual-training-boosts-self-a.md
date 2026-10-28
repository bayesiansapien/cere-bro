---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.35295
url: https://huggingface.co/papers/2610.35295
arxiv_url: https://arxiv.org/abs/2610.35295
date: 2026-10-27
---

# Did the Model Use That? Counterfactual Training Boosts Self-Attribution in Language Models

A fundamental challenge for explainable and accountable language models is revealing how external information influences their answers. This paper examines whether models are self-attributive: that is, whether they indicate when -- and only when -- their responses to questions are influenced by information provided alongside the question. Furthermore, we explore how self-attribution can be improved through counterfactual training, which explicitly teaches models to distinguish between answers that do and do not depend on supplied information.
  We found that most of the eleven frontier models rarely attribute influential information in their answers, and the rest attribute non-influential information. Training acknowledgment into reasoning does not fix this: the acknowledgment does not reach the final answer.
  We introduce CREDIT, which directly supervises final-answer self-attribution with counterfactual labels, without the need for human annotation. CREDIT substantially improves attribution in four open models, including two distilled reasoning models, and outperforms reasoning-level fine-tuning and prompting baselines. Among answers that agree with a user's suggestion, CREDIT distinguishes those changed by the suggestion from those the model would have given anyway. Gains transfer partly to unseen information types and prompts containing sources that support conflicting answers.
