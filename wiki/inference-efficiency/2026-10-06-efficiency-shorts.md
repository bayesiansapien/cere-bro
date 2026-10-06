# Efficiency shorts, 2026-10-06: linear attention with a 3D state, shorter CoT, direction-constrained SFT, and more

**Source:** HuggingFace Daily Papers, 2026-10-05 (window of the 2026-10-06 digest), plus Kurate cs.AI / cs.LG for 2026-10-06. Raw files under `raw/huggingface/2026-10-05-*` and `raw/kurate/2026-10-06-*`.

Short entries for papers that matter to the efficiency thread but do not need a full page.

## Triadic linear attention ([arXiv 2609.36529](https://arxiv.org/abs/2609.36529))
Linear attention stores history in a fixed-size matrix written by an outer product of key and value. Triadic linear attention writes the outer product of a key, a second key and a value into a 3D tensor, and reads by contracting both key axes with two queries. An E-dimensional second key gives E times the state for only two extra projections. Works with data-dependent forgetting, the delta rule and chunkwise-parallel training; applied to Gated DeltaNet and scalar-gated linear attention it improves long-context modeling and recall over other ways of enlarging the state. Adds to the [attention mechanisms](../llms-foundation-models/attention-mechanisms.md) thread on state capacity (Proteus 09-25, ARM 09-23). Raw: [file](../../raw/huggingface/2026-10-05-triadic-linear-attention-three-dimensional-recurrent-states.md).

## Efficient reasoning training vs CoT faithfulness ([arXiv 2610.03509](https://arxiv.org/abs/2610.03509))
Three ways to shorten chain-of-thought (fixed budget, per-example length target, group-relative length reward). Faithfulness (does the CoT reflect decisions on related inputs) drops in most settings, mostly because trained models become less consistent. Monitorability (does the CoT admit when an input intervention changed the answer) holds up even when CoT is much shorter. For cost work: you can cut reasoning tokens without losing the main oversight property. Raw: [file](../../raw/huggingface/2026-10-05-efficient-reasoning-training-does-not-always-harm-cot-faithf.md).

## OPSFT: on-policy update direction ([arXiv 2609.36659](https://arxiv.org/abs/2609.36659))
SFT moves parameters in a consistent direction; on-policy training keeps changing direction. Constraining SFT updates to the cumulative direction found by a few on-policy steps (OPSFT) transfers on-policy generalization to cheap SFT, and lets high-quality offline trajectories keep improving a post-trained model without undoing RL gains. Same "the signal is a direction" claim as the 10-02 [distillation](knowledge-distillation.md) entry. Raw: [file](../../raw/huggingface/2026-10-05-on-policy-parameter-update-direction-underlies-generalizatio.md).

## Pivot-SD for diffusion LMs ([arXiv 2610.03665](https://arxiv.org/abs/2610.03665))
In masked diffusion LMs a few commitments during denoising decide most of the answer. Pivot-SD trains only on those "pivots," chosen by information gain over the remaining masked positions: cross-entropy on pivots from successful runs, targeted unlikelihood on pivots from failed runs. With 200 questions and four rollouts each it beats full-sequence SFT and budget-matched diffusion RL on LLaDA-8B-Instruct. Same "train on the few tokens that matter" idea as TIP (04-16) for autoregressive distillation. Raw: [file](../../raw/huggingface/2026-10-05-pivot-sd-efficient-self-distillation-for-masked-diffusion-la.md).

## KeyRec: bounded visual memory ([arXiv 2609.32182](https://arxiv.org/abs/2609.32182))
Training-free visual-token memory for streaming video VLMs: a recent-frame cache plus an event bank maintained by add-merge-evict, and a text-only router that splits a fixed readout budget between them. Best compressed result in 13 of 15 settings at 10% of the dense visual-token budget. A KV-eviction design with a router in front. Raw: [file](../../raw/huggingface/2026-10-05-keyrec-bounded-visual-memory-for-streaming-and-long-video-un.md).

## GTR: gated token recurrence for vision ([arXiv 2609.26590](https://arxiv.org/abs/2609.26590))
Softmax-free recurrent vision backbone distilled from a DINOv3 detection teacher. 58.9 box AP on COCO at 1.908 ms batch-one on an RTX 4090; its chunkwise CUDA operator is 4.0x faster than FLA v0.5.0 at 1.6K tokens; 2.3 to 8.8 ms on DRIVE AGX Thor with TensorRT. Raw: [file](../../raw/huggingface/2026-10-05-gtr-gated-token-recurrence-for-efficient-dense-prediction.md).

## Tail-Influence Sampling (HF and Kurate cs.LG #1) ([arXiv 2609.38096](https://arxiv.org/abs/2609.38096))
How to spend a fixed evaluation budget to estimate a policy's lower-tail CVaR (the average of its worst outcomes). Derives a per-component "tail influence," then reallocates queries toward components that matter for the tail. 41% lower MSE than learned occupancy and 76% lower than full rollouts on CliffWalking; 2.4 to 3.4x lower MSE than rollouts on six-call FinQA review workflows with frozen LMs. Relevant to cost-aware agent evaluation: measure rare failures without paying for full rollouts. Appears in both HF and Kurate this window, but Kurate's tournament had not scored this week's list yet (every entry at the 1200 seed score). Raw: [file](../../raw/huggingface/2026-10-05-tail-influence-sampling-for-cvar-policy-evaluation.md).

## Collective Bias Mitigation via routing ([arXiv 2610.03240](https://arxiv.org/abs/2610.03240))
Routes and organizes several LLMs (debate, committee topologies) to reduce bias; a top-7 committee cuts an age-bias score from 0.25 to 0.10, with the committee balancing mitigation against inference cost. Routing used for a value objective rather than cost. See [LLM routing](../ai-routing/llm-routing.md). Raw: [file](../../raw/huggingface/2026-10-05-collective-bias-mitigation-via-model-routing-and-collaborati.md).

## Kurate titles to track (no abstracts captured)
Serving and compression papers on this week's unscored Kurate lists: *Jumping the Line: Exploiting Length Predictions in LLM Scheduling* ([2610.03430](https://arxiv.org/abs/2610.03430)), *Exact Memory-Time Optimization for Prefix-Cached Language Model Serving* ([2610.02766](https://arxiv.org/abs/2610.02766)), *Dynamic Expert Pruning for Multi-Agent Systems* ([2610.02951](https://arxiv.org/abs/2610.02951)), *DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation* ([2610.04596](https://arxiv.org/abs/2610.04596)), *Frequency Is Not Sensitivity: Safety-Sensitive Experts in Sparse MoE* ([2610.02910](https://arxiv.org/abs/2610.02910)).

## Related
[KV cache](kv-cache.md) · [Knowledge distillation](knowledge-distillation.md) · [Daily digest 2026-10-06](../daily-digest/2026-10/2026-10-06.md)
