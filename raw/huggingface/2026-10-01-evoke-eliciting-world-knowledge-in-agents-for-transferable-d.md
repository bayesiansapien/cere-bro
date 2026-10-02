---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.344953+05:30
arxiv_id: 2609.38334
url: https://huggingface.co/papers/2609.38334
arxiv_url: https://arxiv.org/abs/2609.38334
date: 2026-10-01
---

# EVOKE: Eliciting World Knowledge in Agents for Transferable Decision-Making

Large language models (LLMs) are increasingly deployed as agents for multi-step decision-making, yet transfer poorly to unseen environments. World-model methods address this by training agents to predict future observations, at the cost of additional training and errors that compound when predictions are used for planning. However, for LLM agents operating in digital environments, much of this world knowledge is already internalized during pretraining, which shifts the problem from acquiring it to eliciting it. We argue that typical post-training provides little pressure for such elicitation, since supervision under a single goal at each visited state inadvertently drives policies to rely on superficial contextual habits. We introduce EVOKE, a post-training method that supplies this pressure through goal diversity at fixed states. Motivated by theory showing that an agent competent across diverse goals must encode a world model recoverable from its action preferences, EVOKE holds the environment state and interaction history fixed and ranks the same candidate actions under alternative goals, forcing action preferences to change, so that a policy relying on contextual habits or single-goal correlations cannot order them correctly. This implicitly elicits the policy's pretrained world knowledge to inform decisions. We evaluate EVOKE across diverse tasks in three backbones, demonstrating improved task performance, unseen environment generalization, and data efficiency. We further conduct controlled analyses to better understand what drives these gains. These findings offer a new perspective on eliciting internalized world knowledge for transferable action through direct decision supervision.
