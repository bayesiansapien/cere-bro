# The Self-Improving OSS Agent Stack (Marc Klingen, Langfuse)

**Channel:** AI Engineer
**Published:** 2026-10-06
**Source:** https://www.youtube.com/watch?v=TeErpYBUIeM

## TL;DR
Langfuse co-founder Marc Klingen argues that the agent improvement loop (trace production, curate datasets, write evals, propose fixes, backtest, deploy) is now mostly automatable by coding agents, and that humans should stay in only two places: approving changes to datasets and evaluators, and reviewing proposed fixes for overfitting. The demo is an internal changelog-writer agent whose PR approvals and change requests become eval signal. A coding agent with the Langfuse skill diagnoses "leaks internal jargon, low clarity," adds a matching dataset slice and evaluator, writes a v2 prompt, backtests it against v1, and ships it via prompt management. The framing is right and matches what Arize and others are pitching in the same week. The talk is thin on the real risk: once agents also edit the evaluators, the loop can grade itself.

## Key Takeaways
- **Loop hierarchy:** token loop (2023, Copilot) to task loops (2024) to 2025/26 loops where agents decide what to fix, propose fixes, and verify them. Each level unlocked by model capability, not tooling.
- **Online plus offline must be one system:** observability tools (Datadog-style) see production but do not benchmark; MLOps tools (MLflow, W&B) benchmark on stale data. Langfuse's thesis is joining the two.
- **Where AI is used most today:** proposing fixes, hill-climbing against a fixed dataset plus eval criteria (swap model, change context aggregation, try "whatever is on X this week").
- **New in the last month or so:** agents also maintaining datasets (keeping them aligned with real user query distribution) and proposing new evaluators from observed error patterns (e.g. "do not name competitors," "answer in the user's language").
- **Human gates:** review dataset and evaluator edits (they define the boundary other agents optimize against) and review fixes (avoid overfitting to a random production quirk outside the agent's scope).
- **Implicit signal is the fuel:** user swearing, "that's wrong" replies, and accept/edit ratios on drafted messages feed the loop without developer labeling. In the demo, the human edit ratio on changelog PRs was the key metric.
- **Demo result:** v2 held format compliance and accuracy flat while improving the "user-facing language" score. Auto-merged because the agent only opens PRs, never publishes directly.
- **Cadence:** best users run the improvement agent as a cron job (daily or weekly) over batches of fresh traces, feedback, and in-app annotations.
- **Infra shift:** Langfuse workload went from write-heavy (ingest traces) to read-heavy (agents querying huge trace volumes). Implication: retain unsampled traces long-term and own the data layer.

## Architecture & Optimization Mechanics
The loop is greedy hill-climbing with a moving objective. Fix proposal is cheap search over a discrete space (model, prompt, context assembly, skill text). The objective is the union of evaluators, and the dataset defines the distribution. Klingen's key structural point is the separation of concerns: the evaluator and dataset are the "loss function," and only humans may change it; agents may change the "parameters" (implementation). That separation is what prevents the loop from collapsing into Goodhart. The moment the same agent family proposes evaluators, writes the fix, and scores it, you get the self-grading circularity seen in recent reward-hacking work.

Two mechanics matter for an optimization researcher. First, the "positive delta" in the demo is a single-run comparison on a freshly constructed slice designed to reproduce the bug. That is a test set built from the training signal, so the delta is close to guaranteed. A real gate needs a frozen held-out set and variance across runs. Second, the read-heavy shift is a cost story: an improvement agent chewing through months of unsampled traces with LLM calls is itself an inference workload that needs routing (cheap model for filtering and clustering, frontier model only for diagnosis and fix proposal).

## Grounded Context (Web Enrichment)
Ownership has changed since the "own your data, open source" pitch was born: ClickHouse acquired Langfuse on January 16, 2026, alongside a $400M Series D at a $15B valuation. Langfuse already stored telemetry in ClickHouse, so the "scalable cheap data layer" closing pitch is effectively a ClickHouse pitch, and the read-heavy agent workload argument maps directly onto ClickHouse's analytical engine. Langfuse reported 2,000+ paying customers and 19 of the Fortune 50 at acquisition. The "Langfuse agent skills" in the demo are real: shipped May 26, 2026, following the open Agent Skills standard and working with Claude Code, Cursor, and Codex. Klingen gave a separate AI Engineer talk on why skills beat stale pretraining knowledge for instrumentation.

The "I don't write prompts, I have loops" and "auto research" references point to Karpathy's autoresearch (March 2026): an agent edits a training script, runs a 5-minute experiment, keeps or discards based on val_bpb. Commentators flagged the same issue this talk skips: hundreds of greedy iterations against one validation set overfit the metric, and Karpathy himself called it fragile. Langfuse's version is strictly riskier because the metric (LLM-judge evaluators) is softer and is itself being edited by agents. The human review gate on evaluators is not optional overhead. It is the only thing anchoring the objective.

Sources: [ClickHouse acquires Langfuse](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability), [Langfuse: Joining ClickHouse](https://langfuse.com/blog/joining-clickhouse), [SiliconANGLE on $400M round and acquisition](https://siliconangle.com/2026/01/16/database-maker-clickhouse-raises-400m-acquires-ai-observability-startup-langfuse/), [Langfuse agent skill changelog](https://langfuse.com/changelog/2026-05-26-langfuse-agent-skill), [AI Engineer: Skill Issue talk](https://ai.engineer/talks/skill-issue-lessons-from-skilling-up-coding-agents-to-use-langfuse), [Karpathy autoresearch overview](https://kingy.ai/news/autoresearch-karpathys-minimal-agent-loop-for-autonomous-llm-experimentation/), [Autoresearch overfitting discussion](https://techntrek.is-a.dev/posts/2026-03-20-karpathy-autoresearch)

## Real-World Application / Actionable Step
- **Split loss from parameters in your router loop:** let an agent propose routing thresholds, prompt variants, or model swaps nightly, but lock the eval set and judge rubric behind human approval. Version them separately.
- **Use edit ratio as a free label:** wherever a human accepts or edits model output (code review, drafted replies), log the diff size per trace. High edit ratio on cheap-model outputs is a direct routing-failure label.
- **Never trust a single-slice delta:** when an agent reports v2 beats v1 on a slice it just built, require a frozen held-out set, 3+ seeds, and a no-regression check on unrelated slices before merging.
- **Retain unsampled traces:** for compression and routing work, year-old traces are the distribution-shift baseline. If self-hosting, Langfuse on ClickHouse is a reasonable cheap store; otherwise check your vendor's sampling and retention.
- **Route the improvement agent itself:** clustering and filtering traces on a small model, diagnosis and fix proposal on a frontier model. Measure its token bill like any other inference workload.
