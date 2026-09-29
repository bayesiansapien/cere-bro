# AI-Generated Code Is Already Competing With Human Code (Daksh Gupta, Greptile)

**Channel:** AI Engineer
**Published:** 2026-09-27
**Source:** https://www.youtube.com/watch?v=474j-n1Ltxc

## TL;DR
Greptile mined over a million PRs/month from enterprise customers (Nvidia, Coinbase, Datadog, Amex) and found that roughly a quarter of PRs are now fully or largely agent-authored, up from under 1% in early 2025. On revert rate, bug severity counts, and review rounds to merge, agent PRs are statistically indistinguishable from human PRs. The differences are qualitative: each agent has its own failure fingerprint. The bottleneck has shifted from writing code to validating it.

## Key Takeaways
- **Detection is hard.** Git author field flagged <1% as AI. Real signal came from PR footers ("Co-authored-by: Claude") and agent branch-name prefixes (Codex). With these, ~25% of monthly PRs are agent-authored.
- **Adoption is a smooth curve.** No visible step changes at model launches. Diffusion looks continuous, not release-driven.
- **Revert rates:** Codex ~1.0 per 1,000 PRs, humans ~2.5, Devin ~3.5. No meaningful correlation between PR size and revert rate across humans vs agents, which undercuts the "agents only get easy tasks" objection.
- **Bug counts:** 3 of 4 agents produced fewer P0s than humans. P1/P2 rates roughly equal.
- **Review cycles to merge:** Devin 2.1, Codex 2.45, humans in between. No real difference.
- **Failure fingerprints differ by agent.** Claude is ~1.5x more likely than humans to produce SQL injection flags; Devin is ~0.5x as likely to produce auth-bypass issues. Aggregate parity hides per-category skew.
- **Throughput distribution is extreme.** Median Greptile user ships 50 PRs/month, P90 ships 500, P99 ships thousands. Manual review cannot scale to the tail.
- **Validation reframed as three questions:** (1) Does the change violate the user contract? (2) Does it raise the probability of a future violation? (3) Does it fulfill the author's stated intent?
- **~20% of Greptile-reviewed PRs now merge with zero human review or testing**, relying on sandboxed execution, dependency install, browser agents, and mocked inputs.

## Architecture & Optimization Mechanics
- **Review stack:** a swarm of agents per PR inspects changed files plus their dependency neighborhood, then spins the code up in a sandbox and fuzzes it via browser agents. This is execution-grounded review, not static diff reading.
- **Metric design is the real contribution.** Using revert rate, severity-weighted bug counts, and iterations-to-merge as proxies is a reasonable triangulation, but all three are downstream of the same review process (Greptile flags the bugs it then counts). Expect selection bias: teams adopting Greptile plus agents are likely more mature.
- **Keyword-frequency failure taxonomy** (scanning millions of review comments for "SQL injection", "N+1 query") is crude but cheap. A classifier or embedding-cluster pass would give a cleaner taxonomy.
- **Agent routing implication:** if failure modes are agent-specific and orthogonal, the optimal system routes tasks by failure risk (e.g., DB-heavy work away from the agent with elevated SQLi rates) and routes review depth by author identity.

## Grounded Context (Web Enrichment)
Greptile published the underlying analysis in May 2026 ("Rise of the Overnight Agents"), reporting 27.6% of merged PRs as AI-authored in April 2026, up from under 1% in February 2025, across ~65,000 organizations. The talk's "about a quarter" matches. The parity conclusion is the vendor's own data, reviewed by the vendor's own tool, so treat it as directional.

Independent data is less rosy. CodeRabbit's December 2025 report found 10.83 issues per AI co-authored PR versus 6.45 for human-only, with 1.57x more security findings and 2.74x more XSS. The SusVibes benchmark found SWE-Agent with Claude 4 Sonnet produced working solutions 57% of the time but secure ones only 11.8%. Help Net Security (March 2026) reported agents repeatedly reintroducing decade-old vulnerability classes. Reconciling: Greptile measures merged PRs after agent-plus-reviewer iteration loops, while the critics measure raw agent output. The honest reading is that agent code reaches parity *after* automated review, not before. The review loop is doing real work.

Sources: [Greptile blog](https://www.greptile.com/blog/rise-of-the-overnight-agents), [Help Net Security](https://www.helpnetsecurity.com/2026/03/13/claude-code-openai-codex-google-gemini-ai-coding-agent-security/), [Kusari](https://www.kusari.dev/blog/ai-coding-assistants-in-2026-4x-faster-10x-riskier-the-hidden-security-cost), [arXiv 2604.19965](https://arxiv.org/html/2604.19965v1)

## Real-World Application / Actionable Step
- **Route by failure fingerprint.** In any LLM routing work for code tasks, add a per-model vulnerability-class prior (SQLi, auth, N+1) to the cost/quality objective. Parity on average metrics is not parity on tail risk.
- **Budget review compute, not generation compute.** For your own research repos, pair agent-generated PRs with execution-grounded checks (run the eval/benchmark harness in CI) rather than reading diffs. Quantization/kernel code fails silently on numerics, so add numerical-diff tests against a reference fp16 path.
- **Tag agent PRs explicitly** (Co-authored-by footers, branch prefixes) so you can measure your own revert and regression rates by author type later.
