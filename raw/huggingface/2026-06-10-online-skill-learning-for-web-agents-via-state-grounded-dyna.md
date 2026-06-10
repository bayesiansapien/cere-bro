---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.04391
url: https://huggingface.co/papers/2606.04391
arxiv_url: https://arxiv.org/abs/2606.04391
date: 2026-06-10
---

# Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval

Language agents increasingly rely on reusable skills to improve multi-step web automation across related tasks. A growing line of work studies online skill learning, where agents continually induce skills from previous task trajectories and reuse them in future tasks on the fly. However, existing methods mainly reuse skills at the task-level: a fixed set of skills is retrieved based on the initial task instruction and then held fixed throughout execution. This static strategy is misaligned with web execution, where the appropriate next action depends not only on the task goal but also on the current webpage state, which often transitions into situations that the initial skills fail to cover. To address this gap, we propose State-Grounded Dynamic Retrieval (SGDR), an online skill learning method that enables stepwise skill reuse for web agents. SGDR consists of three components: a sliding-window extraction process that turns completed trajectories into reusable sub-procedures invokable at intermediate execution states, a dual text-code representation that connects skill retrieval with executable action, and a state-grounded dynamic retrieval mechanism that matches skills to both the task goal and the current webpage state. Experiments on WebArena across five domains show that SGDR consistently outperforms strong baselines, achieving average success rates of 37.5% with GPT-4.1 and 24.3% with Qwen3-4B, corresponding to relative gains of 10.6% and 10.0% over the strongest baseline, respectively. The code is available at https://github.com/plusnli/skill-dynamic-retrieval.
