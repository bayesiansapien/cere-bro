---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.251265+00:00
arxiv_id: 2611.24025
url: https://huggingface.co/papers/2611.24025
arxiv_url: https://arxiv.org/abs/2611.24025
date: 2026-11-23
---

# Intent Contracts: Taking Tools Away from Agents

Intent contracts are an authorization interface for tool-using LLM agents in which the planning model holds no tools. For each step it submits a short logged contract: a goal, a verbatim quotation of the user, and scope fields. Code validates the contract, and a small trusted model checks it against the user's words and writes the tool call itself. Provided the validation and dispatch code is correct, every executed call is written by the trusted model, the planner's influence on a call is confined to a contract logged before it, and the trusted side decides how much of a request to carry out. We compare contracts with two reviewers of planner-written commands: one sees only the user's words and the command, the information boundary of a reasoning-blind permission classifier, and one also sees the planner's goal and a checked quotation. With gpt-6.1-terra as planner and GLM-5.3-Flash as the trusted model on three AmPermBench task families, every object changed under contracts is named in the goal of the contract that produced the change; under review the planner names objects in its commands and rarely in its goals. When the planner adds work the user never asked for, contracts complete the user's task in 27/30 runs and the intent-visible reviewer in 16/30, because a reviewer can only refuse a whole command. Contracts do not reduce unauthorized actions. They are indistinguishable from blind review, and once the benchmark's environment terms are clarified, every condition that changes state hits a wrong target in 40-49% of those runs. That error is the planner's choice of objects for an ambiguous reference, which no trusted model here can see the environment to check; telling the executor to decline when unsure does not change it. We evaluate benign over-reach with one pair of models, not adversarial planners. We release the plugin and run records.
