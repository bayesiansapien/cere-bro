---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.14051"
url: "https://huggingface.co/papers/2605.14051"
arxiv_url: "https://arxiv.org/abs/2605.14051"
date: 2026-05-17
---

# SPIN: Structural LLM Planning via Iterative Navigation for Industrial Tasks

Industrial LLM agent systems often separate planning from execution, yet LLM planners frequently produce structurally invalid or unnecessarily long workflows, leading to brittle failures and avoidable tool and API cost. We propose SPIN, a planning wrapper that combines validated Directed Acyclic Graph (DAG) planning with prefix based execution control. SPIN enforces a strict DAG contract through validate_plan_text and repair prompting, producing executable plans before downstream execution, and then evaluates DAG prefixes incrementally to stop when the current prefix is sufficient to answer the query. On AssetOpsBench, across 261 scenarios, SPIN reduces executed tasks from 1061 to 623 and improves Accomplished from 0.638 to 0.706, while reducing tool calls from 11.81 to 6.82 per run. On MCP Bench, the same wrapper improves planning, grounding, and dependency related scores for both GPT OSS1 and Llama 4 Maverick.
