---
source: farmer/huggingface
farmed: 2026-08-08T23:44:03.927649
arxiv_id: 2608.05784
url: https://huggingface.co/papers/2608.05784
arxiv_url: https://arxiv.org/abs/2608.05784
date: 2026-08-08
---

# Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and Replay

Computer-use agents pay full frontier inference to re-derive routines their user has already performed, because an agent's memory today records what the user said, not what the user did. We compile passively captured screen activity into agent memory with a deterministic, zero-model pipeline: it segments a local capture stream into typed activity frames, bounded episodes carrying application, site, timing, input volume, and evidence pointers back to the raw rows, with no model in the loop, so the output is byte-identical, cacheable, and mechanically auditable. On one professional's single-user corpus of 128,756 frames over 51 active days, the compiler reduces a day of raw capture to a prompt-ready context block 86x smaller in 68 ms, and an agent reading that block answers questions about the day at 98.4% accuracy (Wilson 95% CI 91.7-99.7%) against an independent oracle, versus 66-80% for an LLM summary of the same capture, a mid-tier model reading the block matching a frontier one.
  The same compiler doubles as a demand-side cost instrument. Read off passive, pre-delegation human activity rather than agent rollouts, it supplies two parameters that agent-cost models assume but, to our knowledge, have not measured: the Routine Overhead Ratio R and the routine recurrence h. We report first values of R, a modeled upper bound, at 60-343x, and a delegable recurrence of 9.0% in-sample and 7.7% out-of-sample, for a realistic all-fleet token ceiling near 8%; a compiled routine replays deterministically with the model out of the loop, demonstrated live at zero model tokens on a guard-matched hit. Schema, compiler, and evaluation harness are open.
