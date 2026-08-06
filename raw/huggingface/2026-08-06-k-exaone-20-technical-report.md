---
source: farmer/huggingface
farmed: 2026-08-06T10:35:34.247620Z
arxiv_id: 2608.04505
url: https://huggingface.co/papers/2608.04505
arxiv_url: https://arxiv.org/abs/2608.04505
date: 2026-08-06
---

# K-EXAONE 2.0 Technical Report

This technical report presents K-EXAONE 2.0, an open-weight multilingual foundation model developed by LG AI Research as a step in our effort toward global frontier-scale foundation models. Rather than training from scratch, we upcycle K-EXAONE and expand its architecture, yielding a Mixture-of-Experts (MoE) model with 750B total parameters and approximately 37B activated per token---more than three times the capacity of its predecessor. K-EXAONE 2.0 supports context lengths of up to 256K tokens and expands multilingual coverage from six to ten languages. Its training pipeline combines continual pre-training, difficulty-focused mid-training, and post-training to strengthen reasoning, agentic coding, multilingual capability, and safety grounded in Korean sociocultural contexts. Across nine evaluation categories selected to reflect the conditions of practical use, K-EXAONE 2.0 improves over K-EXAONE and remains competitive with open-weight models, showing its largest gains in agentic coding and long-context understanding and its clearest strengths in long-context retrieval and safety. Released under the Apache 2.0 license, K-EXAONE 2.0 enables the wider AI ecosystem to evaluate, deploy, adapt, and build upon it, while marking the beginning---rather than the endpoint---of our challenge toward the global frontier.
