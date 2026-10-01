---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.32915
url: https://huggingface.co/papers/2609.32915
arxiv_url: https://arxiv.org/abs/2609.32915
date: 2026-09-30
---

# AgentTell: Behavioural Side-Channel Leakage in Browser-Use Agents

Browser-use agents often carry information in their context as they move between websites. While it may be necessary for task completion, it also creates a privacy risk, especially when the information contains a private fact regarding the user. For example, an agent may learn a user's affiliation after reading a membership record. If it later selects a registration option specific to that affiliation on another website instead of a general option, the information gets leaked. In this work, we define and study behavioural side-channel leakage in browser-use agents, where an agent's actions inadvertently reveal private information (secret) retained from a prior website, despite an explicit instruction not to disclose it. We introduce AgentTell, a benchmark of 20 scenarios and 100 tasks in which an agent acquires a secret on one website and then completes a task on another website that offers secret-specific actions alongside a general action that reveals nothing. Our evaluation across 9,760 sessions on six backbones shows that agents carrying a secret reveal it through their actions in 61.1% of sessions. Even when agents explicitly state in memory that the secret must not be shared, they still reveal it in 56.7% of those sessions. Moreover, in 34.5% of leaking sessions, their final responses falsely assure users that the secret was not disclosed. These findings show that agents often fail to recognize side-channel leakage as a privacy risk.
