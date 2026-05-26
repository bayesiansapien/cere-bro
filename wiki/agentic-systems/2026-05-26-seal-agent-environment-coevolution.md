# SEAL: Synergistic Co-Evolution of Agents and Learning Environments

**Source:** [arXiv:2605.24426](https://arxiv.org/abs/2605.24426), via HuggingFace Daily Papers 2026-05-26.
**Topic:** Agent self-evolution / tool-use RL / training-data evolution.

## TL;DR

Self-evolution methods for tool-use agents adapt the policy or the environment in isolation. SEAL diagnoses this as Agent-Environment Misalignment: the agent's capability frontier moves during training, but the training environment that supplies supervision stays static or only weakly coupled to the agent's actual failures. SEAL closes the loop. It collects on-policy trajectories under executable verification, diagnoses failures into turn-level labels, and uses those diagnoses simultaneously to (a) evolve the environment by exposing clearer tool affordance cues, constraint information, and recovery feedback, and (b) update the policy with diagnosis-guided advantage reweighting. With only 400 training samples it produces +8.25 to +26.25 average-point gains across three backbones, and shows positive out-of-distribution transfer.

```
                     ┌────── on-policy trajectories ──────┐
                     │                                    │
                     ▼                                    │
              ┌───────────────────────┐                   │
              │  executable verifier  │                   │
              └────────────┬──────────┘                   │
                           │                              │
                           ▼ failure diagnosis            │
                  ┌────────────────┐                      │
                  │ turn-level     │  shared signal       │
                  │ failure labels │ ─────────┐           │
                  └───────┬────────┘          │           │
                          │                   ▼           │
        ┌─────────────────┴────────┐    ┌────────────────────┐
        ▼                          ▼    │  Policy update     │
  Environment evolves         Policy reweights  │  diagnosis-weighted │
  (better affordance cues,    (advantage)       │  advantage          │
   constraint info, recovery)                   └─────────┬───────────┘
                                                          │
                                                          └─► new trajectories
```

## What it does

- On-policy rollouts under an executable environment that can verify whether tool calls succeed.
- A diagnosis step converts each failed trajectory into turn-level labels (which tool calls were wrong, which were missing, which were sequenced badly).
- Two consumers of the diagnosis signal in parallel:
  - **Environment side**: the training environment's tool descriptions, constraint surfaces, and error messages evolve to expose the information the agent was missing.
  - **Policy side**: per-turn advantage gets re-weighted using the diagnosis so the gradient concentrates on the failure-relevant turns.
- The two updates are synchronized inside one training loop. Neither side is static during the run.

The conceptual claim is that the training environment is itself a policy and should be co-trained.

## Key results

- 400 training samples, three backbones.
- +8.25 to +26.25 average-point gains across in-distribution and OOD multi-turn tool-use benchmarks.
- Positive out-of-distribution transfer (not just in-distribution improvement).

## How this relates to prior wiki pages

SEAL is the symmetric counterpart of Life-Harness (2026-05-23, the runtime harness that evolves from training trajectories and stays fixed during evaluation, with 88.5 percent average relative improvement). Life-Harness evolved the runtime artifact and froze model weights; SEAL evolves the training environment and updates the policy. Together with SkillOpt (2026-05-25, the deep-learning-style optimizer for the skill document with a held-out validation gate), three axes are now independently trainable: the harness (Life-Harness), the skill (SkillOpt), and the training environment itself (SEAL). The decomposition observed in the 2026-05-25 digest is now formalized one step further: stable model + portable harness + portable skill + co-trained environment.

The diagnosis-guided advantage reweighting is mechanistically the same lever as HINT-SD (2026-05-25, the targeted hindsight self-distillation framework that picks failure-relevant action spans and beats per-turn dense feedback by 18.80 percent at 2.26x lower training cost). HINT-SD does it for self-distillation; SEAL does it for RL advantage. Both confirm that selecting where to apply feedback dominates intensity.

## Research angle

The natural next paper composes SEAL's environment evolution with a learned curriculum: not just clearer affordance cues, but selection of which prompts the agent sees next given its current failure distribution. The current SEAL evolves the surface of each environment but not the distribution of environments. That is the obvious extension. The other research question is failure-diagnosis quality: SEAL's diagnosis step uses an LLM grader; whether a verifier-trained diagnosis head outperforms is open.

## Industrial implication

This is the cleanest justification yet for treating training-environment design as a first-class engineering artifact rather than a one-time setup. Production agent training stacks (Anthropic's tool-use RL, OpenAI's deep research training) almost certainly already do something like this internally, but SEAL provides the first public formalization. Expect the pattern to show up in open agent training recipes within a quarter.
