---
source: farmer/huggingface
farmed: 2026-10-14T17:45:17.067247+05:30
arxiv_id: 2610.03825
url: https://huggingface.co/papers/2610.03825
arxiv_url: https://arxiv.org/abs/2610.03825
date: 2026-10-13
---

# Same Output, Different Gold: Measuring How Reference Choice Moves a Multilingual Benchmark Score

A benchmark score compares a system output against a reference, and methodological attention falls almost entirely on the first term. We measure the second. The retained annotation record of a six-language benchmark for personally identifiable information contains two independent annotator labellings, the aggregate shipped as gold, and a reviewer gold from independent expert re-annotation of a sample. Using it, we hold the scored output fixed and exchange the reference. The score moves by 4.95 F1 points for one output and 2.00 for the other (95% CIs [3.23, 6.27] and [0.26, 3.37]), and by 7.55 in the worst language. The comparison between two outputs moves as well: the paired interaction between reference and system is +2.95 points (CI [+1.97, +3.87]), survives correction for multiple testing, and changes one language's margin outright. The cause is an undocumented aggregation default that usually kept one annotator when adjudication did not fire, making the shipped reference a partial copy of an output being scored. We report the resulting reference-sensitivity band, show how to compute one from any retained annotation record, and argue that the quantity belongs beside the score.
