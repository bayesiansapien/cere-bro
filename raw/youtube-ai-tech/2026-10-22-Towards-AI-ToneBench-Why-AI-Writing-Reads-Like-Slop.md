# Why AI Writing Still Reads Like Slop (Louis-François Bouchard, Towards AI)

**Channel:** AI Engineer
**Published:** 2026-10-22
**Source:** https://www.youtube.com/watch?v=_dTF3NpPzGo
**Domains:** ai-tech (primary)

## TL;DR
Bouchard launches ToneBench, a benchmark that asks roughly 120 models to write a full video script in his personal voice from a 14k-token brief, then scores 5 drafts per task across 10 tasks with 4 LLM judges on 9 metrics. Core finding: slop does not shrink as models scale, so pick the model that is least annoying to iterate with, not the one with the best single shot. His recommended production recipe is a cost play: many drafts from a cheap model (GLM 5.3 Flash, about 50x cheaper than the top scorer) merged by one high-reasoning judge pass. Treat the leaderboard as n=1 (one author's voice), and note it was unindexed by search at time of writing.

## Key Takeaways
- **Six-part definition of slop:** overused LLM vocabulary ("delve"), over-generality ("most teams"), saying nothing, repetition, hallucination, and wrong or averaged tone.
- **Setup:** 10 scripts (mix of published and unpublished to check contamination), each with a brief, research doc, rubric, and Bouchard's own reference script. Generation prompt is long and example-heavy; judge prompt is about 14k tokens with about 1k words of guidance per metric.
- **Nine metrics, five families:** tone/voice match (primary), writing craft (hooks, emotional transitions), instruction following (length, format, asset placement), research accuracy (hallucination vs brief), and slop (EQ-Bench slop score plus in-house measures). Length is scored by code, not the judge; judges are blind to model identity.
- **Categorize-then-score judging.** Judge first picks one of six qualitative categories, then assigns a rating within it. He found this beat pure binary, direct categories, or direct percentages for subjective quality.
- **Five drafts per task for intra-model variance.** Weaker models have wider variance; one outlier draft from a weak model can match the top model. Five was the cost/signal sweet spot.
- **Judge bias is real and family-level.** OpenAI judges strongly prefer all OpenAI-family outputs, not just themselves; Anthropic and OpenAI judges appear to penalize each other. Mitigation: judges from multiple families plus about 1,000 human A/B pairs on comparable chunks from 4 raters.
- **Cost:** about 500 human hours to build scripts and rubrics, four months on four top-tier subscriptions. Changing one rubric line costs over $2k to rescore; changing one generation-prompt line costs over $4k to regenerate.
- **Results:** Opus 5.5 extra-high leads; Max thinking gives the same quality at 2.5x the cost, so do not use max reasoning for writing. GLM 5.3 Flash is the value pick at about 50x cheaper than the leader.
- **Writing recipe:** longest possible prompt with positive and negative examples and full prior samples; one to three critic passes from a high-reasoning model (more loops drift back into slop); final human review.

## Architecture & Optimization Mechanics
- **This is a routing result.** "Generate 10 drafts with a cheap model, merge with one strong model" is a cascade: small model for proposal, large model for selection and fusion. The claim that it beats a single Opus call on both cost and quality is plausible but unquantified in the talk. Worth testing.
- **Reasoning budget saturates early on creative tasks.** Extra-high equals Max at 2.5x the price. That is a clean signal for a router: cap reasoning effort for open-ended generation and spend tokens on sampling breadth instead.
- **Variance is a model-quality feature.** Wider draft variance in weaker models means best-of-N helps them more than strong models. A compressed or distilled model with high variance plus a good selector can close much of the gap to a frontier model, which is exactly the regime where pruned/quantized models live.
- **Critic-loop instability.** Quality improves for 1 to 3 critique rounds then degrades. Treat critic depth as a hyperparameter with an early stop, not "more is better."
- **Evaluation economics.** At over $2k per rubric tweak, LLM-judged benchmarks are expensive to iterate. Distilling the judge into a small scorer for development, and reserving the full 4-judge panel for releases, is the obvious optimization he has not done.

## Grounded Context (Web Enrichment)
I could not find ToneBench or a Towards AI announcement in web search; it was released the day of the talk and is not yet indexed, so all numbers above are the speaker's own and unverified. Comparable public efforts exist: Stanford's LitBench (EACL 2026) found the best off-the-shelf judge (Claude 3.7 Sonnet) reached only 73% agreement with human preferences on creative writing, and trained reward models reached 78%. That ceiling is a useful prior for how much to trust any LLM-judged writing leaderboard, including this one. TypeOS's TypeBench uses expert-editor pairwise preferences with tone as one axis, which is closer to Bouchard's human A/B validation.

The family-bias claim is well supported. A September 2026 arXiv paper ("Who Judges Matters," 2609.17857) measures family-conditioned preference separately from self-preference and cites Pombal et al. (2026) finding same-family preference in rubric-based evaluation. Bouchard's "OpenAI prefers its whole family" observation fits that literature. His "Anthropic and OpenAI were post-trained to hate each other" is a joke-level hypothesis with no evidence; the standard explanations are stylistic familiarity and perplexity (Wataoka et al., 2024). The main methodological weakness: the benchmark measures one person's voice, so a model's rank says as much about stylistic proximity to Bouchard as about general writing ability.

## Real-World Application / Actionable Step
- **Run the cascade experiment on your own drafting tasks:** N=5 to 10 samples from a small or quantized model, one merge pass from a frontier model with high (not max) reasoning. Compare cost and blind human preference against a single frontier sample. If it wins, it is a publishable routing result for open-ended generation.
- **Add a reasoning-effort cap to your router for creative/writing queries.** Default to high, never max; the reported 2.5x cost for zero gain is free savings.
- **Use variance as a routing feature.** For candidate small models, measure draft variance on your eval set; high-variance models are good best-of-N proposers, low-variance ones are better single-shot.
- **For any LLM-as-judge eval you run:** use judges from at least two families, never let the judged model's family judge itself, and validate on a few hundred human A/B pairs before trusting rankings.
- **For your own writing with agents:** put full prior samples and an explicit negative-example list in the prompt, and stop after at most three critic passes.
