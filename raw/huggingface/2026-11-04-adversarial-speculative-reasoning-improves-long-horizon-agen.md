---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.364148+05:30
arxiv_id: 2611.05345
url: https://huggingface.co/papers/2611.05345
arxiv_url: https://arxiv.org/abs/2611.05345
date: 2026-11-04
---

# Adversarial Speculative Reasoning Improves Long Horizon Agents

Speculative decoding has been treated purely as a systems optimization that speeds up large language model decoding without changing the model behavior. Under this view, the growing effort to train better draft models has been focused solely on acceptance rate. We argue that this view does not hold true for long-horizon agent reasoning. Measuring frontier open-weight models on complex agentic tasks with different speculative decoding approaches, we found that numerical noise grows within verification windows, and the draft acceptance results of the thinking process can change the output distribution of the model after 30 steps, thus noticeably influencing the reasoning accuracy of long-horizon agents in random directions. In this work, we improve the reasoning capability of target models by controlling such noise. While we cannot change the overall token distribution verified by the target model, we can encode critical reasoning with highest precision by training the draft model to be rejected. We identify these points in agent traces and train the draft model to favor adversarial preference. At inference the trained draft and the target part ways precisely at these decision points, verification restarts, so that critical thinking tokens are sampled from the target model and encoded under its least noisy conditions. This approach makes critical reasoning better indexed and more durable over a long horizon. On complex agentic coding benchmarks, our approach raises end-to-end success rate with no change to the target model or its output distribution. Our results recast the speculative decoding mechanism from a pure accelerator into an active allocator for context precision that improves the accuracy of long-horizon agents by training 0.06% to 0.28% of hosted parameters.
