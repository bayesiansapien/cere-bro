---
title: "RL signal shorts: NOPO, SPLICE, counterfactual SQL rewards, and when a critic pays (PPO vs GRPO)"
date: 2026-11-27
source: https://arxiv.org/abs/2611.17287
source2: https://arxiv.org/abs/2611.34777
source3: https://arxiv.org/abs/2611.34363
source4: https://arxiv.org/abs/2611.32013
raw: ../../raw/huggingface/2026-11-26-negative-only-policy-optimization-for-one-sided-verifiable-r.md
tags: [rlvr, grpo, ppo, reward-hacking, credit-assignment, agent-rl]
signal: HuggingFace 11-26 (three papers) + X feed (Scale AI/CMU critic study)
---

# RL signal shorts, 2026-11-27

**TL;DR.** Four papers on the same question: what do you do when the reward signal is missing, one-sided or hackable? NOPO trains only on trusted failures. SPLICE builds local targets when every rollout in a group fails. Counterfactual databases stop text-to-SQL reward hacks. And a 1,200-run study says PPO's critic wins at small batches while GRPO catches up at large ones.

## NOPO: Negative-Only Policy Optimization (2611.17287)

Many checks can only falsify: a unit test can prove a solution wrong, but passing does not prove it right. The paper calls this one-sided verifiability. Reinforcing "verified positives" then rewards shortcuts that pass partial checks. NOPO treats positives as unlabeled and only suppresses trusted negatives, with a reference-relative loss and a group adapter scaled by the share of non-falsified answers. Improves pass@k on code, logic and math with unit-test, constraint and self-verifiers when no oracle exists.

## SPLICE (2611.34777)

On long-horizon agent tasks, GRPO (group relative policy optimization, which scores each rollout against its group) often gets all-fail groups and no gradient. Supplying full solutions from a stronger model is expensive and off-policy. SPLICE picks a splice point inside a failed current-policy trajectory, generates a few bounded options from there, values them with current-policy continuations, and fits the policy on the positive ones. +2.8 to +9.8 points over GRPO on SWE-bench Verified and BrowseComp-Plus across two policy families.

## Single-Database Rewards Are Hackable (2611.34363)

Text-to-SQL RL pays a query if its result matches on one database. A wrong query can match by luck. Running the final query on a few hidden, code-generated database copies and paying only if all match cut reward hacks paid in full from 54.1% to 1.9% and buggy queries paid in full from 29.5% to 16.8%, rejecting 0 of 2,847 correct queries. But a GRPO run on a 3.35B model did not improve in-domain accuracy, because the rewards disagreed on only 5-7% of rollouts, and one seed reversed both signs. Single-seed reward comparisons mislead.

## To Critic Or Not To Critic (Scale AI + CMU, 2611.32013)

More than 1,200 runs (96 with LLMs) on control, short-horizon math and multi-turn terminal agents. PPO with a critic leads at small batch sizes; GRPO overtakes heavily bootstrapped PPO and ties lightly bootstrapped PPO at large batches. On terminal agents PPO led by up to 5.9 points at batch 128 and 512, all within 0.6 points at 2,048. PPO at batch 128 matched GRPO at 512 for 91 vs 342 GPU-hours. Longer horizons need bigger GRPO batches to catch up. Critics pay off at small budgets, with diminishing returns at large ones.

## How these relate to prior wiki pages

- **Resolves an open thread.** The 11-12 digest noted a Scale AI critic result circulating on X and said learned critics had not been tested on long-horizon agents. This is that paper: critics help where credit assignment is hardest and batches are small, which is exactly the agent-RL regime.
- **Pattern with RLVB (11-26, NTU's verifiable-beliefs fix for "lazy agents" that answer against their own written belief):** reward design is moving from "is the final answer right" to "what can the verifier actually certify". NOPO and counterfactual SQL are both explicit about verifier asymmetry.
- **SPLICE and CARE-OPD** ([11-27 distillation page](../inference-efficiency/2026-11-27-together-lao-distillation-and-care-opd.md)) both rescue long-horizon training by building targets inside the learner's own trajectories rather than importing full teacher solutions.

Related: [rl-for-llms](rl-for-llms.md)
