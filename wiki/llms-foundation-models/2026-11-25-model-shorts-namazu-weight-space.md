---
title: "Model shorts: Sakana Namazu Small, weight-space programming round two, GPT-6 science claims"
date: 2026-11-25
source: https://sakana.ai/namazu-small/#English
raw: ../../raw/labs/2026-11-25-103617-labs.md
tags: [open-models, continued-pretraining, weight-space-programming, science-agents]
signal: AI lab watcher (OpenAI, Sakana); X Following feed; HuggingFace 11-24
---

# Model shorts, 2026-11-25

## Sakana Namazu Small (30B)

Sakana AI released [Namazu Small](https://sakana.ai/namazu-small/#English), a 30B reasoning model built on NVIDIA Nemotron 3 Nano's base model with Sakana's own continued pretraining and post-training. On the average of 25 benchmarks (BrowseComp, FRAMES, LongBench v2, SimpleQA Verified and others) it beats both the same-size Nemotron 3 Nano (30B-A3B) and the roughly 4x larger Nemotron 3 Super (120B-A12B). The target use cases are long-document reading with citations and multi-step web research. On-prem availability details are promised in early December.

The interesting part for this wiki is the recipe, not the score: a lab with no pretraining run of its own takes someone else's base model and beats that vendor's own 4x-larger post-trained model on its chosen axis. That is post-training as the cheap lever, the same economics as [CSPD](../agentic-systems/2026-11-25-rlm-compositional-harnesses-and-cspd.md) (distill each expert into a soft prompt on a frozen base) at a company scale.

## Weight-space programming, round two

Weight-Space Programming (WSP) is the idea that a frozen language model can write executable code that reads and sets another network's weights directly, with no gradient training. The wiki opened a page on this field on [11-19](2026-11-19-weight-space-programming-field.md). Three new data points:

- **WeightCode** ([2611.25476](https://arxiv.org/abs/2611.25476)): installs new capabilities into trained networks from a grammar or eight demonstrations. Unseen command compositions go from 0% to 99.8%; a new action from 0% to 98.4%; on ImageNet, four weight programs add 8.84 to 17.62 points of robustness while keeping clean accuracy, beating the best of eight fine-tuning methods under matched budgets. Programs rerun on five independently trained Vision Transformers keep 83 to 110% of their original gains, while copying the fixed weight edits gives almost nothing. That last control is the paper's strongest claim: the **program** generalizes, not the diff.
- **Self-WSP** ([2611.28833](https://arxiv.org/abs/2611.28833)): Qwen3.5-0.8B reads its own weights, proposes an edit, then continues as both solver and editor. GSM8K rises from 11.8% to 62.2% and MATH500 from 7.0% to 32.2%, sometimes by changing only 16 parameters. The honest caveat: the model shows little understanding of its own edits, and random search sometimes does as well, so this is not yet evidence of understanding-driven self-improvement.
- **Looped WSP** (X thread, [@ahmedmm72234641](https://x.com/ahmedmm72234641/status/2124869402634129901)): Opus 5.5 solved 26% of hard mazes when answering directly, then wrote a transformer and set its weights by hand, reaching 100% on the test mazes in 39 minutes for $19.

## GPT-6 science claims

OpenAI published a [preprint summary](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities) arguing its GPT-6 models can do structural biology design work through general reasoning and code rather than by calling specialist scientific models, with partner wet-lab validation. Specialist models still handled parts of the pipeline, so the claim applies to the generation step rather than the whole workflow. Separately, OpenAI described [two amateur astronomers using Codex and Astra](https://openai.com/index/searching-for-distant-planets-with-astra) to search public Kepler and survey data (about 100,000 and 19 million stars) for exoplanet transit signals, producing candidate systems for professional follow-up. Both are the same pattern: a general model plus code replacing a domain-specific tool chain, which is the capability claim behind the week's recursive-self-improvement debate.

## Relation to prior wiki pages

- **Namazu Small** adds to the open-weight small-model thread on [index](../index.md) and to the continued-pretraining economics in [scaling-laws.md](scaling-laws.md).
- **WSP results extend** [weight-space programming (11-19)](2026-11-19-weight-space-programming-field.md) and connect to [Self-WSP's RSI framing](../agentic-systems/self-evolving-agents.md): editing weights is the fourth self-improvement surface after prompts, tools and harness.
- **GPT-6 science claims** are the evidence base for the recursive-self-improvement argument that CAIS's MisAnthropic statement and the Axios reporting both reference (see [responsible-ai.md](../responsible-ai/responsible-ai.md)).
