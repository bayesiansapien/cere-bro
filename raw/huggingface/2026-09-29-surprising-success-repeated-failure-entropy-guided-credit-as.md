---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.929609+00:00
arxiv_id: 2609.33781
url: https://huggingface.co/papers/2609.33781
arxiv_url: https://arxiv.org/abs/2609.33781
date: 2026-09-29
---

# Surprising Success, Repeated Failure: Entropy-Guided Credit Assignment for Exploration in LLM Reasoning

Reinforcement learning with verifiable rewards (RLVR) enhances reasoning in large language models (LLMs) through outcome-level feedback, yet recent approaches to finer-grained credit assignment often require auxiliary models, additional sampling, or privileged information. Although policy entropy provides a readily available signal, prioritizing uncertain positions under both reinforcement and penalization concentrates penalties where failed responses still retain alternatives for recovery, which can suppress opportunities for exploration. To address this, we introduce Entropic Advantage Policy Optimization (EAPO), an entropy-guided credit assignment method that treats success and failure asymmetrically. Specifically, motivated by the observation that success under uncertainty is less repeatable while confident failures tend to recur, EAPO couples normalized policy entropy with the sign of the response advantage to reinforce surprising success and correct repeated failure. It assigns stronger reinforcement to high-entropy decisions in successful responses and stronger penalties to low-entropy decisions in failed responses, while attenuating penalties at uncertain positions to preserve opportunities for recovery. By redistributing the response advantage across tokens, EAPO derives token-level credit directly from existing rollout signals without additional supervision. We validate EAPO on a range of reasoning tasks across both base and reasoning backbones, demonstrating that it achieves the best overall performance. We further show that EAPO promotes more effective exploration, broadening problem coverage and generating more diverse candidate answers.
