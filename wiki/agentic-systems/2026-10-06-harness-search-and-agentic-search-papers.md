# Harness search and agentic search: SelfSearch, CorpusMap, simpler interfaces, and the seven-part harness

**Source:** X Following feed, 2026-10-05 US day (posts by @omarsar0, @dair_ai, @santtiagom_, @AnnatarXBT), with linked papers enriched by the Twitter farmer · raw: `raw/twitter/feed/2026-10-05-*-ranked.json` (gitignored)

Four papers the feed surfaced that were not in HuggingFace or Kurate this window.

## SelfSearch: reward-free self-improvement ([arXiv 2609.37968](https://arxiv.org/abs/2609.37968), Seoul National University)
Agents edit their own instructions, tools and procedures using records of earlier self-edit attempts (reasoning, actions, outcomes), with no benchmark reward during search. The edited agent becomes the next improver. Population-mean success rises in all six model-benchmark settings, up to +11.2 points on Terminal-Bench 2.1 for single agents. On SWE-bench Multilingual one evolved agent gains 5.0 points and cuts execution cost 38.5% on tasks both versions solve. With $4.03 of search spend it produces a harness where DeepSeek V4 Flash solves 82.0% of Terminal-Bench 2.1, matching Codex in a public nine-harness comparison.

## CorpusMap: follow the entities ([arXiv 2609.37226](https://arxiv.org/abs/2609.37226), Microsoft and KAIST)
An offline layer over a document collection: resolve recurring entities across documents and give each an Entity Page linking every document that mentions it. The agent follows entities instead of re-searching a flat corpus. Across 7 models and 3 benchmarks (EnterpriseRAG-Bench, WixQA, HERB), answer quality +6.4 to +11.7 points with 34% to 57% fewer input tokens. Beats four alternative navigation layers, including a Karpathy-style LLM wiki and Corpus2Skill. Built without LLM calls, updated incrementally.

## Engineering Simplicity ([arXiv 2609.36365](https://arxiv.org/abs/2609.36365), Harvard and MIT)
In auctions and matching markets with known optimal strategies, "plan ahead" or "model the other players" prompts made agents play worse. A sequential ascending-auction interface cut bid errors across four model families; spelling out payoffs also helped. Stated plans did not track choices. Judge a scaffold by the decisions it produces.

## The seven-part harness ([arXiv 2609.00006](https://arxiv.org/abs/2609.00006), Wavestone AI Lab)
Teardown of 11 coding agents (Claude Code, Codex, Gemini CLI, Aider and others): all share loop, LLM layer, tools, memory, safety, orchestration and extensions, differing in size. SKILL.md in 9 of 11, MCP in 8; almost none use agent frameworks or embeddings. 18 design rules and a 90-line reference harness.

## How these relate to prior wiki pages
- SelfSearch and ActiveSaddler (10-03, [page](2026-10-03-multi-harness-rl-activesaddler-prover.md)) make harness optimization cheap enough that its budget allocation is the research question. Both feed [agent harness engineering](agent-harness-engineering.md) and [self-evolving agents](self-evolving-agents.md).
- CorpusMap is the retrieval-side counterpart of Context Language Models (10-01, [page](2026-10-01-context-language-models.md)): both cut tokens while raising accuracy, one by pre-structuring the corpus, the other by letting the model edit its own context.
- Engineering Simplicity agrees with VeriHarness (10-05) that agent self-reports are weak evidence; grade outcomes.

## Related
[Agent harness engineering](agent-harness-engineering.md) · [Agent memory](agent-memory.md) · [Daily digest 2026-10-06](../daily-digest/2026-10/2026-10-06.md)
