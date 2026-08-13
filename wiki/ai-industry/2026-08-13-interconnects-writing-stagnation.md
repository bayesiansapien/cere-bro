# Interconnects: "I wrote an AI textbook. How long until AI can do it better?"

**Source:** Nathan Lambert, [Interconnects](https://www.interconnects.ai/p/i-wrote-an-ai-textbook-how-long-until) · [raw](../../raw/gmail/2026-08-13-starred.md) (starred Gmail)

## TL;DR

Nathan Lambert just finished writing a post-training textbook, *Reinforcement Learning from Human Feedback* (Manning / Amazon), using LLMs heavily throughout: LaTeX wrangling, copyediting, TikZ and Python diagram generation. His report from that experience is a genuinely load-bearing negative result, and it is not the usual complaint about AI prose being soulless.

The claim: **long-form non-fiction technical writing has stagnated while everything else raced ahead.** The models widely regarded as the best writers are old ones, GPT-4.5 and Kimi K2. Over the same interval, models went from mediocre to superhuman at coding and mathematics, and from incapable to decent at search and research. Writing did not move with them.

His diagnosis of the failure mode is specific and it is the part worth carrying forward. The models are excellent at **every individual unit of content**. GPT-5.5 Pro found deep, surprising typos across a 200-to-300-page manuscript. Claude models are the better editors, with more taste and a better mental model of the task. What they cannot do is **revisit components and string them together** as additions accumulate. Lambert calls it "a sort of irreducible compounding errors," and then makes the observation that turns this into a research claim rather than a gripe: **that is the same failure class that RLVR solved for math and code.** Reinforcement learning from verifiable rewards, where a checkable outcome supplies the training signal, was "a truly magical solution" for compounding errors in domains where correctness is checkable. Prose has no such checker.

The stakes he draws are the reason this belongs in the digest at all. **"Organizing knowledge is a compression. This compression is needed to make insight."** If today's LLMs *increase* entropy in long-form non-fiction, then the pipeline from "model reads the literature" to "model produces novel scientific insight" has a missing stage, and that stage is not a matter of scale. He writes this deliberately on the day Anthropic published Claude making progress on the Riemann Hypothesis, and his read is that scientific problems have vast breadth and current coverage is narrower than the headline results suggest.

He is explicit that he is not pessimistic about AI generally. His prediction is that LLM-for-science progress will look like **low-hanging fruit plus merging distant connections across fields**, with humans as guides, rather than revolutionary insight, until this is solved.

---

## Key claims

- **Writing quality has been roughly flat while coding, math, and search improved steeply.** The best-regarded writing models are old ones.
- **The failure is compositional, not local.** Per-sentence, per-equation, per-figure the models are strong. Across a chapter they produce muddled organization, confused wording, and "random conceptual errors" from trying to be cute where they need not be.
- **RLVR is the named precedent.** Compounding errors were the same problem in math and code, and a verifiable reward fixed it. There is no verifier for prose.
- **He does not expect harnesses to close this.** He names specialized harnesses like Claude Code, better prompts, and inference-heavy training environments as low-hanging fruit that will help "but I don't think these will have a multiplicative impact on ability."
- **Well under 1% of the book's sentences came from a model**, included only where he genuinely loved them.
- **The division of labor is stable and asymmetric**: GPT models for exhaustive local error-finding, Claude models for editorial taste and unsticking writer's block.

## How this relates to prior wiki pages

**His claim that harnesses will not fix writing lands on the same board as the strongest evidence yet that harnesses fix other things.** [AI4AI at Test-Time (08-13)](../inference-efficiency/2026-08-13-ai4ai-test-time-harness-transfer.md) nearly doubles a weak model's Theory-of-Mind accuracy from 0.49 to 0.91 by having a strong model write it an inference-time harness, with the target's weights frozen. Its own mechanism analysis explains *why* Lambert is probably right: the gains came from **offloading unstable reasoning into deterministic code, per-question-type routing, and strict answer-format enforcement**. All three require a checkable output. None of them has an analogue in "is this chapter well organized." The two pieces published on the same day and together they draw a boundary: the harness substitutes for capability wherever the output can be checked, and it has nothing to offer where it cannot.

**It is the sharpest available counter-argument to the [continual-learning market thesis (08-12)](2026-08-12-continual-learning-market.md).** Ben Lorica's survey of twenty-plus startups argues the economic case for systems that compress their own experience into durable improvement. Lambert's claim is that today's models **increase entropy** in exactly the operation that thesis depends on, organizing accumulated knowledge into a form that yields insight. If organizing is compression, and models are anti-compressive at length, then the loop compounds volume rather than understanding.

**It is a human-side confirmation of the [SkillZip (08-12)](../agentic-systems/2026-08-12-skillzip-skill-compression.md) premise.** SkillZip's whole method rests on an agent's accumulated skill file being substantially compressible, which is a measurement that appended text is structurally redundant. Lambert is reporting the same redundancy from the writer's chair, on prose the model produced.

**It extends the failure this wiki has named across four negative results since 08-06:** deciding what to do with a resource you already have. SPIEval found 79% of agent failures were inaccurate information localization with under 2% of retrieval actions using any advanced search. Lambert's models hold every unit of the book and cannot decide how to arrange them. Same faculty, different surface.

## Gaps in the argument

**It is one author, one book, one domain.** A post-training textbook is unusually structured and unusually technical; it is the hardest case for organization, which cuts both ways.

**"Best writing models are old" is a reputation claim, not a measurement.** No benchmark is cited, and long-form writing quality has no accepted benchmark, which is arguably the actual problem: **the absence of a verifier is simultaneously why training cannot fix it and why the stagnation cannot be quantified.**

**He does not test the strongest counter-case.** An inference-heavy loop with an explicit outline-then-fill-then-revise structure and a human-supplied structural check is closer to a real harness than what he describes using, and his dismissal of harnesses is asserted rather than tried.

## Industrial implication

The practical read for anyone using models on long documents is his division of labor, stated plainly: **use models for local verification at scale and for editorial provocation, keep global structure human, and do not expect that boundary to move soon.** That is a workflow recommendation with a mechanism behind it, not a preference.

The forecasting read is sharper. Every "AI does autonomous science" projection assumes the model can organize what it knows into a presentable argument. Lambert's point is that this is a strictly easier prerequisite than open-ended discovery, and it is currently not met. Anyone modeling AI research automation timelines should treat **long-form technical exposition quality as a leading indicator**, and it has not moved in a year.

---

**Related:** [AI4AI at Test-Time](../inference-efficiency/2026-08-13-ai4ai-test-time-harness-transfer.md) · [The continual-learning market](2026-08-12-continual-learning-market.md) · [SkillZip](../agentic-systems/2026-08-12-skillzip-skill-compression.md) · [Digest 2026-08-13](../daily-digest/2026-08/2026-08-13.md)
