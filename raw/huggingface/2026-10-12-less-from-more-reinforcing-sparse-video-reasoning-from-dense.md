---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.223891+05:30
arxiv_id: 2610.10893
url: https://huggingface.co/papers/2610.10893
arxiv_url: https://arxiv.org/abs/2610.10893
date: 2026-10-12
---

# Less from More: Reinforcing Sparse Video Reasoning from Dense References

Video-language models commonly assume that more temporal observations lead to more reliable reasoning. We question this assumption and argue that the key challenge is not merely processing more video frames efficiently, but learning to reason reliably under limited temporal evidence. We propose SAVER, a dense-to-sparse post-training framework that uses dense video views as training-time references for sparse-frame inference. During reinforcement post-training, paired dense and sparse views are optimized with grounding rewards and a reliability-gated reference reward, encouraging sparse view predictions to preserve task-relevant temporal evidence. Notably, SAVER is trained only on 1,250 randomly sampled temporal grounding examples, without using any video question answering annotations. Across three temporal grounding benchmarks and six video question-answering benchmarks, SAVER consistently improves performance across frame budgets. In particular, SAVER can match or surpass dense-frame Qwen3.5 baselines while using substantially fewer frames. These results show that temporal grounding can serve as an effective evidence-localization proxy for learning sparse video reasoning that transfers to broader video understanding tasks.
