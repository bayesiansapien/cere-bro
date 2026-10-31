---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.162975+00:00
arxiv_id: 2610.38174
url: https://huggingface.co/papers/2610.38174
arxiv_url: https://arxiv.org/abs/2610.38174
date: 2026-10-30
---

# Scaling Lean Theorem Proving for Real-World Code Verification

We present EasyProver, a Lean proving system built from recursive agents with isolated contexts, asynchronous search, parallel tactic probing, and an elastic elaboration service. Using an off-the-shelf frontier model with no additional training, it proves 669/672 PutnamBench problems and all six IMO 2026 formalizations and resolves 597/600 NTP4VC verification conditions and all 189 VERINA tasks by proof or refutation. Because these benchmarks are close to saturation, we also introduce Aegis, which converts competitive programming problems into much harder verification tasks over real implementations. The pipeline writes safe Rust solutions, translates them into Lean with Aeneas, generates specifications, and labels each frozen statement with a kernel-checked proof or refutation. It produces 2,045 differentially validated Rust-Lean program pairs and 11,533 candidate specifications. Unlike hand-written benchmarks, these tasks carry implementation-level obligations from fixed-width arithmetic, explicit failure, generated loops, casts, and functionalized mutation. On a stratified sample of 2,000 statements, EasyProver proves 1,054 (52.7%) within a 30-minute budget per statement. The same tasks can also be used to benchmark other provers and as rewards for reinforcement learning.
