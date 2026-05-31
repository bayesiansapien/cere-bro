---
source: farmer/huggingface
farmed: 2026-05-31T09:25:04Z
arxiv_id: 2601.07525
url: https://huggingface.co/papers/2601.07525
arxiv_url: https://arxiv.org/abs/2601.07525
date: 2026-05-31
---

# Thinking Before Constraining: A Unified Decoding Framework for Large Language Models

Natural generation allows Large Language Models (LLMs) to produce free-form responses with rich reasoning, yet the lack of structure makes outputs difficult to verify. Conversely, constrained decoding ensures standardized formats but can inadvertently restrict reasoning capabilities by imposing constraints too early in the generation process. We propose a hybrid approach, namely In-Writing, that combines free-form reasoning and structured generation in a single call. The model first performs unconstrained reasoning and only applies structured decoding after a trigger token is generated, explicitly decoupling reasoning from formatting. We establish that our trigger-token strategies are able to virtually eradicate premature triggering, a failure mode in which constrained decoding interrupts on-going reasoning. Evaluations across diverse datasets covering classification and reasoning tasks demonstrate that our approach outperforms the state-of-the-art by achieving accuracy gains of up to 27% over natural generation. Our code are available at: https://github.com/Nokia-Bell-Labs/InWriting.
