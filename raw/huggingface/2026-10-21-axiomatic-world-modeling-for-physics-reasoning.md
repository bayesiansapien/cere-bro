---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.648031
arxiv_id: 2610.24519
url: https://huggingface.co/papers/2610.24519
arxiv_url: https://arxiv.org/abs/2610.24519
date: 2026-10-21
---

# Axiomatic World Modeling for Physics Reasoning

Recent research-level physics-reasoning benchmarks for LLMs reveal a failure mode that lies not in knowledge or execution, but in modeling the world being reasoned about. Models often silently alter given quantities, fabricate laws, or inject unstated assumptions to force a problem into familiar patterns, and then reason inside this corrupted world. We define this premise-level divergence as modeling drift: the gap between a model's internal axiomatic world model (AWM) and the true physical world specified in the problem. Although RLVR and PRM have yielded substantial gains in mathematics and code, their reward shapes do not directly supervise world modeling in axiomatic domains such as physics. We propose Reinforcement Learning with Axiomatic World Modeling (RLAWM), which optimizes the policy by penalizing divergence between its inferred axiomatic world model and the true physics world. RLAWM probes physics reasoning at two hierarchical levels (modeling and solving), each scored by a physically grounded reward. The modeling reward targets abstract knowledge formulation, evaluating whether the model captures the true axiomatic world before attempting calculation. The solving reward targets instantiated knowledge reasoning, checking whether the model's concrete derivation remains consistent with the axiomatic world. This two-level structure separates what world the model believes it is reasoning in from how it reasons within that world. The framework operates exclusively during training, with no extra cost during inference. RLAWM improves performance by up to +12.2 points on PhysReason and +5.2 on PHYSICS over the baseline. It also generalizes zero-shot across difficulty, source, and domain, with a 2.45x gain and +10 points over the strongest baseline on olympiad-level physics and math.
