---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.11284
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.11284
published: 2026-04-16
authors: Augustus Haoyang Li
---

# THEIA: Learning Complete Kleene Three-Valued Logic in a Pure-Neural Modular Architecture

**arXiv:** https://arxiv.org/abs/2604.11284
**Authors:** Augustus Haoyang Li

## Abstract

arXiv:2604.11284v2 Announce Type: replace-cross  Abstract: We present THEIA, a modular neural architecture that learns complete Kleene three-valued logic (K3) end-to-end without any external symbolic solver, and investigate what architectural prior enables compositional generalization under uncertainty. THEIA processes four mathematical domains (arithmetic, order, set membership, propositional logic) through dedicated engines that converge in a final logic module. Trained on a 2M-sample dataset with input space ~3.4 x 10^13, it achieves 12/12 Kleene K3 rule coverage across 5 seeds in 7.93 +/- 1.40 minutes (6.5x faster under matched settings; ~3.6x under Transformer-standard tuning, App. G). A mod-3 sequential composition experiment generalizes from 5-step training to 500-step evaluation at 99.97% +/- 0.02% -- a result requiring a structured backbone: replacing the four-engine backbone with a flat MLP collapses length generalization to chance by 50 steps at both tested capacities (0.80M and parameter-matched 2.75M), while a pre-LN TF8LTuned Transformer baseline (3,582,147 params) trained under the identical protocol reaches 99.24% at 500 steps (Appendix F). Mechanistic probing reveals that modularity induces a delayed verdict: upstream engines encode domain-specific variables without committing to the final truth value (probe accuracy <= 74% uncertainty-only ceiling), with the verdict emerging only at the Logic Engine boundary -- causally confirmed by activation patching (100% flip rate on 986 matched OR pairs, replicated across n=5 seeds; 100.0% aggregate on 4,898 pairs; generalized to AND with 100% flip rate on 4,719 pairs). The Transformer baseline reaches equivalent correctness through a qualitatively different representational trajectory (contraction then expansion), suggesting that modular and monolithic architectures implement distinct compositional strategies.
