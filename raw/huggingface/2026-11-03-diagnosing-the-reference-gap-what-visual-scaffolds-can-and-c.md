---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.39419
url: https://huggingface.co/papers/2610.39419
arxiv_url: https://arxiv.org/abs/2610.39419
date: 2026-11-03
---

# Diagnosing the Reference Gap: What Visual Scaffolds Can and Cannot Fix in Multimodal Reasoning

Multimodal large language models can recognize visual content yet struggle to reason reliably over it across multiple steps. In counting, a model may see all objects but lose track of which ones it has counted. We argue that such failures, commonly attributed to perception, reveal a reference gap: the failure to bind language to the relevant visual entities, regions, or locations. Motivated by the theory of visual routines, we test whether external references such as numbering can narrow this gap. We introduce ReGap-Bench, a paired benchmark of five visual reasoning tasks in which the scene, question, and answer are fixed and only the reference varies. Results show that task-matched references improve accuracy by up to 25\%, while mismatched references provide little benefit or even hurt performance. These findings identify the reference gap as a bottleneck distinct from visual perception and show that constructing task-appropriate visual references can serve as a training-free visual skill for improving multimodal reasoning.
