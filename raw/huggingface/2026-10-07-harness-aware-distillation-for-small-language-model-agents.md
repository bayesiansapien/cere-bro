---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.02858
url: https://huggingface.co/papers/2610.02858
arxiv_url: https://arxiv.org/abs/2610.02858
date: 2026-10-07
---

# Harness-Aware Distillation for Small Language Model Agents

Language model agents are deployed with a harness, the software around the model that manages its context, tools, and feedback. When such an agent is distilled into a smaller one, the harness stays in place, so the student mainly needs the teacher-specific abilities that the harness cannot provide, such as acting correctly on harness information. Standard distillation, however, imitates the teacher's full outputs and treats the harness as part of the input. We propose Harness-Aware Distillation (HAD), which focuses distillation on what the teacher adds beyond the harness. HAD complements on-policy distillation with two components: an action preference that contrasts the same teacher's actions with and without the harness information, scored after the student's own reasoning, and a validity check that drops preference pairs whose preferred action contradicts the harness records. We show that the contrast gives the student information that imitating the teacher alone cannot provide, and HAD needs no task rewards, success labels, or future information. Across multiple long-horizon agent benchmarks and models, HAD outperforms on-policy distillation baselines with the same fixed harness. Our analysis shows that HAD enters fewer unproductive loops and recovers from errors more often than the baselines, and suggests that it adaptively keeps learnable feedback in its weights while reading state information from the harness.
