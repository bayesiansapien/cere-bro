# Themis — Robust Multilingual Code Reward Models for Multi-Criteria Scoring

**Source:** HuggingFace Daily Papers
**Raw:** [raw/huggingface/2026-05-04-themis-robust-multilingual-code-reward-models-multi-criteria-scoring.md](../../raw/huggingface/2026-05-04-themis-robust-multilingual-code-reward-models-multi-criteria-scoring.md)
**arXiv:** https://arxiv.org/abs/2605.00754
**Date:** 2026-05-04
**Tier:** 2 — code reward modeling, post-training

## TL;DR

Themis is the first systematic attack on the "execution-feedback monoculture" in code reward modeling. Existing code RMs almost exclusively optimize for functional correctness, which constrains post-training to self-contained executable code only. The authors release **Themis-CodeRewardBench** (a benchmark across 5 preference dimensions × 8 programming languages), profile 50+ existing code/math/general-purpose RMs (most fail outside functional correctness), and release **Themis-CodePreference** (>350K preference pairs — the largest open-source code preference collection to date). The trained **Themis-RM** suite spans 600M to 32B parameters and shows positive scaling, strong cross-lingual transfer, and the necessity of multi-criteria training.

## Key claims

- Existing code reward models optimize ~one dimension (functional correctness via execution feedback). Themis-CodeRewardBench evaluates 5 dimensions across 8 languages.
- 50+ existing RMs profiled — strong on functional correctness, weak on the other four dimensions.
- Themis-CodePreference: >350K preference pairs, multi-criteria, multilingual.
- Themis-RM scaling from 600M to 32B; positive scaling on multi-criteria evaluation.
- Cross-lingual transfer: training on diverse-language preferences improves performance on under-represented languages.

## Why this matters (Tier 2)

Three threads converge here:

1. **The dimension-collapse problem from ViPO/Semi-DPO (05-02) reaches code.** Both 05-02 papers argued that collapsing multi-dimensional preferences to binary labels produces conflicting gradients. ViPO's fix was better data; Semi-DPO's fix was treating conflicting pairs as noisy. Themis is the code-domain version of the same diagnosis: functional-correctness-only is a single-dimension reduction; multi-criteria training is the cure. **This is the third paper in three weeks naming the same root cause.**
2. **Code RMs gate everything in agentic coding.** SWE-Bench, Aider, and Xiaomi MiMo-V2.5-Pro (05-03) all depend on a code reward signal during RL post-training. If the reward signal optimizes only correctness, agents miss style, idiomaticity, security, maintainability, performance — exactly the dimensions Marcus (05-02) and Armin Ronacher (Pi/Pragmatic Engineer 04-29) flagged as the "vibe slop" problem.
3. **Open-source preference data scale.** 350K pairs is a structural infrastructure release, not just a paper. Pairs with ViPO's 1M visual-preference set (05-02) — the open-source preference-data ecosystem now spans visual quality and code multi-criteria.

## Connections to prior wiki pages

- **ViPO (05-02)** + **Semi-DPO (05-02)** — same root-cause diagnosis (multi-dim preferences collapsed to binary → conflicting gradients), now extended to code.
- **CoPD Co-Evolving Policy Distillation (05-01)** — uses code reward signals; could pair Themis-RM with CoPD for multi-criteria distillation.
- **C2 Rubric Reward Modeling (04-18)** — earlier rubric-based reward modeling thread; Themis is the code-specific instantiation.
- **Marcus on 80% AI code (05-01)** + **Armin Ronacher / Pi (04-29)** — the qualitative problem statement Themis turns into a measurable benchmark.
- **GFT/SFT as degenerate RL (04-21)** — multi-criteria reward shaping is exactly the SFT-vs-RL boundary this paper investigates.

## Research angles

- **Themis-RM × CoPD distillation pipeline.** Use Themis-RM as the multi-criteria reward inside CoPD's policy-distillation loop. The natural follow-up paper.
- **Cross-domain dimension generalization.** ViPO (visual quality), Semi-DPO (visual quality), Themis (code multi-criteria) — does the same multi-criteria scaling pattern hold for math, scientific reasoning, dialogue? A dimension-aware DPO theory would generalize across.
- **Reward-hacking under multi-criteria.** Wang & Huang's reward-hacking-as-structural-equilibrium (Defense Trilemma post 05-02) predicts that adding criteria expands quality dimensions combinatorially and increases reward hacking. Themis tests this empirically: do multi-criteria-trained models reward-hack *less* (because more dimensions are covered) or *more* (because more dimensions are gameable)?
