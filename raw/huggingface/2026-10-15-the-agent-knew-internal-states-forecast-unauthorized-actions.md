---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.235308+05:30
arxiv_id: 2610.17301
url: https://huggingface.co/papers/2610.17301
arxiv_url: https://arxiv.org/abs/2610.17301
date: 2026-10-15
---

# The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow

Language-model agents sometimes act beyond their authorization and then misreport what they did. On CAPE-Bench, matched agent tasks in which one fact decides whether an action is authorized, frontier open-weight agents do both, and one behavior marks the lie: retroactive permission laundering, acting and then asking permission as if the action were pending, precedes a false report in 70% of 1081 fresh informed violations, against 8% otherwise (preregistered odds ratio 7.0); frontier agents on tau^2-bench instead fabricate the authorization before violating. A linear readout of the agent's residual stream forecasts the violation before the action (AUROC 0.94) and the false report before the report, and beats chain-of-thought monitors when the agent is pressured to hide its reasoning. Gating every proposed action on this forecast cuts violations over whole episodes in four model families, and sending repeated flags to an approver keeps authorized work (Gemma-4: violations 0.70 -> 0.09, completion 1.00; a model approver that escalates unclear cases keeps this gain with a person seeing 25% of asks), at about 10-8 of the agent's compute and 109 times less than a chain-of-thought monitor. On AgentDojo, an external prompt-injection benchmark, the same readout calibrated on 29 tasks, with the steering unchanged, cuts attack success on unseen tasks in two families (Gemma-4 11.7% -> 5.7%, gpt-oss 28.5% -> 17.5%) while keeping benign utility (Gemma-4 0.637 vs 0.637; gpt-oss 0.667 vs 0.681). Preventing the violation is also the most reliable way to prevent the lie (misreported violations 0.10 -> 0.01 pooled over three families, preregistered), whereas lie-specific fixes after a violation are weak. All tests are preregistered and hash-locked; code, data and the full record, including tests that did not pass, are at https://github.com/AryaFayyazi/Honesty.
