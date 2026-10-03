---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820501+00:00
arxiv_id: 2609.38987
url: https://huggingface.co/papers/2609.38987
arxiv_url: https://arxiv.org/abs/2609.38987
date: 2026-10-02
---

# Smaller Models, Better Rejects: Preference Distillation Scaling

Preference distillation typically treats a teacher response as preferred and the student's own response as rejected. This assumes that self-generated failures are the most informative negatives and that rejects must come from a model at least as large as the student, making generation costly at scale. We find neither assumption holds: across students from 7B to 72B, smaller frozen models generate rejects with less inference compute yet train stronger students than self-generated rejects, before and after sequence-level knowledge distillation, on code generation and mathematical reasoning. To explain this result, we derive a finite-horizon utility bound for Direct Preference Optimization in a linearized feature model. The bound characterizes favorable reject distributions and motivates three interventions. First, mixing rejects from smaller and student-scale models improves performance as the smaller model's share increases. Second, reassigning rejects to other prompts and shuffling their code tokens still outperform length-matched gibberish, showing that task structure contributes to reject utility. Third, selecting candidates with lower likelihood under the reference policy improves net transfer when higher-likelihood candidates provide less useful contrast. Lower-likelihood selections outperform higher-likelihood ones for every source. These results suggest that effective rejects preserve task structure while limiting coupling to the reference policy, and that smaller frozen models can provide them at low cost.
