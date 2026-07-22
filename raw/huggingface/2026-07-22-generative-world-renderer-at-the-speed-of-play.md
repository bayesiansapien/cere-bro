---
source: farmer/huggingface
farmed: 2026-07-22T05:46:30Z
arxiv_id: 2607.18703
url: https://huggingface.co/papers/2607.18703
arxiv_url: https://arxiv.org/abs/2607.18703
date: 2026-07-22
---

# Generative World Renderer at the Speed of Play

Generative world renderer AlayaRenderer receives structured world states exported from physics engines and synthesizes RGB frames. Unlike models that generate frames from text/control-hints prompts, AlayaRenderer preserves scene structure without altering the underlying world dynamics. This demonstrates an alternative path toward interactive world modeling and user-controllable play. However, the original AlayaRenderer is too computationally expensive for real-time deployment. This technical report introduces AlayaRenderer-Flash, a real-time-oriented generative forward world renderer that pushes AlayaRenderer from 0.56 FPS to 31.54 FPS, reaching the speed of play. AlayaRenderer-Flash reformulates the original renderer as a few-step autoregressive streaming model and introduces lightweight distilled codecs for efficient latent encoding and frame reconstruction. It retains the teacher model's G-buffer and text-prompt interfaces while enabling continuous rendering over input streams of unbounded length. We evaluate AlayaRenderer-Flash on G-buffer streams across content preservation, temporal consistency, cross-window stability, prompt controllability, and runtime efficiency. Our results show that AlayaRenderer-Flash substantially reduces inference cost while preserving the core rendering capabilities of the teacher model. By integrating AlayaRenderer-Flash with a physics engine, we build a fully playable generative world running at 30 FPS.
