# Gowers + ChatGPT 5.5 Pro: PhD-level math research in under two hours

**Source:** [The Decoder, 2026-05-09](https://the-decoder.com/fields-medalist-says-chatgpt-5-5-pro-delivered-phd-level-math-research-in-under-two-hours-with-zero-human-help/) · [raw](../../raw/rss/2026-05-09-the-decoder-fields-medalist-says-chatgpt-55-pro-delivered-phd-level.md)
**Tier:** 2 — Active learning (intersects Tier 1 research-agent thread)

## TL;DR

Fields Medalist Timothy Gowers gave ChatGPT 5.5 Pro open problems in number theory. Within an hour, the model improved a known exponential bound to a polynomial one. An MIT collaborator on the problem called the key idea "completely original." Gowers' own framing: the bar for human mathematical contribution is now "prove something LLMs can't do."

## What is being claimed

- ChatGPT 5.5 Pro produced a meaningful research-grade contribution on a real open problem with **zero human help during the two-hour run**.
- The improvement was structural, exponential to polynomial bound, not arithmetic tightening of constants.
- An independent expert (MIT) inspecting the proof said the central idea was novel.
- Gowers' meta-claim is the headline: research mathematics is now in the regime where the marginal human contribution must be defined as "what the model cannot do."

## Why this matters in light of prior wiki pages

This is the third data point in two weeks for the "AI does science" thread.

- **2026-05-09 — AI Co-Mathematician (FrontierMath Tier 4 at 48%)** sets the agentic-workbench benchmark for math research. Gowers' run is the human-evaluated complement: a Fields Medalist running a real open problem rather than a curated benchmark.
- **2026-05-09 — Auto Research with Specialist Agents (+38.7% on NanoChat-D12 CORE)** does the same thing for ML research recipes: closed-loop empirical search, no human in the loop.
- **Kurate cs.AI #5 this week — "AI scientists produce results without reasoning scientifically"** is the explicit counter-claim. Gowers' run is one anecdotal datapoint that pushes against that framing in this specific case (a real problem, an expert reviewer, a structural improvement). It does not refute the cs.AI #5 claim, which is a methodology critique about reproducibility and reasoning patterns. Both can be true.

The composition with the **Skill curation cluster** (StraTA, Skill1, SkillOS — also from yesterday) is not yet realized. Gowers' two-hour run is a single-shot inference from an off-the-shelf chat model, not a skill-augmented agent. The natural follow-up is the same problem class with an agent that has persistent failed-hypothesis memory.

## Open questions

- **Reproducibility.** A single run on a single problem with an expert reviewer is an existence proof, not a frequency claim. What fraction of Gowers-tier open problems can ChatGPT 5.5 Pro improve in two hours?
- **The "originality" bar.** The MIT collaborator called the idea "completely original." Originality of an idea is hard to verify without exhaustive literature search; the model could have surfaced a 1970s-era technique that the modern reviewers had forgotten. Worth tracking whether the proof appears in any prior literature.
- **What survives peer review.** The bound improvement still has to clear refereeing. The wiki should track whether a written-up proof appears on arxiv with both Gowers and the model credited as authors, or whether the improvement gets reframed by the human author after re-derivation.

## Implication for cere-bro tracking

Gowers' "now the bar is what LLMs can't do" line is the framing every research-agent paper should be measured against from this point forward. The skill-curation, agentic-workbench, and Auto-Research papers are all building toward this regime. The Fields-Medalist-attested datapoint says the regime has arrived in at least one subdomain (analytic number theory).

## Related pages

- [AI Co-Mathematician (2026-05-09)](../agentic-systems/2026-05-09-ai-co-mathematician.md)
- [Auto Research with Specialist Agents (2026-05-09)](../agentic-systems/2026-05-09-auto-research-specialist-agents.md)
- [GPT-5.5 launch + system card (2026-04-24)](2026-04-24-gpt-55-launch-system-card.md)
