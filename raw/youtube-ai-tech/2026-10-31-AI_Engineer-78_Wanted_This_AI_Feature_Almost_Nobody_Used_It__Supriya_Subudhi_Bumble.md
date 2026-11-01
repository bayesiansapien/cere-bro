# 78% Wanted This AI Feature. Almost Nobody Used It (Supriya Subudhi, Bumble)

**Channel:** AI Engineer
**Published:** 2026-10-31
**Source:** https://www.youtube.com/watch?v=CvmZtAPmAW4

## TL;DR
A Bumble PM's post-mortem on shipping AI Photo Feedback (LLM tips on dating-profile photos): for GenAI features, a positive A/B test is where the work starts. Five lessons. 78% of surveyed users said they wanted it, but only 10-15% used it. Positive averages hid bad tails (telling already-smiling users to "smile more"). The frontier model cost about 10x a simpler approach and didn't scale. Swapping to a cheaper model erased the lift, which showed the win came from the model, not the concept. Regulation kept it US-only. The most useful lesson for Amit: an A/B test on a GenAI feature measures the concept-model-prompt combination together, so model-cost routing has to be part of the experiment design, not done afterwards.

## Key Takeaways
- **Stated vs revealed demand:** 78% said yes in research and 10-15% adopted in the 50/50 test. Adoption rose only after the feature was moved into existing flows (offered at photo upload, and nudged when users hit a no-match wall).
- **Average win, tail failure:** more photos added and more profile edits overall, while specific outputs were wrong or harmful. Fixes: hard guardrails (never comment on uncontrollable traits such as skin colour or height) and reading real outputs through evals, sliced by gender, language and country.
- **Error tolerance depends on the domain:** a bad AI-DJ song is fine, a bad budgeting instruction is not. Set guardrail strictness to the cost of an error.
- **GenAI unit economics flip ML's:** classic ML is mostly upfront training cost with near-zero marginal cost. GenAI cost grows with success (users × frequency). Eval cost adds on top.
- **Model confound:** the cheaper model lost accuracy and the A/B lift went with it. After rapid eval-driven iteration on models and prompts, they landed on the "cheapest option that got the good result."
- **Regulatory scoping:** shipped in the US and stopped there. Decide early between a lowest-common-denominator global build and per-region variants.

## Architecture & Optimization Mechanics
- **This is a routing problem in disguise.** The A/B treatment arm was "frontier model + prompt," not "photo feedback." The right setup is a cost-quality sweep across model tiers on an offline eval set *before* the online test, then testing the cheapest model on the quality plateau.
- **Tail-aware evaluation:** score per segment (language, gender, photo type) and track worst-segment quality, not just the mean. A cheap model may match the frontier model on the mean while failing in French or on edge-case photos. That is where a router should escalate.
- **Multimodal cost lever:** most photo feedback is pattern-level (sunglasses in every shot, group photos, low light). A small vision classifier or quantized VLM could handle the common cases, with the frontier model only for ambiguous ones. The talk doesn't describe the final architecture.
- **Gaps:** no numbers for the final model, cost per user, adoption after the in-flow redesign, or eval agreement rates.

## Grounded Context (Web Enrichment)
Bumble announced two tools on February 26, 2026: Profile Guidance (bio/prompt feedback, global) and AI Photo Feedback (US-only). The photo tool flags things like over-reliance on sunglasses photos and recommends more varied images. Coverage confirms the US-only scope the speaker describes. Bumble has said basic versions will reach all users with advanced features later.

On regulation, the "can't ship globally" problem got only partly easier. The EU Digital Omnibus on AI (Regulation (EU) 2026/1744, in force July 27, 2026) pushed standalone Annex III high-risk obligations to December 2, 2027 and product-embedded ones to August 2, 2028. Prohibited-practice rules, GPAI rules and most Article 50 transparency duties were not delayed, and sources disagree on the watermarking date. A photo-feedback tool is unlikely to be high-risk, but transparency and GDPR biometric-adjacent processing still apply in the EU and UK. Her "think about compliance from day one" point still holds.

## Real-World Application / Actionable Step
- **Use this as a routing case study.** When advising product teams, insist on a pre-launch model sweep: 3-4 tiers (frontier, mid, small, quantized open-weight) × the same prompt × a segmented eval set. Plot cost against worst-segment quality and pick the knee before any A/B test.
- **Make the router's escalation signal segment-aware.** Route by input difficulty plus language and locale, since quality gaps between cheap and expensive models tend to grow in low-resource languages.
- **Report adoption-weighted ROI:** expected value = adoption × lift × (1 − tail-error cost) − inference cost. A 10-15% adoption rate makes a 10x model cost almost impossible to justify.
