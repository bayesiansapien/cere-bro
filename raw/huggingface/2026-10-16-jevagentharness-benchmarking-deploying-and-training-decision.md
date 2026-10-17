---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.21412
url: https://huggingface.co/papers/2610.21412
arxiv_url: https://arxiv.org/abs/2610.21412
date: 2026-10-16
---

# JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs

Large language model (LLM) agents now fix software, operate computers and serve customers, but their harnesses, the programs that run them, call a large LLM at every step, which makes long tasks slow and costly. Most of these calls end in a multiple-choice decision, such as which tool to call next. Decision models such as Jev answer these questions directly, at a fraction of an LLM call's time and price. We ask how a harness can delegate these decisions to a decision model with little loss of success. To evaluate decision models in agentic tasks, we build AgentDecisionBench, which tests them from isolated questions up to control of a running agent, on public benchmarks and our DecisionGym environment. The decision model most accurate on isolated questions solved only 69.5% of agent tasks, and without a fitted confidence threshold, delegating tool choices lowered success by 19.0 points. Building on these findings, we then design JevAgentHarness, which fits this threshold for each choice on the agent's own trajectories and lets the LLM decide below it. Because existing decision models never see the states an agent reaches after its own mistakes, we train AgentDecision-4B, an open 4B model, on such states with Jev's answers as labels. On tasks unlike its training data, the agent solved 91.5% of them with AgentDecision-4B and 82.0% with Jev. On tasks like their training data, 4B models trained this way made agents 81.1-89.0% cheaper and up to 2.5 times faster, without losing 3 or more points of task success. The models, data, and harness will be released at https://github.com/JevAgentHarness/JevAgentHarness.
