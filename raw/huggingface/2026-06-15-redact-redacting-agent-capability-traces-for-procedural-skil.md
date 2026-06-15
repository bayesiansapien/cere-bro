---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.10813
url: https://huggingface.co/papers/2606.10813
arxiv_url: https://arxiv.org/abs/2606.10813
date: 2026-06-15
---

# RedAct: Redacting Agent Capability Traces for Procedural Skill Protection

Users rely on execution traces to observe agent behavior, diagnose failures, and ensure accountability. These traces contain rich procedural detail, including tool invocations, intermediate decisions, and error-recovery logic. Yet this detail can expose private procedural skills, allowing downstream methods to recover key formulas, thresholds, and strategies without access to model weights or skill files. To quantify this risk and evaluate protection, we construct CapTraceBench, a benchmark of 75 specialized long-horizon tasks and 154 curated skills across seven domains. We also introduce RedAct https://github.com/XuShuwenn/RedAct, a protected trace release framework that localizes protected key information, rewrites traces while preserving verifier-critical evidence, and embeds behavioral watermarks for downstream provenance analysis. Across representative trace reuse methods, RedAct reduces normalized skill transfer (NST) from 44.7--67.1% on raw traces to below the no-skill baseline, while preserving audit evidence. Its standalone behavioral watermarks reach 93.6--100.0% true detection with a false alarm rate of at most 1.9%. These results frame public agent traces as security interfaces and show that selective redaction can reduce procedural capability leakage without removing audit evidence.
