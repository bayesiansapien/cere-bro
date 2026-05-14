---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.10365
url: https://huggingface.co/papers/2605.10365
arxiv_url: https://arxiv.org/abs/2605.10365
date: 2026-05-13
---

# Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values

Autonomous agents have rapidly matured as task executors and seen widespread deployment via harnesses such as OpenClaw. Safety concerns have rightly drawn growing research attention, and beneath them lie the values silently steering agent behavior. Existing value benchmarks, however, remain confined to LLMs, leaving agent values largely uncharted. From intuitive, empirical, and theoretical vantage points, we show that an agent's values diverge from those of its underlying LLM, and the agentic modality further introduces dataset-, evaluation-, and system-level challenges absent from text-only protocols. We close this gap with Agent-ValueBench, the first benchmark dedicated to agent values. It features 394 executable environments across 16 domains, offering 4,335 value-conflict tasks that cover 28 value systems and 332 dimensions. Every instance is co-synthesized through our purpose-built end-to-end pipeline and curated per-instance by professional psychologists. Each task ships with two pole-aligned golden trajectories whose checkpoints anchor a trajectory-level rubric-based judge. Benchmarking 14 frontier proprietary and open-weights models across 4 mainstream harnesses, we uncover three concerted findings. Agent values first manifest as a Value Tide of cross-model homogeneity beneath interpretable counter-currents. This tide bends non-additively under harness pull, and yet more decisively under deliberate steering via embedded skills. Together these results signal that the agent-alignment lever is shifting from classical model alignment and prompt steering toward harness alignment and skill steering.
