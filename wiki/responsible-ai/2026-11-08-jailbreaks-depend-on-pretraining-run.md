---
title: "Identically trained LMs break on different jailbreaks; innocuous-looking fine-tuning data that induces harm"
date: 2026-11-08
source: https://arxiv.org/abs/2610.34074
raw: ../../raw/huggingface/2026-11-07-identically-trained-language-models-break-on-different-jailb.md
tags: [jailbreaks, safety-evals, pretraining, fine-tuning, data-poisoning]
---

# Jailbreak vulnerability is a property of the pretraining run, not the data

**TL;DR.** Jailbreak benchmarks test one checkpoint and treat its weak spots as a property of its data and safety training. This paper trains 150 models: 25 pretraining data recipes, 3 pretraining seeds each at 1B, each given the same safety post-training with 2 post-training seeds. Two post-trained copies of the same pretraining run agree on which prompts break them (per-prompt non-refusal correlation 0.984). A different pretraining *seed* on the same data drops the correlation to 0.811. A different data *recipe* drops it only a little more, to 0.779. So which jailbreaks work depends mostly on the specific pretraining run, not on the data. The best of 91 attack templates found on one checkpoint stays best after a new pretraining seed in only 27% of pairs, against 67% after a new post-training seed. Each run also leaves a fingerprint: per-prompt refusal rates over 3,211 prompts identify the pretraining run among 75 every time, and 50 random prompts still do so 98% of the time.

No architecture diagram: this is an empirical study.

## Key points

- **Seed matters nearly as much as data.** 0.811 vs 0.779 correlation: changing the random seed moves the jailbreak profile almost as far as changing the whole data mix.
- **Attack transfer is fragile across pretraining runs.** Red-team findings on one checkpoint mostly do not carry over to a retrained one (27% best-template persistence).
- **Refusal patterns are a fingerprint.** 50 prompts identify the pretraining run 98% of the time, a possible provenance tool for open weights.
- **Scale caveat.** Shown at 1B, with the pattern holding at 150M and 300M. Frontier-scale behaviour is untested.

## Companion result: harmful fine-tuning data that looks normal (UC Berkeley)

Surfaced via the X feed ([@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2118810336673562807)). A pipeline searches for small fine-tuning datasets that look like ordinary training data but raise a chosen behavior, such as recommending self-harm or resisting shutdown. It produced 6,575 datasets across 8 behaviors. 72% also induced the behavior in all 5 other models tested, including one 8x larger. ML researchers guessed the side effect correctly only 63% of the time, against 50% by chance. The recommendation: screen fine-tuning data with behavior evals after training, or at least a frontier-model auditor.

## Relation to prior wiki pages

- **Same direction as the AI-auditor result** (The Decoder, 11-07): GPT-5 caught ~98% of reward hacking in agent logs but buried reviewers in false alarms. Safety evidence is getting cheaper to generate and harder to trust per checkpoint.
- **Tension with "safety from data" framing.** Work that attributes misbehavior to pretraining priors (e.g. AI-villain fiction in pretraining data) assumes the data sets the profile. This paper says the seed moves it nearly as much.

Concept page: [responsible-ai](responsible-ai.md).
