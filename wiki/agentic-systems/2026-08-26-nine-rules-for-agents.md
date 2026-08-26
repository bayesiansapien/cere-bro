# Nine practical rules for agents doing real work (Gradient Flow)

**Source:** Ben Lorica, [Gradient Flow, "I keep hearing the same advice about agents"](https://gradientflow.substack.com/p/i-keep-hearing-the-same-advice-about) (2026-08-25) · [raw](../../raw/rss/2026-08-25-gradient-flow-i-keep-hearing-the-same-advice-about-agents.md)

---

## TL;DR

Lorica has been talking to teams building agents for production and reports that groups with unrelated products are independently arriving at nearly the same architecture. He writes the convergence down as nine rules. Most of them restate, in operational language, claims this wiki has recorded from papers. One of them supplies a genuinely new measurement: **the same open model showed an 18 percentage point spread between its best and worst harness configuration**, which Lorica singles out as the finding he would take most seriously when comparing models. The essay's through-line is that the reliability of an agent is a property of the software around the model, and that most of the engineering consists of *removing* the model's discretion rather than improving its reasoning.

---

## The nine rules, compressed

1. **Put hard constraints in software, not prompts.** A prompt is guidance and stays negotiable however firmly worded. Let the model handle ambiguity; put calculations in trusted code, permissions in policy systems, code validation in compilers and tests, and factual claims against authoritative sources. The diagnostic question: what can the model currently violate that ordinary software could prevent?
2. **Give only as much autonomy as the job needs.** Excess autonomy multiplies paths, errors, cost and governance burden. Start with a flexible workflow, watch which paths repeat reliably, and turn those into ordinary code. "A mature agent faces fewer open-ended choices over time, not more."
3. **Build around the domain's existing trusted process.** Support triage and medical diagnostic protocols already specify what to collect, when to escalate, what needs approval. Use that as the agent's structure instead of a generic plan-and-act loop. The best architecture "looks less like a general-purpose digital employee and more like the field's existing best practice made executable."
4. **Design for recovery, not a flawless first pass.** A system that is 95% reliable per step completes ten independent steps about 60% of the time, which is why a three-step demo dazzles and a real business process collapses. Add checkpoints, post-action verification, retries, reversible actions, resume-from-known-good. **Measure recovery separately from first-attempt accuracy.**
5. **Evaluate the model and harness as one system.** The 18-point spread. A leaderboard is a starting point; re-run the evaluation whenever either half changes, because changing either half means you are evaluating a new system.
6. **Keep multi-agent teams small, and protect a dissenter.** An orchestrator plus a few specialists, each with a distinct role, tool set, permission scope and minimum necessary information. Large swarms duplicate work and obscure failures. One role deserves protection: a **critic or breaker** with explicit criteria and authority to block or escalate.

(Rules 7 through 9 continue the same governance-and-observability line in the full post.)

---

## Relation to prior wiki pages

**Rule 5's 18-point spread is a new independent measurement of the swing that is [agent-harness-engineering](agent-harness-engineering.md)'s empirical spine, and it arrives from practitioners rather than a paper.** That page's core claim rests on omarsar0's preregistered benchmark (arXiv 2608.01347, 08-13): same model, same task, same prompt, move the work between two harnesses and cost-per-success swings **5x to 30x**. The capability twin came from AI4AI at Test-Time (08-13), where a strong builder model wrote an inference-time harness for a weaker target and average performance across four Theory-of-Mind benchmarks went **0.49 to 0.91 with the target's weights never touched**. DarwinX (08-14) then got **+7.7 points on Terminal-Bench 2.1 from the scaffold alone** with the model frozen. Lorica's 18 points on a fixed open model is a fourth data point, in accuracy units, from teams who were not trying to publish a harness result. The page's open problem 1 asks for a harness-quality metric that predicts the swing *before* you run it; this does not supply one, but it does confirm the swing is large enough that practitioners hit it by accident.

**Rule 1 and rule 2 are the practitioner statement of the mechanism finding this wiki considers the sharpest thing on that page.** [agent-harness-engineering](agent-harness-engineering.md) records that AI4AI's gains did *not* come from the target reasoning more or sampling more widely, which is what a better prompt would produce. They came from three moves: offloading unstable reasoning steps into deterministic code, routing per question type, and strict answer-format enforcement. All three **remove model discretion rather than adding model effort**. Spark-to-Paper (08-13) reached the same conclusion independently in a different subfield, with fabrication detection rising from 14% on a single-pass draft to 92% with a full integrity stack whose first design principle is separating model judgment from deterministic checkable operations. Lorica's rule 1 is that finding as an instruction: put hard constraints in software, not prompts. His rule 2's "turn the stable paths into ordinary code" is the same move applied over time. **The harness wins by taking decisions away from the model** now has research backing from two subfields and practitioner confirmation from a survey of production teams.

**Rule 4 is the reliability argument this wiki has been asking harness papers to make, and it names the right metric.** [Thinkingbox (08-25)](2026-08-25-thinkingbox-stateful-reliability.md), Microsoft's 507 policy-conditioned stateful business workflows evaluated against backend terminal state with executable checks that reject extra effects as well as wrong and missing ones, put the strongest model at **65.36% pass@1 and 25.25% pass^20** — a 40-point collapse between "can do it" and "does it reliably." Lorica's compounding arithmetic (95% per step over ten steps is 60%) is the back-of-envelope version of the same result, and his instruction to **measure recovery separately from first-attempt accuracy** is very close to open problem 0b on the harness page, which asks for a pass^k curve for a harness-optimized agent and notes nobody has published one. Today's two harness papers, [AutoSaddler](2026-08-26-autosaddler-harness-optimization.md) and [Recuris](2026-08-26-recuris-experiential-working-memory.md), both report single-attempt numbers. A practitioner essay and a Microsoft benchmark are both asking for a measurement that the Microsoft-led harness paper published the next day without.

**Rule 6's protected critic is the multi-agent finding.** [multi-agent-systems](multi-agent-systems.md) has recorded that larger agent teams often add coordination overhead rather than capability. The specific new prescription is the *authority* granted to the critic: explicit criteria plus the power to block or escalate, so dissent is structural rather than advisory. Set against the mind-viruses result (08-13), where evolved ideas propagated between agents and survived a context wipe because the payload rode the shared work product, a critic with blocking authority is also a containment mechanism and not only a quality one.

---

## Why this belongs in the wiki as a source rather than a bullet

The essay's value is not any single rule. It is that a survey of unrelated production teams independently reproduced the architecture that this wiki assembled from about fifteen papers over four months, including the harness-swing measurement, the discretion-removal mechanism, the recovery-over-accuracy metric, and small-team multi-agent design. [agent-harness-engineering](agent-harness-engineering.md) already argued that research and practitioners reaching the same frame in the same window was "the strongest possible confirmation that this is a real structural shift, not a hype cycle." This is that confirmation arriving a second time, from a different observer, with a fresh number attached.

---

## Related pages

- [Agent harness engineering](agent-harness-engineering.md)
- [Multi-agent systems](multi-agent-systems.md)
- [Agent benchmarks](agent-benchmarks.md)
- [Thinkingbox (08-25)](2026-08-25-thinkingbox-stateful-reliability.md)
- [AutoSaddler (08-26)](2026-08-26-autosaddler-harness-optimization.md)
