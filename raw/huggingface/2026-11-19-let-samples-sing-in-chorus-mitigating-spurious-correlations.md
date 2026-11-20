---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.149010+00:00
arxiv_id: 2611.22668
url: https://huggingface.co/papers/2611.22668
arxiv_url: https://arxiv.org/abs/2611.22668
date: 2026-11-19
---

# Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view Consensus

Deep models often rely on spurious correlations that fail on underrepresented groups. Existing methods either correct human-specified bias attributes or infer unknown biases from the learned representation space. However, annotated attributes may differ from the shortcuts actually used by a model, while a single representation provides incomplete and potentially noisy evidence. Our key insight is that a bias obscured in one feature space may be clearer in another. In this work, we propose CHORD (Cross-view Harmonic Outlier Reversal for Debiasing), a multi-view framework that allows samples to "sing in chorus" across diverse representation spaces to achieve robust cross-view consensus. CHORD aggregates aggregates within-class partitions in each view, which is a proxy for specifying candidate biases, to debias the target representation and classifier without bias supervision. Experiments on seven benchmarks across vision, language, speech, and medical imaging show consistent improvements in worst-group accuracy. Code and checkpoints are available at https://github.com/davelee-uestc/chord_debiasing_public .
