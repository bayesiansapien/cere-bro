# Iris: Climbing to the Search Frontier

**Source:** HuggingFace Daily Papers, 2026-09-07 · [arXiv 2609.04304](https://arxiv.org/abs/2609.04304) · [raw](../../raw/huggingface/2026-09-07-iris-climbing-to-the-search-frontier.md)

**TL;DR.** Two open search agents, **Iris-mini at 35B-A3B and Iris-pro at 397B-A17B**, released with the full data pipeline and training recipe. On BrowseComp, BrowseComp-ZH, DeepSearchQA and Humanity's Last Exam they reach **82.2 / 84.8 / 86.9 / 52.3** and **88.6 / 85.1 / 92.9 / 56.4**, the strongest open-source results in their parameter classes, all from **a single ReAct agent with no sub-agents and no test-time verification**. The claim in the paper that matters most to this wiki is not the score. It is a methodological one, stated plainly: **inference-time context management is worth more on these benchmarks than most reported differences between systems**, so they evaluate every benchmark both with and without it, holding tool set, context limit and judge fixed.

## The pieces worth stealing

**Task construction from link structure, with string matching deliberately broken.** Multi-hop chains are built over an entity graph distilled from a seed page and its out-links. Every non-answer entity is then **rewritten into a descriptive reference**, so no clue in the question can be resolved by matching a string against the corpus. Only questions that a reference model fails closed-book but solves once the supporting evidence is supplied are admitted, which filters out both trivia the model already knows and questions the evidence does not actually answer.

**Two-level trajectory filtering before supervised fine-tuning.** Trajectories are filtered at the trajectory level and again at the turn level, so a mostly-good rollout does not teach a bad turn.

**RL against live search, with the judge and summarizer served inside the training cluster.** The reward judge and the observation summarizer run in-cluster rather than as external API calls, and over-long rollouts are **interrupted at the request level and resumed from their committed prefix at the next step** rather than discarded. That is a prefix-reuse discipline applied to RL rollouts, and it is the same economics the [KV cache](../inference-efficiency/kv-cache.md) page has been recording on the serving side.

**SFT-RL climbing.** The two stages alternate, and each RL round returns its **hardest solved and most efficient rollouts** to the next supervised pass. Difficulty and efficiency, not just correctness, are the selection criteria.

## Relation to prior wiki state

**The context-management disclosure is the important contribution and it is an indictment.** [ContextPipe (09-06)](2026-09-06-contextpipe-database-context-assembly.md) argued that context assembly is structurally the same problem as relational query execution and cut an agent's total token volume 31% and its call count 23% by planning the prompt instead of appending to it. Iris says the same lever, applied at inference time, is **larger than the gaps between the systems on a public leaderboard**. Put together: **the search-agent leaderboard has been substantially measuring harness quality while reporting it as model quality**, and Iris is the first entry to say so and publish both columns.

That is the [agent harness engineering](agent-harness-engineering.md) page's central thesis (the harness, not the model, is the primary cost and design surface) arriving as a leaderboard-integrity problem rather than as a cost argument. **The page should now hold a stronger version: any agent benchmark that does not fix or disclose its context-management policy is not comparing models.**

**The no-sub-agents result is a quiet counterpoint to the day's other agent signal.** The DAIR.AI weekly digest surfaced Harness-of-Harness, which wraps an existing coding harness in repeated plan-code-test increments and reports a 52.25% average relative gain over standalone harnesses after three iterations. Iris reaches the open-source frontier on search with **one flat ReAct loop**. Both cannot be the general rule, and the honest reading is that the orchestration premium depends on whether the task decomposes: multi-day software projects do, single-answer multi-hop retrieval does not.

## Gaps

The headline numbers are quoted with context management enabled, and while the paper commits to reporting both, the abstract does not give the without-management column, so the size of the effect it identifies as decisive is not visible from the summary. No inference cost per query is reported for either model, which for a system whose main methodological claim is about inference-time technique is the omission that matters. And weights and recipe are promised rather than released.

## Related

- [Agent harness engineering](agent-harness-engineering.md) · [Agent benchmarks](agent-benchmarks.md) · [ContextPipe (09-06)](2026-09-06-contextpipe-database-context-assembly.md) · [Tool calling](tool-calling.md)
- [Daily digest 2026-09-07](../daily-digest/2026-09/2026-09-07.md)
