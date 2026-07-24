---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.16859
url: https://huggingface.co/papers/2607.16859
arxiv_url: https://arxiv.org/abs/2607.16859
date: 2026-07-24
---

# Dataset Distillation by Influence Matching

We revisit dataset distillation from an outcome-centric perspective. Rather than aligning process surrogates (per-step gradients or training trajectories), Influence Matching (Inf-Match) aligns the final outcome of training: it learns a compact synthetic set whose effect on the converged parameters matches that of the full dataset. Concretely, we introduce a fully differentiable, sample-level influence estimator that quantifies parameter shifts from adding or removing data, without time-consuming inverse-Hessian products or convexity assumptions. The estimator runs in linear time by unrolling the optimization dynamics and applying a first-order Taylor approximation. We then learn the synthetic set by minimizing the mismatch between its influence and that of the real dataset, yielding outcome alignment rather than heuristic process imitation. Inf-Match delivers the best accuracy across standard classification benchmarks. For instance, on Tiny-ImageNet (IPC=10), Inf-Match attains 31.5\%, a +4.7\% improvement over NCFM. Beyond classification, Inf-Match scales to vision-language distillation on Flickr30K, outperforming strong process-matching baselines. For instance, with 200 to 1000 synthetic samples, our method achieved a leading impressive average on image/text retrieval tasks, higher than NCFM by 2.5\%. The code will be released via https://github.com/hrtan/infmatch.
