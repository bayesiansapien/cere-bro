# Rebuilding CI for AI-Scale Commit Volume (Gautam Korlam, SonarSource)

**Channel:** AI Engineer
**Published:** 2026-10-14
**Source:** https://www.youtube.com/watch?v=7b9tov5Uc5s

## TL;DR
CI and code review were designed as serialized queues for human commit rates. Agents break that assumption: PR volume grows exponentially, individually green PRs combine into a red trunk, and humans rubber-stamp reviews they cannot keep up with. Korlam (ex-Uber build/merge infra, Gitar co-founder, now Sonar after the May 2026 acquisition) prescribes four fixes: make CI incremental and fast, push checks left to the agent's local loop, auto-approve low-risk changes by policy, and keep a durable audit record of who (or what) wrote, tested and approved each change. The diagnosis is sound and well-grounded in Uber's SubmitQueue work. The prescriptions are standard good hygiene with a Gitar product pitch on top, and the "25% month-over-month PR growth" number is Gitar's own platform data, not an industry measurement.

## Key Takeaways
- **The queue is the bottleneck, not the model.** CI and review are centralized serial stages. Agents and background "software factory" workflows submit PRs concurrently, so both queues saturate.
- **Uber precedent:** a monorepo with thousands of daily changes would take up to ~20 days to merge fully serialized, while unserialized merging left the iOS trunk red constantly. SubmitQueue speculatively tested likely commit combinations in parallel, predicted breakage, and ejected PRs before they hit trunk.
- **Gitar's own commit rate ~10x in 3 years** with the same small team. PRs reviewed on its platform grow ~25% MoM.
- **13% of PRs have at least one CI failure.** Each is a full repair round trip (read logs, root cause, push, rerun), and human reviewers usually wait for green, so CI failures serialize review too.
- **CI speedup recipe:** Rust build output caching, reducing compiler cache invalidation churn, sharding. Result: ~10 min to under 1 min for warm incremental runs.
- **Policy-based auto-approval:** doc changes, non-breaking dependency bumps, security patches and low-risk internal tooling get auto-approved by plain-English rules. Payments or auth paths require a human. The authoring agent never approves its own change.
- **Audit trail as first-class artifact.** CI logs expire, force-pushes repoint branches, an approval stamp says nothing about what was checked. Record per PR: which agent, which session, who triggered it (human or automation), the commit CI was trusted on, saved test reports, how every finding was resolved, named overrides with reasons, and an approver independent of both the bot and the human who prompted it.

## Architecture & Optimization Mechanics
- **Merge queue as a speculative execution problem.** SubmitQueue is branch prediction for commits: build a speculation tree over pending changes, test the most probable outcomes in parallel, commit the ones that pass in order. This trades compute for latency, exactly like speculative decoding trades draft compute for wall-clock time.
- **Risk-based routing for review.** "Auto-approve low-risk, escalate high-risk" is LLM routing applied to the SDLC: a cheap classifier decides which PRs need the expensive reviewer (a human). Policy rules are the router; the escalation threshold is the quality knob.
- **Shift-left equals better context locality.** The local agent already has the failing context loaded, so fixing a check there is cheaper than a CI round trip that must re-ingest logs. Analogous to keeping hot state in cache rather than paying a reload.
- **Separation of duties in a zero-trust sense:** author agent, prompting engineer, and approver must be three distinct identities. Without it, an agent-heavy pipeline collapses into self-certification.

## Grounded Context (Web Enrichment)
The Uber history checks out. SubmitQueue is documented in the EuroSys 2019 paper "Keeping Master Green at Scale," which reported that with just 16 concurrent potentially conflicting changes there was a 40% chance of a trunk break, and Uber later reported that a SubmitQueue enhancement cut CI resource use by 53% and wait times by 37%. The Sonar acquisition of Gitar was announced May 21, 2026 (terms undisclosed, Gitar had 9 employees and $9M seed from Venrock), and Gitar continues as a standalone product beside SonarQube. So this is a vendor talk, and the auto-approve feature is the thing being sold.

The industry growth claim is directionally right but his numbers are self-sourced. GitHub's Octoverse 2025 reported close to 1 billion commits in a year (about +25% YoY) and secondary reports cite roughly 43M PRs merged per month (+23% YoY). That is annual growth, nowhere near 25% month over month, so Gitar's curve reflects customer acquisition on its own platform as much as an industry trend. The Uber London anecdote is real in outline: TfL refused Uber's licence in late 2019 citing unauthorized drivers able to work under other drivers' accounts, and Uber won it back in court in 2020 after demonstrating new controls. Attributing it to a single feature-flag change is his simplification.

## Real-World Application / Actionable Step
- **For research repos with agent-generated PRs:** add a merge queue (GitHub merge queue is enough at research scale) so concurrent agent PRs are tested against each other, not just against stale main.
- **Cache aggressively in eval CI:** cache model downloads, tokenized datasets and compiled kernels keyed by content hash. Aim for sub-minute incremental runs so agents iterate in-loop instead of waiting on CI.
- **Write an auto-approve policy:** configs, docs, plotting code and dependency bumps auto-merge; anything touching quantization kernels, routing thresholds or eval harness logic needs a human.
- **Log provenance for every experiment-affecting merge:** agent, session, triggering prompt, and the commit hash eval results were produced on. Expired CI logs are how irreproducible benchmark numbers happen.
- Related: [[2026-10-12-Claude-Managed-Agents-Part4-Evals-CICD-MultiTenancy]], [[2026-10-06-AI-Engineer-Harness-Engineering-How-To-Build-A-Software-Factory-Tessl]].
