---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.908653+00:00
arxiv_id: 2611.17287
url: https://huggingface.co/papers/2611.17287
arxiv_url: https://arxiv.org/abs/2611.17287
date: 2026-11-26
---

# Negative-Only Policy Optimization for One-Sided Verifiable Rewards

Reinforcement learning with verifiable rewards (RLVR) typically relies on a verifier that can reliably judge whether sampled solutions are correct. However, in many realistic settings, complete verification is generally unavailable, while cheap checks can only falsify failures. We formalize this regime as one-sided verifiability (OSV): verified negatives are reliable counterexamples, but verified positives are merely non-falsified candidates and may contain many false positives. This asymmetry makes standard RLVR unreliable, because reinforcing verified positives can directly reward shortcuts that pass partial checks. To address this issue, we propose Negative-Only Policy Optimization (NOPO), which treats verified positives as unlabeled and updates the policy only by suppressing trusted verified negatives. Specifically, NOPO combines a reference-relative negative suppression loss with a group-level adapter that scales each update by the proportion of non-falsified responses. Across unit-test, constraint-check, and LLM self-verifiers, NOPO improves pass@k over baselines on code, logic, and math benchmarks when oracle rewards are unavailable. These gains persist under inference-time scaling and cross-benchmark transfer.
