# SCRL: Subproblem Curriculum Reinforcement Learning for LLM Reasoning

**Source:** HuggingFace daily papers, 2026-05-23. "From Reasoning Chains to Verifiable Subproblems".
**arxiv:** [2605.22074](https://arxiv.org/abs/2605.22074)

## TL;DR

Outcome-based RLVR is inefficient on hard problems because correct final-answer rollouts are rare and sample-level credit assignment cannot use partial progress in failed attempts. SCRL (Subproblem Curriculum RL) derives verifiable subproblems from reference reasoning chains, with the final subproblem fixed as the original problem. Each subproblem position gets independently-normalized reward, and the advantages are assigned to the corresponding answer spans. The result is finer-grained credit assignment without external rubrics or reward models. SCRL lifts hard problems out of gradient dead zones, with larger relative gains as problems become harder. On seven math benchmarks, SCRL beats GRPO by +4.1 (Qwen3-4B) and +1.9 (Qwen3-14B) average points. On AIME24/25 and IMO-Bench, pass@1 improves by +3.7 and pass@64 by +4.6 on Qwen3-4B.

## What this paper does that prior RLVR did not

The credit-assignment problem in RLVR is that a single scalar reward at the end of a long reasoning chain provides no signal about which intermediate steps were good. Failed rollouts contribute zero gradient even when the first 80% of reasoning was correct. SCRL solves this by decomposing the original problem into a sequence of verifiable subproblems extracted from a reference chain. Each subproblem has its own normalized reward; advantages are then assigned to the answer spans for each subproblem. The final subproblem is the original problem, so the curriculum ends where standard RLVR begins.

The mechanism is best understood as a sparse-to-dense reward conversion. Standard RLVR has one sparse reward per trajectory. SCRL has one sparse reward per subproblem, which means roughly K rewards per trajectory if there are K subproblems. The variance reduction at fixed compute is the source of the gain on hard problems.

## Connections to prior wiki state

This is the third paper this week on RLVR's credit-assignment problem, alongside [DelTA (today, 2605.21467)](2026-05-23-delta-discriminative-token-credit-rlvr.md), which reshapes RLVR updates at the token-gradient level, and [uPRM (today, 2605.10158)](2026-05-23-unsupervised-process-reward-models.md), which replaces the response-level reward with an unsupervised process-level reward.

The three attack the same problem at three different granularities: SCRL at the subproblem level, uPRM at the step level, DelTA at the token level. The pattern is unambiguous: RLVR's outcome-only signal is too coarse, and the field is rapidly developing finer-grained credit-assignment machinery. Three papers on the same day with the same diagnosis is a strong signal.

A natural composition: use SCRL to break the problem into subproblems, use uPRM to verify step-level correctness within each subproblem, use DelTA to reshape the token-level updates from the resulting per-step rewards. If anyone runs that composition and gets additive gains, that is the first end-to-end finely-granular RLVR pipeline.

It also extends the [LongAct (04-18) finding that long-context training signal is concentrated in the first 5% of tokens](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md): both papers find that uniform reward distribution across a long sequence is wasteful, with most of the useful signal living in a small fraction of positions. SCRL's subproblem boundaries are an explicit way of identifying those positions.

## Gaps

SCRL requires reference reasoning chains to extract subproblems from. The paper does not specify how those references are obtained at scale or whether subproblem extraction is sensitive to the quality of the reference chain. If high-quality references require human annotation, SCRL re-introduces an annotation cost that PRM800K-style supervision was supposed to solve.

The +3.7 pass@1 / +4.6 pass@64 gain on AIME24/25 and IMO-Bench is impressive but on a small Qwen3-4B base. Whether the gain scales to larger models (where standard RLVR is already strong) is the natural question.

## Research angle

The strongest open question: does subproblem decomposition compose with explicit world-model planning (as in [today's SR²AM paper](../agentic-systems/2026-05-23-sr2am-efficient-agentic-reasoning-self-regulated.md))? Both papers attack the long-horizon reasoning problem. SCRL decomposes the supervision signal; SR²AM decomposes the action policy. A combined system would have explicit subproblem-aware planning with subproblem-aware credit assignment.

The cleanest follow-up is the automatic generation of reference chains. If a frontier model can produce reasonable reference chains for problems the policy can't yet solve, SCRL becomes a self-improving curriculum. If references must be human-curated, SCRL is more of an offline distillation technique than a scalable training procedure.

## Raw source

[raw/huggingface/2026-05-23-from-reasoning-chains-to-verifiable-subproblems-curriculum-r.md](../../raw/huggingface/2026-05-23-from-reasoning-chains-to-verifiable-subproblems-curriculum-r.md)
