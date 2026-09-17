# Harness choice barely moves success rate and strongly moves cost (7 models x 3 harnesses)

**Source:** X home feed, [@melissapan](https://x.com/melissapan/status/2100278487185817818), amplified by [@matei_zaharia](https://x.com/matei_zaharia/status/2100286529633706166)
**Status:** social-sourced research preview. Thread reports results; no paper link attached at time of capture.

## TL;DR

The study evaluates **seven models across three coding-agent harnesses** (Claude Code, Codex, and Pi) and reports three findings, all of which land on this wiki's most active concept page. First, **harness choice has little effect on task success rate but can significantly affect cost**. Second, **a simple harness can be competitive** with a heavily engineered one. Third, **the native harness is not always the best** for its own model. Matei Zaharia's framing of the same result is the one to keep: harnesses make a lot of difference **at least for cost**, even on open-source coding benchmarks.

## Why this matters here

The [agent-harness-engineering](agent-harness-engineering.md) page has spent five weeks accumulating evidence that the harness is an optimizable cost surface separate from the model. What it has not had is a **factorial** measurement: the same models run through several harnesses with success and cost reported separately. Almost every prior result varies one axis. This varies both and separates the outcomes, and the separation is the finding: **the harness is nearly free on the quality axis and expensive on the cost axis.**

That is a stronger and more useful claim than "harnesses matter," because it tells you what to optimize the harness **for**. If success rate is roughly harness-invariant across a reasonable set of engineered harnesses, then harness engineering is a pure cost-reduction exercise at a fixed quality bar, which is a much easier optimization problem than a joint one.

## How this relates to what the wiki already knows

**It is the fourth independent source in eight days naming harness efficiency as a measurable, separable quantity, and the first to say the quality axis is flat.** [SoL-Pi (09-11)](2026-09-11-sol-pi-harness-auto-research.md), which auto-searched harness configurations, cut tokens **45-49% while holding about 94% of task score** and beat GPT-5.6 Sol's own native Codex harness on EdgeBench. [Elo-per-token (09-15)](../inference-efficiency/2026-09-15-elo-per-token-agent-test-time-scaling.md), which converts within-task solution quality at each token budget into a cross-task Elo, located the budget at which an agent's marginal token stops beating an independent sample and showed that re-slicing 100M tokens across parallel sessions at that cap buys **+264 Elo at the same bill**. [OpenAI's software factory account (09-16)](2026-09-16-openai-agentic-software-factory.md) named harness efficiency as a live operational constraint at a frontier lab. This adds the controlled comparison the other three lacked.

**"The native harness is not always the best" is a direct confirmation of SoL-Pi's most contested single result.** That paper's headline was that a searched harness beat the model vendor's own harness for that vendor's own model. One result is an anomaly. Two independent results, one from automated search and one from a controlled seven-model sweep, is a finding: **vendor-native harnesses are not tuned to the frontier of their own model's capability.** The commercial reading matters more than the technical one. It says the integration moat that [OpenAI's account (09-16)](2026-09-16-openai-agentic-software-factory.md) describes, total dependence on one harness with the model fixed, is a moat built on switching cost rather than on the harness being better.

**"A simple harness can be competitive" is the awkward one, and it contradicts the direction of this page's own recent literature.** [HarnessDev (09-03)](2026-09-03-harnessdev-harness-creation-evolution.md), [Ecdysis (09-12)](2026-09-12-ecdysis-harness-training.md) and [COBRA-Skills (09-13)](2026-09-13-cobra-skills-robustsgpo-harness-search.md) all invest search or training budget in producing a **better** harness. If a simple harness is competitive on success rate, then what all that search actually buys is the cost reduction, not the capability, which is consistent with SoL-Pi's own numbers (45-49% fewer tokens, ~94% of score) but is not how that work is usually framed. Stated plainly: **harness search is a compiler optimization, not a capability unlock.**

**It also closes a specific gap in the routing page.** [The routable unit is the model-harness pair](../ai-routing/llm-routing.md) has been an entry there since 08-26 with no proposal attached. The obstacle was always that nobody had priced the pair's two coordinates separately. If success is harness-flat and cost is harness-sensitive, the routing decision factorizes: **choose the model for quality, choose the harness for cost, and the two decisions do not interact much.** That is the first time this page can say what a model-harness router should actually optimize.

## Gaps

This is a thread, not a paper, and the numbers behind "significantly affect the cost" are not in the captured text. Three harnesses and seven models is a small grid, and coding benchmarks are the domain where harness design is most mature and therefore where the harnesses are most likely to have converged, so the flat-success finding may not transfer to domains with less-developed tooling. There is also no reported variance: "little effect on task success rate" across seven models could hide per-model reversals that matter for a router. And crucially, nothing here reports cost-per-**success**, which is the quantity the [08-28 entry](2026-08-28-pilot-live-self-improvement.md) argued is the only one that composes.

## Research angle

The falsifiable version is the interaction term. If success is harness-flat on average but the per-model ranking of harnesses changes across models, then the flat average is hiding exactly the structure a router needs, and the right output is a model-by-harness cost matrix rather than a headline. The first public version of such a matrix appeared on [Terminal-Bench 3.0 (08-13)](agent-harness-engineering.md) and has not been reproduced since. This study has the data to produce the second one.

## Related

- [agent-harness-engineering.md](agent-harness-engineering.md) · [llm-routing.md](../ai-routing/llm-routing.md)
- [SoL-Pi (09-11)](2026-09-11-sol-pi-harness-auto-research.md)
- [Elo-per-token (09-15)](../inference-efficiency/2026-09-15-elo-per-token-agent-test-time-scaling.md)
- [Inside OpenAI's agentic software factory (09-16)](2026-09-16-openai-agentic-software-factory.md)
- [LangChain custom agent harness (09-14)](2026-09-14-langchain-custom-agent-harness-middleware.md)
