# π-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows

**arXiv:** [2605.14678](https://arxiv.org/abs/2605.14678) · [HuggingFace](https://huggingface.co/papers/2605.14678)
**Raw:** [`raw/huggingface/2026-05-24--bench-evaluating-proactive-personal-assistant-agents-in-lon.md`](../../raw/huggingface/2026-05-24--bench-evaluating-proactive-personal-assistant-agents-in-lon.md)
**Date ingested:** 2026-05-24

## TL;DR

π-Bench is a 100-task multi-turn benchmark across five persona-driven domains, built specifically to measure whether assistant agents can act on hidden user intent before the user has stated it. The benchmark separates two scores: task completion (did the user get what they asked for) and proactivity (did the agent surface needs the user did not articulate). Initial results show those two scores are weakly correlated, frontier agents can complete tasks competently while still being passive, and prior interactions across sessions help proactive intent resolution downstream.

## Why this matters

Most existing agent benchmarks (TerminalWorld, Spreadsheet-RL, SWE-bench, GAIA) score task completion under fully specified requests. The implicit assumption is that the user already knows what they want and types it in. π-Bench breaks that assumption. It evaluates whether the agent can fill a gap the user did not signal, which is the live failure mode of current consumer AI assistants. Frontier models still default to literal interpretation of explicit requests, which is what makes their "assistant" use case feel transactional rather than agentic.

## Method

- 100 multi-turn tasks across 5 user personas, each persona spans multiple related tasks with cross-session continuity.
- Hidden user intents are seeded into each persona profile (preferences, constraints, recurring obligations) that the user does not state outright but the agent should respect.
- Inter-task dependencies: completing task N depends on having inferred something during task N-1 that was never explicitly stated.
- Scoring is decomposed: a task-completion score (standard pass/fail), and a proactivity score (did the agent surface or address the hidden intent without being asked).

## Findings

1. Proactive assistance remains an open problem. Frontier agents complete the explicit task at high rates but score poorly on proactivity.
2. Task completion and proactivity scores are distinct axes, not a single capability. Models can be high on one and low on the other.
3. Prior interaction history is load-bearing: when the same model encounters the same persona across tasks, its proactivity score increases on later tasks. This validates persistent memory as a real lever for proactive behavior.

## Relation to prior wiki state

- Connects to [agent-memory.md](agent-memory.md) — π-Bench's cross-session result is direct downstream evidence for why persistent agent memory matters. Persona profiles function as an external memory store the agent must keep coherent across sessions.
- Connects to the 2026-05-13 LongMemEval v2 work (long-horizon memory evaluation): π-Bench is a complementary benchmark that measures the consequence of memory failure (passive behavior) rather than memory accuracy directly.
- Connects to 2026-05-23 SR²AM (self-regulated simulative planning): SR²AM learns when to plan; π-Bench would be a natural eval where the planner has to invoke deliberation in response to anticipated unstated needs rather than in response to explicit prompts.

## Open questions

- How does the proactivity score correlate with hallucination? An agent that volunteers unstated assumptions may also be one that confidently invents constraints the user does not actually have. The benchmark needs to penalize false-positive proactivity.
- Are the five personas representative of the proactivity surface, or is there persona overfitting? A benchmark with 100 tasks across 5 personas has only 20 tasks per persona, which is small for the long-horizon claim.
- The OpenClaw assistant is named in the abstract. Whether π-Bench results inform a future commercial proactive-assistant release is a watch item.

## Source

HuggingFace Daily Papers, [arxiv 2605.14678](https://arxiv.org/abs/2605.14678). First appeared on the wiki via this summary on 2026-05-24.
