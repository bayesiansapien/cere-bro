---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.141713+00:00
arxiv_id: 2611.23751
url: https://huggingface.co/papers/2611.23751
arxiv_url: https://arxiv.org/abs/2611.23751
date: 2026-11-19
---

# Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow

Autonomous LLM agents incur substantial cost and latency by invoking a large model (System-2) at every step, even when many intermediate actions choose among a small set of known candidates. Existing dual-system agents offload such decisions to a lightweight System-1 model, but rely on workflow-specific hooks authored per environment. We present AnyS1, a framework that turns human-authored procedural skills, whose instructions naturally specify where choices arise and which options apply, into a shared, domain-general source of decision points. Offline, AnyS1 mines grounded enumerable decisions across over 1,000 public skills, gathers execution-grounded trajectory states inside isolated containers to construct Any-DP, and trains a single calibrated 4B pointer System-1 with label smoothing. At run time, compiled workflows resolve routine decisions in one forward pass and fall back to System-2 when confidence falls below a calibrated threshold. Across three unseen benchmarks and distinct System-2 model families, AnyS1 preserves task reliability while cutting episode cost by 75-91% and model-call time by 63-92% relative to an uncompiled System-2 agent, and maintains performance under zero-shot threshold transfer.
