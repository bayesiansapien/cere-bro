---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.307072+00:00
arxiv_id: 2610.36544
url: https://huggingface.co/papers/2610.36544
arxiv_url: https://arxiv.org/abs/2610.36544
date: 2026-11-05
---

# Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors

Classification accuracy and true-positive and false-positive rates alone do not determine whether restarting an AI agent improves success. Using an exact alarm-to-action identity for an independent clean restart with zero monitoring overhead, we show analytically that a monitor with fixed 90% accuracy can swing from a five-percentage-point loss to a 35-point gain in success rate, depending solely on the replacement attempt's residual-budget success probability. We introduce two techniques for evaluating monitors and progress signals in decision terms. First, a decision-sufficiency criterion, a binary-action specialization of Blackwell's comparison of experiments, identifies which progress representations or context compressions preserve the information needed to choose optimally between the specified actions, independent of trace reconstruction fidelity. Second, a finite-sample, model-free decision audit uses simultaneous binomial intervals over existing agent traces, without additional model calls, to certify a preference for "restart" or "continue" under stated sampling assumptions, or return "abstain" when evidence is insufficient. In a study of 194 externally evaluated model executions on 19 selected SymPy issues from SWE-bench Verified, with a retrospective audit of 130 of these traces, we find a 2.29-point apparent restart gain traced to a single surviving failed attempt, a 42.29-point loss on a second model, no positive replication of the initial gain on prospective task cohorts, and zero of 103 live comparisons meeting the specified certification bar. These results motivate evaluating agent monitors through recovery opportunity, decision value, and statistical support, rather than classification performance alone.
