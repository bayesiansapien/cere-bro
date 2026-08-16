# The Slow Death of Scaling, and Data Inside the Loop (Sara Hooker, Adaption)

**Source:** Sara Hooker, Adaption Labs, at AI Engineer · [Talk](https://www.youtube.com/watch?v=XEd_SRVHBgU)
**Raw:** [raw/youtube-ai-tech/2026-08-12-Adaption-Sara-Hooker-Gradient-Free-Continual-Learning.md](../../raw/youtube-ai-tech/2026-08-12-Adaption-Sara-Hooker-Gradient-Free-Continual-Learning.md)
**Topic:** scaling laws, compute economics, automated research, routing

## TL;DR

Hooker's argument is that the barrier to building frontier AI is dissolving, and the mechanism is her "slow death of scaling" thesis turned into a business plan. **Pre-training size has stopped being the most lucrative axis of scale** because the current architecture is saturated. The axes that now pay, post-training, agentic compute, test-time compute, and data curation, **do not require co-located GPU fleets**, so the compute-hoarding advantage decays. Her structural point is the sharpest thing in the talk: pre-training compute must be co-located and over-provisioned for redundancy, while inference, post-training, and agentic compute can be distributed and return more per FLOP.

Her product answer is AutoScientist, which automates the full training and alignment loop. The load-bearing technical finding is not that it works but *what made it work*: **they got no meaningful returns from automated model search until they put data quality inside the same optimisation loop.** Most auto-research projects treat data as an agent decision (create data or not, which data); Hooker says returns only appeared once they ran the same adaptation loop over the data that they ran over the model.

## Key findings

- **Co-optimising data alongside the model was necessary, not incremental.** No returns from architecture search alone.
- **The system beats their own research staff**, and the stated reason is search breadth rather than insight: it sweeps dense and MoE, many sizes, and many hyperparameters simultaneously in ways human researchers, who carry architecture-specific priors, are too cautious to try.
- **A candid methodological admission**: the 60-plus percent win rates in their charts are an artifact of a budget stopping rule that exits the genetic search once it clears 60. With the cap removed the numbers keep climbing. That is a rare disclosure and it makes the rest of the numbers more believable, not less.
- **The claimed second-order benefit is predictability of training, not just quality.** A higher probability that a given compute spend succeeds shortens the innovation cycle, which is the real lever on customisation cost.
- **The routing argument arrives from the democratisation direction.** Her objection to the current deployment model is stated as efficiency, not fairness: shipping one model to billions spends the same compute on every query when some problems are hard and most are easy.
- Scale of the human bottleneck, as she frames it: **fewer than 5,000 people worldwide know how to train frontier models at scale**, and that apprenticeship knowledge is an exploitable search space. Beta demand concentrates in medical, legal, and code; 242 languages from day one.
- **Caveat on the talk itself**: it is titled gradient-free continual learning and barely touches it, mentioning gradient-free inference-time adaptation only obliquely via the parametric-versus-non-parametric storage question.

## Relation to prior wiki pages

**Her "same compute on every query" objection is the [LLM routing page](../ai-routing/llm-routing.md)'s founding premise, restated by someone who is not a routing researcher.** [LLMRouter (08-14)](../ai-routing/2026-08-14-llmrouter-unified-routing-infrastructure.md), which unified 16+ routers under one formalism and a cost-aware benchmark, found that learned routers beat the strongest *fixed-model* baseline by 14.6% relative and that lightweight routers get more competitive as budgets tighten. Hooker reaches the same conclusion as a consequence of who gets to build models. **Routing is arriving at the same destination from efficiency, from personalisation, and now from access.**

**The scaling thesis has an existence proof two days later.** [GLM-5.3 (08-14)](../llms-foundation-models/2026-08-16-glm-5-3-post-training-only-frontier.md) is the same base model as GLM-5.2 with substantially extended post-training, roughly 750B parameters against Kimi K3's ~2.2T, matching or surpassing frontier models on many agentic coding benchmarks. Z.ai's own sentence is "scaling post-training is all we did." That is Hooker's thesis with a model attached, published two days apart, neither referencing the other.

**And the search-not-insight finding is now cross-confirmed.** [Prime Intellect's 153-run autonomous research study (08-16)](../agentic-systems/2026-08-16-measuring-autonomous-ai-research.md) found agents are strong at optimizer search, hyperparameter sweeps, and stacking known methods, and weak at proposing new ideas, needing upstream human records to keep climbing. **Hooker treats exactly that property as the product's competitive advantage; Prime Intellect treats it as the ceiling.** Same empirical finding, opposite valence, and the disagreement is about whether breadth of search substitutes for originality or merely postpones needing it.

## Gaps

A vendor talk with no paper, no reproducible benchmark, and win rates whose stopping rule the speaker herself flags as distorting. "Beats our research staff" is unquantified. The slow-death-of-scaling evidence cited (the Open LLM Leaderboard ratio of best sub-13B model to all larger models flipping over time, plus recent large models missing stepwise gains) is suggestive rather than decisive, and the same evidence is compatible with a temporary plateau.

## Related pages

- [../ai-routing/llm-routing.md](../ai-routing/llm-routing.md)
- [../llms-foundation-models/scaling-laws.md](../llms-foundation-models/scaling-laws.md)
- [../hardware/compute-economics.md](../hardware/compute-economics.md)
- [../agentic-systems/2026-08-16-measuring-autonomous-ai-research.md](../agentic-systems/2026-08-16-measuring-autonomous-ai-research.md)
