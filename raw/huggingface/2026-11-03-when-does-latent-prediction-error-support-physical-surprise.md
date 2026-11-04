---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.01815
url: https://huggingface.co/papers/2611.01815
arxiv_url: https://arxiv.org/abs/2611.01815
date: 2026-11-03
---

# When Does Latent Prediction Error Support Physical Surprise Claims in Video World Models?

Prediction errors from video world models are often treated as physical surprise, but they can also reflect appearance, static content, motion, or ordinary prediction difficulty. We present an evaluation framework that separates what frozen representations contain, how they organize appearance and physical differences, and what changes a model's own prediction error. On IntPhys2, a benchmark of physically possible and impossible events, we compare representations from latent prediction, masked pixel reconstruction, and simple visual statistics. Appearance remains easy to decode, while V-JEPA2 exposes modest information about whether events are possible or impossible. Looking at the latent geometry, appearance changes become smaller compared with differences between videos, their directions line up more consistently across scenes, and their overlap with physical changes decreases in deeper layers. Across action-conditioned models, incorrect actions raise prediction error, while appearance changes also produce substantial responses. In Physion++ video clips, repeating a single frame can produce higher error than the original clip, while changing color throughout the clip can lower it. Using Kubric, a simulation and rendering framework, we find that impossible events can produce lower error than possible events. A fixed error threshold also incorrectly flags many possible events as impossible. A model can therefore represent physical information and respond to incorrect actions without its native prediction error reliably measuring physical surprise.
