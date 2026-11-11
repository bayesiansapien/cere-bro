---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.323918+00:00
arxiv_id: 2611.11558
url: https://huggingface.co/papers/2611.11558
arxiv_url: https://arxiv.org/abs/2611.11558
date: 2026-11-10
---

# InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure

While Recursive Self-Improvement (RSI) accelerates isolated algorithm and kernel synthesis, distributed LLM training depends on tightly coupled launch settings, operator kernels, and communication schedules, where single edits often hit out-of-memory (OOM) boundaries, compiler conflicts, measurement jitter, or silent numerical drift. We present InfraRSI, the agentic harness that turns open-ended human commands into verified training optimizations via a five-stage workflow: init locks editable scope and a fixed task contract over workload, loss, and timing invariants to prevent reward hacking, doctor profiles baseline phases and calibrates cluster noise, run co-optimizes launch knobs and code patches before re-verifying top candidates against the baseline and logging findings to a cross-hardware experience bank, and report and apply audit source paths, track failed-trial costs, and commit promoted changes. Rather than stepping greedily from a single incumbent, InfraRSI initializes from diverse experience-seeded configurations and fits global execution-time and censored peak-memory models across all trials, including OOMs. Using these models, it prices per-setting memory costs, revises miscalibrated LLM priors from live runs, and pairs memory-hungry optimizations with memory savers and verified code patches. Across four single- and multi-node dense and Mixture-of-Experts (MoE) LLM workloads, InfraRSI achieves a speedup of up to 2.75times and lifts mean Model FLOPs Utilization (MFU) from 17.4% to 30.0%, outperforming existing tuners and coding agents while transferring experience across GPUs. As it improves training infrastructure efficiency, InfraRSI forms a two-level Recursive Self-Improvement loop---revising priors online within runs and distilling experience across clusters---to push foundation model scaling.
