# AgentLens: the Lucky Pass problem in SWE-agent evaluation

**Source:** HuggingFace Daily Papers · 2026-05-14
**Paper:** [arXiv 2605.12925](https://arxiv.org/abs/2605.12925)
**Raw:** [raw](../../raw/huggingface/2026-05-14-agentlens-revealing-the-lucky-pass-problem-in-swe-agent-eval.md)
**Tier:** 2. Agent evaluation, benchmark integrity, process-level scoring

## TL;DR

SWE-bench Verified is judged by a binary signal: did the final patch pass the tests? AgentLens shows 10.7% of passing OpenHands trajectories are Lucky Passes — regression cycles, blind retries, missing verification, or temporally disordered exploration. The framework merges passing trajectories per task into a Prefix Tree Acceptor reference space and labels actions via a context-sensitive intent-stage labeler. Some models drop five ranking positions when scored by trajectory quality instead of pass rate. The bench: 1,815 trajectories from 47 tasks across 8 model backends, released as AgentLens-Bench.

## Why it matters

The wiki has been tracking benchmark-integrity papers since [Soohak](../llms-foundation-models/2026-05-12-soohak-research-math-benchmark.md) (research-math benchmark with calibrated refusal subset) and the [AAAI-26 AI Review Pilot](../../raw/kurate/2026-05-14-cs-ai.md) (Kurate #10). AgentLens adds the agentic axis: even on a benchmark with verifiable test outcomes, the trajectory that *produced* the pass matters. A correct answer obtained through 47 regression cycles is not the same as a correct answer obtained cleanly. The implication for the post-Mythos cyber-eval debate, where models pass cyber ranges and the rate-of-pass is the headline number ([AISI report, 2026-05-13](https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing)), is that the doubling-rate metric is incomplete: how many of those passes are Lucky?

## Mechanism

Two components:

```
  passing trajectories per task ──► merged into Prefix Tree Acceptor (PTA)
                                    reference space of correct behaviors
                                    (47 task-level PTAs)
                                                    │
                                                    ▼
  trajectory under test ──► intent-stage labeler ──► Exploration / Implementation
                                                     / Verification / Orchestration
                                                    │
                                                    ▼
                                            composite quality score
                                            (Lucky / Solid / Ideal)
```

The intent-stage labeler is context-sensitive — it uses the trajectory history, not the tool identity, to decide what stage an action belongs to. The same `bash` call is Exploration if it follows a failed run, Verification if it follows an edit. That distinction is what allows the labeler to detect temporally-disordered work patterns (Verification before Implementation, etc.).

Five Lucky-Pass mechanisms surface from the 10.7%: regression cycles, blind retries, missing verification, temporally disordered phases, and orchestration drift. The paper does not claim these are exhaustive; they are the categories that recur often enough in the 1,815-trajectory corpus to be named.

The most striking number: some of the 8 evaluated model backends move by 5 ranking positions when scored by quality instead of pass rate. That ranking instability suggests pass-rate is not just incomplete, it is *misleading* for between-model comparison.

## Connections

- **DAgger for LLM agents** ([2026-05-14](2026-05-14-dagger-llm-agents.md)) and AgentLens share a diagnosis: covariate-shifted trajectories produce chaotic state distributions. AgentLens measures the symptom (Lucky Passes), DAgger fixes the cause (train on on-policy states with dense supervision). The most useful composition: filter trajectories with AgentLens, keep Solid+Ideal only, train DAgger on those. The paper does not propose this.
- **Soohak refusal subset** ([2026-05-12](../llms-foundation-models/2026-05-12-soohak-research-math-benchmark.md)) showed that frontier models confidently produce wrong answers on ill-posed problems. AgentLens shows that frontier models also produce *right* answers via wrong processes. Two papers in three days establishing that pass-rate alone underreads model quality.
- **AISI cyber doubling-rate report** ([2026-05-13](https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing)) reports the length of cyber tasks that frontier models solve has doubled every 4.7 months. AgentLens's framing implies that doubling rate may be partially driven by Lucky Passes. The cyber-eval community needs an AgentLens for its trajectories before treating doubling-rate as the headline.
- **MAP (Map-then-Act)** ([2026-05-14](2026-05-14-map-then-act-paradigm.md)) attributes the bottleneck to *delayed environmental perception* — agents that don't build a global prior fall into trial-and-error loops. That is the structural cause of the Lucky Pass pattern AgentLens names. MAP's "Map-then-Act" proposes the architectural fix, AgentLens provides the measurement. Two papers on the same day with one diagnosis and one prescription.

## Research angle

1. **Per-stage post-training targets.** With process labels for Exploration / Implementation / Verification / Orchestration, the natural follow-up is stage-conditional reward shaping during RL post-training. Reward Verification more, penalize Verification skipped. AgentLens-Bench is the dataset for this.
2. **Public-to-hidden ranking stability.** AssetOpsBench ([2026-05-14](https://arxiv.org/abs/2605.08518)) reports public-to-hidden score correlation of −0.13. AgentLens reports rank movements of up to 5 positions when re-scored. Both papers say the same thing: aggregate leaderboard standings are unreliable. The shared frame ("aggregate metrics over-aggregate") is now a third paper in the benchmark-skepticism thread (Soohak, AssetOps, AgentLens).
3. **Generalization beyond OpenHands.** All 2,614 trajectories analyzed are from OpenHands. Whether the 10.7% Lucky rate is OpenHands-specific or a property of SWE-bench plus reward-only training is the immediate question. If it generalizes, the field needs to re-rank every SWE-bench leaderboard.

## Where it lives

Update [agent-benchmarks.md](agent-benchmarks.md) — first paper in the wiki to do process-level evaluation of SWE-bench. Update [tool-calling.md](tool-calling.md) — the stage-labeler framework is reusable beyond SWE-bench.
