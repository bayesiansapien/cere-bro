---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.18890
url: https://huggingface.co/papers/2610.18890
arxiv_url: https://arxiv.org/abs/2610.18890
date: 2026-10-16
---

# AI-Driven, Timing-Aware Power Optimization

Post-route power recovery changes cell choices under tightly coupled timing, electrical and physical constraints, and the value of each change depends on what it costs to repair its side effects. We propose an AI-driven framework in which a learned model drives both phases of the optimization: it ranks the powerrecovery edits to try and the repair actions that follow, while deterministic electronic design automation (EDA) analyses govern every acceptance. The framework records baseline constraint margins, identifies the damage a recovery transaction introduces in each analysis view, holds pre-existing violations at their baseline rather than working them inside the power step, and caps repair spending at a fraction of the measured saving. An ensemble of gradient-boosted models predicts power change, normalized damage reduction and constraint-regression risk from action and timing-context features available before each trial; calibrated, conservative estimates feed separate acquisition scores for recovery and repair, with a deterministic fallback when the model is uncertain. Recovery and repair remain speculative until physical implementation and fresh analysis establish baseline preservation and positive net saving. We specify the contract, the learned policy, the transactional flow and a pre-registered public evaluation protocol on open designs. Evidence from a companion study on public designs supports the contract; the learned policy is proposed, and no trained-model results or proprietary design measurements are reported.
