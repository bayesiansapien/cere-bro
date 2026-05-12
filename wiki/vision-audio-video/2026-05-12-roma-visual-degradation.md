# ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation

**Date:** 2026-05-12
**Source:** HuggingFace Daily Papers
**arXiv:** [2605.09262](https://arxiv.org/abs/2605.09262)
**Tier:** 2 — Multimodal RL / robustness / vision-language

## TL;DR

RL-fine-tuned MLLMs achieve strong reasoning but stay brittle against real-world visual corruptions (blur, compression artifacts, low-resolution scans). Naively injecting degraded views during rollout causes **reward poisoning**: perceptual occlusions trigger hallucinated trajectories that destabilize optimization. ROMA modifies RL fine-tuning dynamics with four ingredients: a dual-forward-pass strategy that evaluates corrupted views against clean-image trajectories via teacher forcing; a token-level surrogate KL penalty against the worst-case augmentation; an auxiliary policy-gradient loss anchored to clean-image advantages to prevent collapse under regularization; and correctness-conditioned regularization that restricts enforcement to successful trajectories. On Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, +2.4% on seen and +2.3% on unseen corruptions over GRPO.

## Why it matters

Robustness work has historically relied on static data augmentation or value-based regularization. Neither composes cleanly with critic-free RL fine-tuning of autoregressive MLLMs. ROMA is the first robustness paper in the wiki to surface a specific failure mode (reward poisoning) and design the optimization to avoid it. The dual-forward-pass trick is the key engineering move: it lets the policy receive degradation signal without taking real rollouts on degraded inputs, which is where the poisoning enters.

## How it relates to prior wiki state

- **DeltaRubric and ARR (today).** All three papers modify multimodal RL fine-tuning, attacking different failure modes. DeltaRubric attacks lazy judging in the reward model. ARR attacks scalar-collapse in preference labels. ROMA attacks input-distribution brittleness. The same week now contains three independent fixes for distinct RLHF-on-MLLMs failure modes, which is the strongest signal yet that multimodal RL fine-tuning is becoming an engineering discipline rather than a research curiosity.
- **AVR (2026-04-20, Adaptive Visual Reasoning).** AVR added test-time compute on hard visual inputs. ROMA adds training-time robustness against perturbed visual inputs. Adjacent fixes, same underlying observation: vision is the brittle modality in multimodal reasoning.
- **LongAct / Saliency-guided sparse RL (2026-04-18).** Both papers add structure to RL update dynamics: LongAct concentrates updates on saliency peaks, ROMA conditions regularization on rollout correctness. Two flavors of "do not update uniformly, condition on what matters."

## Research angle

The +2.4% gain is modest but the methodological contribution is the failure-mode diagnosis. The diagnosis predicts a generalization: any RL-fine-tuned MLLM whose rollouts include perceptually-difficult inputs will have a reward-poisoning surface, and the dual-forward-pass mitigation should transfer. The follow-up to track: does the same mitigation work when the "corruption" is not perceptual noise but adversarial perturbation? Adversarial robustness is the harder regime, and the dual-forward-pass machinery is structurally suited to it.

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2605.09262)
- [HuggingFace page](https://huggingface.co/papers/2605.09262)
- Raw source: [raw/huggingface/2026-05-12-reinforcing-multimodal-reasoning-against-visual-degradation.md](../../raw/huggingface/2026-05-12-reinforcing-multimodal-reasoning-against-visual-degradation.md)

## Related wiki pages

- [DeltaRubric](2026-05-12-delta-rubric.md)
- [Auto-Rubric as Reward](2026-05-12-auto-rubric-as-reward-arr.md)
- [AVR: Adaptive Visual Reasoning](../inference-efficiency/2026-04-20-avr-adaptive-visual-reasoning.md)
- [LongAct: saliency-guided sparse RL](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md)
