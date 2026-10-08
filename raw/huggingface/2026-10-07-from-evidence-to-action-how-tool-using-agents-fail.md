---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.07753
url: https://huggingface.co/papers/2610.07753
arxiv_url: https://arxiv.org/abs/2610.07753
date: 2026-10-07
---

# From Evidence to Action: How Tool-Using Agents Fail

Tool-using agents make consequential changes to external state, yet correct outcomes do not guarantee that their actions were supported by evidence established beforehand. We study where this evidence-to-action chain breaks as agents move from deciding whether to act to executing single actions and dependent workflows. Across ten model-harness configurations, strong static action assessment can coexist with much weaker interactive execution. Failures often begin before execution: agents stop with incomplete investigation or act before required evidence is established. Once required evidence is obtained, single-action execution is usually reliable, while multi-action workflows additionally expose unresolved prerequisites and incomplete execution. For this analysis, we introduce SafeActBench, comprising 656 cases across six operational domains and five protocols that progress from static action judgment and investigated non-action to single- and multi-action workflows. A provenance-bound Evidence Ledger and deterministic trajectory evaluator track what information was established, when actions occurred, and whether downstream dependencies were satisfied. These results show that failures arise not only from missing information, but also from how agents use established evidence when deciding and executing actions.
