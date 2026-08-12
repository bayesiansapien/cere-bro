# Three benchmarks, one shape of failure: DSAgentBench, SPIEval, VibeLifeBench

**Source:** HuggingFace Daily Papers, 2026-08-12 · [DSAgentBench 2608.10366](https://arxiv.org/abs/2608.10366) · [SPIEval 2608.10692](https://arxiv.org/abs/2608.10692) · [VibeLifeBench 2608.10875](https://arxiv.org/abs/2608.10875)

**TL;DR.** Three benchmarks landed on one board, each measuring a different kind of real-world agent work, and all three report the strongest available model failing roughly half the time or worse. What makes them worth reading together is not the scores. It is that two of the three diagnose *the same underlying failure*: the agent stops gathering evidence too early and commits to a plausible guess. SPIEval measures this directly and puts a number on it: **79% of failures come from inaccurate information localization**, with fewer than 2% of retrieval actions using any advanced search method.

---

## The three

**DSAgentBench** (2608.10366) puts agents in a real computer environment to run end-to-end data-science workflows: wrangling, exploration, modeling, visualization and validation, coordinating notebooks, IDEs, terminals, browsers and databases. 275 tasks, each with a deterministic evaluator that checks analytical correctness, visual outputs and model performance rather than just whether code ran. Fifteen models tested. **Claude-4.6-Sonnet, the strongest, reaches 56.70%. Every open-source agent stays below 1%.** Failures concentrate in tool orchestration, OS grounding and multi-step reasoning. [Code released](https://github.com/vis-nlp/DSAgentBench).

**SPIEval** (2608.10692) tests LLMs as mobile assistants working over personal information scattered across apps: 250 human-curated tasks, 4,335 personal records across 10 apps, 21 tools, multi-turn. It is built around five named capabilities: reasoning, disambiguation, integration, preference inference and multi-intent decomposition. **GPT-5.5 (xhigh) reaches 57.3%; the weakest model 16.4%.** The diagnostic result is the valuable one: **79% of failures are inaccurate information localization**, because models "commit to plausible but incorrect information instead of continuing retrieval for verification," and **under 2% of retrieval actions use advanced search methods** at all. [Dataset](https://huggingface.co/datasets/Junjie-Ye/SPIEval).

**VibeLifeBench** (2608.10875) is the hardest to game and the most different in kind. 200 long-horizon tasks across ten everyday-life domains, each a scripted multi-week timeline inside a simulated world of 22 mock services. The world **advances on its own clock and many of its changes are silent**, so only an agent that re-inspects the world discovers them. Grading reads only what the agent actually left behind, and covers end state, timeliness of actions, and whether implicit constraints were upheld. Seven frontier models tested; **all score low**. The design target is proactivity and consistency: deciding when to act, when to ask, and when to stay silent, over weeks.

## The shared diagnosis, and why it matters more than the scores

SPIEval's 79%-localization finding and DSAgentBench's "grounding decisions in intermediate outputs" requirement are the same failure seen from two angles. In both, the agent has access to the information it needs and stops looking before it has it. VibeLifeBench turns that failure into the entire task design: a world that changes silently punishes exactly the agent that does not re-inspect.

**This wiki already named that faculty, twice, and it is the same one.** The [self-evolving-agents concept page](self-evolving-agents.md) recorded on 08-06 that three of four negative results converged on one missing faculty: **deciding what to do with a resource you already have.** [Shadow evaluations (08-06)](2026-08-06-shadow-evaluations-open-ended-research.md) found frontier agents ending research runs with **under 50% of budget spent and hours remaining** despite being told to spend down. [InMind (07-29)](2026-07-29-inmind-implicit-association-blind-spot.md) found retrieval memory surfaces a fact only when it resembles the query, six systems at at most 14.4% on indirect queries against 84.0% for the same memory simply placed in context. SPIEval's under-2%-advanced-search figure is the cheapest, most direct measurement of that faculty anyone has published. It is not that the agents search badly. It is that **they mostly do not search at all**, and then commit.

## How this relates to what the wiki already knows

**This is the second consecutive day of agent-benchmark papers, and the framing has shifted in a useful way.** The 08-10 and 08-11 boards produced four benchmark-*validity* failures in two days: [SWE-Bench ProMax (08-11)](2026-08-11-swe-bench-promax.md) citing nearly 60% of unsolved SWE-bench Verified instances having flawed tests, [StreamArena (08-10)](2026-08-10-streamarena-streammind.md) finding a four-frame baseline matching complex streaming models, plus A²E arguing correctness cannot describe a harness. Those were papers saying *the instruments are broken*. Today's three are papers **building instruments that are hard to break**: deterministic multi-artifact evaluators (DSAgentBench), human curation with named capability axes (SPIEval), and a world clock that advances whether the agent looks or not (VibeLifeBench). The measurement crisis is entering its constructive phase.

**And the timing against the same board's self-improvement papers is the sharpest thing here.** The same 2026-08-12 HuggingFace board carries [Mendel Gödel Machine](2026-08-12-mendel-godel-machine.md), which improves how a coding agent rewrites its own source code, and the [Co-Evolution survey](2026-08-12-co-evolution-survey.md), which taxonomizes agents and environments imposing adaptive pressure on each other and asks whether the evolution mechanism itself can evolve. Meanwhile the best agent in the world completes 56.70% of real data-science tasks and open-source agents complete under 1%. **The recursive-improvement literature and the measured-capability literature are describing different objects on the same day**, and this wiki has now logged that gap for three consecutive days, since Ouroboros's 86.74% on Terminal-Bench sat next to ProMax's 41.2% on 08-11.

**VibeLifeBench also supplies the horizon test the memory literature has been missing.** The concept page's standing complaint about the self-evolution cluster is that everything is "validated on episodes measured in dozens of steps rather than days," so "whether learned curation survives at the horizon where drift actually appears is the untested question that matters most." VibeLifeBench's multi-week timelines with silent world changes are that horizon, in a simulator, with grading that reads only durable artifacts. It is the natural evaluation target for [RoMeRL (08-11)](2026-08-11-romerl-reduced-order-memory.md)'s bounded memory states and [SkillZip (08-12)](2026-08-12-skillzip-skill-compression.md)'s compressed skills, and neither has been run on it.

## Gaps

- **DSAgentBench's sub-1% open-source result is suspicious as a capability claim.** A floor that uniform across many models usually indicates a harness or environment-interface failure rather than a reasoning gap, and the paper attributing it to "tool orchestration, OS grounding" is consistent with that. Whether a better harness lifts open models substantially is unreported, and A²E's finding that harness choice swings outcomes as much as the model makes it the obvious confound.
- **All three are simulated or mock environments.** VibeLifeBench's 22 services are mocks, SPIEval's 4,335 records are curated, and DSAgentBench's "real computer environment" is still a controlled one.
- **No cost reporting in any of the three.** A long-horizon multi-week benchmark where an agent must repeatedly re-inspect the world has a token bill that is part of the result, and it is absent.
- **SPIEval's 79% localization figure is not decomposed by which of its five capabilities failed**, so the headline diagnosis is not yet actionable.

## Related

- [agent-benchmarks.md](agent-benchmarks.md) · [self-evolving-agents.md](self-evolving-agents.md) · [agent-memory.md](agent-memory.md)
- [Mendel Gödel Machine (08-12)](2026-08-12-mendel-godel-machine.md) · [Co-Evolution survey (08-12)](2026-08-12-co-evolution-survey.md)
- [SWE-Bench ProMax (08-11)](2026-08-11-swe-bench-promax.md) · [StreamArena and StreamMind (08-10)](2026-08-10-streamarena-streammind.md)
- [Shadow evaluations (08-06)](2026-08-06-shadow-evaluations-open-ended-research.md) · [InMind (07-29)](2026-07-29-inmind-implicit-association-blind-spot.md)
- [Daily digest 2026-08-12](../daily-digest/2026-08/2026-08-12.md)
