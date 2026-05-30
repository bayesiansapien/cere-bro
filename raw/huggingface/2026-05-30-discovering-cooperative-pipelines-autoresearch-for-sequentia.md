---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.30003
url: https://huggingface.co/papers/2605.30003
arxiv_url: https://arxiv.org/abs/2605.30003
date: 2026-05-30
---

# Discovering Cooperative Pipelines: Autoresearch for Sequential Social Dilemmas

We study two-level autoresearch for cooperation: an outer-loop AI agent autonomously redesigns the inner-loop pipeline of an LLM policy-synthesis system for multi-agent Sequential Social Dilemmas (SSDs). A researcher agent R (run as a coding agent) reads the inner-loop source code, edits system prompts, feedback functions, helper libraries, and iteration logic, runs evaluations, and decides what to keep, following the autoresearch paradigm. Across two games (Cleanup and Gathering), two policy-synthesizer LLMs, and two welfare objectives (utilitarian efficiency and Rawlsian maximin), the researcher reliably exceeds hand-designed baselines, sharply tightens run-to-run variance, and outperforms prompt-only optimization. The discovered pipelines are objective-dependent: only under maximin does the researcher inject an explicit fairness mechanism into synthesizer pipelines, a class of mechanism that is absent from its own objective-agnostic system prompt and from every efficiency-optimized pipeline. This supports an information-design reading in which the researcher chooses what to reveal to the boundedly rational synthesizer as a function of the welfare objective. Code at https://github.com/vicgalle/autoresearch-social-dilemmas.
