---
source: farmer/huggingface
farmed: 2026-08-07T06:50:52.124211+00:00
arxiv_id: 2608.06197
url: https://huggingface.co/papers/2608.06197
arxiv_url: https://arxiv.org/abs/2608.06197
date: 2026-08-07
---

# EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning

Training large language model agents for long-horizon tool use typically relies on interactions with real or synthesized executable environments, whose construction and verification are costly, or on external simulators that are difficult to ground. We introduce EnvACE, an agentic reinforcement learning method that replaces external environment interaction during training with world rehearsal. The policy alternates between acting and rehearsal: it first generates a tool call, then plays the role of the environment to produce the response induced by that action, and conditions subsequent decisions on the rehearsed response. Both roles are jointly optimized end-to-end using task-success rewards. Through world rehearsal, the policy internalizes the relationship between actions and their environment responses in its parameters, yielding an agent world model that directly supports decision making. Across BFCL-v4, tau^2-Bench, VitaBench, and FinMCP-Bench, EnvACE achieves strong and transferable performance, outperforming environment-scaling baselines in the overall evaluation. Controlled studies further show that world rehearsal consistently improves policy learning across model scales. At test time, the internalized world model enables private rehearsal before committed execution, yielding further gains under a moderate rehearsal budget without additional external interaction. Our findings establish world rehearsal as a new path toward scaling LLM agent training beyond the constraints of external environments. Our code is publicly available at https://github.com/Within-yao/EnvACE.
