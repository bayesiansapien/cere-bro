---
source: farmer/rss
feed: lilian-weng
farmed: 2026-07-08T05:20:40Z
title: Scaling Laws, Carefully
url: https://lilianweng.github.io/posts/2026-06-24-scaling-laws/
published: 2026-06-23
author: 
---

# Scaling Laws, Carefully

<p>Scaling laws are one of the most critical empirical findings in deep learning. The observation is simple in form: the training loss $L$ decreases predictably as we scale up model size $N$, dataset size $D$, and compute $C$, following a power-law curve, which appears as a straight line on a log-log plot. We can view scaling laws as a framework for describing the relationship between compute, loss, model size and data; at its core, it is about how to allocate precious compute optimally between $N$ and $D$.</p>
