# Meta Muse Wonder and Muse Wonder Full

**Sources:** AI Breakfast (Gmail), The Decoder and The Information (RSS), X Following feed (Zuckerberg, Alexandr Wang, Artificial Analysis, Vals AI). Raw: `raw/gmail/2026-10-13-newsletters.md`, `raw/rss/2026-10-12-the-decoder-meta-s-new-frontier-model-muse-wonder-full-breaks-into.md`, `raw/twitter/feed/2026-10-1[23]-*-ranked.json`. [Meta research blog](https://research.meta.ai/blog/muse-wonder).

## TL;DR

Meta Superintelligence Labs shipped Muse Wonder and Muse Wonder Full on 2026-10-12, its first models it calls frontier, trained at the gigawatt-scale Prometheus data center. The pitch is personal and professional agents: **Active Memory** carries user context across conversations and **Active Focus** keeps working a goal through blockers and checks in before consequential actions.

- **Benchmarks:** Meta's chart puts Full at 57.5 on its SWE-Marathon (build a whole project over 2-10 hours) vs 46.3 for Claude Opus 5.5. Independent: Artificial Analysis Intelligence Index 56 for Full at max effort vs 58 for Opus 5.5, top-three on 6 of 10 evals; standard Wonder at 52 (Muse Spark 1.3 was 48 six weeks ago). Vals Index: Full (Max) debuts at #5, above every OpenAI model.
- **Price and serving:** Wonder is $4 / $20 per million input/output tokens, 1M context, in the Meta Model API and Muse Code. Artificial Analysis puts cost per benchmark task at $4.52, nearly 3x Spark 1.3's $1.60, cheaper than Anthropic's lineup and pricier than GPT-6 Astra or Gemini 4 Argon. Full has no API price yet.
- **Evals:** Meta built an internal Personal Superintelligence Index (PSI) to measure usefulness for personal agents.
- **Safety:** described as Meta's "most aligned model so far", but the full safety report is "coming soon", not published. Zuckerberg told the FT Meta rejects calls to slow down and the next step is in progress; next priorities are "memory and persistence" for tasks lasting weeks.

## Relation to prior wiki pages

- **Memory as the product:** Active Memory is the commercial bet on agent memory just as the [UCLA memory null result (10-13)](../agentic-systems/2026-10-13-stateless-agents-self-compaction-and-idea-basins.md) found a persistent memory tier adds cache cost with no measurable accuracy gain on single-question benchmarks. The two are not in direct conflict (personal assistants are multi-session by design), but no public benchmark yet measures what Active Memory buys.
- **Cost per task rising at the frontier** contrasts with Agent Arena's report the same day that open models matched July's leader at 89-96% lower cost per task. The frontier gets pricier per task while the trailing edge collapses in price.

## Gaps

No safety report. SWE-Marathon is Meta's own benchmark. Full's API price unknown.

## Related

[scaling-laws](scaling-laws.md) · [agent-memory](../agentic-systems/agent-memory.md)
