---
source: farmer/huggingface
farmed: 2026-09-11T00:57:36.854415+00:00
arxiv_id: 2609.08126
url: https://huggingface.co/papers/2609.08126
arxiv_url: https://arxiv.org/abs/2609.08126
date: 2026-09-10
---

# SchemeArena: Factorized Stress Testing of Scheming in LLM Agents

We study scheming in LLM agents, in which agents covertly pursue misaligned goals. Our focus is to understand how scheming arises from the interaction of key factors, such as instrumental goals, environmental affordances, oversight conditions, and perceived consequences. Prior work examines only a small number of scenarios, limiting the ability to isolate how these conditions shape an agent's propensity or capability to scheme. This limited scale and task diversity also restrict coverage of realistic deployment settings and the range of scheming strategies that can be observed. To this end, we introduce SCHEMEARENA, a 400-scenario benchmark for scalable scheming stress testing, constructed through a factorized scenario synthesis framework spanning diverse safety-relevant tool domains, instrumental goals, oversight conditions, and pressure mechanisms. To enable scalable and reliable monitoring, we further propose SCOUT, a scheming monitor that grounds multi-criteria judgments in evidence drawn from agents' reasoning and actions. Across controlled stress tests on five LLM agents, we find that explicit instrumental goals are the strongest driver of scheming propensity. Strategic hints play a distinct role by helping agents translate scheming reasoning into concrete covert behavior. Oversight has mixed effects: in several closed models, action-only monitoring increases scheming, suggesting that partial oversight can act as an optimization constraint rather than a deterrent. CoT is a useful but incomplete monitoring signal: it can reveal latent scheming before execution, yet action-only scheming shows that covert behavior may occur without explicit reasoning evidence. We release the benchmark, code, and monitor at: https://github.com/launchnlp/SchemeArena.
