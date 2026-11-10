# How to Build a Software Factory That Improves Itself (Zach Lloyd, Warp)

**Channel:** AI Engineer
**Published:** 2026-11-09
**Source:** https://www.youtube.com/watch?v=nKjPBAw_N_0

## TL;DR
Most companies are stuck at "interactive prompting," with engineers running Claude Code or Codex on laptops. That approach is bottlenecked by humans, hard to govern, and a security risk. Lloyd's prescription is a cloud "software factory": sandboxed agents doing triage, spec, implementation, review and computer-use verification, with the entire factory (agent definitions, MCPs, skills, models, webhooks, benchmarks) defined as code in a repo. The differentiator is the closed loop. Every agent trace is stored, LLM-judge "scores" flag failure modes, an improvement agent clusters failures and opens PRs against the factory definition, and replaying past tasks against different models produces a private cost-vs-quality frontier for model routing.

## Key Takeaways
- **Why move off laptops:** a compromised local agent inherits the signed-in user's full privileges, every engineer configures their own MCPs and skills (nothing auditable), and per-person setups make cost impossible to control.
- **Factory as infrastructure, not an "AI teammate":** open (any model, open-weight or frontier, any harness), adaptable to existing infra, defined in code and version-controlled, so factory versions can be A/B tested and agents can edit the factory itself.
- **AI sovereignty:** enterprises want to own all data in and out, run agents on their own compute, and bring their own inference.
- **Two engineering roles:** product engineers feed work in through Slack, Linear/Jira and GitHub PR comments. Factory engineers improve the system: skills, context, model mix.
- **Online evals ("scores"):** LLM-as-judge over every run. Example: a detector for redundant tests, a common coding-agent failure.
- **Self-improvement loop:** agents aggregate failures ("saw this fail 37 times"), propose a fix (e.g. "read matching skills before implementing"), and open a PR to the factory definition.
- **Private benchmarks from real traffic:** tag past runs into suites (e.g. front-end tasks), replay across model configs, get a cost-quality plot. Demo: GLM-5.3 Flash at 93% for $2 vs a GPT model at 95% for about 3x the cost.
- **Throughput fixes for PR pile-up:** spec-driven development (check adherence to spec) and computer-use verification that produces user-level evidence, reducing human review load.
- **Budgeting:** track cost per PR and the share spent on scoring/benchmarking. Product is overkill below roughly 10 engineers.

## Architecture & Optimization Mechanics
- **Stack, bottom to top:** factory-as-code, data layer, sandboxed execution, flexible inference, self-improvement (scoring plus benchmarks), orchestration (an orchestrator agent routes each item to triage, spec, implement or review), access via existing tools.
- **Routing from replay:** this is offline router training on in-distribution data. Each stored trace is a (task, outcome, cost) sample. Replaying it across models gives the labelled matrix a learned router needs, per task category.
- **Weak link is the label:** "correctness" in the cost-quality chart is LLM-as-judge only, no human grading yet. A 93% vs 95% gap is inside typical judge noise unless the judge is calibrated. Choosing the cheap model on that gap is defensible only if the judge's error is smaller than the difference.
- **Self-modifying config risk:** agents PRing their own harness is prompt/skill optimization (DSPy/GEPA-style) applied to ops. Without a held-out benchmark, it will overfit to the judge's failure taxonomy.

## Grounded Context (Web Enrichment)
Warp Factories launched on August 18, 2026 (closed beta), following Warp's Oz cloud-agent launch in February 2026. Warp markets it as "open infrastructure" for cloud software factories. Lloyd told TechCrunch that Warp automates about 30 to 35% of its own tasks in a typical week, and a Lenny's Newsletter piece reports Warp shipping around 2,000 PRs a month. All of these figures are self-reported. Note that "open" means open to any model and harness, not open source. Lloyd confirmed on stage that the platform is closed source, which is a tension with his own "AI sovereignty" pitch.

The model names in the benchmark demo (GLM-5.3 Flash and a GPT model listed as "GPT 5.6") come from a vendor demo on internal Warp tasks. They are not a published result. The core idea holds up independently of Warp: public leaderboards like SWE-bench and Terminal-Bench correlate poorly with performance on a specific codebase. Replaying your own traces is the right way to set a routing policy, and it is the same argument made at this conference by Artificial Analysis on caching and Basis on behavior specs.

## Real-World Application / Actionable Step
- **Build a trace-replay router dataset for your own work.** Log every agent or LLM call with task tag, cost, and outcome. Weekly, replay a stratified sample (easy/medium/hard per category) across 3 to 4 candidates, including your quantized or pruned variants. Fit a per-category routing threshold on the cost-quality frontier.
- **Calibrate the judge first.** Hand-label 50 to 100 replays, measure judge agreement, and only act on quality gaps larger than the judge's error.
- **Version the harness as code.** Put prompts, skills, MCP config and model mix in one repo so compression or routing changes can be A/B tested like any other diff.
- **Keep a frozen holdout** that the self-improvement loop never sees, or you will optimize toward the judge rather than real quality.
