---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2609.31662
url: https://huggingface.co/papers/2609.31662
arxiv_url: https://arxiv.org/abs/2609.31662
date: 2026-10-06
---

# Learning Steadily: Accumulating Relative Point Margin Scores for Face Image Quality Assessment

Face Image Quality Assessment determines the suitability of captured face images for automated face recognition (FR), a critical capability for reliable biometric systems. Existing state-of-the-art FR-integrated FIQA methods suffer from temporal instability: as the feature space evolves during training, single-epoch quality estimates fluctuate, creating a moving target that undermines reliable quality prediction. We introduce CARPM-FIQA, a stabilization strategy for FR-integrated FIQA that accumulates relative point margin measurements, the ratio between intra-class compactness and inter-class separation, across the entire training trajectory rather than relying on single-epoch estimates. This cumulative averaging approach provides theoretically grounded advantages: reduced variance in quality estimates, improved mean squared error, and enhanced ranking stability with convergence guarantees as training progresses. Through controlled experiments on the SynFIQA dataset with labeled quality groups, we demonstrate that cumulative averaging achieves superior discriminative ability, and ablation studies across different training configurations confirm consistent improvements. Evaluated against twelve FIQA methods on eight challenging benchmarks with four FR models at two FMR thresholds, CARPM-FIQA places 4th (CARPM-FIQA(L)) and 6th (CARPM-FIQA(S)) of 17 compared methods by pAUC-EDC and AUC-EDC averaged across FR models and, after per-benchmark normalization, across benchmarks, staying within a few percent of the best method's normalized average for every FR model, providing a principled solution to training instability while maintaining the performance benefits of FR integration. More broadly, our work demonstrates that temporal aggregation strategies can stabilize training objectives in deep learning systems where target values inherently fluctuate due to evolving feature representations.
