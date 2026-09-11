# Interconnects: Open-Source AI and Open Models Reading List

**Source:** Nathan Lambert / Interconnects, 2026-09-11
**Raw:** [raw/rss/2026-09-11-interconnects-ai-open-source-ai-open-models-reading-list.md](../../raw/rss/2026-09-11-interconnects-ai-open-source-ai-open-models-reading-list.md)
**Links:** [Post](https://www.interconnects.ai/p/open-source-ai-reading-list)

## TL;DR

Nominally a curated bibliography, in practice the most useful single document on the open-model question in this wiki, and it landed on the same day Anthropic's threat report made open-versus-closed a national-security story. It is organized in three parts: **Foundation** (what open models are and why labs release them), **US-China Competition** (who leads, how that changed, and the regulatory history), and **Technical Details** (distillation, cyber risk, and how far behind open models actually are). The reason it earns a page rather than an Industry Pulse bullet is that the third section is an argument, not a list, and it is the argument the day's dominant story needs.

## The claims worth carrying

**The open-closed gap is roughly 4 to 6 months, and every leading open model since about 2024 has come from a Chinese lab.** The evidence he cites is triangulated rather than asserted: SemiAnalysis's independent evaluations in *Are Open Models Catching Up?* (Aug 2026), Epoch AI's benchmark trend data, Artificial Analysis's open-versus-proprietary intelligence series, and Håvard Tveit Ihle's independent analysis across public and private evals (May 2026). Four sources, different methodologies, converging.

**Distillation is "the single most eventful debate around open models in 2026,"** and his position has three parts that are often collapsed into one. It genuinely helps Chinese labs. It does not take away from their innovation. And the political framing, that distillation is the *only* reason Chinese models are near the frontier, is not grounded in the evidence, which is the thesis of his earlier [The Distillation Panic](../inference-efficiency/2026-05-04-distillation-panic-lambert.md).

**He revises a prior confident claim, in public, with the reason.** In April 2025 he wrote confidently that DeepSeek did *not* distil OpenAI's o1. He now writes that, given the reasoning-trace extraction methods documented in [Stealing Reasoning Traces from Proprietary LLM APIs](https://arxiv.org/abs/2608.09867), it is more possible than he gave it credit for, and notes that **Anthropic confirmed the technique was used by Chinese labs** in the report published that same day. This is the intellectual event in the post. An analyst updating a named prior with the specific evidence that moved him is worth more than the bibliography.

**Adoption is moving on cost, with named cases.** Perplexity adopting DeepSeek R1 in January 2025, Thomson Reuters building on Qwen to move off Claude (Business Insider, Aug 2026). Against that, lawmakers have probed DoorDash, Airbnb, Anysphere/Cursor and Apple over their use of Chinese models. Both pressures are live simultaneously.

**Release velocity is a strategy, not an accident.** He quotes Z.ai's product lead from Nov 2025: "Get it out fast. We open source it within a few hours."

## How this relates to prior wiki pages

**It is the counterweight the [Anthropic threat report page (09-11)](2026-09-11-anthropic-threat-report-illicit-distillation.md) needs, published the same day and citing it.** The report frames illicit distillation as the story. Lambert's list, which links directly to the report's illicit-distillation anchor, frames it as *one input among several* into a gap that independent evaluation puts at 4 to 6 months. This wiki should hold both: the extraction happened at nine-figure scale and is confirmed, **and** the causal claim that extraction explains the gap remains unsupported by the measurement that would settle it.

**It sharpens the open question the [knowledge distillation page](../inference-efficiency/knowledge-distillation.md) has carried since the trace-extraction paper.** That question is whether trace-level theft is actually competitive with licensed dense supervision, since a recovered trace gives you text but not the teacher's per-token distribution. Lambert's own July 2026 piece on distillation's performance uplift is the closest published attempt at that number, and his framing here, that distillation matters in an era of scaling RL environments across agentic behaviours, suggests the answer is task-dependent rather than a single ratio. Still nobody has measured it directly.

**It also names a risk position this wiki should record.** Citing Joshua Saxe (Jul and Aug 2026), he argues you cannot effectively ban open models to deny bad actors cyber capability, because those actors will always have access, and that the policy response should be observation and orientation rather than in-house capability assessments gating releases. That is a concrete, falsifiable governance stance rather than a mood, and it sits directly against the direction the threat report's reception pushed the discourse today.

## Gaps

It is a reading list, so its own claims are load-bearing only in the framing sentences, and the strongest ones (the 4-to-6 month gap, distillation's real but bounded contribution) are inherited from the cited sources rather than re-derived. The author is an interested party: he runs the ATOM Project advocating US investment in open models, which he discloses by linking it, but it shapes the selection. And the technical section's cyber subsection is explicitly marked "to develop," so the risk half of the argument is the thinnest part.

## Related

- [Anthropic threat report: illicit distillation (09-11)](2026-09-11-anthropic-threat-report-illicit-distillation.md)
- [The Distillation Panic (05-04)](../inference-efficiency/2026-05-04-distillation-panic-lambert.md)
- [Knowledge distillation](../inference-efficiency/knowledge-distillation.md)
