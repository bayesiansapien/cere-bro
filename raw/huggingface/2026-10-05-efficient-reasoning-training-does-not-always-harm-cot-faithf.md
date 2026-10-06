---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2610.03509
url: https://huggingface.co/papers/2610.03509
arxiv_url: https://arxiv.org/abs/2610.03509
date: 2026-10-05
---

# Efficient Reasoning Training Does Not Always Harm CoT Faithfulness and Monitorability

Chain-of-thought (CoT) reasoning allows humans to inspect how large language models reach their answers, and oversee model behaviour. This reasoning comes at an increased inference cost, motivating efficient methods that train models to solve tasks using fewer tokens. However, a common concern is that such training may cause models to skip important reasoning steps, so the CoT no longer faithfully reflects the model's decision. It is unclear whether or when this occurs in practice, since different efficiency methods apply length pressure to models' CoT in distinct ways, and faithfully explaining a model's decision takes more tokens on some tasks than others. To understand these dynamics, we fine-tune a variety of models with three methods that apply length pressure differently, namely a fixed generation budget, a per-example length target, and a group-relative length reward. We evaluate how efficient reasoning affects CoT faithfulness (i.e., how well the CoT reflects model decisions on related inputs) and monitorability (i.e., whether the CoT reveals when input interventions alter the output). We find that it affects faithfulness and monitorability differently. Faithfulness falls in most settings, primarily because the trained models are less consistent. Monitorability is more robust, as models keep acknowledging the influence on their answer even when the CoT is much shorter.
