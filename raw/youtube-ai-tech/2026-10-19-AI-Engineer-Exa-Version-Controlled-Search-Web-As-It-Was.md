# Version-Controlled Search: The Web as It Was | Ryan Ahern, Exa

**Channel:** AI Engineer
**Published:** 2026-10-19
**Source:** https://www.youtube.com/watch?v=vS2IA9pq0Q4

*Short talk, AI Engineer New York. Condensed version of the workshop in [[2026-10-19-AI-Engineer-Exa-Backtest-Agent-Against-Yesterdays-Web]]; this page covers only what is new.*

## TL;DR
Same thesis as the workshop: Exa Snapshot (400B+ dated web snapshots) lets agents search the web as of a past date so backtests of financial, risk and prediction systems do not leak future information. New details: Exa's dynamic highlights now select snippets across all results, claiming higher quality at 95% fewer tokens than full-page text; Exa Agent Ultra is its new long-running deep-research agent; and Exa released a benchmark meant to separate search-tool quality from the model calling it.

## Key Takeaways
- **Agents search differently from humans:** verbose, detailed queries, many searches per task, persistence. Search volume per task is much higher than human search.
- **Cost is per trajectory, not per call.** The metric that matters is total agent cost to complete the task, including input tokens from search results.
- **Dynamic highlights:** cross-result snippet selection; claimed 95% token reduction versus full page text with better quality.
- **Exa Agent Ultra:** recently released, claimed state-of-the-art on long-running search benchmarks because Exa owns both the search backend and the research harness.
- **Search-only benchmark:** isolates retrieval quality from the inference model, since model and tool effects are confounded in end-to-end agent benchmarks.
- **Snapshot modes:** URL-as-of-date and search-as-of-date.
- **OpenAI revenue example:** snapshot as of 1 October shows ~$70B annualized run rate reporting (Axios); a later live search shows ~$50B on net-of-cloud-pass-through accounting.
- **Overfitting example:** a workshop feature ending in "or is the company named Dominion" shows how an agent tuned on a visible set can memorize; Snapshot plus holdouts lets you detect this offline instead of waiting months in production.
- **Semantic features:** Exa's embedding search allows complex, natural-language features ("adverse media against VC partners who said X on podcast Y") that keyword search could not express, and Snapshot makes them backtestable.

## Architecture & Optimization Mechanics
- **Token-efficient retrieval is context compression.** Selecting snippets across the whole result set is extractive compression before the LLM sees anything. For an inference-cost budget, a 95% cut in retrieved tokens often matters more than switching to a cheaper model.
- **Separating tool quality from model quality** matters for routing: if your router picks a cheap model for search-heavy queries, you need to know whether failures come from the model or from retrieval.

## Grounded Context (Web Enrichment)
Snapshot launched as a research preview in mid-September 2026 on `/search` and `/contents` with a `snapshotAsOf` parameter. Third-party coverage notes the cutoff constrains content, not ranking, so it does not recreate the results page of the time ([AlphaSignal](https://alphasignal.ai/news/exa-snapshot-lets-ai-search-the-web-as-it-existed-years-ago), [ExplainX](https://explainx.ai/blog/exa-snapshot-versioned-web-search-api-2026)). The 95% token-reduction figure is Exa's own claim; I found no independent benchmark. Treat it as a hypothesis to test on your workloads.

## Real-World Application / Actionable Step
- **Measure retrieval token share.** For your agent or RAG workloads, log what fraction of input tokens come from retrieved content. If it is above 50%, test snippet-level highlights (Exa or your own reranker plus extractor) before optimizing the model.
- **Routing feature:** add "expected retrieval volume" as a router input. Search-heavy queries may be better served by a cheap model plus aggressive snippet compression than by a frontier model with full pages.
- **Eval hygiene:** report search-tool quality separately from end-to-end agent score in your router comparisons.
