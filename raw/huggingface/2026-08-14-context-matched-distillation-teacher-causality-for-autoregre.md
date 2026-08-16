---
source: farmer/huggingface
farmed: 2026-08-16T08:10:48.292809+00:00
arxiv_id: 2608.13391
url: https://huggingface.co/papers/2608.13391
arxiv_url: https://arxiv.org/abs/2608.13391
date: 2026-08-14
---

# Context-Matched Distillation: Teacher Causality for Autoregressive Video Distillation

Interactive autoregressive video generation demands both low-latency rollouts and precise online control. Few-step distillation accelerates generation by reducing denoising steps, while online control imposes a causal constraint: frames and blocks should depend on history and controls available during generation. Existing video distribution matching distillation (DMD) pipelines, however, often supervise causal few-step students using bidirectional teachers that score complete clips. The score for a target can therefore depend on future frames and controls that were unavailable when the student generated it, misaligning teacher supervision with the student's causal information set. We introduce Context-Matched Distillation (CMD), a causal DMD framework that aligns teacher supervision with the information available when each target is generated. CMD replaces bidirectional full-clip scoring with a causal teacher that evaluates each target without access to future frames or controls. The same causal teacher initializes the few-step student, establishing a consistent causal formulation across teacher training, student distillation, and inference. Beyond aligning the temporal information boundary, Prefix Scoring matches supervision to the student's realized rollout context by evaluating each target under the cached student-generated prefix that produced it. Prefix Corruption further stabilizes training by perturbing unreliable prefixes produced early in training while preserving this target-context alignment. With a simple causal formulation, CMD naturally extends to frame-wise and chunk-wise generation, long video distillation, and camera-conditioned distillation. Experiments demonstrate state-of-the-art aggregate performance among autoregressive methods on both short- and long-video benchmarks, together with substantially improved adherence to time-varying camera controls.
