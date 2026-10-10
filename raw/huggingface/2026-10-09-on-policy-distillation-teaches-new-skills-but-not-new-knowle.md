---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.419573+00:00
arxiv_id: 2610.09639
url: https://huggingface.co/papers/2610.09639
arxiv_url: https://arxiv.org/abs/2610.09639
date: 2026-10-09
---

# On-Policy Distillation Teaches New Skills but Not New Knowledge

On-policy distillation (OPD) strengthens language-model reasoning, yet whether students acquire new factual knowledge or compositional skill for multi-step reasoning remains unknown. We separate these capabilities using a controlled synthetic framework that measures the student's initial capabilities and independently controls the teacher's additional facts, compositional skill, or both. Across four models from three families, reverse-KL OPD reliably transfers compositional skill across unseen reasoning structures, but transfers minimal factual knowledge. Decoupling the distillation recipe reveals the source of this asymmetry: replacing reverse KL with forward KL restores factual transfer, whereas student rollouts specifically improve the execution of multi-step reasoning. Experiments on recent factual QA and competition mathematics show a similar asymmetry under reverse-KL OPD, yielding notable reasoning gains without factual memory expansion. Together, these results demonstrate that on-policy distillation does not expand a model's parametric knowledge, but instead teaches it to organize and compose the knowledge it already possesses.
