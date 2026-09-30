---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.932856+00:00
arxiv_id: 2609.32821
url: https://huggingface.co/papers/2609.32821
arxiv_url: https://arxiv.org/abs/2609.32821
date: 2026-09-29
---

# Routing Drift Alone Does Not Diagnose Failure in Merged MoE LLMs

Model merging efficiently combines specialized large language models (LLMs) without joint retraining, but can substantially alter expert routing in Mixture-of-Experts (MoE) models. Such routing drift is often interpreted as routing failure, raising a fundamental question that remains unclear: does routing drift after MoE merging actually indicate routing failure, and what evidence should justify repair? We investigate these questions across DeepSeekMoE, OLMoE, and Qwen3-MoE proposing a routing analysis toolkit for controlled counterfactual interventions and token-level analysis. By crossing source and merged router inputs and parameters, we attribute most expert reassignments to input shifts rather than parameter changes at the same layer. However, source-relative routing differences poorly predict next-token likelihood gains from source-route restoration, and different expert selections can produce directionally similar mixture outputs. We therefore operationalize routing failure as task loss recoverable under a specified routing intervention, with non-routing parameters fixed. These tests detect recoverable loss under deliberate router corruption, whereas source-route restoration does not establish reliable task benefits in the evaluated merged models. Motivated by these, we propose Selective Router Repair (SRR) as a case study, and find that source-specialist token-likelihood advantages do not reliably identify beneficial local corrections. Together, these findings show that routing drift alone is insufficient evidence of routing failure: source-informed corrections must be judged by their task-level intervention effects. The analysis toolkit and SRR code are released.
