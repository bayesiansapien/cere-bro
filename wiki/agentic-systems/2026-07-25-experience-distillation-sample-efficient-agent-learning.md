# Experience Distillation: Bake an Agent's Trial-and-Error Into Its Weights Without Touching the Environment Again

**TL;DR.** Agents learn fast from in-context learning (ICL, putting past interaction transcripts in the prompt) and slowly from reinforcement learning. But ICL's gains vanish the moment you drop the transcript from the context, and RL needs enormous numbers of environment interactions, which is fatal when each interaction is a slow test suite, a real experiment, or a human. This paper (Monash + ByteDance Seed) names the missing step **Experience Distillation**: collect experience once, let ICL exploit it, then internalize the ICL-improved behavior into the weights with **zero further environment interaction**. On 749 curated software-engineering tasks and six text-adventure games it retains at least **64.8%** of the ICL gain, where plain supervised fine-tuning on the same collected experience recovers only **3.8%**. Against classical RL baselines it matches performance with at least **9.6x fewer environment samples**.

```mermaid
flowchart LR
  ENV[(Expensive environment<br/>tests, experiments, humans)] -->|collected ONCE| EXP[Trial-and-error<br/>experience]
  EXP --> ICL[In-context learning:<br/>teacher sees experience<br/>in its prompt]
  ICL --> BEH[Improved behavior]
  BEH --> ED[Experience Distillation:<br/>student without the context<br/>learns to reproduce it]
  ED --> W[(Weights carry<br/>the experience)]
  W --> DEP[Deploy: no transcript,<br/>gains persist]
  SFT[Plain SFT on<br/>the same transcripts] -.recovers only 3.8%.-> FAIL[Gains lost]
  RERUN[Re-running the<br/>teacher in the env] -.would destroy.-> ENV
  classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  classDef warn fill:#fee2e2,stroke:#ef4444,color:#7f1d1d
  classDef aux fill:#e0e7ff,stroke:#6366f1,color:#312e81
  class ENV,EXP input
  class W,DEP,BEH output
  class SFT,FAIL,RERUN warn
  class ICL,ED aux
```

## What problem this solves

Two learning mechanisms exist for agents and each has a disqualifying flaw.

**Reinforcement learning** works when interaction is cheap and scalable, which is why it succeeded at Go self-play and lightweight coding tasks. It is impractical when every rollout costs a slow experiment, a paid annotator, or a long-running test suite, because RL's sample efficiency in environment terms is terrible.

**In-context learning** is extraordinarily sample-efficient. Show the agent a handful of its own past attempts and it adapts immediately, no gradient steps and no training corpus. But nothing is written to the weights, so the improvement lasts exactly as long as the transcript stays in the prompt. In a long-running deployment that transcript grows without bound and eventually gets evicted, and the agent forgets.

**Context distillation** is the obvious bridge: train a student with no context to reproduce the behavior of a teacher that had the context. The problem is that recent attempts at combining ICL with context distillation for agents **re-run the experience-conditioned teacher inside the environment** during the distillation phase, which spends exactly the resource the whole exercise was trying to conserve.

Experience Distillation is the version where the distillation phase touches the environment zero times. The collected experience is the only environment cost, and it is paid once.

## Why plain fine-tuning fails so badly

The 64.8% versus 3.8% gap is the paper's most useful number and it deserves emphasis, because "just fine-tune on the trajectories" is what most teams would try first.

Supervised fine-tuning on collected experience trains the model to *imitate the transcripts*. But a trial-and-error transcript is mostly failure. Imitating it teaches the agent to reproduce the failures alongside the eventual success. Experience Distillation instead targets the *behavior of a model that has already read and internalized those failures*, which is a qualitatively different signal: the teacher conditioned on "here are twelve things that did not work" behaves like an agent that knows not to try them, and that behavior is what gets distilled. The transcripts are the teacher's input, not the student's target.

The authors also position this against model-based RL, which generates synthetic trajectories from a learned world model and suffers compounding error over long rollouts. Experience Distillation never rolls out anything; it works entirely off real collected experience.

## Key takeaways

- Retains ≥64.8% of the in-context-learning gain after the context is removed, across both software engineering (749 curated tasks) and six text-adventure games.
- Direct supervised fine-tuning on the same collected experience recovers only 3.8%, a ~17x difference in signal recovery from identical data.
- Matches classical RL baselines with at least 9.6x fewer environment samples.
- Zero environment interaction during distillation, which is the property that separates it from prior ICL-plus-context-distillation attempts.
- Two very different domains (code repair, text adventures) rather than one, which is meaningful evidence the mechanism is not domain-specific.

## Relation to prior wiki

**This is the missing modality on the [parametric context internalization](../inference-efficiency/parametric-context-internalization.md) axis, and that page predicted it.** The open-questions section there asked, after documenting Doc-to-LoRA (text), [Code2LoRA (06-06)](../inference-efficiency/2026-06-06-code2lora-hypernetwork-repo-adapters.md) (a repository snapshot compiled into a per-repo adapter) and [Video2LoRA (06-06)](../inference-efficiency/2026-06-06-video2lora-parametric-video-internalization.md) (a video compiled into a LoRA in one hypernetwork pass): "Audio, tabular, **tool-call histories** next?" Experience Distillation is tool-call histories. The mechanism differs (this is distillation, not a hypernetwork predicting an adapter in one pass), but the cost model is the identical flip: pay once to move context into weights, then pay zero context tokens per query forever.

**It resolves the durability problem in the [self-evolving agents](self-evolving-agents.md) thread.** [Socratic-SWE (06-08)](2026-06-08-socratic-swe-trace-derived-skills.md) reused an agent's own historical solving traces by distilling them into structured skills, and [Ctx2Skill (05-05)](2026-05-05-ctx2skill-self-evolving-skills.md) turned context into reusable skills. Both keep the learned artifact *outside* the weights, as a skill library the agent must retrieve and follow. That keeps the [Disentangling Agent Self-Evolution (06-08)](2026-06-08-disentangling-agent-self-evolution.md) problem alive: harness benefit is non-monotonic in model strength, because a weak solver cannot activate the scaffold and a strong solver does not need it. Experience Distillation sidesteps the activation question entirely by putting the experience in the parameters, where there is nothing to activate.

**It is the offline-agent-learning sibling of [ReOPD (07-24)](../inference-efficiency/2026-07-24-reopd-multiturn-onpolicy-distillation.md)**, which made multi-turn on-policy distillation offline by reusing pre-collected teacher trajectories as replay prefixes so the student never calls a tool during training. Two papers in two days, both removing the environment from the training loop for agent distillation, both by treating already-collected trajectories as a reusable asset rather than a one-shot cost. ReOPD's problem was the *teacher's* reliability on shifted prefixes; this paper's problem is the *student's* retention after the context is gone. Same economics, opposite ends of the same pipeline.

## Gaps

"At least 64.8% retained" means roughly a third of the ICL gain is still lost, and the paper does not characterize what kind of gain is the part that fails to internalize. The teacher is a model conditioned on experience, so the ceiling is whatever ICL achieves, and nothing here compounds beyond that ceiling the way an RL loop eventually can. Both evaluation domains have automatic verification (tests pass, game state advances), which is also where collecting the experience is cheapest, so the headline motivation of "expensive environments like real experiments and human feedback" is argued rather than demonstrated. And there is no result on repeating the cycle: collect, distill, collect again with the improved agent. Whether that compounds or saturates is the interesting question and it is untested.

## Industrial implication

For anyone running a coding agent in a real repository, this is the cheapest available upgrade path that does not require an RL infrastructure. Log what the agent tried, let a context-loaded teacher show what better behavior looks like on those same tasks, distill, ship. The environment cost is the logging you were already doing. The 3.8% number is the warning: teams currently fine-tuning on raw agent trajectories are recovering almost nothing from data they already paid for.

## Sources

- Paper: [arXiv 2607.21051](https://arxiv.org/abs/2607.21051) — Chenhui Gou (Monash / ByteDance Seed, corresponding), Haoqin Tu, Yunhao Fang (ByteDance Seed), Jianfei Cai, Hamid Rezatofighi (Monash)
- HuggingFace Daily Papers, 9 upvotes (2026-07-24)
- Raw: `raw/huggingface/2026-07-24-sample-efficient-learning-from-agent-experience.md`
- Related: [parametric context internalization](../inference-efficiency/parametric-context-internalization.md) · [self-evolving-agents](self-evolving-agents.md) · [ReOPD](../inference-efficiency/2026-07-24-reopd-multiturn-onpolicy-distillation.md) · [agent-memory](agent-memory.md)
