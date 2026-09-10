---
source: farmer/huggingface
farmed: 2026-09-10T08:36:11.637058+00:00
arxiv_id: 2609.05779
url: https://huggingface.co/papers/2609.05779
arxiv_url: https://arxiv.org/abs/2609.05779
upvotes: 1
date: 2026-09-10
---

# Diffs vs. Whole Files: An Empirical Comparison of Iterative Edit-Based and Direct Generation for Flutter/Dart Code Models

Large language models used for code editing can be trained and deployed in at least two output regimes: direct generation, where the model emits the entire modified file in one shot, and iterative diff-based generation ("steps"), where the model emits a sequence of localized search/replace edits applied one at a time until it signals completion or a step budget is exhausted. The diff-based regime is attractive because it mirrors how developers edit code and should require far fewer generated tokens per turn. We train two code models - a 100M-parameter model trained from scratch (Rainbow-Pony-100M) and a fine-tuned Qwen2.5-Coder-0.5B - in both regimes on a shared Flutter/Dart dataset, and evaluate all four resulting models on a held-out set of approx 1,790 tasks per model. Direct generation substantially outperforms diff-based generation on every metric we measure - compilation/static-analysis pass rate, bits-per-byte, character-level similarity to the reference, and blinded LLM-judge ratings of goal fulfillment, correctness, and code quality - and the gap persists after controlling for task difficulty via a matched-ID comparison and when restricting to code that compiles on both sides. We then identify a single, architecture-independent mechanism behind the conditions where diff-based generation does win: it is competitive on short, spatially localized edits, and its category-level wins concentrate in exactly the two task categories - refactoring and error-handling/edge-case fixes - with the lowest mean edit-step count in our dataset. We term this task locality and discuss its implications for when an edit-based training regime is and is not the right choice for a code-editing model.
