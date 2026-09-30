---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.932788+00:00
arxiv_id: 2609.35279
url: https://huggingface.co/papers/2609.35279
arxiv_url: https://arxiv.org/abs/2609.35279
date: 2026-09-29
---

# Measuring Collapse and Correction in Homogeneous-Panel LLM Debate

Multi-agent large language model (LLM) debate is often evaluated by whether final answers improve, but movement is not necessarily improvement: the same discussion can rescue an initially wrong majority or destroy an initially correct one. Standard final-accuracy evaluations conflate these opposing mechanisms. We introduce an auditable protocol for homogeneous debate on multiple-choice questions (MCQs) that records each run as a transition ledger over collapse, correction, onset, and signed intervention utility. On 6,925 MMLU-Pro debates, the protocol identifies 253 collapses and a parallel correction ledger that changes how interventions should be judged. Replay experiments reveal the central tradeoff: a leave-one-model-out probe-gated freeze prevents 29 collapses but loses 108 corrections under equal weights, so collapse prevention alone can recommend the wrong policy. A compact pre-debate 8-probe screen is a triage signal: its unadjusted family-level association with conditional-collapse risk is high (G=7, Spearman rho=0.893, exact two-sided p=0.0123), but initial-majority accuracy is a close comparator (rho=0.821; family partial rho=0.767, p=0.0877), so we do not treat it as calibrated or capability-adjusted prediction. Round-level traces localize many collapses to the first debate round, where early disagreement can precede both harmful cascades and useful recovery. We release replayable schemas, coders, audits, cost cards, and zero-API rebuild scripts so future model-scaffold rows can be compared under the same denominators and signed utility ledger.
