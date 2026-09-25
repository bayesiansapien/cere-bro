---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.28256
url: https://huggingface.co/papers/2609.28256
arxiv_url: https://arxiv.org/abs/2609.28256
date: 2026-09-24
upvotes: 9
authors: ["Tej Deep Pala", "Navonil Majumder", "Bryce Goh", "Raphael Yee", "Jianfei Yang", "Liming Chen", "Soujanya Poria"]
---

# MemBodied: Recurrent Associative Memory for Vision-Language-Action Models

**Authors:** Tej Deep Pala, Navonil Majumder, Bryce Goh, Raphael Yee, Jianfei Yang, Liming Chen, Soujanya Poria

**Upvotes:** 9

**Links:** [HuggingFace](https://huggingface.co/papers/2609.28256) · [arXiv](https://arxiv.org/abs/2609.28256)

Vision-Language-Action models provide a strong foundation for general-purpose robot control, yet a vast majority of policies do not preserve and leverage episode-level information beyond the current observation. This limitation is consequential in history-dependent manipulation tasks that depend on information available only in past observations. Retaining past observations in context can aid in recovering this information, but at the significant cost of ever-growing, bloated context and inference latency. We thus introduce MemBodied, a fixed-size episodic memory with two complementary components: an associative state that records interactions across policy calls and an episode anchor that preserves a compact representation of the initial scene as a reference. At each policy call, the model conditions action generation on the current input and the memory components, rather than directly using past observations. Across five evaluated RMBench tasks requiring memory, MemBodied achieves 7.81times the mean success rate of a stateless policy and 2.98times of vanilla recurrent memory, while outperforming the strongest memory-augmented baseline by 1.3times with 10times fewer added parameters. On the fully observable LIBERO-Long suite, it reached 90.6%, a 5.4% improvement over the stateless π_0 policy. These findings support MemBodied as a practical alternative to expanding the policy context for history-dependent manipulation.
