---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.147918+00:00
arxiv_id: 2611.24102
url: https://huggingface.co/papers/2611.24102
arxiv_url: https://arxiv.org/abs/2611.24102
date: 2026-11-19
---

# IDEA: Intent-Dominance Evidence Audit for Inference-Time Backdoor Detection in GUI Agents

Organizations increasingly deploy downloaded open-weight GUI agents. A backdoored agent passes acceptance tests on clean data and misbehaves only when a visual trigger appears on screen, turning an unvetted checkpoint into a supply-chain risk. However, existing sample-level detectors target image classifiers and CLIP-style encoders, leaving step-level backdoor detection for GUI agents unaddressed. On clean steps, the instruction drives the action; when an unreferenced screen region hijacks the step, the instruction loses control over the decision state or that region dictates it instead. We term this signature intent--evidence dominance inversion and propose IDEA (Intent-Dominance Evidence Audit) to detect backdoor activation at inference time for each step without trigger knowledge or attack data. Specifically, Intent Counterfactual Probing (ICP) measures how far redirected instructions move the decision state, and Region Causal Audit (RCA) quantifies how far ablating a candidate region moves it. A gated conformal score compares both displacements against clean steps at the same distance from the clean manifold, providing a finite-sample false-positive guarantee. Extensive experiments on Qwen2.5-VL-3B across five attack families show that IDEA consistently detects backdoor activation under a controlled false-positive rate and outperforms state-of-the-art detection methods, while localizing the trigger region for every alarm and adding only modest inference overhead.
