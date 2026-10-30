# How Anthropic Merges 30,000 Code Changes a Day (Manish Kapur, Sonar & Addy Osmani, Anthropic)

**Channel:** AI Engineer
**Published:** 2026-10-28
**Source:** https://www.youtube.com/watch?v=AnsXWH2_EBU

## TL;DR
A fireside chat on "who verifies the software factory." The title stat (Anthropic went from about 2,500 merges a day in May to 30,000 by September) is real but barely discussed. The substance is Addy Osmani's description of how Anthropic gets confidence at that volume: Claude does the first-pass review while actually exercising the change like a user (browser, E2E, linters), hooks rerun checks on every edit, team taste is codified in CLAUDE.md/AGENTS.md, and humans review the agent's evidence (videos, screenshots, test output) rather than the diff. Sonar's contribution is a three-layer verification stack: deterministic analysis, agentic review, supply-chain scanning. Thesis: writing code is solved, verification is the bottleneck, and autonomy is earned per loop.

## Key Takeaways
- **Light vs dark software factory:** a "software factory is harnessing loops at scale." Light: agents plan, build, check, ship while humans apply judgment at most steps. Dark: humans only set intent and handle rare exceptions. Osmani's 2027 prediction: "light factories with some dark corners."
- **Anthropic's review loop:** Claude first-pass review with the ability to run the experience end to end, edit hooks that re-study diffs and fix the PR, Anthropic's code-review product, codified taste in shared agent docs, then human sign-off on evidence artifacts.
- **Verification is the 2-3x lever.** Giving the agent a way to check correctness and completeness can 2-3x output quality, per Osmani. The tests he leans on: end-to-end, property-based, visual verification.
- **Claude.ai refresh:** roughly 3,000 PRs merged in a short window by engineers, designers and other functions, yielding a claimed 3x performance gain.
- **Sonar survey (1,000+ devs, upcoming State of Code):** 84% say AI ships features faster, PRs are larger and more complex, 31% more code reaches production unreviewed, 5% of companies run software factories today, expected 34% (39% in financial services).
- **Enterprise worries:** agent sprawl (hundreds to thousands of untracked agents), identity, telemetry, permissions, sandbox escape. Sonar rebrands guardrails as "guide rails."
- **Label agent-written PRs:** both agree, mainly for accountability and to trigger stricter checks. The human who launched the run still owns the change.

## Architecture & Optimization Mechanics
- **Verification evidence beats line review.** The shift is from humans reading diffs (O(lines)) to humans auditing artifacts the agent produced (O(features)). That only scales if the checks are trustworthy, so test quality becomes the real engineering surface.
- **Layering maps to cost tiers.** Deterministic static analysis is cheap and high-precision for known patterns. Agentic review is expensive and targets intent and logic. Supply-chain scanning is orthogonal. This is a cascade: run the free layer on everything and spend LLM tokens on what it cannot judge.
- **The bottleneck moved downstream.** At 30k merges a day, Anthropic reportedly outgrew Git and built a custom system (Scion). The constraint is no longer code generation or even review, it is merge infrastructure and CI throughput.
- **Weak spots:** no numbers on defect escape rate, review-agent precision, or rollback frequency at Anthropic. "Safe to merge when you have full confidence" is not a policy.

## Grounded Context (Web Enrichment)
Anthropic's engineering post (published around 2026-10-13) confirms more than 30,000 merged changes per day as of September 2026, up roughly 12x from about 2,500 in May, and describes migrating off Git to an internal system called Scion because Git could not keep up. Secondary coverage cites Claude writing over 80% of merged production code at Anthropic, with one single-source report claiming about 90% for Claude Code itself. Critics note the obvious risk: at that volume, intent-only review lets plausible but wrong changes through.

The CircleCI numbers are partly right. The 2026 State of Software Delivery report did analyze about 28 million workflows from 22,000+ orgs and found a 59% year-over-year jump in average daily throughput, the largest since 2019. But the median team improved only 4%, the bottom quartile saw nothing, and CircleCI's later Q2 Pulse report found main-branch throughput flat while feature-branch activity grew. A third-party critique points out that "throughput" mixes feature and main branches and is not deployments. The "3 in 10 merges fail" figure could not be verified directly. The honest reading: AI inflated CI activity far more than shipped software, which reinforces the talk's own thesis that verification, not generation, is the constraint.

## Real-World Application / Actionable Step
- **Make every agent task self-verifying.** For Amit's research code (quantization kernels, routing logic), require the agent to produce evidence: a perplexity or accuracy delta on a fixed eval slice, a latency/throughput table, and a numerical-equivalence test against the FP16 reference. Review that, not the diff.
- **Add property tests for compression code.** Invariants such as "dequant(quant(W)) within tolerance," "router never selects a model above budget," "MoE top-k weights sum to 1." These are exactly the test type Osmani says enables auto-merge.
- **Codify taste in CLAUDE.md** for the research repos: preferred eval harness, seeds, numeric tolerances, banned shortcuts (for example, no eval on calibration data). This is the cheapest quality lever named in the talk.
