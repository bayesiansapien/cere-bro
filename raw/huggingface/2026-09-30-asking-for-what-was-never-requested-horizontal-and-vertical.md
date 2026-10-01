---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37236
url: https://huggingface.co/papers/2609.37236
arxiv_url: https://arxiv.org/abs/2609.37236
date: 2026-09-30
---

# Asking for What Was Never Requested: Horizontal and Vertical Proactivity in Agents

An agent that uses tools typically responds to what the user explicitly asks, yet completing the task may require information the user never requested. Work on proactive agents mainly studies whether and when an agent should act on its own, not what information it should pursue. We study a distinct axis of proactivity: its content. Horizontal proactivity pursues unstated information that the current context already identifies, and vertical proactivity pursues needs that only earlier evidence reveals. A need graph, recovered from a benchmark's own decomposition, records which needs depend on which, so both forms, and whether the agent stops at the right time, can be scored from a transcript without a model judge. To learn this behavior, we propose Q&D (questioner and drafter), which trains a questioner to prefer the question whose continuation retrieves more of the required evidence, with no reward model or judge. On held-out splits of three multi-hop question-answering benchmarks, at equal retrieval spend, the trained questioner improves both forms of proactivity over the same model, prompted, and outperforms a prompted model 15times larger in the same role on two of the three, and the gain persists after controlling for question volume and length. Without further training, we place the questioner in an interactive customer-service agent with a simulated customer, where it completes more tasks while asking fewer questions, and in retail it outperforms the 15times larger model with fewer follow-up turns from the customer. These results show that proactivity depends not only on whether an agent acts without being asked, but also on what it chooses to pursue and when it stops.
