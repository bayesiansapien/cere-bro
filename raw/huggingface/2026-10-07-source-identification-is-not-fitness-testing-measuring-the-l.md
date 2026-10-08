---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.00417
url: https://huggingface.co/papers/2610.00417
arxiv_url: https://arxiv.org/abs/2610.00417
date: 2026-10-07
---

# Source Identification Is Not Fitness Testing: Measuring the Limits of Synthetic-Data Attribution

Repeated training on model-generated data can degrade later models. One possible response is to use provenance when deciding which generated examples to reuse. We test both how reliably that provenance can be recovered and whether it helps identify better training data. Using financial-risk text, we first identify the source of generated passages and then repeat the test after rewriting them. Generator attribution is 98.7% accurate on the original passages but falls to 53.1% after paraphrasing and 29.0% after style rewriting. Generated-versus-human detection remains close to perfect against the tested human comparison set. We then compare two ways of selecting generated examples over three rounds of generation and retraining. One uses source information. The other uses a score from a separate reference model. The two rules select different examples, but the planned comparison does not detect a stable difference in the degradation of the resulting models. The results show that identifying where data came from and identifying which data are useful for training are separate problems. The experiment therefore separates source identity, criterion-facing selection, and recursive training outcome: neither the provenance score nor the tested criterion-facing proxy is established as sufficient for future recursive behaviour.
