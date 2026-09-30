# Software Engineering Is Becoming Factory Engineering (Zach Lloyd, Warp)

**Channel:** AI Engineer
**Published:** 2026-09-27
**Source:** https://www.youtube.com/watch?v=tUPPVhBBcoM

## TL;DR
Warp's founder (ex-Google Docs engineering lead, no hand-written code in six months) predicts that every sizable project will run a "software factory" as routinely as CI/CD, and engineers will become factory engineers who build the thing that builds the product. Warp open-sourced its terminal/ADE largely to run a public factory (build.warp.dev), using agents to absorb the classic open-source pains: noisy issues, sloppy PRs, review hell.

## Key Takeaways
- Development eras: chat/autocomplete → interactive agents (now) → automation (next 6 to 12 months).
- Factory loop: ideas in → agent triage → spec (if hard) → **human spec review** → agent implementation → agent then **human code review** → agent verification → **human product review** → ship → agent monitoring → back to the top.
- Triage rule: easy and unambiguous goes straight to implementation. Hard gets a **product spec** (product invariants) plus a **tech spec** (architecture, code shape).
- Human code review becomes a risk-management decision: agent reviews first, humans come in selectively.
- Verification: computer-use agents produce videos and screenshots; CI/CD stays.
- Reference architecture: input channels → control plane (work distribution) → execution (cloud sandboxes, harness plus model choice) → **data plane** for memory and learning.
- Self-improvement via **skill loops**: observer agents watch where senior engineers correct the review agent's comments and update the skill.
- Measure factory efficiency: software shipped per unit of human time plus token cost.
- Business point: when software is cheap to build it is trivial to clone, so a great product is not enough. Moats are distribution, ecosystem, brand, data, capital. Building in the open is the startup's route to ecosystem.
- Warp: 60K+ GitHub stars, ~800K active developers, hiring more than ever.

## Architecture & Optimization Mechanics
- **Factory = DAG with human checkpoints at high-leverage nodes.** Human attention is placed at spec, product, and selective code review. This is a cost-aware allocation of the most expensive resource.
- **Harness and model are per-node choices** in the execution layer. Model routing becomes a factory configuration concern: cheap models for triage, stronger ones for specs and hard implementation.
- **Efficiency metric = output / (human time + tokens).** This is the right objective function for a router at the system level, not per query.
- **Observer-agent skill loop** is a form of learning from human corrections without weight updates. It is prompt-level RLHF.

## Grounded Context (Web Enrichment)
Warp open-sourced its ADE on April 28, 2026, with OpenAI as flagship sponsor. GPT models (including GPT-5.5) power the agentic workflows that ship improvements to Warp's own codebase. The orchestration layer is **Oz**, Warp's cloud agent platform, and **Warp Factories** lets teams define triggers, agents, models, and approval gates as config checked into the repo. So the "you should probably buy, not build" advice in the talk is also a product pitch. Lloyd acknowledges the contradiction in Q&A: everyone deploys a factory, but tuning skills for your domain stays in-house.

The factory thesis is contested in this same batch of talks. Conductor's Holtz rejects the metaphor ("orchestras, not factories"), and WorkOS found a naive factory gave no gain over local agents. Industry DORA data shows PR volume rising faster than delivered value when review becomes the bottleneck. Lloyd's own point that review is "the most painful part" is where factories currently stall.

## Real-World Application / Actionable Step
- **Use the product-spec / tech-spec split for research tasks.** Before agents implement a new pruning method, have one agent write the "invariants" (target sparsity, accuracy floor, latency budget, hardware) and another the implementation plan. Review only the invariants closely.
- **Instrument your own efficiency metric.** Track research results per (your hours + token spend) per week, so you can tell whether agent tooling is actually helping.
- **Build an observer loop on your review comments.** When you correct an agent's experiment code, log the correction. Periodically have an agent fold those corrections into your skills/CLAUDE.md.

Sources: [Warp newsroom: open source](https://www.warp.dev/newsroom/2026/4/28/warp-open-sources-its-agentic-development-environment), [Warp blog: now open source](https://www.warp.dev/blog/warp-is-now-open-source), [Introducing Oz](https://www.warp.dev/blog/oz-orchestration-platform-cloud-agents), [warp.dev](https://www.warp.dev/)
