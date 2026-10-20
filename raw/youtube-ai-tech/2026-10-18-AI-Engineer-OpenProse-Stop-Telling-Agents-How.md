# Stop Telling Agents How | Dan Barrett, Raymond Weitekamp & Jose Montes de Oca, OpenProse

**Channel:** AI Engineer
**Published:** 2026-10-18
**Source:** https://www.youtube.com/watch?v=7T-gldvgfpo

*Workshop, AI Engineer New York. Vendor talk (OpenProse, open-core, permissive license).*

## TL;DR
Prompting, then context engineering, then harness engineering have each been absorbed by the layer below. OpenProse's bet for the next layer: write declarative, composable "contracts" (goal, inputs, outputs, required skills/tools, sub-agents) in plain Markdown, and let any harness (Claude Code, Codex, your own) act as the compiler and runtime. Jobs are contract plus trigger (cron or webhook), event-driven rather than chat. Once an expensive model finds a good path, you "pin the how" from the trace to run it cheaply. The interesting new piece: cheap "decision models" (Jev, mentioned repeatedly) as contract verifiers, routers and semantic cache invalidators.

## Key Takeaways
- **Two things to remember:** it is just Markdown (a ~70 to 80k-token kernel prompt acts as bootloader, compiler and VM: "You are the compiler. This is not an analogy."), and it is event-driven, not chat.
- **Declarative over imperative.** Specify end state, not steps. Over-specifying the how wastes capability and blocks cheaper execution.
- **Composition over inheritance.** Contracts compose into a DAG; intermediate contracts act as checkpoints that constrain the path without scripting it.
- **Hard dependencies.** If a declared skill or CLI (e.g. Exa search) is missing, the program does not compile rather than silently falling back.
- **Pin the how.** Run loose with a strong model, take the golden trace, codify it into procedural steps, then run on a cheaper model. Cost falls as the spectrum shifts from "what" toward "how."
- **Adversarial review via fresh sessions.** Each PR is checked by new sessions against the contract, avoiding self-review bias. Some PRs took 14 review rounds before passing.
- **Shapes as templates:** fan-out/fan-in, map-reduce, adversarial review, loop-until-condition, all expressible without code on any harness with sub-agents.
- **Enterprise use case:** quant model documentation. Big banks have about 4,000 models re-documented yearly, a $10M to $50M per year cost. Demo generated SOFR curve model docs in Codex with a cheap model.
- **Data sovereignty:** run on-prem on open models with your own harness; your SOPs (institutional knowledge) never go to labs.
- **Not for exploration.** Use chat for one-offs; OpenProse is for repeatable, reliable, auditable work.
- **Contrast with DSPy:** same goal (abstraction over complex LLM workflows), opposite implementation. DSPy isolates each LLM call behind typed deterministic code; OpenProse lets everything live in "fuzzy land."
- **Weakness admitted:** the agent self-declares that the contract is met, and results vary a lot between a small and a frontier model.

## Architecture & Optimization Mechanics
- **Decision models as verifiers.** A cheap System-1 classifier (Jev) checks "does the output satisfy the contract?" at the end of each job. Much cheaper than a full LLM-judge session.
- **Decision models as event routers.** Instead of manually wiring "issues to job A, PRs to job B," a classifier routes every GitHub event to the right contract. Same problem as LLM routing, applied to workflows.
- **Semantic memoization.** In React-style dependency graphs of contracts, a decision model decides if an upstream change invalidates downstream outputs, replacing expensive agent-based staleness checks.
- **Prefix caching and RL.** A 100k-token stable kernel prefix is an ideal KV-cache prefix. All-text workflows plus contract pass/fail signals form a clean RL dataset. They suggest self-hosters could compress the kernel into a more token-efficient form.
- **Evolutionary kernel shrinking:** they benchmark candidate shorter kernels and keep those that still produce conformant runs. Prompt pruning, measured against task success.

## Grounded Context (Web Enrichment)
"Jev" is Typesafe AI's Jev System One, part of an October 2026 wave of "decision models": LLMs that output probabilities over choices instead of generating text. Cloudflare launched open-source Clef and Clef-flash on Workers AI (later Clef-omni, a 30B-A3B multimodal model at about $0.15 per million input tokens). Microsoft-Decision-1 (unveiled 9 October, reportedly a 9B Qwen-based model) claims 35x faster than GPT-6 Sol at $0.042 per million input tokens with free output; an independent JevBench test measured 459 ms median latency versus Microsoft's 85 ms claim. Perplexity's pplx-decider-v1-27b and AWS Strands Decider 2B were also reported ([Cloudflare](https://blog.cloudflare.com/clef-decision-models/), [Hackaday](https://hackaday.com/2026/10/06/a-new-type-of-llm-on-the-block-decision-making-models/), [Windows Forum](https://windowsforum.com/news/microsoft-decision-1-in-foundry-fast-ai-classification-model-benchmarks-and-pricing-caveats-megathread.447797/), [Tech Insider](https://tech-insider.org/microsoft-decision-1-ai-model-35x-speed-2026/)). Many figures come from aggregators; verify on vendor pages.

On OpenProse itself: the declarative-contract idea is sound and aligns with Anthropic's dynamic multi-agent workflow patterns. But a 70k to 80k-token kernel is a heavy fixed cost on every run, and "the agent says it is done" is exactly the silent-failure mode the Langfuse talk warns about ([[2026-10-18-AI-Engineer-Langfuse-Evals-High-Stakes-Agents]]). Until an independent verifier is wired in, auditability is weaker than claimed. No cost or quality numbers were shown for the quant-docs case beyond "shockingly good."

## Real-World Application / Actionable Step
- **Benchmark decision models as router backbones.** The decision-model category is essentially a productized router head: single forward pass, probabilities over options, near-zero output cost. Test Clef-flash, Decision-1 and Jev against your current router classifier on your routing dataset. Compare calibration (ECE), not just accuracy, because routing thresholds depend on well-calibrated probabilities.
- **Distillation pipeline from "pin the how":** log frontier-model traces that pass the contract, then distill them into a smaller model or a fixed procedure. This is the same loop as router training (expensive model labels, cheap model serves).
- **Prefix-cache the kernel:** if you run anything with a large fixed system prompt, make it byte-stable and put it first. On vLLM, enable automatic prefix caching; the 70k-token prefix becomes almost free after the first call.
- **Try the pattern locally:** `npx skills add openprose/prose`, write one contract for a recurring task (e.g. weekly paper digest), and wire a decision model as the final pass/fail gate.
