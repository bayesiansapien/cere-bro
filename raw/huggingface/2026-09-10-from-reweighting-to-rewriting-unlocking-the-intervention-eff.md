---
source: farmer/huggingface
farmed: 2026-09-11T00:57:36.854415+00:00
arxiv_id: 2609.02771
url: https://huggingface.co/papers/2609.02771
arxiv_url: https://arxiv.org/abs/2609.02771
date: 2026-09-10
---

# From Reweighting to Rewriting: Unlocking the Intervention Effects of Influential Samples in Training Data Attribution

Training data attribution (TDA) aims to identify training examples that shape model behavior, but its intervention value depends on both which examples are selected and how they are modified. Influence functions (IF) estimate behavioral changes under infinitesimal reweighting, yet IF-selected examples often show limited advantages over random selection under conventional weight-based interventions. This raises the question of whether influential examples lack intervention value or whether reweighting fails to realize their behavioral leverage.We introduce influence-guided response rewriting, which uses IF to identify intervention targets and replaces their responses with behavior-aligned or behavior-opposed supervision while keeping instructions fixed. Across four open-weight LLMs, we compare rewriting and reweighting on the same influence-selected examples using epistemic abstention as our primary testbed. Response rewriting produces stronger, more persistent, and bidirectional behavioral shifts, while reweighting the same examples yields weak and inconsistent effects. Further analyses show that influence-selected examples provide greater rewriting leverage than alternative selectors, with changes remaining concentrated on target-relevant behaviors. The same qualitative contrast extends to safety refusal. These results distinguish the local reweighting effects captured by influence estimates from the broader intervention leverage of the examples they identify, motivating intervention-aware evaluation of TDA methods.
