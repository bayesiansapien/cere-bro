# Optima: Artificial Analysis ships cost-and-time-per-task benchmarking

**Source:** The Decoder, [Optima tackles AI benchmarking's biggest flaw by letting users test models against their own data](https://the-decoder.com/optima-tackles-ai-benchmarkings-biggest-flaw-by-letting-users-test-models-against-their-own-data/) (2026-08-16)
**Raw:** [raw/rss/2026-08-16-the-decoder-optima-tackles-ai-benchmarking-s-biggest-flaw-by-lettin.md](../../raw/rss/2026-08-16-the-decoder-optima-tackles-ai-benchmarking-s-biggest-flaw-by-lettin.md)
**Topic:** benchmarking, cost per completed task, routing economics

## TL;DR

Artificial Analysis launched **Optima**, a platform where you build a benchmark out of **your own data and workflows** and compare models on **quality, cost, and time per task** rather than on a public leaderboard score. The Decoder's framing of why this matters is exactly right for agent workloads: for agent-based applications, cost and time per task tell you more than raw token pricing does.

## Why this is a bigger deal than a product launch

**It resolves a standing prediction in this wiki, two days after it was made.** [08-14's Looking Ahead](../daily-digest/2026-08/2026-08-14.md) predicted: *"A major leaderboard makes dollars-per-completed-task its primary metric within 60 days, or the cost literature stays incomparable,"* with the signal named as "xRouteBench, Artificial Analysis, or Terminal-Bench publishing cost-per-solved-task as the headline column rather than as a side field." Artificial Analysis is one of the three named parties and it shipped inside 48 hours of a 60-day window. **Resolved, early, by the named actor.**

**It is the productisation of the measurement disagreement recorded on 08-14.** The [AlphaSense study (08-14)](2026-08-14-alphasense-token-price-vs-task-cost.md) found that across 246 financial-analysis tasks, per-token price ranks models *backwards*: GPT-5.6 Sol cost about 13% less than Kimi K3 at roughly 20% higher quality, and Opus 4.8 cost about half of Kimi K3 at 13% higher quality, despite both carrying higher sticker prices, because a stronger model finishes in fewer tokens and fewer retries. Artificial Analysis's own cost-to-accomplish rankings disagreed, placing the Chinese models significantly cheaper. Both parties were right about their own workload and neither could be checked against the other's. Optima's answer is to stop arguing about which workload is representative and let each buyer measure their own. That is the correct resolution of a workload-dependent disagreement, and it is notable that the party that shipped it is the one whose numbers were being contested.

**It makes the routing literature's cost objective auditable.** [LLM Routing](../ai-routing/llm-routing.md) currently carries the finding that most routing results optimise a per-token cost objective, and that [LLMRouter's xRouteBench (08-14)](../ai-routing/2026-08-14-llmrouter-unified-routing-infrastructure.md) inherits that choice while reporting that lightweight routers get more competitive as the cost constraint tightens. If the constraint is measured in the wrong currency, that regime boundary is in the wrong place. A tool that produces per-task cost on a user's own traffic is the instrument that would let someone check.

## Corroborating evidence from the same day

Two social-layer datapoints landed alongside it, and both say the per-token metric is wrong in a direction that matters.

**DHH's same-task cost spread.** Running an identical Rust-rewrite challenge (a port of the TerminalTextEffects Python library), the completed runs cost roughly **$550 for Fable in 45 minutes, $55 for Grok 4.6 in 1.5 hours, $43 for GPT Sol, and $23 for DeepSeek Pro V4 Max in 2.5 hours**, with DSV4 Flash and GPT Luna failing to complete at all ([source](https://x.com/dhh/status/2088657836586807687)). That is a **24x spread in dollars and a 3.3x spread in wall-clock on one completed task**, plus a completion-rate axis that a price table cannot express at all.

**The tokenizer term nobody prices.** Anthropic's Tibo Sottiaux stated publicly that OpenAI's tokenizer is significantly more efficient than Anthropic's, roughly 30% fewer tokens for the same text, and that this matters because API billing is per token ([source](https://x.com/thsottiaux/status/2088856449959276836)). A circulated comparison table puts the total at **493 words rendering as 766 tokens under OpenAI's o200k, 900 under legacy Claude, and about 1,170 under a Claude Opus 5 estimate**, a **34.5% reduction for OpenAI overall** and **53.2% on multilingual prose**, the worst case. Two vendors quoting the same dollars-per-million-tokens are not quoting the same price, and no published leaderboard normalises for it.

## Gaps

Optima is a platform, so its value depends entirely on whether people bring real workloads to it, and bring-your-own-benchmark tools have a long history of being used once. Custom benchmarks are also unshareable by construction, which is the price of the fix: the field trades a comparable-but-wrong public number for an accurate-but-private one, and cross-paper comparison gets no better. And nothing here addresses the tokenizer normalisation problem, which sits underneath both metrics.

## Related pages

- [LLM Routing](../ai-routing/llm-routing.md)
- [AlphaSense: token price versus task cost (08-14)](2026-08-14-alphasense-token-price-vs-task-cost.md)
- [Compute Economics](../hardware/compute-economics.md)
- [Agent Benchmarks](../agentic-systems/agent-benchmarks.md)
