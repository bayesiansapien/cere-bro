# r/MachineLearning | 2026-05-13 IST | sort=top
> Scraped 2026-05-13 10:36 IST | lookback=24h | tier_default=2
> Filter to [R]/[P]/Research/Project flair only — drops the [D] discussion noise. Generic news is excluded.

### Steam Recommender using similarity! (Undergraduate Student Project) [P]

**Meta:** score=57 · comments=9 · tier=2 · flair=Project · posted=2026-05-12 17:30Z
**Author:** u/Expensive-Ad8916
**Reddit:** [https://www.reddit.com/r/MachineLearning/comments/1tb8k3n/steam_recommender_using_similarity_undergraduate/](https://www.reddit.com/r/MachineLearning/comments/1tb8k3n/steam_recommender_using_similarity_undergraduate/)
**Link:** [https://www.reddit.com/gallery/1tb8k3n](https://www.reddit.com/gallery/1tb8k3n)

---

### TabPFN-3 just released: a pre-trained tabular foundation model for up to 1M rows [R][N]

**Meta:** score=53 · comments=11 · tier=2 · flair=Research · posted=2026-05-12 14:33Z
**Author:** u/rsesrsfh
**Reddit:** [https://www.reddit.com/r/MachineLearning/comments/1tb3fh5/tabpfn3_just_released_a_pretrained_tabular/](https://www.reddit.com/r/MachineLearning/comments/1tb3fh5/tabpfn3_just_released_a_pretrained_tabular/)

TabPFN-3 was released today, the next iteration of the tabular foundation model, originally published in Nature.

Quick recap for anyone new to TabPFN: TabPFN predicts on tabular data in a single forward pass - no training, no hyperparameter search, no tuning. Built on TabPFN-2.5 (Nov 2025) and TabPFNv2 (Nature, Jan 2025), which together crossed 3M downloads and 200+ published applications.

What's new:

* Scale: 1M rows on a single H100 (10x larger than 2.5).A reduced KV cache (\~8GB per million rows per estimator) and row-chunked inference make this practical on a single GPU
* Speed: 10x-1000x faster inference than previous versions. 120x on SHAP via KV caching
* Thinking Mode (API only): test-time compute pushes predictions further via one-time extra fitting at inference. Beats every non-TabPFN method on TabArena by over 200 Elo, including 4-hour-tuned AutoGluon 1.5 extreme. Gap more than doubles to 420 Elo on the larger-data slice.
* Accuracy: it has a 93% win rate over classical ML on TabArena
* Many-class: native non-parametric retrieval decoder supporting up to 160 classes
* Calibrated quantile regression: bar-distribution regression head produces calibrated quantile predictions in a single forward pass
* Lifts adjacent tasks: time-series, interpretability, and new SOTA on relational benchmarks.
* 3 deployment paths: API, enterprise licensing, and open-source weights (permissive for research and academic evaluation)

You can try it [here](https://docs.priorlabs.ai/quic

[…truncated, see permalink]

---
