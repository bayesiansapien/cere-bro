# Revisiting DAgger in the era of LLM agents

**Source:** HuggingFace Daily Papers · 2026-05-14
**Paper:** [arXiv 2605.12913](https://arxiv.org/abs/2605.12913)
**Raw:** [raw](../../raw/huggingface/2026-05-14-revisiting-dagger-in-the-era-of-llm-agents.md)
**Tier:** 2. Long-horizon LM agents, covariate shift, on-policy training

## TL;DR

The paper applies Dataset Aggregation (DAgger) — a 2011 imitation-learning algorithm by Ross, Gordon, and Bagnell — to multi-turn LM agents. DAgger collects trajectories by interpolating student and teacher policies at the turn level, then trains the student via supervised teacher labels on those trajectories. The student therefore sees realistic deployment states, not idealized teacher trajectories, and gets dense teacher feedback rather than sparse outcome rewards. On SWE-bench Verified, this beats the strongest post-training baseline by +3.9 points at 4B and +3.6 at 8B. The 4B model reaches 27.3%, beating several published 8B SWE-agent systems.

## Why it matters

The wiki's agentic-systems thread has been tracking the trilemma between SFT (dense supervision but covariate-shift), RLVR (on-policy but sparse outcome), and self-distillation variants. DAgger is the cleanest answer in months: keep the dense teacher supervision, but expose the student to the on-policy state distribution by interpolating. It is also the answer that requires zero new ideas, only a re-application of a 2011 imitation-learning paper to a modern setting. The interesting move is the timing. The wiki recorded the same diagnosis from a different angle on 05-12 in the [Multi-Agent Bystander Effect paper](https://arxiv.org/abs/2605.10698) ([Twitter retweet from @dair_ai](https://nitter.net/dair_ai/status/2054547408529530980#m)): agents compute the correct answer internally but suppress it under multi-agent social pressure. DAgger's mechanism cuts the same problem from the supervision side: train the student to behave correctly *in the states it will encounter*, not in the states the teacher gives it.

## Mechanism

DAgger's loop:

```
  step 1: collect trajectory by interpolating student and teacher
          actions at the turn level (β·teacher + (1−β)·student)
  step 2: at every state encountered, query teacher for label
  step 3: aggregate into the training set, train student on union
  step 4: anneal β toward 0 over rounds
```

The key property: the student trains on the state distribution it will see at deployment, not the teacher's distribution. Covariate shift is the structural failure of SFT — train on teacher rollouts, deploy on student rollouts, and the two distributions diverge because a single early student mistake derails the trajectory. DAgger removes that by mixing during data collection.

For SWE-bench Verified, the result is +3.9 points over the strongest published post-training baseline at 4B. The 27.3% number is what makes this a publishable contribution: a 4B student beats several published 8B SWE agents. The scale-efficiency story is consistent with what TIP and ListOPD already say — the right *target* matters more than the model size.

## Connections

- **TIP** ([2026-04-16](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md)) and **The Extrapolation Cliff** ([2026-05-14](../inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md)) both said the target distribution matters more than the loss. DAgger says the same thing one level up: the trajectory distribution matters more than the loss. The three papers compose into the same prescription: train on the data the deployed model will actually see, even when that costs more.
- **Bystander Effect paper** ([@dair_ai retweet, 2026-05-13](https://nitter.net/dair_ai/status/2054547408529530980#m)) found that agents compute the right answer and then conform to the swarm. DAgger fixes the supervision-side analogue: train on states the agent will actually encounter alone.
- **AutoTTS** ([2026-05-11](2026-05-11-autotts-agentic-discovery-test-time-scaling.md), retweeted by [@zhengtoong](https://nitter.net/zhengtoong/status/2054575535066350080#m)) automated test-time scaling discovery. DAgger is the training-time scaling complement: at training time, expose the student to states it will encounter. At test time, AutoTTS's controllers decide when to branch. The two papers approach the same problem (long-horizon agent quality) from opposite ends of the lifecycle.
- **AgentLens** ([2026-05-14](2026-05-14-agentlens-lucky-pass-swe-eval.md)) says 10.7% of passing SWE-bench trajectories are Lucky Passes — they got the right answer through chaotic trial-and-error. DAgger directly attacks the cause: covariate-shift trajectories that drift far from teacher behavior. The natural composition: use AgentLens to filter Lucky-vs-Solid passes, and train DAgger on Solid only.

## Research angle

1. **β-schedule learning.** DAgger requires a hyperparameter schedule (how aggressively to anneal β). For LM agents, the schedule should arguably be state-conditional, not step-conditional. A learned scheduler is the obvious follow-up.
2. **Teacher cost.** DAgger queries the teacher at every state the student reaches. For 4B/8B SWE-bench experiments, the teacher is presumably a larger model whose query cost dominates. The paper's wall-clock economics are not in the abstract; whether DAgger's gains hold under a tight teacher-query budget matters for adoption.
3. **DAgger + AgentLens process labels.** AgentLens produces process-level labels (Exploration, Implementation, Verification, Orchestration). Using those as stage-aware teacher labels in DAgger is the cleanest follow-up: dense supervision on *what kind* of action to take at each stage, not just *which* action.

## Where it lives

Update [tool-calling.md](tool-calling.md) and [multi-agent-systems.md](multi-agent-systems.md) — DAgger is the first paper in the wiki to formally solve the SFT-vs-RLVR trilemma for LM agents.
