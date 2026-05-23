# DelTA: Discriminative Token Credit Assignment for RLVR

**Source:** HuggingFace daily papers, 2026-05-23.
**arxiv:** [2605.21467](https://arxiv.org/abs/2605.21467)

## TL;DR

RLVR (reinforcement learning from verifiable rewards) treats a response-level reward as the only signal, and the policy gradient implicitly assigns credit to tokens via advantage-weighted averaging of token-gradient vectors. DelTA shows this implicit credit assignment is dominated by high-frequency formatting tokens, which dilutes the sparse, discriminative directions that actually distinguish good rollouts from bad ones. The fix is to view the policy-gradient update as a linear discriminator over token gradients, then reweight tokens to amplify side-specific (positive-only or negative-only) directions and downweight shared ones. On seven math benchmarks, DelTA beats the strongest same-scale baselines by +3.26 (Qwen3-8B-Base) and +2.62 (Qwen3-14B-Base) average points. The effect generalizes to code and out-of-domain evaluations.

## What this paper actually claims

The core observation is conceptual, not algorithmic. RLVR has been treated as "GRPO with a verifier reward" for the past year, and improvements have focused on stability tricks (KL regularization, clipping, normalization). DelTA points out that the *direction* of the policy gradient update is geometrically a linear discriminator between positive-side and negative-side token-gradient centroids. When the centroids are dominated by formatting tokens that appear in both positive and negative responses (whitespace, "the", chain-of-thought scaffolding), the discriminator points in a near-useless direction.

The fix is a token-coefficient reweighting that maximizes side-specificity. Tokens that gradient-flow only in positive rollouts get amplified. Tokens that appear in both directions get downweighted. The resulting effective centroid is more contrastive, and the policy update direction is sharper.

## Connections to prior wiki state

This is the second paper this week, after the [Kurate cs.LG #11 "LLMs Gaming Verifiers"](../) (the paper showing RLVR can lead to reward hacking when the verifier is gameable), to attack the silent failure modes of RLVR. The two papers attack different layers: Gaming Verifiers attacks the reward signal, DelTA attacks the credit-assignment step that converts the reward into per-token learning signal.

It also lines up with [TIP from 04-16 (Token Importance on-policy distillation, the paper that showed standard distillation trains on every teacher token but only 10% carry signal)](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md): both papers are about token-level filtering of learning signal, but DelTA does it inside RLVR rather than inside distillation. The same insight ("most tokens carry no signal, training all of them is wasteful") now applies on both the SFT-distillation side and the RLVR side. That is a real pattern.

[From Reasoning Chains to Verifiable Subproblems / SCRL (also HF 2026-05-23, 2605.22074)](2026-05-23-scrl-subproblem-curriculum-rlvr.md) attacks the same problem at the trajectory level: rather than reweight tokens within a rollout, SCRL gives partial credit for subproblem progress. DelTA and SCRL are complementary attack vectors on RLVR's credit-assignment problem.

## Gaps

Tested only on math (seven benchmarks) with code as a sanity check. Whether the discriminator-view reweighting helps for harder-to-verify domains (creative writing, multi-turn dialogue, long-horizon agents) is unproven. The mechanism analysis would be much stronger with an ablation that quantifies how much of the gain comes from downweighting specific formatting tokens versus upweighting genuinely discriminative reasoning tokens.

## Research angle

The cleanest open question: does this generalize when the reward signal itself is noisy (semi-verifiable rewards, model-based PRMs)? DelTA assumes the response-level reward is correct. If the reward has bias, the discriminator is wrong and amplifying it makes things worse. Combining DelTA with the unsupervised process reward model from [today's uPRM paper](../llms-foundation-models/2026-05-23-unsupervised-process-reward-models.md) is the obvious next experiment.

## Raw source

[raw/huggingface/2026-05-23-delta-discriminative-token-credit-assignment-for-reinforceme.md](../../raw/huggingface/2026-05-23-delta-discriminative-token-credit-assignment-for-reinforceme.md)
