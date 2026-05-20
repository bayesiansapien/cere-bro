---
source: farmer/huggingface
farmed: 2026-05-20T09:55:04.521172+00:00
arxiv_id: 2605.20075
url: https://huggingface.co/papers/2605.20075
arxiv_url: https://arxiv.org/abs/2605.20075
date: 2026-05-20
---

# CopT: Contrastive On-Policy Thinking with Continuous Spaces for General and Agentic Reasoning

Chain-of-thought (CoT) is a standard approach for eliciting reasoning capabilities from large language models (LLMs). However, the common CoT paradigm treats thinking as a prerequisite for answering, which can delay access to plausible answers and incur unnecessary token costs even when the model is able to identify an answer before extended thinking, a behavior known as performative reasoning. In this paper, we introduce CopT, a reformulated reasoning pipeline that reverses the usual order of thinking and answering. Instead of thinking before answering, CopT first elicits a draft answer and then invokes subsequent on-policy thinking conditioned on its own draft answer for reflection and correction. To assess whether the draft answer should be trusted, CopT recasts continuous embeddings as inference-time contrastive verifiers. Specifically, it contrasts the model&#39;s support for the same generated tokens under discrete-token inputs and continuous-embedding inputs, yielding a sequence-level reverse KL estimator for answer reliability. Our analysis shows that under certain assumptions, the expected estimate equals the mutual information between the unresolved latent state and the emitted answer token, explaining why it captures answer-relevant uncertainty rather than arbitrary uncertainty in the latent state. When the answer is deemed insufficiently reliable, CopT performs further on-policy thinking, where a second KL estimator dynamically controls draft-answer visibility, preserving useful partial information while reducing the risk of being misled by unreliable content. Across mathematics, coding, and agentic reasoning tasks, CopT improves peak accuracy by up to 23% and reduces token usage by up to 57% at comparable or higher accuracy, without any additional training. The code is available at this https URL .
