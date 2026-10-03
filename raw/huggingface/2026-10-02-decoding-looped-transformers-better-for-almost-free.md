---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.819506+00:00
arxiv_id: 2610.02185
url: https://huggingface.co/papers/2610.02185
arxiv_url: https://arxiv.org/abs/2610.02185
date: 2026-10-02
---

# Decoding Looped Transformers Better for (Almost) Free

Looped Transformers achieve parameter efficiency by repeatedly executing a shared block across recurrent loops. Each loop yields an intermediate representation decodable for the same next token, yet standard decoding discards earlier states. Because earlier loops embody less computation, recurrence inherently supplies aligned weak-and-strong prediction pairs without auxiliary models or external training. We introduce LoopCD, a training-free contrastive decoding framework that guides token selection by contrasting the final prediction with an earlier recurrent pass, operating either in logit space with one extra output pass (LoopCD-Logits) or in hidden-state space with zero output overhead (LoopCD-Hidden). Across four looped Transformer families, LoopCD delivers substantial, consistent gains at full recurrent depth: LoopCD-Logits raises Ouro-2.6B-Thinking's AIME 2024 pass@1 from 61.88% to 73.33%, while LoopCD-Hidden lifts Huginn's HumanEval pass@1 from 22.56% to 31.71%. Crucially, these performance gains enable halving the number of recurrent loops while still matching or exceeding full-depth unguided baselines, reducing forward FLOPs by 22.5% to 48.2%. By transforming intermediate recurrent states into effective guidance signals, LoopCD achieves superior decoding quality while substantially reducing inference compute.
