# Reliable, Smart Workflows for Finance, Wealth and Insurance (Karthic Rao, Perpetual)

**Channel:** AI Engineer
**Published:** 2026-10-12
**Source:** https://www.youtube.com/watch?v=8g0g1ncwzG0

*Note: the available transcript was an Arabic dub/translation, not the original English audio. Numbers and structure below are from that translation.*

**Secondary domain:** finance (wealth-management operations)

## TL;DR
Perpetual's CTO argues that "more agency vs more rules" is the wrong question for regulated workflows. The right question is where the boundary sits: determinism owns control flow, evidence, and side effects, and the model owns only interpretation and judgment. Their engine has a model-based planner translate a request into a typed semantic graph, then a model-free 11-stage compiler checks it against 42 typed action contracts and emits an immutable, hash-pinned plan (or fails closed). A state machine executes it, calling a model only for small typed judgments. About 95% of those judgments are designed to run on a flash-class model, and every frontier-model decision is logged and human-confirmed so it becomes training data to shrink the frontier share further. This is the most rigorous version of the "workflows, not autopilot" thesis in this AIE batch, and it is effectively a static router plus a built-in distillation flywheel.

## Key Takeaways
- **Four constraints of finance workflows:** complex enough to need runtime strategy (cannot pre-script every path), sensitive data (need a path to fully privately hosted models), policy violations have serious consequences, so execution must be highly reliable and deterministic.
- **Contrarian to lab messaging:** labs push token consumption. In regulated work, maximizing tokens is the wrong objective. Most steps are near-deterministic and just follow the next edge of a large state machine.
- **Worked example, "fill out a W-9 for Mr. Harper":** three Harper families (disambiguation), W-9 vs W-8 branch for foreign persons, single tax-classification box, LLC letter, SSN vs EIN from a verified document (never from memory), exemption codes that never apply to S-corps, perjury signature. Three missing values trigger client email, follow-ups at two days, partial replies, e-sign reminders, write-back with provenance. One sentence becomes a multi-day, multi-system process. Provenance of a value matters as much as the value.
- **Why existing tools fail:** fixed flowcharts break on the first ambiguity, and improvising agents without a system-of-record integration cannot be approved by compliance.
- **Pipeline:** planner (one model call, translation only) → typed semantic graph of intents, entities, facts, tools, events, constraints, each node grounded to source words → compiler (no model, 11 stages) → verdict of valid, needs-clarification, or rejected. Ambiguity returns as a question, never a guess.
- **Closed vocabulary:** 42 typed action contracts (forms, documents, email, e-sign, calendar, human steps). Around 40 fail-closed error modes, from graph cycles to unsupported actions. The compiler adds required steps the planner did not ask for (PDF generation, attachment, reply evaluation) because the contracts demand them. Contract digests are pinned across engine, backend, and UI.
- **Gates:** one approval covers the plan, and every external side effect (send email, request signature) has its own gate bound to the exact data fingerprint, re-verified just before sending. Default wait is 72 hours (configurable from 1 minute to 30 days). On timeout, a rule decides, not a model.
- **Side-effect lifecycle:** prepared → sending → succeeded, or unknown → manual review. No automatic retries. Chat can approve a step or answer a question but cannot mutate an approved plan. Follow-ups spawn new sub-plans, max five rounds.
- **Model budget:** in a 20-decision demo run, 19 went to flash-class, 1 to frontier. Design target is ~95% of decisions never needing a frontier model. Moving to private hosting is a config change per call, not a rewrite.

## Architecture & Optimization Mechanics
- **Static routing by construction.** Instead of a learned router deciding at runtime, the compiler shapes every judgment into a small, typed question (is this reply complete, does this document match, which field is which) that a flash model can answer. Routing difficulty is engineered away upstream. Only the planner and genuinely hard judgments go to frontier.
- **Distillation flywheel by design.** Every frontier judgment is typed, logged, and confirmed or rejected by a human, producing clean labeled (input, schema, verdict) pairs. That is ideal distillation and fine-tuning data for the flash tier. The logs exist today. The training loop is not built yet, so "frontier share shrinks every release" is still a roadmap claim.
- **Compile-time verification as a safety layer.** The model proposes a graph and a deterministic compiler validates it against a contract vocabulary. This is the same pattern as constrained decoding at the system level: the model can only request actions the firm already knows how to execute safely.
- **Private-hosting feasibility follows from shape.** Small, short-context, schema-checked calls are exactly the workload where quantized 7B to 14B models on in-house GPUs are viable. The architecture makes on-prem inference a deployment decision.

## Grounded Context (Web Enrichment)
The company could not be verified. Searches for "Perpetual" with an AI-driven acquire-and-modernize wealth model and for Karthic Rao as CTO returned nothing. The well-known Perpetual Limited is an Australian group that agreed in March 2026 to sell its wealth management business to Bain Capital for ~A$500M, which does not match "we acquire traditional wealth firms and boost them with AI." This is almost certainly a different, likely early-stage US firm, so treat all operational claims (95% flash, 42 contracts) as self-reported design targets from a small deployment, not proven scale. The acquisition-plus-AI thesis does fit the 2026 market: RIA consolidation remains intense (Fidelity's mid-2026 review counts 120 deals and $342.9B of acquired assets in H1).

On the technical side, the claim that small typed judgments do not need frontier models is consistent with the late-2026 decision-model category (TypeSafe Jev, OpenAI's Decisions API on GPT-6 Luna, Microsoft Decision-1 post-trained from Qwen3.5-9B, Amazon Strands Decider 2B). Microsoft Decision-1 being a 9B model and Strands Decider being 2B and Apache-licensed makes "run the flash tier on hardware you control" practical today, not aspirational.

Sources: [PrivSource: Perpetual Wealth Management sold to Bain Capital](https://www.privsource.com/acquisitions/deal/perpetual-wealth-management-business-sold-to-bain-capital-private-equity-for-a-500-million-ZoS4Nl), [Fidelity: M&A in wealth management 2026 mid-year update](https://clearingcustody.fidelity.com/insights/topics/running-your-business/mergers-and-acquisition-in-wealth-management-mid-year-update), [eesel.ai: Decision models explained](https://www.eesel.ai/blog/decision-models), [Product Builder: Microsoft Decision-1](https://www.productbuilder.net/models/microsoft-decision-1)

## Real-World Application / Actionable Step
- **Frame "routing via task shaping" as a baseline your learned router must beat.** For a given workflow, compare (a) a learned router over unshaped prompts versus (b) decomposing into typed small judgments with a fixed small-model assignment. If (b) wins on cost at equal quality, routing research should target the residual hard 5%, not the whole stream.
- **Prototype the flywheel this talk only promises.** Take human-confirmed frontier verdicts as targets, distill into a small model (then quantize with GPTQ/AWQ and serve on vLLM), and track frontier-share decline per iteration. It is a clean, publishable setup: distillation on narrow typed decisions with human-verified labels.
- **Evaluate quantized small models specifically on typed judgment tasks** (completeness checks, field matching, document verification). These short-context classification calls are where aggressive quantization should hold up best, and they are what regulated customers want on-prem.
- **Finance angle, low priority:** AI-enabled RIA roll-ups are an active 2026 pattern. No portfolio action from this talk.
