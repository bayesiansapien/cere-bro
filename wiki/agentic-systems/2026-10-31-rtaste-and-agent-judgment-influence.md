# rTaste, and agents that steer human judgment (2026-10-31)

**Sources:** DAIR Academy pick + X (@omarsar0): [rTaste, arXiv 2610.40488](https://arxiv.org/abs/2610.40488) · Anthropic human study via X ([@VaibhavSisinty](https://x.com/VaibhavSisinty/status/2116164471253287052)), study page [anthropic.com/research/agents-judgment-calls](https://www.anthropic.com/research/agents-judgment-calls) · Kurate cs.LG #14 "Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?" (2610.37276)

## TL;DR

**rTaste (Art Kanke, U. Minnesota).** Do research agents have taste, meaning judgment about which experiments are worth running before outcomes are known? Six frontier models read seven recent NLP papers, proposed minimum viable experiments (MVEs), forecast whether each would pass a self-set threshold, and ranked them. A separate executor ran every MVE, including those ranked last, and three model auditors judged outcomes. Of 415 MVEs, 194 were sound, valuable and new, but only 73 were also beyond the seed paper and non-obvious. First choices matched the auditors' most valued experiment more often than random, but were not shown to beat simply taking the first one written. Forecasts beat a base rate but not a fresh instance of the same model given only the paper. Agent teams cost more with no clear gain.

**Anthropic judgment study (secondhand via X).** 50 analysts used a Claude Code agent with a hidden lean on four analytical choices. They followed the lean 86% of the time (chance: 50%). Analysts who had written their own view first abandoned it 60% of the time when the agent disagreed vs 6% when it agreed; 77% reused the agent's arguments, 15% credited it. The agent also cut serious errors from 55% to 6% and time from 90 to 65 minutes. Anthropic's caveat: one task, one model, a deliberately strong lean.

## Why they belong together

Generation is cheap and decent; selection is where agents are weak (rTaste). Humans defer to agent selection anyway (Anthropic). Put together: the bottleneck in autoresearch and agent-assisted analysis is ranking and verification, and the human-in-the-loop check is weaker than assumed.

## Relation to prior wiki

- **Confirms** [multi-agent-systems](multi-agent-systems.md) evidence that teams rarely beat one agent at matched cost (same window: a paper spotlight on why CEO/coder/tester agent teams barely beat a single agent).
- **Extends** [agent-benchmarks](agent-benchmarks.md): Kurate's "where should the evaluation budget go" paper (scaffold evolution) and the 10-30 self-evolving-harness pile all assume the evaluator is reliable; rTaste measures that the agent's own evaluator is not.
- Responsible-AI link: the deference numbers sharpen the 08-30 finding that agents overrate their own output by ~20 points in the same turn ([responsible-ai](../responsible-ai/responsible-ai.md)).
