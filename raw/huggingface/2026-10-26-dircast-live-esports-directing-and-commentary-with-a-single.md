---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.799370+00:00
arxiv_id: 2610.31734
url: https://huggingface.co/papers/2610.31734
arxiv_url: https://arxiv.org/abs/2610.31734
date: 2026-10-26
---

# DirCast: Live Esports Directing and Commentary with a Single Streaming Video-Language Model

A live esports broadcast needs a director who chooses which camera goes on air and a caster who talks over that choice, every second and without knowing what comes next. Streaming video language models have learned to commentate, but only over a broadcast that a human director has already produced. We study live broadcast production, in which a model receives the raw camera of every player and must both direct and commentate from the past alone. We present DirCast, a single streaming video language model that does both. Every second it scans all cameras at low resolution, decides with a hold-or-switch director whether and where to cut, and reads the chosen camera at high resolution before it speaks. Its context keeps what went on air and what was said and lets the other views expire, which bounds the cost of a stream of any length. We build a dataset of 27 professional Dota 2 matches with a camera for every hero, the human director's choices and the casters' commentary. DirCast directs better than rule-based and zero-shot directors including GPT-5, and its commentary wins 29.2 percent of comparisons against GPT-4o under the Proact-VL protocol, against 19.4 percent for the strongest of eleven streaming commentators that watch the human broadcast.
