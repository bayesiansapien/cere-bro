# Does Code Quality Still Matter? It Depends on This (Max Kanat-Alexander, Capital One)

**Channel:** AI Engineer
**Published:** 2026-10-21
**Source:** https://www.youtube.com/watch?v=bU5gDVyu_28

## TL;DR
Code quality exists only to serve two things: understanding a system's actual behavior and safely modifying it. Structure is what makes that possible. AI is creating a flood of "disposable software" (low consequence, near-zero replacement cost, few dependents, negligible maintenance) where code quality genuinely does not matter. Durable software still needs full rigor, and the real lever is making rigor cheap so you can be wrong about where a system sits on the disposable-to-durable spectrum.

## Key Takeaways
- **Two understandings matter:** what the system concretely does, and how to change it correctly and safely. Tests, debuggers, evals, and observability all exist to serve these.
- **Every change carries two risks:** causing a problem now, and making future changes harder. The second feeds the first and compounds non-linearly. Every postmortem reduces to an understanding failure.
- **Four axes place software on the spectrum:** consequences of failure, cost of replacement, number of dependents, cost of maintenance. All low means disposable; all high means durable. Default to assuming durable.
- **You can engineer disposability:** isolated environments with no PII or customer data, no inbound calls from other prod systems, a clunky durable backup behind vibe-coded front ends, and tight scope.
- **Lower the cost of rigor instead of debating it:** standardize languages, frameworks, and RPC protocols to remove possibilities; build "inward flow" tooling that runs automatically, fast, with low false positives; make tests fast and deterministic by default (agents can now generate in-memory fakes of services); turn lint strictness to maximum on day one.
- **Answer:** disposable software, no. Durable software, yes. Does rigor have to be expensive? No.

## Architecture & Optimization Mechanics
- The framework is a cost model, not a style argument. Rigor spend should be proportional to expected future modification cost, which compounds with lost understanding.
- "Reduce the cost of rigor" maps directly to research infra: deterministic, fast eval harnesses and strict configs make it cheap to promote a throwaway experiment into a durable pipeline.
- Weak point: the claim that durable software volume will grow because AI makes it easier is asserted, not evidenced. Also, "disposable" systems frequently become durable by accident (the classic prototype-in-prod), which is exactly why his "make rigor cheap" hedge carries the talk.

## Grounded Context (Web Enrichment)
The talk is consistent with Kanat-Alexander's long-running position (author of Code Simplicity and Understanding Software; now Executive Distinguished Engineer at Capital One focused on developer experience). On the DX Engineering Enablement podcast he argued that a throwaway script and decade-lived enterprise software should not face identical quality bars, and that review trust should be scoped to a person plus codebase pair rather than given as blanket exemption. He has also promoted a preprint proposing "cognitive debt" (loss of understanding) and "intent debt" (loss of goals, constraints, decisions) as AI-era additions to technical debt, which is the formal version of this talk's "understanding" thesis. The "write-only, disposable code" framing circulating via InfoQ comes from a separate QCon London talk by Phillip Mortimer, so the idea is converging across practitioners rather than being unique to Capital One.

Sources: [DX podcast: How Capital One assesses AI readiness](https://getdx.com/podcast/how-capital-one-assesses-ai-readiness/), [AI Engineer speaker page](https://www.ai.engineer/speakers/max-kanat-alexander), [InfoQ: write-only disposable code](https://infoq.com/news/2026/08/code-AI-write-only-disposable)

## Real-World Application / Actionable Step
- Classify your research code explicitly. One-off sweeps, plotting scripts, and ablations: disposable, let agents write them with no review. Quantization kernels, routing policy, and shared eval harnesses: durable, full rigor.
- Enforce disposability structurally: run agent-written experiment code in a sandbox with read-only access to checkpoints and no write path to shared eval sets or prod routing configs.
- Spend effort on the cost of rigor for the durable layer: max-strict lint and typing in the shared repo, deterministic seeded eval runs, and agent-generated in-memory fakes for any serving dependency (vLLM endpoints, router backends) so tests run in seconds.
