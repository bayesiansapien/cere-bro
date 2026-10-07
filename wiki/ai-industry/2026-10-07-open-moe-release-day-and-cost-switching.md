# Open MoE release day, companies switching models on cost, and OpenAI's 722 math manuscripts

**Sources:** [The Decoder on Beam](https://the-decoder.com/reflections-beam-becomes-the-most-capable-open-weight-model-built-outside-china/) · [The Decoder on Mistral Large 4](https://the-decoder.com/mistral-large-4-is-said-to-be-the-most-powerful-open-ai-model-from-europe-and-the-u-s/) · [Mistral Large 4 model card](https://huggingface.co/mistralai/Mistral-Large-4.0-1T05-A52B) · [Marin 535B-A23B thread](https://x.com/stanfordnlp/status/2107517241361379758) · AI Weekly "AI got too expensive, so companies are moving to cheaper models" (Gmail) · [The Information: token maxing to value maxing](https://www.theinformation.com/articles/ai-agenda-live-token-maxing-value-maxing-getting-every-unit-compute) · [The Information: Nvidia's dealmaking](https://www.theinformation.com/articles/nvidias-100-billion-dealmaking-juggernaut-will-go-next) · [OpenAI math repo](https://github.com/openai/math) · [The Decoder on OpenAI math](https://the-decoder.com/openai-dumps-372-ai-generated-math-proofs-on-github-telling-the-academic-world-to-keep-up/)
**Raw:** `raw/rss/2026-10-06-the-decoder-reflection-s-beam-*.md` · `raw/rss/2026-10-06-the-decoder-mistral-large-4-*.md` · `raw/rss/2026-10-07-the-information-ai-agenda-live-*.md` · `raw/rss/2026-10-07-the-information-where-nvidia-s-*.md` · `raw/rss/2026-10-07-the-decoder-openai-dumps-*.md` · `raw/gmail/2026-10-07-newsletters.md` (gitignored)

## TL;DR

**Open MoE (mixture-of-experts: each token runs through a few specialist sub-networks, so compute follows active, not total, parameters).** Three large Western open MoEs landed in one US day, all sold on cost per active parameter:

| Model | Total | Active | Notes |
|---|---|---|---|
| Reflection Beam | 501B | 23B | 23.8T tokens on 6,144 GB300s; **RL on 10,500 GB300s for 4 weeks, 100M+ rollouts, ~1M environments**; claims GLM-5.2 quality at 3-4x less compute (estimated from active params, not measured); FP8/NVFP4 Apache-2.0 weights later this month |
| Mistral Large 4 | ~1T | ~52B | natively multimodal; weights on HF; pitched at security work US models refuse; Intelligence Index still well behind Claude, GPT-6 and Chinese leaders |
| Marin (Stanford) | 535B | 23B | fully open lab, half-trained, training log public |

**Cost switching becomes the norm.** Harvey's gross margin fell from ~50% to **-50%** as token use grew 20x; it moved to its own model on Moonshot's open-weight Kimi K3 and margins turned positive (Bloomberg via AI Weekly). Open models carry **40% of AT&T's AI workloads** (FT). Anthropic ends ~15% enterprise discounts once contracted volume is used up. Uber says token costs stabilized while agent use grew, crediting caching pushed down to sub-agents and per-engineer usage visibility; NVIDIA pitched Dynamo's KV-cache lookup to avoid recomputation; Nebius tunes speculative decoding on each customer's traffic. The panel's phrase: from "token maxing" to "value maxing", measured as turns, tokens and dollars per outcome. Musk said SpaceX's Grok Bot will use "the best back end model for any given task, including Claude".

**Capital.** SpaceX seeks **$40B led by Apollo to buy Nvidia chips** ($10B loans, $30B other; close in 2027). Nvidia inked **$140B+ of deals in two months**, including a $105B credit guarantee, after losing OpenRouter to Stripe's $8B bid. A new company from Anjney Midha and ex-Google/Apple/Nvidia executives aims to make GPU access cheaper for startups.

**OpenAI's math drop.** OpenAI published 722 manuscripts (372 result families) from an unreleased internal model, run on ~4,000 open problems at about 3 hours of compute each, many with Lean formalizations. One claims to lower the matrix-multiplication exponent from ~2.3712 (AlphaEvolve's August record) to ~2.25, a theoretical bound with no practical GPU routine. 25 Fields medalists warned mass-produced results could crowd out fertile ground; a Hacker News commenter who spent 24 years on Barnette's Conjecture saw it listed as solved.

## Relation to prior wiki pages

- **Resolves part of a 10-06 prediction.** The 10-06 digest predicted another large customer would publicly cap frontier spend within 30 days. AT&T (40% open) and Harvey (margin-driven switch) are switching rather than capping, and Nvidia, Palantir and Booz Allen restricted Anthropic's Fable over 30-day log retention. Partial resolution: the behaviour is spreading, though not yet as a Fortune-100 per-seat cap.
- **RL compute overtaking pretraining** is now a vendor-disclosed number (Beam), confirming the [compute economics](../hardware/compute-economics.md) thread and the [RL infrastructure](../hardware/2026-10-07-fbtriton-tbe-rl-kernel-coco.md) response.
- **Active-parameter marketing** links to [looped transformers](../llms-foundation-models/looped-transformers.md) and the looped-MoE debate (Foil vs LOOM): both lines try to buy quality per active FLOP.

## Related

[Subscription economics (10-06)](2026-10-06-subscription-economics-and-claude-pullback.md) · [LLM routing](../ai-routing/llm-routing.md) · [Compute economics](../hardware/compute-economics.md)
