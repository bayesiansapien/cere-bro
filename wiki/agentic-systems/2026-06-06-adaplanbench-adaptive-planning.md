# AdaPlanBench: Evaluating Adaptive Planning under World and User Constraints

**TL;DR.** Real planning problems do not hand you all the constraints up front; they leak out as you go ("actually it can't go in the dishwasher", "I need this before 6pm"). AdaPlanBench is a dynamic, interactive benchmark that reveals world and user constraints **only when the agent proposes a plan that violates them**, forcing iterative re-planning under accumulating feedback. Built on 307 household tasks. The best of ten leading LLMs reaches only **67.75%**, performance degrades as constraints pile up, and *user* constraints are harder than *world* constraints, with failures tracing to weak physical grounding.

**Source:** HuggingFace Daily Papers · arxiv [2606.05622](https://arxiv.org/abs/2606.05622)

## What it is

A testbed for *adaptive* planning: agents interact with an environment over multiple turns, propose plans, and discover hidden constraints reactively when a plan trips one. They must infer and track the accumulating constraint set while re-planning effectively. A scalable construction pipeline augments each of 307 household tasks with dual (world + user) constraints.

## Key results

- Best model: **67.75%** accuracy; the task is hard for every frontier model tested.
- Performance **degrades as more constraints accumulate**, the realistic long-horizon regime.
- **User constraints** pose a larger challenge than world constraints; failures often stem from weaker physical grounding and reduced re-planning effectiveness.

## How it relates to prior wiki knowledge

AdaPlanBench extends the wiki's benchmark-skepticism / trajectory-grounded-evaluation thread (see [agent-benchmarks.md](agent-benchmarks.md)): like GTA-2 (04-20, top models 14.39% on open-ended workflows) and AgentLens (05-14, pass rate overstates real competence), it shows agents look much weaker once the evaluation grades the *adaptive process* rather than a single static plan. It is the planning-side analogue of today's [SABER](../responsible-ai/2026-06-06-saber-operational-safety-coding-agents.md) (grade the final environment state, not the turn): both move the unit of evaluation from response to interaction-with-consequences.

## Gaps

Household tasks are a narrow, simulated slice; whether the progressive-disclosure protocol predicts performance on real interactive workflows (software, ops) is untested. The constraint-construction pipeline is automated, so constraint realism and difficulty calibration depend on its quality, which the abstract does not characterize.

## Related pages

- [agent-benchmarks.md](agent-benchmarks.md)
- [../responsible-ai/2026-06-06-saber-operational-safety-coding-agents.md](../responsible-ai/2026-06-06-saber-operational-safety-coding-agents.md)

Raw source: `raw/huggingface/2026-06-06-adaplanbench-evaluating-adaptive-planning-in-large-language.md`
