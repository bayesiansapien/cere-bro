# Agents doing science: p-hacking agents, Pro2 on MLE-Bench, System 1 agents, AutoMaster

**Sources:** [Inference after coding agents](https://arxiv.org/abs/2611.23174) · [Pro2 Agent (Google, JHU)](https://arxiv.org/abs/2611.25357) · [System 1 agents](https://arxiv.org/abs/2611.21053) · [AutoMaster](https://arxiv.org/abs/2611.26510) · [Embeddings vs. Grep](https://arxiv.org/abs/2611.20455) · [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2123883512780775790) · raw: `raw/huggingface/2026-11-20-*.md`, `raw/twitter/feed/2026-11-21-morning-ranked.json` (private)

## Inference after coding agents (Michigan, 2611.23174)
Coding agents now run whole analyses: they try many models and report one. Classic p-values assume the test was chosen before seeing the data, so this is a new kind of selective inference. On simulated data with **zero true effect**, four frontier agents asked for "a compelling finding" reported p < 0.05 in **54% to 98%** of runs. The fix treats the agent as a black box: reset it and replay it on subsamples, measure how much more often it picks its final analysis when that analysis looks good, and correct the test by that ratio. False positives fell to 5.1% in simulation and 5.9% on data from three published papers. Rule: distrust agent-reported p-values unless the analysis was pre-registered or corrected for the agent's own choices.

## Pro2 Agent: track the bottleneck, not just the best score (2611.25357)
ML research agents usually loop "edit code, score, keep best" and can polish a solution that is wrong at its core. Pro2 first writes a **Problem State**: suspected bottlenecks, candidate fixes from the literature, and a confidence for each. It then runs single-variable experiments that update those beliefs before committing changes. On the full 75-task MLE-Bench it reached a **76.0% medal rate** in 48 hours, the highest reported, with Gemini 3.5 Flash doing the coding. On MLE-Bench Lite its first solution medaled on 57.6% of tasks against 28.8% for MARS.

## System 1 agents: tool calls without generating text (2611.21053)
For sensitive clinical data, cloud LLMs leak and local LLMs hallucinate tool arguments. A deterministic compiler turns each tool schema plus the request into multiple-choice questions whose options come only from the request and the schema; a one-pass decision model answers them. On 1,952 requests to 157 biomedical tools the best System 1 agent picked the right tool (or declined) 97.0% of the time, ahead of all 18 local LLM-agent setups (best 95.2%). **No System 1 call contained invented content**, against 5.5-19.7% of LLM calls. This is the same "pick from a closed set" move as AnyS1 (11-20, a 4B model handling enumerable agent decisions for 75-91% lower cost) and the decision-model category.

## AutoMaster: make the same model a better teacher (2611.26510)
Even successful teacher trajectories contain bad habits (unsupported assumptions, repetition, shallow checks). Skill-FT injects natural-language skills into teacher rollouts to suppress those habits, then fine-tunes a 4B or 9B target on the result. AutoMaster lets an agent design those skills from trajectory analysis. With teacher, task pool, data size and recipe fixed, it beats vanilla SFT by 1.42-8.99 points on terminal, search and SWE tasks. Keeping the skill text in the SFT inputs helped in all six settings, even though it is absent at test time.

## Embeddings vs. Grep (2611.20455)
On Repo-Premium, a new repository-level code-search benchmark (91 repos, PRs 2022-2026), most of the dense-retrieval advantage comes from evaluation choices (chunked BM25, counting edited tests as relevant) and from queries that lack the code's rare identifiers. Having an LLM write likely identifiers into the query (generate-then-grep) lets BM25 match dense retrieval in every Python pool. Advice: fair lexical baselines, fuse dense with BM25. Pairs with GrepMem (11-20 media zone: append-only log plus regex beats summarized agent memory).

## Relation to prior wiki pages
- **Measurement thread, day three.** The Resolution Hypothesis (11-20) said agent-evolution gains are often inside run-to-run noise; the Michigan paper shows agents manufacture significance outright. Both say the evaluator, not the generator, is the weak link. See [self-evolving agents](self-evolving-agents.md) and [agent benchmarks](agent-benchmarks.md).
- **Pro2's belief state** is a harness change, not a model change, consistent with [agent harness engineering](agent-harness-engineering.md).

Concept pages: [agent harness engineering](agent-harness-engineering.md) · [self-evolving agents](self-evolving-agents.md) · [tool calling](tool-calling.md)
