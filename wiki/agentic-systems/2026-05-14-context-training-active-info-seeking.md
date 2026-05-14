# Context Training with Active Information Seeking

**Source:** HuggingFace Daily Papers · 2026-05-14
**Paper:** [arXiv 2605.13050](https://arxiv.org/abs/2605.13050)
**Raw:** [raw](../../raw/huggingface/2026-05-14-context-training-with-active-information-seeking.md)
**Tier:** 2. Context optimization, agentic retrieval, deployment-time adaptation

## TL;DR

Most context-optimization methods are closed-loop: they manipulate the prompt using only the model's intrinsic knowledge. This paper adds Wikipedia search and browser tools so the optimizer can actively seek information. The headline finding is the failure case first: naively wiring tools into a sequential context-optimization pipeline *degrades* performance. The recovery is a search-based training procedure that maintains and prunes multiple candidate contexts. With that, active info-seeking delivers consistent gains across Flores+ translation, HealthBench, LiveCodeBench, and Humanity's Last Exam. Robust across hyperparameters, data-efficient, and the generated contexts transfer across models.

## Why it matters

Two threads in the wiki converge on this paper. [Bright-Pro Rtriever](2026-05-07-bright-pro-rtriever-reasoning-retrieval.md) (05-07) introduced reasoning-aware retrieval. [DCI (Direct Corpus Interaction)](2026-05-09-dci-direct-corpus-interaction.md) (05-09) bypassed retrieval entirely with direct corpus interaction. Active Info Seeking sits between them: keep retrieval, but make the retrieval policy itself an optimization target. The contextual-knowledge-at-deployment problem just keeps getting more design space.

## Mechanism

The negative result is the most useful part. A naive pipeline — let the context optimizer call tools — degrades performance. The reason, implicit in the abstract: a sequential single-context optimizer keeps overwriting itself when tool outputs contradict prior context decisions. The recovery mechanism is a search-based training procedure that maintains and prunes multiple candidate contexts. The optimizer keeps a beam of contexts alive, lets each pursue different search trajectories, and prunes based on downstream performance.

Three properties the paper claims:

- Data-efficient. Specific numbers not in abstract but flagged.
- Robust across hyperparameters.
- Generated contexts transfer across models.

The transfer claim is the structurally important one. If the optimized contexts work across base models, the optimization is buying something about *the problem* rather than *the model*, which means deployment-time context tuning can be a one-time cost rather than per-model.

## Connections

- **MAP (Map-then-Act)** ([2026-05-14](2026-05-14-map-then-act-paradigm.md)) builds an environment prior before acting. Active Info Seeking builds a context prior before answering. Both are the same architectural move applied at different scales (environment vs information).
- **Bright-Pro Rtriever** ([2026-05-07](2026-05-07-bright-pro-rtriever-reasoning-retrieval.md)) introduced reasoning-aware retrieval; Active Info Seeking is the more active version where the optimizer chooses what to retrieve based on context-trajectory performance, not query embedding.
- **HuggingPapers δ-mem** ([@HuggingPapers tweet, 2026-05-13](https://nitter.net/HuggingPapers/status/2054431768779067542#m), [paper arXiv 2605.12357](https://arxiv.org/abs/2605.12357)) provides a frozen-model memory layer; Active Info Seeking provides a deployment-time context layer. Both bypass fine-tuning to give models new information. The two compose: δ-mem for short-term memory across a session, Active Info Seeking for long-term context construction across deployments.

## Research angle

1. **Composes with DAgger.** Both papers attack covariate shift, but at different layers. DAgger interpolates teacher/student policies during data collection; Active Info Seeking maintains a beam of contexts during optimization. A composed system would maintain beams of trajectories *and* contexts simultaneously.
2. **Tool-call budget under search.** The search-based procedure presumably costs more tool calls than the naive pipeline. The paper claims data efficiency, but the budget the search consumes in tool calls vs the naive pipeline is the production-relevant economic question.
3. **What does context transfer mean.** If contexts optimized on one model help another, this is closer to "discovering the right problem framing" than "tuning the model." That is the same kind of model-independent search ARC-AGI-3 papers have been pointing at, but applied to natural-language tasks.

## Where it lives

Update [tool-calling.md](tool-calling.md) — Active Info Seeking is the first paper in the wiki where the tool-using *optimizer* is the load-bearing component, not the deployed agent.
