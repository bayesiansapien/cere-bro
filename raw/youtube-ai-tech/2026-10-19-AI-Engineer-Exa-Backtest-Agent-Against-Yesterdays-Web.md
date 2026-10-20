# Backtest Your Agent Against Yesterday's Web | Ryan Ahern, Exa

**Channel:** AI Engineer
**Published:** 2026-10-19
**Source:** https://www.youtube.com/watch?v=L4dUFimVDKU

*Workshop, AI Engineer New York (finance track). Vendor talk. Short-form version of the same content: [[2026-10-19-AI-Engineer-Exa-Version-Controlled-Search-Web-As-It-Was]].*

## TL;DR
Exa Snapshot lets you run web search, or fetch a URL, as of a past date, using the version history Exa accumulates while crawling (~100B documents, trillions of URLs; 400B+ snapshots). The point is to eliminate future-information leakage when backtesting anything that uses web search: prediction models, adverse-media/KYC agents, equity research agents, even coding-agent RL environments. The workshop had ~100 people write yes/no "features" to predict acquisitions 1, 7 and 30 days before announcement. The winners overfit (one feature was literally "is this company not named Qiagen, Vitris, Bank of Cyprus or American Electric Power"), which the speaker admits shows why a holdout set is mandatory.

## Key Takeaways
- **Two modes:** content versioning (URL as of date, nearest earlier version) and versioned search (execute a query as of date; only results available then).
- **Live search leaks the future.** If a backtest searches today's web for "was X acquired," it finds the deal and scores 100%.
- **Publish dates are unreliable.** Publishers update dates for real edits and for SEO; Snapshot uses crawl timestamps instead.
- **Three adoption patterns:** (1) traditional model, use Snapshot only to gather point-in-time features from pages that do not keep history (prices, T&Cs, sentiment); (2) add agentic web features (adverse media scan, equity research) to an existing model and backtest them one by one; (3) fully agentic predictor that decides when to search, with the web pinned to the decision date.
- **Coding RL:** freeze the web right before a PR was merged so a model cannot just find the answer online.
- **Exa's pitch:** own crawler, index, embeddings and retrieval; sub-300 ms search up to 20-minute deep research runs (one run found 3,212 video game publishers); token-efficient highlights; a "regenerative" benchmark customers rebuild for their use case to avoid benchmark contamination.
- **Example signal:** OpenAI's reported annualized revenue was revised from ~$70B to ~$50B (gross vs net of cloud pass-through). Snapshot lets you test whether your agent could have found the accounting footnote before the market did.
- **Workshop scoring:** +1 for predicting an acquisition that happened, -1 for a false alarm, 0 for misses. "Exploring a sale" plus leadership turnover combined with AND beat OR.

## Architecture & Optimization Mechanics
- **Point-in-time correctness for retrieval** is the web analogue of survivorship-bias-free financial databases (CRSP, Compustat point-in-time). Without it, every agent backtest is optimistic.
- **Hidden leak the talk does not cover:** Snapshot constrains which documents can be returned, not the ranking. Exa's embedding and ranking models are trained today, on data that includes the future. A ranker that learned "articles about Company X matter" after X's acquisition can still surface the right pre-acquisition document more often than a 2025 ranker would. The same applies to the LLM consuming results: its weights contain post-date knowledge.
- **Feature-level ablations:** testing agentic features one at a time against outcomes is just classical feature selection, but now possible for unstructured, search-derived features.

## Grounded Context (Web Enrichment)
Exa launched Snapshot as a research preview around 17 to 18 September 2026, accessible through `/search` and `/contents` with a `snapshotAsOf` parameter, covering 400B+ snapshots over about two decades. Exa frames RL-training and eval leakage as the main use case, with backtesting secondary. Coverage confirms the limitation above: the cutoff applies to content, not ranking, so Snapshot does not reconstruct the search results page you would have seen at the time. The pay-as-you-go tier reportedly allows 10 QPS and a five-month lookback before needing a sales contract ([AlphaSignal](https://alphasignal.ai/news/exa-snapshot-lets-ai-search-the-web-as-it-existed-years-ago), [ExplainX](https://explainx.ai/blog/exa-snapshot-versioned-web-search-api-2026), [Digg](https://digg.com/ai/rcc2bsld)). A competing product, Ross Taylor's BackSearch, also targets historical web search ([Digg](https://digg.com/ai/divhrbm1)).

The talk is honest about overfitting, but the bigger issue for finance users is that the LLM itself knows the outcomes. A frontier model asked "is Delivery Hero exploring a sale?" with a 2025-pinned web may still answer from post-2025 weights. Serious backtests need models with training cutoffs before the test window, or at least a check that the model cannot answer without the retrieved context.

## Real-World Application / Actionable Step
- **Router and agent evals with live search:** any eval that calls a search tool is contaminated over time. Pin search to the dataset's creation date (Snapshot or a frozen local corpus) so router comparisons stay reproducible month to month.
- **Leakage check:** for each backtest question, run the model with no retrieval. If it answers correctly above chance, the weights leak the outcome; exclude those items or use an older-cutoff model.
- **Holdout discipline:** split events by time (train on 2023 to 2024, test on 2025), not randomly, and never inspect the test set during feature design.
- **Personal investing:** if you build any LLM-based screener (e.g. "activist pressure plus 60% drawdown from 5-year high" as an M&A signal), backtest it point-in-time before trusting it. The winning workshop feature is a decent hypothesis to test on your own holdout.
