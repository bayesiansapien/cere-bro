# OpenAI reasoning model disproves Erdős unit-distance conjecture

**Source:** The Decoder (Maximilian Schreiner), 2026-05-21, with critique by Gary Marcus (citing Cal Newport) and confirmation from Fields Medalist Tim Gowers and mathematician Thomas Bloom.

**Links:**
- [The Decoder writeup](https://the-decoder.com/openai-shifts-the-boundary-of-automated-reasoning-with-a-milestone-in-ai-mathematics-that-experts-are-now-unpacking/)
- [OpenAI announcement and companion article](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)
- [Bloom's companion PDF on the proof](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf)
- [Marcus critique](https://garymarcus.substack.com/p/checking-the-math-behind-openai-and)

## TL;DR

A not-yet-released OpenAI reasoning model produced a counterexample disproving a 1946 Paul Erdős conjecture on unit-distance geometry. Mathematicians extracted the counterexample from a long chain-of-thought transcript and rewrote it as a standard proof. Tim Gowers calls it a milestone and warns competing with AI on math problems will become very difficult. Cal Newport, communicated through Gary Marcus, says the headline is not that AI is now smarter than mathematicians but that pure chain-of-thought reasoning (without elaborate symbolic scaffolding) accomplished a result that previously required heavy computer-aided math infrastructure.

## What was proven

The 80-year-old Erdős conjecture concerned discrete geometry of unit distances in the plane. The community had largely assumed the conjecture was true. Bloom's commentary credits the LLM with succeeding precisely because the model did not share the human bias of presumed truth, and instead systematically applied techniques from algebraic number theory that human researchers had dismissed as unlikely to apply.

## Why this matters for cere-bro

Tier 1 / Tier 2 angle: the result is in the same lineage as the [Gowers GPT-5.5-Pro math post on 2026-05-10](2026-05-10-gowers-gpt55-pro-math.md) which established that frontier reasoning models can reach professional-mathematician productivity on graduate-level problems. The May 21 Erdős disproof escalates that one step further: a research result publishable in a top journal, not just a solved exam problem.

The interpretive split between Gowers (genuine milestone, hard to compete with AI from here) and Marcus/Newport (impressive but narrow, expensive, and analogous to how CAD made architects more capable rather than replaceable) is the active debate. Both can be true. The wiki should treat the result as load-bearing evidence for:

1. **Long chain-of-thought reasoning** as an effective way to approximate dynamic computation and memory inside a feed-forward LLM (Newport's framing).
2. **Smaller, cheaper, math-tuned LLMs combined with scaffolding** as the likely future direction once the marketing dust settles (Newport's prediction).
3. **Math + code as the narrow streetlight** under which current reasoning models excel, with much weaker evidence of generalization to open-ended business problems.

## Open questions

- No public data on inference cost per prompt or denominator of failed prompts. Marcus notes "we have a numerator but not a denominator."
- No public information on the model architecture, training recipe, or relationship to OpenAI's response to Anthropic's Mythos.
- Whether the systematic-techniques-application capability generalizes to other open math conjectures, or whether the Erdős problem was unusually ripe (because the field had stopped trying after assuming it true).

## Cross-references

- [Gowers GPT-5.5-Pro math (2026-05-10)](2026-05-10-gowers-gpt55-pro-math.md) — frontier reasoning at mathematician-level on contest-style problems.
- [Soohak research-math benchmark (2026-05-12)](2026-05-12-soohak-research-math-benchmark.md) — research-math evaluation methodology.
- Anthropic separately predicted Nobel-prize-level discoveries within a year (carried in the Twitter morning slot and 2026-05-22 social-stream).

## Source

Raw: `raw/rss/2026-05-21-the-decoder-the-first-ai-proof-worthy-of-maths-top-journal-landed-a.md` plus `raw/rss/2026-05-21-marcus-on-ai-checking-the-math-behind-openai-and-anthropics-latest-h.md`.
