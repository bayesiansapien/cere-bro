---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.345474+05:30
arxiv_id: 2609.38827
url: https://huggingface.co/papers/2609.38827
arxiv_url: https://arxiv.org/abs/2609.38827
date: 2026-10-01
---

# More Choices, Fewer Decisions: Ordinal-Scale Bias in JEV-like Direct-Decision Models

Direct-decision models turn text into low-latency structured labels and scores, making them attractive for classification and automatic evaluation. Yet reliability requires more than accuracy: a model must also use the ordinal decision scale supplied by the user faithfully. We analyze JEV~1.13 and three open KEV models. Our investigation begins with ANLI, where JEV assigns 38.8\% of all predictions and 51.3\% of errors to Neutral despite 74.95\% accuracy, nearly balanced gold labels, and balanced candidate positions. Across 36 ordinal datasets, final decisions use only 67--76\% of the effective gold support, versus 87--102\% on four nominal tasks. Randomizing candidate order weakens but does not remove this compression. Holding items and source scores fixed while balancing gold support and positions, we refine scales from K=2 to 14; utilization falls for every model and reaches 26--75\% at K=14, although candidate probabilities remain broad for most models. Targeted BA-LoRA post-training raises gold-relative utilization from roughly 47\% to 86\% on eight supervised scales at both KEV sizes, showing that the compression is learned and modifiable rather than an immutable architectural limit. We call this ordinal scale-utilization bias: decision-stage candidate-space compression distinct from accuracy, gold imbalance, fixed position, and candidate count alone. The code and data are available at https://github.com/Glax147/jev_ordinal_scale_bia
