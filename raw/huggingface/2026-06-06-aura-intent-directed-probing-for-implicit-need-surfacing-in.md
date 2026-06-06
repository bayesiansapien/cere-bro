---
source: farmer/huggingface
farmed: 2026-06-06T09:05:36Z
arxiv_id: 2606.05557
url: https://huggingface.co/papers/2606.05557
arxiv_url: https://arxiv.org/abs/2606.05557
date: 2026-06-06
---

# AURA: Intent-Directed Probing for Implicit-Need Surfacing in Situated LLM Agents

A situated query like "where is Lin Wei?" often encodes more than its literal content: the user may also want to know whether Lin Wei is free, in a good mood, or worth interrupting now. Standard tool-use agents answer the literal question and stop. AURA inserts an inference step between scene perception and tool use that produces an IntentFrame: a structured estimate of the implicit need with a scalar gap score that controls per-query probe budget and tool selection. On a 100-query four-scene implicit-intent benchmark, AURA improves implicit-need coverage over ReAct-style probing (Delta = +0.07, p < 10^-6); three of four scenes are individually significant, the gain reproduces on a second backbone, and a prompt ablation attributes the lift to gap calibration rather than answer memorisation. On factual lookup the controller trades raw accuracy for 82% fewer probes and zero forbidden-tool violations on a privacy-sensitive slice; scope conditions are detailed in Limitations. Code, simulator, and benchmark are released at https://github.com/innovation64/AURA.
