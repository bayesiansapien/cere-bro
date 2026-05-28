# LearnWeak: Automated Domain Specialization for Small Computer-Use Agents

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.28775](https://arxiv.org/abs/2605.28775) · [HuggingFace](https://huggingface.co/papers/2605.28775) · [raw](../../raw/huggingface/2026-05-28-learn-from-weaknesses-automated-domain-specialization-for-sm.md)

## TL;DR

Deploying a separate large computer-use agent per software domain is expensive, but small open agents are weaker with uneven failures. Synthesizing more training data for the target domain barely helps. LearnWeak uses a stronger reference agent to specifically identify the student's weaknesses in the domain, synthesize targeted tasks to address them, and build supervision automatically. It adds an error-aware specialization objective that disentangles planning errors from execution errors so updates can be precisely targeted. On OSWorld, LearnWeak gains average +11.6pp over EvoCUA-8B and +11.1pp over OpenCUA-7B across eight domains.

```
Naive specialization:    synthesize lots of domain data → ~ no improvement
                         (the data isn't focused on student weaknesses)

LearnWeak:
  reference agent ──► identify student's failure modes ──► synthesize targeted tasks
                                                                     │
  student ◄────── error-aware loss (planning vs execution disentangled) ◄──┘
```

## Key findings

- Naive scale-up of domain-specific training data yields only marginal improvements; targeting matters.
- LearnWeak: reference agent identifies the student's specific weaknesses, synthesizes weakness-targeted training tasks.
- The error-aware objective splits planning errors from execution errors so updates only affect the failing component.
- OSWorld: +11.6pp over EvoCUA-8B and +11.1pp over OpenCUA-7B average across eight domains.

## How this fits prior wiki state

The "student-aware data generation" frame is the same shape as the SkillOpt selection-gate (failed-edit buffer becomes negative feedback so the optimizer avoids past mistakes). Both papers operationalize the same intuition: random new attempts are wasteful; targeted attempts at the student's specific failure modes are not. AXPO (today) makes the same argument at the rollout level (resample only the all-wrong tool-call subgroups).

A pattern is forming this week: post-training methods that work by selectively focusing on the student's failure space are beating methods that uniformly expand training distribution. LearnWeak, AXPO, ESR, PEAM (failure-correction pairs), and SkillOpt are all examples.

## Related pages

- [[2026-05-28-axpo-explorative-policy-optimization]] — resample all-wrong rollouts
- [[2026-05-28-peam-parametric-embodied-memory]] — failure-correction pairs as training signal
- [[2026-05-25-skillopt-executive-optimizer-agent-skills]] — rejected-edit buffer
- [[gui-agents]] — concept page

## Research angle

The planning-vs-execution disentangling is the structural piece that should travel beyond computer-use. If you can attribute an agent's failure to one component, you can target the corresponding update without touching the working components — exactly the trick that PEAM's physically-isolated LoRA adapters use. A clean unification of LearnWeak and PEAM would put failure-attribution and weight-isolated updates together, giving a continual-learning recipe with both targeted data and targeted parameters.
