# All Code Is Slop (Except Mine): Lauren Tan, SpaceXAI

**Channel:** AI Engineer
**Published:** 2026-11-14
**Source:** https://www.youtube.com/watch?v=O_zcc6Xl12g

## TL;DR
Lauren Tan ("Potato"), who works on Grok Bot at SpaceXAI (ex-Cursor, ex-React compiler), argues that high-volume agent coding does not have to produce slop. The approach is to invest in the agent's environment, ordered as an inverted pyramid: codebase design and architecture first, then static analysis, then runtime and formal verification, and only last prose rules like AGENTS.md. Every time you correct an agent, turn the correction into a deterministic check rather than another line of instructions. Her claimed results: 3,000 PRs a month personally, about 11,000 for the team in October, a revert rate steady at about 0.5%, and an Electron app that got faster as velocity rose.

## Key Takeaways
- **Inverted pyramid of trust.** Spend most effort where it is deterministic: API design, architecture, lint rules, type systems, compilers, tests. Verification goes next. Prose rules and skills are the thin top layer because they need judgment and are not enforceable.
- **The codebase is the agent's largest input.** Agents copy whatever looks like the established pattern, so tech debt and workarounds spread like weeds. Keep the codebase pristine so agents copy the good stuff.
- **Ban nuance-heavy APIs.** `useEffect` is banned in product code and allowed only inside the framework (Dune, "Next.js for Electron"). That removes a whole class of bugs from review.
- **Directory structure as enforced context.** `electron-main` and `electron-renderer` are top-level dirs, and imports between them are blocked by a dependency-graph checker. This stops agents from dragging heavy main-thread code into the renderer, which caused jank in Cursor.
- **Ban ~99% of code comments.** Agents use comments to justify shortcuts, such as `setTimeout` and `requestAnimationFrame` hacks that patched an imperative/declarative clash in Cursor. Those hacks spread and drove GC churn. Comments go stale and cannot be enforced. Lint errors that point at the root cause replace them.
- **Review means reviewing artifacts.** The review step shrinks to checking videos, screenshots, state charts and formal proofs. A "feature map" skill gives agents a shared vocabulary for the UI. Custom CLIs inside skills cut tokens and are testable.
- **Formal methods are now affordable.** They use TLA+ for multi-device notification flows, Lean proofs for a custom virtualization library (no flicker or jitter), and Bombadil for property-based UI testing. Most of her tokens go to verification, matching Cindy's "70% of daily tokens" anecdote.
- **Automate only after the inner loop is clean.** Automating a loop that produces slop just produces more slop at higher token cost. Once the loop is clean, every release triggers a Cursor project that fuzzes the whole app, opens fix PRs, and auto-merges them.

## Architecture & Optimization Mechanics
- **Static constraints are a token-cost optimization.** Each lint rule takes a review concern out of every future agent run. Think of it as moving cost from inference time (LLM review over tens of millions of tokens) to compile time (a fixed, near-zero-cost check). In the companion YC interview she frames the codebase explicitly as "a form of memory" that is cheaper than review tokens.
- **Verification is the binding constraint, not generation.** Throughput is limited by how cheaply you can establish correctness. Runtime verification (CDP, running the app), model checking and property testing all replace an expensive, low-reliability judge (a human or LLM reviewer) with cheap, high-reliability oracles.
- **Adversarial multi-model review overfits.** In the YC interview she says she has scaled back cross-family adversarial review. Without product intent, reviewers flag "correct but irrelevant" issues. This is a useful caution for anyone using LLM-as-judge ensembles.
- **Performance held at volume:** startup, typing, opening chats and switching chats all got faster after launch, despite 227 contributors in October and a daily stable release.

## Grounded Context (Web Enrichment)
Grok Bot is real. SpaceXAI launched it as a work-assistant and agent product closely tied to Cursor, and xAI's own guides describe its use for engineering. The specific PR numbers are hard to verify. A Chinese-language profile (BAAI Hub) reported Tan running 20+ agents in parallel, more than 1,000 PRs in one month, and about 3,000 PRs over five months, with a goal of doubling output. That is lower than the "3,000 in a month" claimed here, although the timelines differ and growth since then is plausible. I found no independent source for the 11,000 team PRs or the 0.5% revert rate. Treat them as self-reported.

Two caveats. First, Tan works at a lab with effectively unlimited tokens, so the verification-heavy loop may not transfer to cost-constrained teams. Second, PR count is a vanity metric unless PR size is held constant. The stronger evidence is the flat revert rate together with improving latency, and those are the numbers worth tracking in your own repo.

## Real-World Application / Actionable Step
- **For your inference/compression codebases:** each time an agent makes a recurring mistake (wrong dtype path, silently falling back to an fp16 kernel, calibration data leaking into eval), write a lint rule or a runtime assertion, not an AGENTS.md line. For example, a check that fails CI if a quantized model's perplexity delta goes over a threshold, or an import ban between `kernels/` and `eval/`.
- **Make verification the agent's oracle:** give agents a CLI that runs a fixed micro-benchmark (tokens/s, p50/p99 latency, memory) plus a quality probe, and require them to attach the numbers to every PR. That is the "run the code like a user" loop for ML systems.
- **Routing angle:** the inverted pyramid maps directly to cost-aware review routing. Run cheap deterministic checks first, then escalate to a small model, and only send a frontier model the residual cases. Measure what fraction of review tokens you eliminate per new rule.

Sources:
- [xAI: Grok Bot for Engineering](https://x.ai/bot/guides/grok-bot-for-engineering)
- [Constellation Research: SpaceXAI launches Grok Bot](https://www.constellationr.com/insights/news/spacexai-launches-grok-bot-work-assistant)
- [InfoQ: Grok Bot agent](https://infoq.com/news/2026/08/grok-bot-agent)
- [BAAI Hub profile of Lauren Tan](https://hub.baai.ac.cn/view/57615)
