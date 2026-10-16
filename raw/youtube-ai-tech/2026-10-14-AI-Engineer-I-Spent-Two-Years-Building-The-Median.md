# I Spent Two Years Building the Median (Hariprasad Sudharshan)

**Channel:** AI Engineer
**Published:** 2026-10-14
**Source:** https://www.youtube.com/watch?v=0JZy5AuuQzc

## TL;DR
When everyone rents the same frontier models and the same harnesses, pointing a problem at a coding agent returns the same answer for everyone: the median. Sudharshan, a long-time product builder, burned two years and several Max plans shipping apps with a "build-first reflex," only to find 2 to 60 near-identical products in every lane. His fix is a "novelty budget": before building, name the one novel thing; if you cannot, call it a learning exercise or fork the existing open-source twin. The only concrete win he shows is telling: his calculator escaped the median only once it targeted a hard, unglamorous problem (true cost of running open weights in-house vs buying tokens from a neocloud), the kind of infra knowledge Amit already has. The thesis is sound but not new; it is a long-winded restatement of "the model is a commodity, distribution and taste are the moat."

## Key Takeaways
- **The world still runs on deterministic software.** AI's role is (1) to produce deterministic software faster and cheaper, and (2) to make previously unaffordable software viable. Probabilistic gear cranking out deterministic artifacts.
- **Frontier gaps are noise for roadmaps.** Elo differences of a few dozen points (Anthropic 1503 vs Mistral 1460 in his slide) are relative rankings in one eval environment, not an intelligence scale. Like the 2015 100m final (nine runners within 0.27s), on a given day anyone wins.
- **People compare harnesses and call it model comparison.** Claude Code vs Cursor vs Codex is "Jamaica vs USA": athlete plus training system. Model = engine, harness = tools/context/orchestration/memory, product = why anyone cares.
- **The median trap.** Same model + same harness gives the next person what it gave you. Pre-2023 the median product cost a team and a quarter; now it is free, for everyone, so distribution becomes the moat.
- **"Slop" is the wrong word.** Median apps that satisfy their creator (Lovable/Replit builders) are legitimate success. Just do not count them as differentiation.
- **Build-first reflex.** Searching used to precede building; now building is cheaper than deciding. His agent built "the nth RAG system" and, when challenged, admitted it should have pointed to mature OSS.
- **Novelty budget.** Name one unit of real novelty (his analogy: PageRank) before starting; review it like spend. "When the AI says done, your work begins."
- **Four rules:** be highly opinionated (cheapest novelty you can own); prompt-to-production is a median path, fine for internal tools; "done" from the agent is the median baseline; agents give you "the last great design for free," not the next Kafka/Kubernetes.
- **Three questions for leaders reviewing demos:** Who already did this? What do we have that others don't? Where will this live (distribution)?
- **His exit from the median:** a calculator comparing identical open weights self-hosted vs bought as tokens. "Open weights are not open inference": ~10 layers sit between weights and tokens (precision, KV cache, batching, parallelism...), and utilization (his "layer nine") is structural and cannot be bought. None of 244 competing calculators modeled this. Open source.

## Architecture & Optimization Mechanics
- **Model-harness-product decomposition** is the useful mental model: benchmarks measure the engine, users experience the harness, and most "which model is best" debates are confounded by harness differences.
- **Elo intuition:** an 87-point gap means the higher model is preferred ~62% of the time head-to-head, not "87 points smarter." A 25-point gap is ~54%, near coin-flip.
- **Open-weight TCO stack.** The non-commodity layers he lists (quantization precision, KV cache management, continuous batching, tensor/pipeline/expert parallelism, utilization) are exactly where inference engineering creates cost advantage. Self-hosting economics are dominated by utilization: cost per token scales roughly inversely with it.
- **Convergence applies to routing too.** He notes LLM routing solutions are converging like everything else, so a generic router is median; the novelty is in a domain-specific quality signal or cost model.

## Grounded Context (Web Enrichment)
His Elo numbers come from the Stanford AI Index 2026: as of March 2026, Anthropic (1,503), xAI (1,495), Google (1,494) and OpenAI (1,481) sat within 25 Arena Elo points, with Alibaba (1,449) and DeepSeek (1,424) further back. Note the "six labs within 25 points" framing circulating in secondary coverage is wrong per the primary chapter, and the same report shows the closed-vs-open gap widening again (3.3% in March 2026, up from 0.5% in Aug 2024), so "everyone has the same engine" is truer among closed labs than across open weights. The Mistral 1460 figure was not verified.

On self-hosting, 2026 breakeven analyses span from ~12M tokens/day (70B FP8 on one H100 vs a frontier API) to ~264M/day for frontier-size open models on 4 to 8 GPUs, and some configurations never beat mini-tier APIs. Real cluster utilization often sits below 50 to 60%, and an MLOps hire runs $145k to $275k fully loaded. That supports his core claim that utilization is the hidden variable. It also says his calculator's value is entirely in its utilization and staffing assumptions, which should be scrutinized before use. See [[2026-10-03-Nebius-What-Makes-Open-Models-Fast-In-Production]], [[2026-09-27-ZAI-GLM-5-2-Open-Weights-Near-Frontier-Intelligence]], [[2026-07-25-Dropbox-Feature-vs-Platform-Commoditisation-ColdFusion]].

## Real-World Application / Actionable Step
- **Run the novelty check on your own projects.** For each routing/compression project, write the one-line novel element before coding. A generic cascade router or a vanilla GPTQ pipeline is median; a router with a domain-calibrated quality signal or a quantization recipe tuned for MoE expert memory is not.
- **Search before build.** Make "who already did this?" step zero for agent-driven prototypes (RouteLLM, vLLM features, existing calculators). Fork the twin, spend tokens only on the delta.
- **Use his calculator as a sanity check, not a decision.** Plug in measured throughput and realistic utilization (40 to 60%) for your target open model before advocating self-hosting; compare against cached-token API pricing.
- **When comparing models for routing, hold the harness fixed.** Otherwise you are measuring the harness.
