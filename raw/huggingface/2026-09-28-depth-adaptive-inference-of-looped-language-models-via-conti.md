---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.601318+00:00
arxiv_id: 2608.09444
url: https://huggingface.co/papers/2608.09444
arxiv_url: https://arxiv.org/abs/2608.09444
date: 2026-09-28
---

# Depth-adaptive Inference of Looped Language Models via Continuous Depth Batching

A main promise of looped language models is depth-adaptive inference. By looping a block of shared layers a variable number of times, the model can use less compute for "easy" tokens and more for "hard" ones. However, tokens with different numbers of loops cannot share a uniform forward pass and therefore cannot be handled by standard batching systems such as vLLM. The practical value of depth-adaptive inference thus hinges on whether batching can be made efficient. We introduce the first efficient method for depth-adaptive looped LMs via continuous depth batching (CDB), which forms new batches between loop steps. Our method dynamically schedules looped and non-looped parts of the architecture, manages looped KV-caching, and predicts which tokens will exit the loop in advance so it can prepare batches asynchronously. Experiments on Ouro 1.4B and Huginn 3.5B show that fully looped architectures are best suited to depth-adaptive inference, as large non-looped layers outside the recurrent core (e.g., token embedding, LM head, and unshared transformer blocks) slow down and complicate scheduling. Overall, CDB realizes up to 99% of the estimated maximum speedup available, leaving further gains primarily dependent on model architecture and exit behavior.
