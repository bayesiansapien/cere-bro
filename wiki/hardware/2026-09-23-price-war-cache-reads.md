# The price war of 2026-09-22, and the number inside it that matters: cache reads fell 60%

**Source:** [Simon Willison](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) · [The Decoder on GPT-6 Sol/Luna](https://the-decoder.com/openais-gpt-6-sol-and-luna-cut-prices-in-half-but-barely-move-the-needle-on-performance/) · [The Decoder on Opus 5.5](https://the-decoder.com/claude-opus-5-5-matches-fable-5-1-at-40-percent-lower-cost-as-anthropic-promises-to-fix-claudish-writing/) · [The Information](https://www.theinformation.com/)
**Raw:** [raw/rss/2026-09-22-simon-willison-claude-opus-5-5-gpt-6-sol-gpt-6-luna-and-a-new-price-wa.md](../../raw/rss/2026-09-22-simon-willison-claude-opus-5-5-gpt-6-sol-gpt-6-luna-and-a-new-price-wa.md)

## TL;DR

On 2026-09-22 Anthropic released Claude Opus 5.5 and, about an hour later, OpenAI released GPT-6 Sol and GPT-6 Luna. Anthropic cut Opus from $5/$25 per million input/output tokens to **$4/$20**, a 20% reduction, after five consecutive releases held that price. OpenAI halved both new models against their GPT-5.6 equivalents, putting **GPT-6 Luna at $0.10/$0.50**, one of the cheapest models it has ever shipped. The headline everyone wrote was the price war. **The number that matters for anyone building agents is the third column: Opus cache reads fell from $0.50 to $0.20 per million, a 60% cut, three times deeper than the headline cut.**

## The pricing landscape

| Model | Input | Cached input | Output |
|---|---|---|---|
| GPT-6 Luna | $0.10/M | $0.01/M | $0.50/M |
| GPT-5.6 Luna | $0.20/M | $0.02/M | $1.20/M |
| Grok 4.7 | $2/M | $0.50/M | $6/M |
| GPT-6 Sol | $2/M | $0.20/M | $10/M |
| **Claude Opus 5.5** | **$4/M** | **$0.20/M** | **$20/M** |
| GPT-5.6 Sol | $4/M | $0.40/M | $20/M |
| Claude Fable 5.1 | $10/M | $0.25/M | $50/M |
| GPT-6 Astra | $10/M | $1/M | $50/M |

GPT-5.6 has a scheduled 25% price increase for November, so GPT-6 is half the price of *promotional* pricing on the models it replaces. The war is being fought in the tier below the flagships: Astra and Fable 5.1 both sit untouched at $10/$50.

## Why the cache-read line is the real story

Simon Willison states the mechanism plainly: in longer agentic conversations, **90%+ of input tokens are processed at cached token prices.** So for an agent workload, the cached-input column is most of the input bill, and Opus 5.5 cut it by 60% while cutting the headline input price by 20%.

That is a deliberate pricing signal about where the load is. Anthropic is not discounting inference, it is discounting **prefix reuse**, which is the specific thing an agent loop does hundreds of times per task. The wiki has been treating the KV cache as a technical object with compression ratios and eviction policies. This is the [08-14 kv-cache entry](../inference-efficiency/kv-cache.md), "the cache becomes a billing surface," maturing into the phase where **the billing surface is being used as a competitive weapon and is moving faster than the compute price around it.**

## How this connects to the rest of the wiki

**It validates the harness-cost thesis with a vendor's own price sheet.** [HarnessTax (09-22)](../agentic-systems/2026-09-22-harnesstax-cost-success-frontier.md) found that across 21 model-harness combinations, cost per attempt spanned $0.67 to $1.33 while success spanned 96.7% to 97.8%, and traced the spread to standing context: longer instructions and larger tool definitions ride along on every call, so a heavy harness pays its fixed overhead once per turn. **Standing context is exactly what a cached prefix is.** A 60% cut in cache-read price cuts the harness tax by 60% for every heavy harness, which narrows the gap HarnessTax measured without anybody changing a line of harness code.

**It cuts against the Meta-Harness and RRSI optimization case, slightly.** Today's Stanford/MIT Meta-Harness reports discovered harnesses beating hand-engineered agents on TerminalBench-2 while **cutting context token usage 4x**, and [RRSI (09-22)](../agentic-systems/2026-09-22-rrsi-regularized-harness-evolution.md) produced a harness running on 30% fewer policy tokens. Those are token-count optimizations whose dollar value just fell by 60% on the cached portion. The optimizations still matter for latency and for context-window pressure, but the *economic* argument for them weakened on the same day the papers landed.

**The 09-21 prediction that "price was never the binding constraint, calibration is" survives contact with this.** The [llm-routing](../ai-routing/llm-routing.md) page recorded that claim two days ago, on evidence that the crudest possible routing policy (send everything cheap) already captures most of the available saving. A 50% price cut on the cheap tier and a 60% cut on cache reads makes the cheap-by-default policy cheaper still, which *strengthens* rather than weakens the finding: if the market keeps cutting prices faster than routers can learn, a learned router's payback period keeps receding.

**The economics are moving in one direction and the infrastructure costs in the other, which is the tension to watch.** The same week: data-centre bonds on a Jane Street-leased build yielding 11.3% against an August issue two points tighter; CoreWeave completing an upsized **$4.2 billion** convertible; Anthropic in talks to lease up to **1 gigawatt** directly from Apollo-controlled Stream Data Centers to reduce cloud dependence, filling it with Broadcom-and-Google-designed TPUs; the CFTC stalling CME's GPU rental futures; roughly **$130 billion** of US data-centre projects blocked or delayed in Q1 2026 with 71% of surveyed Americans opposing one near them; and Texas freezing new grid-connected projects. **Token prices are falling while the cost of the capacity to serve them is rising and its financing is getting more expensive.** Those cannot both continue indefinitely.

## The quality caveat nobody should skip

The Decoder's read is that GPT-6 Sol and Luna "barely move the needle on performance," and independent analyses found little gain in actual intelligence: this is a price cut, not a capability release. And Willison recorded a concrete regression on Opus 5.5 at "max" thinking level, which **failed to return a response at all** on his standard SVG test, twice, because it exhausted the 128,000-token output limit while still reasoning. Two failures at $2.56 each and nearly 20 minutes. His conclusion, that max is "effectively useless" if it over-thinks to breaking point on a trivial prompt, is a data point directly supporting [Taste-Bench's finding](../agentic-systems/2026-09-23-taste-bench-tasteful-agent.md) today that a larger reasoning budget does not improve decision quality. **Two independent observations on the same day that the effort knob has a ceiling and possibly a cliff.**

## Related pages

- [compute-economics](compute-economics.md) · [kv-cache](../inference-efficiency/kv-cache.md) · [llm-routing](../ai-routing/llm-routing.md)
- [HarnessTax](../agentic-systems/2026-09-22-harnesstax-cost-success-frontier.md) · [Taste-Bench](../agentic-systems/2026-09-23-taste-bench-tasteful-agent.md)
