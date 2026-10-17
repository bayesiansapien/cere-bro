---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.15368
url: https://huggingface.co/papers/2610.15368
arxiv_url: https://arxiv.org/abs/2610.15368
date: 2026-10-16
---

# ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs

Rapid advances in large language models have made software engineering agents capable of tackling complex coding tasks. Within a containerized environment, a coding agent receives tool responses or execution results, and determines its later actions by those earlier results. However, most existing coding agents never look ahead: their policies do not anticipate the consequences of actions, and the terminal reward barely attributes a failure to certain earlier steps, so an ill-judged edit can corrupt the repository state irreversibly before any signal arrives. Recent code world models aim to address these challenges, but they are either trained and then frozen before reinforcement learning (RL), or reduced to an auxiliary next-token loss on the environment's outputs. We present ANTE (Anticipate, Then Execute), an agentic RL framework that verifies the policy's pre-action predictions by real execution and turns them into per-step credit for its actions and trust-or-abstain decisions. With an internal belief stated before each action, Belief-Anchored Policy Optimization (BAPO) turns the settled predictions into per-step advantages by anchoring credit on the policy's own forecasts. To turn the trained forecasts into better actions at inference, thereby facilitating effective test-time scaling, ANTE-TTO (test-time optimization) selects among candidate actions without an external scorer. ANTE raises Qwen3-32B from 25.0% to 57.2% pass@1 on SWE-bench Verified, 6.2% above a matched GRPO baseline trained without the belief state; its world model's accuracy climbs from 44% to 69% during RL, and the learned foresight capability transfers across harnesses and out-of-distribution domains. In summary, we aim to build a code world model that knows what has happened, what holds now, and what the next action will achieve.
