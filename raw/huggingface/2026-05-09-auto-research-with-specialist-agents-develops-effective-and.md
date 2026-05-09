---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.05724
url: https://huggingface.co/papers/2605.05724
arxiv_url: https://arxiv.org/abs/2605.05724
date: 2026-05-09
---

# Auto Research with Specialist Agents Develops Effective and Non-Trivial Training Recipes

We study auto research as a closed empirical loop driven by external measurement. Each submitted trial carries a hypothesis, an executable code edit, an evaluator-owned outcome, and feedback that shapes the next proposal. The output is an auditable trajectory of proposals, code diffs, experiments, scores, and failure labels. We instantiate this loop with specialist agents that partition recipe surfaces and share measured lineage across trials. Across 1,197 headline-run trials plus 600 Parameter Golf control trials, humans did not choose proposals, edit recipes, override scores, or repair failed trials during the search. The loop reduces Parameter Golf validation bpb by 0.81%, raises NanoChat-D12 CORE by 38.7%, and reduces CIFAR-10 Airbench96 wallclock by 4.59%.
