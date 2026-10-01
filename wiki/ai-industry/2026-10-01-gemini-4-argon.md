# Gemini 4 Argon: Google's First Frontier Model in Seven Months

**Sources:** [The Decoder](https://the-decoder.com/google-gemini-4-argon-closes-the-gap-with-openai-and-anthropic-but-doesnt-take-a-clear-lead/) · [The Information](https://www.theinformation.com/briefings/google-unveils-gemini-4-argon-pricing-well-rivals) · [@sundarpichai](https://x.com/sundarpichai/status/2105387952478277979) · [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2105388087367127256) · [@arena](https://x.com/arena/status/2105411271525052418) · [@demishassabis repost](https://x.com/demishassabis/status/2105472587354780010)
**Raw:** [The Decoder raw](../../raw/rss/2026-09-30-the-decoder-google-gemini-4-argon-closes-the-gap-with-openai-and-an.md) · [The Information raw](../../raw/rss/2026-09-30-the-information-google-unveils-gemini-4-argon-pricing-it-well-below-riv.md) and the 2026-10-01 X feed captures

## TL;DR

Google launched Gemini 4 Argon on 2026-09-30 (US), its first frontier model in about seven months, pitched at long-horizon workflows, cyber defense and software engineering. It has a **1M-token output limit**. Access starts with select testers; API and paid tiers follow. Independent testing (The Decoder) puts it level with GPT-6 Astra but behind Claude Opus 5.5. The per-token price is well below rivals, but **Argon burns more than twice as many tokens per task as Astra**, so per-task cost is the honest comparison. Arena's Agent Arena lists Argon (High) at #8 with a $0.62 cost per task, on the Pareto frontier.

## Google's internal-use claims

- Argon agents read Google's server data and **freed over 300 TiB of data-center memory**, with up to 1 PiB expected.
- Given quantum software to shrink, it found a version needing 40% fewer qubits and operations than the best published human solution.
- Argon agents are converting legacy C and C++ to Rust, including an 800K-line OS kernel.

These are vendor claims without methodology.

## Why it matters here

- **Token-per-task, not price-per-token.** The 09-30 DevDay page recorded GPT-6.1 Sol at a fifth of Astra's price. Argon's low sticker price paired with 2x token use is the same lesson from the other side: compare cost per successful task, the metric the [llm-routing](../ai-routing/llm-routing.md) page adopted on 09-27.
- **A 1M-token output limit** is a KV-cache and decode-time commitment, not just a context feature (see [kv-cache](../inference-efficiency/kv-cache.md)).
- **Agents optimizing infrastructure** (300 TiB reclaimed) is the first frontier-lab claim of agents cutting hardware need directly, relevant to [compute-economics](../hardware/compute-economics.md).

## Links

- Digest: [2026-10-01](../daily-digest/2026-10/2026-10-01.md)
- Prior: [OpenAI DevDay 2026](2026-09-30-openai-devday-2026.md)
