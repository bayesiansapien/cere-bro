---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.223825+05:30
arxiv_id: 2610.19820
url: https://huggingface.co/papers/2610.19820
arxiv_url: https://arxiv.org/abs/2610.19820
date: 2026-10-15
---

# ActionOPD: Distilling Decisions, Not Tokens

Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a fundamental question: at which states and at what granularity should this alignment be performed? Offline imitation provides dense but token-specific supervision and can suffer from state-distribution mismatch. Token-level on-policy distillation (OPD) addresses this mismatch but typically requires teacher token probabilities and compatible tokenization. We argue that semantic actions provide a natural unit of supervision for agent distillation. We introduce ActionOPD, an action-level on-policy distillation method motivated by maximizing expected teacher-action likelihood at student-encountered states. At each such state, ActionOPD samples actions from both the student and a black-box teacher, rewarding student actions according to their semantic agreement with the sampled teacher actions. Through policy optimization, ActionOPD aligns the student's action-level behavior with the teacher's decisions without requiring reproduction of teacher-written reasoning or access to teacher token probabilities. Training Qwen3-4B and Qwen3-8B with two teachers on diverse, curated tool-use tasks yields average gains of 3.3-6.9 percentage points across four out-of-distribution benchmarks. ActionOPD scales favorably with student size and teacher capability, without requiring the teacher and student to share a model family or tokenizer. On τ^2-bench, ActionOPD achieves competitive performance against offline distillation and token-level OPD. We further explore Self-ActionOPD with a same-model teacher and privileged context. These results establish ActionOPD as a promising approach to agent distillation.
