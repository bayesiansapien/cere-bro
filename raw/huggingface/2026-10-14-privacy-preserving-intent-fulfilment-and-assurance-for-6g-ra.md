---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.513784+00:00
arxiv_id: 2607.08809
url: https://huggingface.co/papers/2607.08809
arxiv_url: https://arxiv.org/abs/2607.08809
date: 2026-10-14
---

# Privacy-Preserving Intent Fulfilment and Assurance for 6G RAN

Intent-based network management automates 6G service lifecycles, but existing fulfilment and assurance approaches require traffic inspection, per-flow tracking, or vendor-internal telemetry. These requirements conflict with privacy constraints in multi-tenant networks and vendor opacity in O-RAN deployments. We present an architecture that provisions resources from declared intent categories without traffic inspection and verifies fulfilment using only cell-level standardised PM counters at the O1 interface. A data-processing inequality bounds resource-allocation leakage about traffic content by log_2 K bits for K categories. Intent-traffic unlinkability and node-opaque verification hold by construction. If verification requires at least q cells per category among M cells, the ceiling becomes log_2 lfloor M/q rfloor bits. This bound covers the category/resource channel, not total inference from PM counters. When individual records add state-independent noise to the category aggregate, the category-mean verifier is at least as powerful as any per-agent verifier. We map the architecture to the 3GPP intent lifecycle and O-RAN Non-RT RIC. On production PM data from four operator networks, the category-mean score has higher AUC on three networks and comparable AUC on the fourth under category-wide replacement, while per-cell screening suits sparse faults. These injection-based experiments do not establish the theorem's observation premise. Within-period cell co-movement limits a category mean to the evidence of 6 to 14 independent cells, and category-level verifiers need per-category calibration.
