# Unsupervised Process Reward Models (uPRM)

**Source:** HuggingFace daily papers, 2026-05-23.
**arxiv:** [2605.10158](https://arxiv.org/abs/2605.10158)

## TL;DR

Process Reward Models (PRMs) provide fine-grained step-level supervision but require expert annotations for every reasoning step, making them expensive and hard to scale. uPRM trains a process reward model without human supervision: no step annotations and no ground-truth final-answer verification. The trick is a scoring function derived from the LLM's next-token probabilities that jointly assesses where in each of a batch of reasoning trajectories the first erroneous step occurs. uPRM beats LLM-as-a-Judge by up to 15% absolute on ProcessBench. As a verifier for test-time scaling, it performs comparably to supervised PRMs and beats majority voting by up to 6.9%. As a reward signal for RL, it enables more robust policy optimization than a supervised PRM trained on ground-truth labels.

## Why this matters

The entire RLVR / PRM pipeline has been bottlenecked by annotation cost. OpenAI's PRM800K (the step-level math reasoning dataset behind o1-style training) cost millions to collect. uPRM proposes that you don't need it: the LLM's own next-token distribution contains enough signal to localize the first erroneous step, if you score across a batch of trajectories jointly rather than per-trajectory.

The "outperforms supervised PRM as a reward signal" claim is the surprise. Even when ground-truth labels are available, training an unsupervised reward model performs better in practice. This suggests the supervised PRM is overfitting to the annotation distribution and not generalizing as well as the unsupervised version that has to rely on the model's intrinsic uncertainty signal.

## Connections to prior wiki state

This is the second paper this week to argue that LLM uncertainty signals beat explicit supervised judging. The first was [DelTA (today's paper, 2605.21467)](2026-05-23-delta-discriminative-token-credit-rlvr.md), which uses token-gradient geometry (an implicit per-token signal) to reshape RLVR updates. Both papers reframe the credit-assignment problem as recovery of signal that is already latent in the model, rather than acquisition of signal from external annotation.

A pattern is forming around RLVR's silent failure modes. [Kurate cs.LG #11 (LLMs Gaming Verifiers, the paper showing RLVR leads to reward hacking when the verifier is gameable)](../) is the third paper. The three together suggest the next wave of RLVR research is moving away from "scale the reward model" toward "extract better signal from the model itself": model-based PRM, gradient-based credit, intrinsic uncertainty.

## Gaps

ProcessBench is a math-heavy benchmark. Whether uPRM scales to broader reasoning domains (code, multi-step retrieval, scientific reasoning) is unproven. The batch-joint scoring trick depends on having multiple trajectories per problem, which is fine at test time but might be expensive during RL rollouts.

The "outperforms supervised PRM" comparison is at the level of policy optimization robustness, not at the level of step-localization accuracy. Untangling whether the supervised PRM is genuinely worse or just less robust under distribution shift would clarify the result.

## Research angle

The strongest open question: does uPRM compose with DelTA? DelTA reshapes RLVR token-credit using gradient geometry. uPRM provides a process-level reward that replaces the response-level reward. A pipeline that uses uPRM for process-level signal and DelTA for token-level signal would be the first fully-model-intrinsic RLVR system, no external annotation anywhere in the loop.

A deeper question: if the LLM's own next-token distribution can localize errors better than a trained supervised judge, what other tasks currently done by trained scorers (RLAIF preference judging, response ranking, hallucination detection) could be replaced by intrinsic-signal scoring? uPRM hints that the answer might be most of them.

## Raw source

[raw/huggingface/2026-05-23-unsupervised-process-reward-models.md](../../raw/huggingface/2026-05-23-unsupervised-process-reward-models.md)
