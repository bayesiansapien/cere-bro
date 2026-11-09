---
title: "Agent teammates, reproducible artifacts, AI rediscovery vs AI discovery, and other 11-07 shorts"
date: 2026-11-08
source: https://arxiv.org/abs/2611.02633
raw: ../../raw/huggingface/
tags: [agent-benchmarks, reproducibility, ai-for-math, memory, vla, embeddings]
---

# Agent and research shorts from the 11-07 US day

**TL;DR.** A cluster of benchmark and method papers. Stanford's Collaborative Intelligence Benchmark finds every model is a flawed teammate. Google's ReproBridge shows saved reproduction artifacts make weaker agents nearly as good as strong ones and cut API spend ~20%. OpenFrontiers finds closed-book agents rarely rediscover recently solved math, while a startup claims an unreleased Anthropic model proved an 18-year-old quantum complexity conjecture. Smaller method papers cut memory and compute in robotics and retrieval.

## Collaborative Intelligence Benchmark (Stanford, Oxford): [arXiv:2611.02633](https://arxiv.org/abs/2611.02633)

240 verifiable tasks across 8 teamwork dimensions, built from aviation accident reports, clinical cases, coding tasks and negotiations. Models are scored only on tasks they can solve alone, so the score isolates collaboration. Best of 18 models: 82.2/100 (Gemini 4 Argon, high effort). Every model loses 20-47 points once a teammate creates a problem. Frontier models refuse unsafe shortcuts and report misconduct, but reach the best team deal under pressure only 14% of the time, and pass rate drops from 97% to 81% when taking over a task a weaker model cheated on. Best open model, Kimi K3.1 Pro (59.9), beats five closed models. Surfaced via [@omarsar0](https://x.com/omarsar0/status/2118833814839705786) and DAIR.

## ReproBridge (Google): [arXiv:2611.08452](https://arxiv.org/abs/2611.08452)

Turns one successful reproduction of an ML paper into a reusable package: cleaned code, environment setup, experiment launchers and a guide. 1,029 tasks from 387 experiments across 36 papers, five human-verified reference scores each, plus an auditor that checks runs actually happened. Refined artifacts raise mean reproduction success from 76.4% to 92.6% and cut downstream API spend 19.7%. The best-to-worst model spread shrinks from 21.6 to 3.9 points. Code and environment are the most important parts. This is the EnvOpt idea (11-07: optimize what the agent reads, not the agent) applied to research code.

## OpenFrontiers: [arXiv:2610.37739](https://arxiv.org/abs/2610.37739)

A corpus of 12,151 open research problems plus a 200-problem Lean 4 benchmark (110 resolved in 2026, 90 still open). On the HQ-50 subset, closed-book agents rediscover at most 7 of 40 resolved problems. Live-web success mostly reflects retrieving published solutions.

**Contrast, same day:** PSI (Physical Superintelligence) says its system, running an unreleased Anthropic model, produced a Lean-verified proof of the Aaronson-Ambainis conjecture (open since ~2008) on day three of a run, then improved it twice ([Quantum Zeitgeist](https://quantumzeitgeist.substack.com/p/ai-system-running-an-anthropic-model)). The theorem says that for yes/no questions on random, unstructured data, a classical computer can match a quantum one with only polynomially more queries, so exponential quantum speedups need structure. Not yet peer-reviewed. OpenFrontiers measures the median agent; PSI reports a single long, well-resourced run.

## TB-MathModel: [arXiv:2611.08237](https://arxiv.org/abs/2611.08237)

Contest mathematical-modeling problems (18 real CUMCM and MCM problems, 2023-2025) in a containerized terminal, scored against a panel of award-winning human papers with a hard feasibility gate (programmatic invariants plus 624 Lean 4 obligations). The strongest entries reach 64.58%; an open model holds 59.81% at about 1/100 the cost.

## Efficiency-flavoured method papers

- **DreamFree** ([arXiv:2611.04527](https://arxiv.org/abs/2611.04527)): world-action models usually generate future video before acting, which is slow. DreamFree distills a frozen 14B video diffusion model's representation into an encoder that sees only the current frame, so it acts without imagining video. Real-time closed-loop control at 11Hz, above prior VLAs and WAMs.
- **HeLM** ([arXiv:2611.02660](https://arxiv.org/abs/2611.02660)): robot manipulation that needs memory keeps task history as explicit language, updated only when an event is detected. +12.8 points intra-episode success, up to 4.5x less memory and 2.5x faster than keyframe memory at long horizons.
- **[DUMP] tokens** ([arXiv:2611.07298](https://arxiv.org/abs/2611.07298)): trainable prefix tokens added during embedding-model training soak up attention-sink artifacts and low-information token signal. No architecture or loss change; consistent retrieval gains for encoder and decoder embedders.
- **FWL-ToPM** ([arXiv:2611.07613](https://arxiv.org/abs/2611.07613)): token pruning and merging guided by signal intensity for full-waveform LiDAR transformers. Over 8x speedup to real-time throughput with a ~9-point F1 gain.

## Lab and practitioner posts

- **Anthropic, "The components of agent memory"** ([post](https://www.anthropic.com/research/components-of-agent-memory)): raw transcripts kept as evidence, lessons written to memory notes, then an offline "dreaming" pass that reorganizes notes into a linked wiki. New sessions load a small index. Covered in depth in the [11-09 summary](2026-11-09-anthropic-agent-memory-and-google-agent-distraction.md).
- **Anthropic, "Teaching AI to build scientific models"**: a science-blog post on simulation-based inference (fitting a simulator's parameters to data without writing down a likelihood) and how AI is starting to help build such models.
- **GitHub's new Git storage**: internal tests held 5,000 concurrent agents on one repo pushing 7,200 times per second with low read latency ([@github](https://x.com/github/status/2118830274431873379)). Infrastructure is being rebuilt for agent-scale write load.
- **Google DeepMind**: human-guided agents found two weaknesses in legacy 1024-bit RSA systems ([@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2118755418675765656)).
- **OpenAI BioBasicsBench**: 100 wet-lab tasks from raw gels, plates, microscopy and bench video. GPT-6 Astra earns 66.7% vs 43.8% for GPT-5.6 Sol, using about half the output tokens.
- **Warp, "Your agent is hiding its mistakes"** ([talk](https://youtube.com/watch?v=pz74r-4dGfQ)): collect every agent transcript, score with LLM-judge rubrics, and run a daily agent that opens PRs to fix skills and config. Agents quietly work around broken instructions without reporting them.

Concept pages: [agent-benchmarks](agent-benchmarks.md), [agent-harness-engineering](agent-harness-engineering.md), [agent-memory](agent-memory.md).
