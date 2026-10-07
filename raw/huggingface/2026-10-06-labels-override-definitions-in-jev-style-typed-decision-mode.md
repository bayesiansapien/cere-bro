---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.02586
url: https://huggingface.co/papers/2610.02586
arxiv_url: https://arxiv.org/abs/2610.02586
date: 2026-10-06
---

# Labels Override Definitions in Jev-Style Typed Decision Models

A typed decision model answers a fixed question about an input by returning a probability for each of several caller-defined options. Each option carries a short label and a written definition, which is where a developer states the rule the model should apply. Jev introduced this interface for routing, moderation and triage, open implementations followed, and the same operation occurs whenever a language model is used as a classifier by scoring label strings. We study the open implementations, whose weights we can inspect and patch, and ask whether the probability follows the definitions or the labels. A preference for the label we call option-label bias. Across four open-weight typed decision models, three ways of reading an answer from a Qwen2.5 backbone, eleven classification tasks and PolicyBench, a synthetic routing suite we introduce in which the rule appears only in the definitions, the answer is mostly the labels. Deleting every definition leaves accuracy unchanged (laya-td: 0.8559 against 0.8487), although those definitions support 0.7971 on their own, and renaming the options to A and B raises accuracy by +0.1511 [+0.1377, +0.1646]. One system, von, is unaffected, and the two code bases differ in one expression: laya writes each option as "{label}: {definition}", while von writes only the definition. Changing that expression in both directions, with no weight changed, makes all three laya checkpoints exactly invariant (+0.0000 [+0.0000, +0.0000]) and creates the effect in von, whose accuracy falls from 0.8511 to 0.2281 when a label contradicts its definition. Earlier work attributed this failure to the constrained decision head these models use in place of a text decoder; our results locate it in the prompt rendering. We give a two-call test that tells a practitioner which case applies to their model, and measure what four mitigations are worth.
