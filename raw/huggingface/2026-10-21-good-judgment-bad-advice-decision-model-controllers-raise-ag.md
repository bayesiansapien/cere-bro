---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.643271
arxiv_id: 2610.24649
url: https://huggingface.co/papers/2610.24649
arxiv_url: https://arxiv.org/abs/2610.24649
date: 2026-10-21
---

# Good Judgment, Bad Advice: Decision-Model Controllers Raise Agent Cost Without Improving Success

Agent scaffolds increasingly delegate small decisions (whether to stop, verify, or change approach) to cheaper models. We ask whether a typed decision model, Jev 1.13, consulted only at deterministic decision points, makes a Claude Sonnet 5.5 terminal agent cheaper without making it worse. In a pre-specified study on Terminal-Bench 2.1, we hold one agent loop fixed and vary only the controller: none, deterministic rules, a small LLM (Claude Haiku 5.5) answering the same questions, Jev, and a placebo that samples Jev's development-phase choice frequencies at the same moments. On 21 held-out tasks (315 trials), Jev raised cost per attempt by 19% (geometric-mean ratio 1.19, 95% CI 1.02-1.36) at an identical pass rate (73.0% vs. 73.0%). Jev was cheaper than the small-LLM controller (ratio 0.81) but 22% more expensive than the placebo, and no pass-rate difference between arms was detectable. Offline, Jev ranked finish requests better than the alternatives (AUROC 0.78 vs. 0.62 for rules and 0.60 for the small LLM) but was poorly calibrated: its mean probability that a run was complete was 0.50 when 87% of those runs passed, so it asked the agent to verify work that was already correct. No controller ever chose to abandon a run. Informative decision signals did not become useful interventions; we discuss what that would require.
