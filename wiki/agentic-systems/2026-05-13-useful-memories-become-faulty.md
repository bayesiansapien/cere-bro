# Useful Memories Become Faulty When Continuously Updated by LLMs

**Date:** 2026-05-13
**Source:** [arXiv 2605.12978](https://arxiv.org/abs/2605.12978) · HuggingFace Daily Papers
**Tier:** 2. Agent memory, consolidation hazards
**Raw:** [`raw/huggingface/2026-05-13-useful-memories-become-faulty-when-continuously-updated-by-l.md`](../../raw/huggingface/2026-05-13-useful-memories-become-faulty-when-continuously-updated-by-l.md)

## TL;DR

Agentic-memory systems aim to consolidate raw trajectories into reusable text "lessons." This paper says today's LLMs cannot do that consolidation reliably. As updates accumulate, memory utility rises then degrades, often falling below the no-memory baseline. Even when consolidating from ground-truth solutions, GPT-5.4 fails on 54% of ARC-AGI problems it had previously solved without memory. The regression traces to the consolidation step, not the underlying experience: identical trajectories yield qualitatively different memories under different update schedules. Episodic-only control (keep raw trajectories, don't consolidate) remains competitive with the best consolidators tested. In a controlled ARC-AGI Stream environment with Retain, Delete, Consolidate actions, agents preserve raw episodes by default and double the accuracy of forced-consolidation counterparts; disabling consolidation matches the auto regime.

## Why it matters

The agentic-memory category has been growing fast (GBrain Twitter retweet 13-May, AgentRunbook in LME-V2 today, Mem0 and Zep referenced across the Twitter feed). All of them assume that consolidating raw trajectories into LLM-rewritten "lessons" is the right primitive. This paper says the assumption is wrong: today's LLMs over-rewrite, lose evidence, and produce memories that hurt performance.

The 54%-of-previously-solved-problems failure rate is the headline. The model loses a problem it had already solved, because the consolidated memory of how it solved the problem is now wrong. The fix is not better consolidation, it is *less* consolidation; episodic preservation as the default with gated consolidation explicitly invoked.

## Mechanism

Consolidation passes a trajectory or set of trajectories through an LLM rewrite step. Each rewrite is a lossy step; the loss is structurally biased (toward narrative coherence, generalization claims, removal of details that "seem incidental"). With multiple rewrites, the error compounds. The same trajectories under different update schedules produce different consolidated memories, because the rewrite-order matters.

The paper's controlled environment exposes three actions: Retain (keep raw), Delete (remove), Consolidate (rewrite into a lesson). Agents that default to Retain and only Consolidate when explicitly triggered double the accuracy of forced-consolidation counterparts. The episodic-only control (Retain everything) matches the auto regime. The implication is that good agent memory is mostly raw retention plus retrieval, not LLM-rewritten distillation.

## Relation to prior wiki

- **LongMemEval-V2 (today)** — companion paper introducing AgentRunbook-C, which stores trajectories as files and uses a coding agent to gather evidence in a sandbox. This is structurally a Retain-and-Retrieve approach, not a Consolidate approach. The Useful Memories paper validates the choice: AgentRunbook-C's 72.5% performance exceeds the best RAG baseline because it does not over-consolidate. The two papers compose into a recipe.
- **GBrain retweet (2026-05-13)** — Garry Tan's "Y Combinator CEO's personal agent brain" pitches consolidated memory that "wires itself, enriches itself, and compounds while you're not even using it." This paper is the direct critique: that exact design pattern produces degraded memory over time. Builders in the agentic-memory space should read this before shipping more consolidation pipelines.
- **Persistent Agent Infrastructure (2026-04-23)** and the **Claude Code Memory Systems (2026-04-25)** entries — Claude Code uses a tiered memory architecture with file-system raw storage as the foundation. Today's paper is the empirical case for that design over the rewrite-everything alternative.
- **NanoResearch retweet (2026-05-13)** — tri-level co-evolution of skill bank, memory, and policy. This paper applies pressure on the memory layer, raw memory beats consolidated memory in current LLM hands.

## Research angle

Three open questions. (1) When *should* consolidation fire? The paper shows that explicit gating helps, but does not propose a learned policy for when to consolidate. That is a tractable next paper. (2) Are the failure modes specific to text-rewrite consolidation, or do they extend to vector-summary memory (Mem0, Zep)? The paper's framing suggests text-rewrite is the worst case, but vector summaries may have analog degradation. (3) Is the failure model-size dependent? GPT-5.4 fails on 54% of ARC-AGI problems. A frontier model trained explicitly on consolidation traces might do better. The paper does not test this.

## Why Tier 2

The agentic-memory category is one of the most active in mid-2026 (multiple Twitter pitches, multiple HF papers in two weeks). This paper makes a falsifiable, load-bearing claim against the dominant design pattern. It should change how the next month of agentic-memory papers frame their contributions.
