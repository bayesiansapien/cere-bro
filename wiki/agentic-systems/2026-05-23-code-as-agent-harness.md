# Code as Agent Harness

**Source:** Twitter farmer 2026-05-23 morning (@burkov retweet of paper).
**arxiv:** [2605.18747](https://arxiv.org/abs/2605.18747)
**Why it is here:** Not in today's HuggingFace top, not in Kurate. Came in via @bayesiansapien curated retweet, and the abstract is substantive enough to warrant a wiki page per the twitter-as-source rule.

## TL;DR

LLMs have moved from producing standalone code to powering agents: systems that plan over many steps, call external tools, keep track of changing state, and recover from their own errors during long-running tasks. Inside these systems, code has become the working material for almost everything: agents write small programs to reason through math, drive a browser, query a database, test their own outputs, and share intermediate work with other agents through files in a repository. Existing surveys treat code as the final answer a model produces. The authors argue that code is now the harness: the persistent, executable, version-controlled substrate that makes long-horizon agents possible.

## Why this matters

The "harness" framing matches what @_vmlops articulated in this morning's retweet thread: same model, same prompt, full harness produces orders of magnitude better output than the same model without harness. Anthropic's internal experiment with Opus 4.5 (cited in the retweet) was the proof-of-concept; this paper is the academic articulation of what a harness actually is.

The thesis is that code is the right medium for harness construction because it is (a) executable, so the agent's plan can be tested, (b) persistent, so state survives across steps and across agents, (c) version-controlled, so failed branches can be reverted, and (d) compositional, so primitives can be combined into larger tools. None of these are true for natural-language plans or for tool-call sequences.

## Connections to prior wiki state

This is the strongest articulation yet of a pattern that has been forming in agent research for a year. [Karpathy's Autoresearch (covered in today's Ken Huang taxonomy)](../agentic-systems/) is a concrete instance: a research agent that edits one Python file, runs a fixed evaluation, and uses git as memory. Karpathy's setup is a Code-as-Harness system in the strict sense.

The taxonomy from Ken Huang's piece this morning maps cleanly: Compound Engineering uses HTML planning artifacts (a Code-as-Harness variant where the harness is browser-readable rather than git-readable). gstack uses skill files (another harness layer). Superpowers uses TDD-enforced spec files. Karpathy's Autoresearch uses program.md + train.py + git log. All four are instances of the same pattern: the harness is a structured, file-based representation of the agent's working environment.

The "agents need memory they can learn from, not just longer prompts" retweet from @DanKornas this morning (ReasoningBank) makes the same point from the memory side. Code-as-Harness is the structural argument; ReasoningBank is the operational one.

## Gaps in the paper (from abstract only)

The abstract surveys the field. Without reading the full paper, the question is whether it goes beyond cataloging known patterns to proposing new ones. The strongest such surveys (the early multi-agent reasoning surveys, the early CoT surveys) anchored the field's vocabulary; the weakest just enumerated.

## Research angle

The most interesting open question: what is the *minimum* harness sufficient for a given task class? Karpathy's three files (program.md, train.py, prepare.py) is one end. Cursor's full IDE-as-harness is another. Whether the right harness is task-dependent or whether there is a single "compound harness" that works for all agent tasks is unresolved.

A deeper question: harness engineering has been almost entirely human-designed so far (Compound Engineering, gstack, Superpowers are all human-authored). Can the agent learn to design its own harness? The "Compound" step in Compound Engineering is a step in that direction; the agent reflects after each feature and updates the harness files. Whether agents can fully bootstrap their own harness from scratch is the recursive self-improvement open problem in concrete form.

## Raw source

Tweet text (curated retweet via @bayesiansapien): see [raw/twitter/2026-05-23-morning.json](../../raw/twitter/2026-05-23-morning.json) (curated item #2).
