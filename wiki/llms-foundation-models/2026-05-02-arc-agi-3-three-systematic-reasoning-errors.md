# ARC-AGI-3 — Three Systematic Reasoning Errors in Frontier Models

**Source:** The Decoder (covering ARC Prize Foundation analysis)
**Raw:** [raw/rss/2026-05-02-the-decoder-even-the-latest-ai-models-make-three-systematic-reasoni.md](../../raw/rss/2026-05-02-the-decoder-even-the-latest-ai-models-make-three-systematic-reasoni.md)
**URL:** https://the-decoder.com/even-the-latest-ai-models-make-three-systematic-reasoning-errors-arc-agi-3-analysis-shows/
**Date:** 2026-05-02
**Tier:** 2 — reasoning evaluation

## TL;DR

ARC Prize Foundation analyzed 160 game runs of GPT-5.5 and Opus 4.7 on ARC-AGI-3. Both stay below 1% on tasks humans solve without much trouble. Three systematic error patterns explain the gap.

## Why this matters

The ARC-AGI-3 sub-1% headline (Algorithmic Bridge #120, covered 05-03) had no mechanism. This piece names three specific patterns. In light of the Compliance vs Sensibility (05-02) finding that *reasoning mode is a steerable linear direction*, the obvious experiment is whether targeted activation steering on the failed patterns can move the needle. If reasoning-mode directions exist for induction/deduction/abduction (which CvS established), they may also exist for the three ARC-AGI-3 failure modes — and intervention could be the cheapest path to non-trivial progress on this benchmark.

## Connections

- **Compliance vs Sensibility (05-02)** — reasoning-mode-as-linear-direction is the candidate intervention substrate.
- **MIT Superposition (05-03)** — explains why these directions exist and become more separable at scale; predicts that the three error patterns might split apart at larger scale.
- **AISN #72 / Algorithmic Bridge (05-01)** — sub-0.5% headline, contextualized.
