# Voice AI Where One Wrong Question Breaks the Rules (Shiv Indap, Upstart & Brooke Hopkins, Coval)

**Channel:** AI Engineer
**Published:** 2026-10-31
**Source:** https://www.youtube.com/watch?v=3osCbSufv8g

## TL;DR
Upstart (fintech lending) automated income/use-of-funds verification calls for the ~10% of applicants not instantly decisioned, in a setting where one wrong follow-up question (e.g. asking the amount after a borrower says "medical") is a regulatory violation, not a UX bug. The headline number: their LLM-as-judge compliance metric agreed with human reviewers only **33%** of the time at launch and **92%** now. The gains came from turning tribal knowledge into rules, resolving human-vs-human disagreement, and then improving the judge. Coval (founded by Waymo's ex-eval-infra lead) supplies the loop: score every call, route flagged calls to human queues, cluster for unknown failures, re-simulate fixes voice-to-voice, and ship behind feature flags.

## Key Takeaways
- **Use case:** 3 questions (income continuity for 3 months, use of funds, outstanding obligations like alimony or garnishment) after identity verification. Conditional branches are compliance-bound: "medical" means never ask the amount, and "graduation" means you must ask whose graduation.
- **Scope discipline:** the agent must refuse adjacent questions (loan status, timing) politely. Compliance wanted a narrow agent.
- **Ops evolution:** Google Sheet review went from 5 to 15+ ad-hoc columns and became unusable, so they moved to structured review queues.
- **Metric pruning:** started broad and settled on accuracy, clarity, completeness, policy alignment, correct escalation and CSAT. "Don't be attached to your metrics."
- **Judge alignment 33% to 92%:** in order, (1) encode undocumented tribal knowledge into the agent, (2) fix disagreement *between human reviewers*, (3) improve the judge prompt using expert feedback.
- **Eval taxonomy (Coval):** outcome (did it finish), process (did it follow required steps), quality (conversation experience). Metric types: LLM judge, heuristics, audio processing.
- **Derive metrics from human labels**, not the reverse. Starting from WER produces numbers nobody acts on.
- **Self-healing loop:** agents propose fixes from eval data (and RL/fine-tuning later), but every change is feature-flagged and human-approved. Compliance signs off on compliance-relevant behaviour.

## Architecture & Optimization Mechanics
- **Judge-as-router for human attention:** with thousands of calls a day, the LLM judge's main job is triage, sending only flagged calls to humans. Its precision sets human cost and its recall sets regulatory risk. At 33% agreement the triage was noise.
- **Label quality caps judge quality:** you can't push judge-human agreement above human-human agreement. Fix the rubric first. The same applies to eval sets used for compression and quantization regressions.
- **Unknown-unknowns via clustering:** embedding and anomaly detection over transcripts finds failure modes no metric covers, the same as long-tail mining in AV simulation.
- **Shift-left simulation:** voice-to-voice synthetic callers (accents, noise, interruptions) replay failure cases before redeploy. This is the gate that makes swapping to a cheaper or quantized model safe.
- **Missing:** no latency or cost figures, no model names, no judge model size, no false-negative rate on compliance violations, which is the number that matters most.

## Grounded Context (Web Enrichment)
Coval raised a $28M Series A in June 2026 (Norwest lead, with Base10, Twilio Ventures and YC) and reports 60+ customers including Zoom and Deepgram. Its product pages describe the identity-verification scenario generation and regulation-scored transcripts (HIPAA, PCI-DSS, FDCPA) shown in the talk. Upstart's use of Coval could not be independently confirmed beyond this talk.

The 33% to 92% story fits current judge research. A June 2026 preprint finds LLM-LLM agreement (r ≈ 0.35) exceeds LLM-human agreement (r ≈ 0.27-0.32), and that only calibration on a small human-anchored set closes the gap. Practitioner consensus in 2026 is to measure human-human agreement first and treat it as the ceiling, reporting Cohen's kappa rather than raw percent agreement. Upstart's "92% agreement" is raw agreement on a likely imbalanced yes/no label (most calls are compliant), so it may hide a weak recall on actual violations. Ask for kappa and per-class recall before treating it as a benchmark.

## Real-World Application / Actionable Step
- **Before trusting any LLM judge in a routing or compression eval,** measure human-human agreement on 100-200 items, then judge-human kappa and recall on the minority (failure) class. Report all three.
- **Make "safe to downgrade" a simulation gate.** When routing traffic to a smaller or quantized model, replay the flagged-failure set (compliance-style hard cases) and require zero regressions on violation recall, not just mean quality.
- **Use the judge as a router for human attention:** tune its threshold for violation recall ≥ 0.95, accept lower precision, and measure reviewer hours saved. This is a clean, quantifiable deployment pattern for a small fine-tuned judge model instead of a frontier one.
