# HRM-Text: 1B Hierarchical Recurrent Model Pretrained on $1.5K Budget Matches 2-7B Open Models

**Source:** HuggingFace Daily Papers 2026-05-21 · arXiv 2605.20613 · [paper](https://arxiv.org/abs/2605.20613) · [raw](../../raw/huggingface/2026-05-21-hrm-text-efficient-pretraining-beyond-scaling.md)
**Topic:** llms / pretraining / architectures

## TL;DR

HRM-Text replaces the standard decoder-only Transformer in pre-training with a Hierarchical Recurrent Model that decouples computation into a slow strategic layer and a fast execution layer (inspired by the frontoparietal loop in biological systems). To stabilize the deep recurrence, the paper introduces MagicNorm (a normalization recipe for deep recurrent stacks) and warmup deep credit assignment. Instead of internet-scale raw text, training uses only instruction-response pairs under a PrefixLM-masked task-completion objective. A 1B-parameter HRM-Text trained from scratch on 40B unique tokens and a $1,500 budget reaches 60.7% MMLU, 81.9% ARC-C, 82.2% DROP, 84.5% GSM8K, 56.2% MATH — roughly 100-900x fewer training tokens and 96-432x less compute than baselines, competitive with 2-7B open models.

## What is new

The headline claim is provocative: co-designing architecture (HRM with slow-fast hierarchy) and objective (instruction-response on PrefixLM-mask) collapses pre-training compute by two orders of magnitude. Both halves of the co-design are load-bearing. The HRM architecture introduces two timescales: the slow layer makes a small number of strategic decisions per sequence, the fast layer executes inside those decisions. The objective change drops the next-token-prediction-on-internet-text paradigm for task-completion-on-instructions. The masking choice (PrefixLM with bidirectional context over the instruction, causal over the response) lets the slow-fast hierarchy align with the prompt-response boundary.

MagicNorm and warmup deep credit assignment are the engineering pieces. Deep recurrent stacks have always been unstable; the prior Mamba-and-similar wave handled it with state-space-specific tricks. HRM-Text's MagicNorm is the first generic recipe in the wiki for stabilizing deep recurrence at language-modeling scale.

## Why it matters

The Bitter Lesson for Data Filtering (Kurate cs.LG #12 this week, Mohri-Duchi-Hashimoto) argued that data filtering has hard limits at scale. HRM-Text attacks the same problem from the opposite direction: do not scale the data, change the objective so that an instruction-aligned dataset is sufficient. The 1B-model-with-40B-token claim implicitly says the bottleneck for small-model performance was never raw token budget; it was the alignment between objective and downstream evaluation.

If the result replicates, the cost-of-training-frontier conversation shifts. The MathFreeLab-style "we made a 4B model that beats 7B" papers do not move the cost frontier by an order of magnitude; HRM-Text claims two orders. Most likely intermediate: HRM-Text trades stronger task-completion accuracy at the trained-objective regime for weaker base-model versatility (less in-context-learning headroom, less ability to absorb post-training that goes off-distribution). The wiki has not yet seen the ICL or post-training comparison.

## Research angle

Three open questions. First, the comparison is to 2-7B open models on five reasoning-heavy benchmarks. The benchmarks chosen all benefit from instruction alignment; the test that matters is on tasks where the open models' raw-text pre-training carries an advantage (long-form generation, code, in-context-learning from few-shot examples). Second, the slow-fast hierarchy in HRM-Text is shallow (two layers); the natural extension to deeper hierarchies (multi-timescale strategic, tactical, execution) is the architectural question DynMuon's spectral-shaping theory could help answer (deeper hierarchies have richer Hessian structure that needs different optimizer regimes). Third, the data efficiency claim composes with the unlearnability finding from today (some examples cannot be learned via RLVR because the representation is wrong); if HRM-Text's pre-training builds the right representation faster, the unlearnable set should shrink.

## Related wiki pages

- [DynMuon spectral shaping (2026-05-21)](2026-05-21-dynmuon-spectral-shaping.md)
- [Delta Attention Residuals (2026-05-20)](2026-05-20-delta-attention-residuals.md)
- [PreRL: RL in pre-train space (2026-04-16)](2026-04-16-prerl-rl-in-pretrain-space.md)
