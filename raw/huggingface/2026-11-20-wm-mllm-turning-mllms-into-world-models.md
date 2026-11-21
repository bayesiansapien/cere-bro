---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.384473+00:00
arxiv_id: 2611.24193
url: https://huggingface.co/papers/2611.24193
arxiv_url: https://arxiv.org/abs/2611.24193
date: 2026-11-20
---

# WM^MLLM: Turning MLLMs into World Models

Video world models keep the world in the context of a generator, so a revisit is synthesized again and earlier edits can drift or disappear. We present WM^MLLM, the first interactive world model built on multimodal large language models (MLLMs), for persistent, editable world generation from a single image. WM^MLLM keeps the world state outside every generator, as a panorama with a revision history, and lets the MLLMs write it: they turn each request into operations on this state, select where a local edit is written, and check every candidate before it becomes the next state. Image generators only propose views, and video only presents them. Users can walk to new places and return, edit objects through text or a box, place subjects, and change lighting, weather or season. By construction, a revisit at the same revision reproduces the earlier view exactly, a local edit leaves every panorama pixel outside its region unchanged, and each request starts from the result of the previous one. Against six world model baselines on MBench-A, WM^MLLM has the highest mean on all four environment-recovery metrics (Epipolar 91.5 versus 0.1 to 74.0) and completes the most camera round trips (85.3% versus at most 50.9%). It has the best value in all 15 CompBench columns against 15 baselines. On 112 local edits judged blind, selecting the region to write after generation raises completion from 34.8% to 83.0%. On 258 WBench and MBench-A items, all 46 revisits recover their earlier views, and all 97 local edits that pass the check leave panorama pixels outside their region unchanged.
