# DiHAL: Where Should Diffusion Enter a Language Model? Geometry-Guided Hidden-State Replacement

**arXiv:** [2605.14368](https://arxiv.org/abs/2605.14368) · **HF:** [paper page](https://huggingface.co/papers/2605.14368) · **Tier:** 2 (architecture, diffusion language models, hybrid)

## TL;DR

Continuous diffusion language models lag behind autoregressive transformers in part because diffusion is applied in spaces poorly suited to language denoising and token recovery. DiHAL is a geometry-guided diffusion-transformer hybrid that asks where diffusion should enter a pretrained transformer. It scores layers with geometry-based proxies, selects a diffusion-friendly hidden-state interface, and replaces the lower transformer prefix with a diffusion bridge while keeping the upper layers and original LM head. By reconstructing the selected-layer hidden state instead of tokens, DiHAL avoids direct continuous-to-discrete recovery. Experiments on 8B-scale backbones show the geometry score predicts effective shallow insertion layers under a fixed bridge-training protocol; hidden-state recovery improves over continuous diffusion baselines in a diagnostic comparison matching diffusion/recovery training budget.

## Key findings

- Continuous diffusion in token space is fundamentally awkward: language is discrete, and continuous-to-discrete recovery is where prior continuous diffusion LMs lose performance.
- DiHAL's structural move: don't apply diffusion to tokens; apply it to a hidden-state interface inside a pretrained transformer. The lower transformer prefix is replaced by a diffusion bridge, and the upper layers plus original LM head are retained.
- The where-to-replace decision is non-trivial. DiHAL scores each layer with a geometry-based proxy (the geometry of the layer's hidden-state distribution) and picks the layer whose geometry is most diffusion-friendly.
- This is hidden-state recovery, not token recovery. The diffusion bridge reconstructs the chosen layer's hidden state and lets the unchanged upper layers and LM head produce the final tokens.
- On 8B-scale backbones, the geometry score predicts which shallow insertion layer makes a good interface. Hidden-state recovery beats continuous diffusion baselines under matched training budget.

## Relationship to prior wiki entries

The wiki has tracked diffusion language models intermittently. The closest prior entry is Orthrus (2026-05-14, the paper that runs an AR head and a diffusion head on the same frozen LLM both attending to the same shared KV cache, with exact-consensus producing bit-identical AR output at up to 7.8x speedup). Orthrus uses diffusion to draft tokens for AR speculative decoding. DiHAL uses diffusion to replace the lower layers of an AR model entirely.

DiHAL also connects to the SNLP (2026-05-19 today, the layer-parallel inference framework with Identity Newton and HC Newton surrogates) framing. Both treat the layer stack as a substrate that can be replaced or parallelised in principled ways given knowledge of the hidden-state structure. SNLP uses architecture-induced surrogates (identity for residual, mHC residual mixing matrix for mHC). DiHAL uses geometry-derived layer selection. Both are non-trivial uses of internal model structure that depart from the standard layer-by-layer assumption.

The framing question (where should diffusion enter) is the right one for the broader question of diffusion-LM hybrid design. Prior work picked the interface arbitrarily. DiHAL gives a principled selection rule.

## Why it matters

Diffusion LMs have remained a research curiosity because the standard recipe (continuous diffusion in token space) does not match the discrete nature of language. DiHAL is the first principled selection rule in the wiki for diffusion-transformer hybrids. If the geometry score generalises (similar proxy works at 30B, 70B, on MoE architectures), the field will have a deployable hybrid-design recipe rather than a per-paper ablation.

The decision to keep the LM head unchanged is also operationally important. It means a DiHAL hybrid is a drop-in replacement for the lower layers of an existing model; existing post-training stacks (RLVR, distillation, knowledge editing) target the upper layers and the head, and those remain compatible.

## Research angle

- **Generalisation of the geometry proxy.** Does the geometry score predict the right insertion layer on a 70B model? On a MoE backbone? Whether the score is a small-scale empirical regularity or a deeper structural prediction is open.
- **Compose with Orthrus.** Both use diffusion within a transformer. Orthrus uses it as a parallel speculative drafter; DiHAL uses it as a lower-layer replacement. Whether a model could have a DiHAL lower-stack feeding an Orthrus dual-view upper-stack is the natural composition.
- **Training-from-scratch DiHAL.** The paper modifies a pretrained transformer. Whether training a DiHAL hybrid from scratch (diffusion bridge below, transformer above) gives different (better, worse, or stranger) geometry is the load-bearing pre-training question.

## Source

`raw/huggingface/2026-05-19-where-should-diffusion-enter-a-language-model-geometry-guide.md`
