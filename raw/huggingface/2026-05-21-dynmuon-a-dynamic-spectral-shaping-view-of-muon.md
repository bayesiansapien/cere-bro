---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.17109
url: https://huggingface.co/papers/2605.17109
arxiv_url: https://arxiv.org/abs/2605.17109
date: 2026-05-21
---

# DynMuon: A Dynamic Spectral Shaping View of Muon

In recent years, Muon has emerged as the dominant method for training large language models, and transformers more broadly. The essential difference, when compared to standard gradient descent methods, is to replace the usual update matrix M=UΣV^top with its polar factor UV^top. In this work, we consider a class of Muon-like updates, where we replace the update M with UΣ^p V^top for some parameter p. We call this a "spectral-shaping" operation, and develop a theory of how to pick p which depends on (a) local curvature of the loss function, (b) noise stemming from stochastic gradients and label noise, and (c) training stage. Our theory and experimentation reveal a previously overlooked behavior: positive p helps early by emphasizing high-curvature directions and accelerating signal contraction, while mildly negative p helps later by reallocating update strength toward low-curvature directions that still contain useful training signals. Building on the insight, we propose DynMuon, an efficient dynamic spectral shaping method that schedules p from positive to mildly negative over training. Extensive experiments across model sizes, architectures, and training settings show that DynMuon consistently achieves lower validation loss than Muon, while requiring 10.6-26.5% fewer steps to reach the same target loss.
