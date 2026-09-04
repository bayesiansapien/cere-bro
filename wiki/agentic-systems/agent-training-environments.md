# Agent Training Environments

**Concept page, created 2026-09-04.** An **environment** for agent training is an executable workspace that can be re-queried into many verifiable tasks and that returns real execution feedback. It is structurally different from a **trajectory**, which is a single frozen demonstration that can be imitated once and never probed again.

This page exists because three papers in eleven days placed agent capability in the environment corpus rather than in the parameter count, which crosses this wiki's three-paper threshold for declaring a pattern. The distinction between environment and trajectory had been implicit in the harness and self-evolution literature; [Terminal-Universe (09-04)](2026-09-04-terminal-universe-trajectories-to-environments.md) states it in one sentence and it deserves its own page.

## Why the distinction is load-bearing

A trajectory supports imitation. An environment supports **reinforcement learning, verification, and re-querying**, which means one environment yields an unbounded number of tasks while one trajectory yields exactly one. The field has an enormous surplus of trajectories, because every deployed coding agent logs them by the millions, and a shortage of environments, because building one has historically meant a human-designed pipeline converting a repository or a webpage into an executable task with a verifier.

That asymmetry sets up two independent scarcity problems, and the 09-04 pair addresses one each:

| Problem | Symptom | Paper |
|---|---|---|
| **Supply** | Environments are scarce because construction is expensive | [Terminal-Universe (09-04)](2026-09-04-terminal-universe-trajectories-to-environments.md) |
| **Difficulty** | The environments you have are too easy, so RL gets no gradient and the build cost is wasted | [Environment Evolution (09-04)](2026-09-04-environment-evolution-terminal-agents.md) |

**These compose and nobody has composed them.** Terminal-Universe's output is exactly Environment Evolution's input: recover 37.3k workspaces, then evolve them generation by generation so they stay at the learnable frontier as the model improves. That is the clearest unclaimed experiment on this page.

## The three results

**[Apodex 1.1 (08-25)](2026-08-25-apodex-1-1-environment-coordination-scaling.md)** named the axis. Its claim is that **working capability** (sustained verifiable progress toward a real objective) is developed along two axes that are explicitly *not* parameter scale: **Environment Scaling**, expanding the diversity and verifiability of executable file, search and code environments, and **Agentic Coordination Scaling**. A **35B** model plus a locally deployable 35B Mini reaches the leading performance band on finance, research, math, coding and search. What it did not publish is a reproducible way to obtain the environments.

**[Terminal-Universe (09-04)](2026-09-04-terminal-universe-trajectories-to-environments.md)** supplies one, from an input every lab running a coding agent already has in volume. The insight is that **a trajectory is an incomplete but authentic recording of its own environment**: the tool-execution history leaks which files existed, what they contained before each edit, what the dependency graph was, and what the test harness expected. Replaying the recorded file operations in reverse restores each touched file to its pre-modification state, yielding a partial workspace; a completion agent then supplies the missing files and dependencies. On the recovered workspace it reconstructs the original intent task and synthesizes new ones, scaled along **breadth** (cross-workspace queries mined from directional dependency relations between related environments, which reproduces the change-library-A-break-consumer-B pattern that single-repository benchmarks structurally cannot test) and **depth** (a user agent turns a single-turn query into a multi-round session with iterative feedback). Output: **37.3k task-sufficient environments**. SFT on Qwen3.5-27B: **+11.9 points on Terminal-Bench 2.1, +13.8 on EvoCode-Bench v2 MT@4**.

**[Environment Evolution (09-04)](2026-09-04-environment-evolution-terminal-agents.md)** (Hunyuan Team, Tencent) attacks difficulty, and its critique of the existing fix is the most general idea on this page. **Agent-environment co-evolution** mines on-policy rollout failures to synthesize harder environments near the model's learnable frontier. That breaks on its own success: **a curriculum sampling from the model's current error distribution has a supply problem built in, because the better the model gets the fewer errors there are to mine, and the ones remaining are increasingly idiosyncratic.** So the curriculum's information rate falls exactly along the trajectory where it should rise, and the environments it produces encode *this* policy's weaknesses, which is why co-evolved curricula transfer poorly. The alternative raises difficulty **off-policy**, deriving three difficulty-increasing directions from the multi-turn learning objective itself and scheduling evolved generations across training, so generation 5 can be pre-built before the model finishes generation 2. Difficulty is validated by measuring rollout success across **three architecturally unrelated frontier agents** (Hy4 preview, Claude Opus 5, GPT-5.6 Sol) and rises monotonically for all of them. **Long-horizon RL: +14.4 points on Qwen3.6-27B, +18.0 on Qwen3.6-35B-A3B.**

## What the pattern claims

**For terminal agents in the 27B-35B scale band, the environment corpus is now the leading capability variable in the published record, and it is the cheapest one to improve.** Three papers, three groups, eleven days, gains of 11.9, 13.8, 14.4 and 18.0 points, all without touching parameter count. That is a stronger and more actionable statement than the harness literature's equivalent, because an environment is a training-time asset consumed once, while a harness is an inference-time artifact paid for on every step.

**A difficulty axis validated across unrelated frontier models is a more durable object than a policy-calibrated one.** This is the most reusable single contribution across the three papers and it is independent of any RL result: it gives the field a way to say an environment is hard without reference to which agent is being trained.

## Connections to adjacent pages

**On [self-evolving-agents.md](self-evolving-agents.md), Environment Evolution's starvation argument is a third explanation for that page's oldest open result.** Evo-Bench's early saturation, where autonomous harness evolution plateaus after a few cycles, has had two prior candidate causes: single-trajectory variance ([Mendel Gödel Machine (08-12)](2026-08-12-mendel-godel-machine.md)) and the availability of self-editing evidence ([AutoWorldModel-Bench (08-13)](2026-08-13-autoworldmodel-bench.md), where agents improved an external artifact in 63 of 64 sessions). **If a loop conditioned on its own observed failures starves by construction, the plateau is the curriculum rather than the operator or the ability, and the predicted fix is to derive harness-edit directions from the objective rather than from observed failures.**

**Against [self-evolving-agents.md](self-evolving-agents.md)'s skill-library cluster, this page describes the cheaper amortization of the same source material.** That cluster runs trajectory → skill, distilling what worked into a reusable prose artifact injected at inference; [Repo-to-Skill DISCO (09-03)](2026-09-03-repo-to-skill-disco.md) does it from repositories. Terminal-Universe runs trajectory → environment. On [SkillZip (08-12)](2026-08-12-skillzip-skill-compression.md)'s accounting, where the recurring half of the bill is the injected artifact, **converting a trajectory into an environment is strictly cheaper than converting it into a skill, because the environment is consumed during training and then free.**

**On [Task-CoEvolve (08-25)](2026-08-25-task-coevolve-adaptive-validation-selection.md), the pairing suggests a missing method.** Task-CoEvolve keeps a *validation* pool at the frontier by variance-weighted **selection**, concentrating evaluation where candidate harnesses disagree and matching full-set search quality at 80% fewer evaluations. Environment Evolution keeps a *training* pool at the frontier by objective-derived **generation**. Both answer "keep the tasks informative." **The unwritten method is variance-weighted scheduling over evolved generations, so training samples the generation where the current policy is most uncertain.**

**On [agent-benchmarks.md](agent-benchmarks.md), this page carries a leakage risk that page should hold against it.** Terminal-Universe mines environments from public trajectories produced by agents driven by benchmark-style prompts, then evaluates on Terminal-Bench 2.1. **The training and evaluation distributions share an ancestor and no held-out-provenance split is reported.** [RealSWE (09-04)](2026-09-04-realswe-realistic-user-requests.md) makes this sharper by measuring that benchmark-style prompts are **7% of the real distribution** (problem-statement-only requests are 88% of real prompts and 7% of benchmarks). A corpus mined from benchmark-driven trajectories inherits the benchmark's prompt distribution.

## Open questions

- **Authentic-versus-synthesized ratio.** How much of a recovered workspace comes from replaying real file operations and how much from the completion agent's guesses? This is the number that decides whether trajectory mining is "environments for free" or "from-scratch synthesis with a better prior," and it is unreported.
- **What makes an environment "task-sufficient."** 37.3k is a headline whose whole quality story lives in the admission filter. No complexity distribution, no verifier-reliability measurement, no estimate of how many carry a task current models actually fail.
- **Off-policy versus on-policy curricula under matched compute, measured late.** The decisive experiment is both curricula, same seed environments, same budget, evaluated when co-evolution's failure supply should be thinnest. Not run.
- **Does an off-policy curriculum transfer across policy families?** Environment Evolution validates *difficulty* across three unrelated agents and trains on one model family, so the central claim against co-evolution is demonstrated for difficulty and assumed for learning.
- **Build cost.** Both 09-04 papers omit the cost of their own mechanism, and Environment Evolution's omission is the more pointed one because the motivating complaint is wasted build cost. A method justified on that ground owes a build-cost number.
- **Beyond the terminal.** Whether the three difficulty directions and the trajectory-inversion trick generalize to browser, GUI and tool-calling environments depends entirely on how tightly they are tied to the terminal's file-operation structure.

## Related pages

- [self-evolving-agents.md](self-evolving-agents.md) · [agent-harness-engineering.md](agent-harness-engineering.md) · [agent-benchmarks.md](agent-benchmarks.md)
- [Terminal-Universe (09-04)](2026-09-04-terminal-universe-trajectories-to-environments.md) · [Environment Evolution (09-04)](2026-09-04-environment-evolution-terminal-agents.md)
- [Apodex 1.1 (08-25)](2026-08-25-apodex-1-1-environment-coordination-scaling.md) · [Task-CoEvolve (08-25)](2026-08-25-task-coevolve-adaptive-validation-selection.md)
- [BCIT (09-04)](2026-09-04-bcit-conditional-experience-transfer.md) — the other side of wasted post-training compute
