---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.351159+05:30
arxiv_id: 2609.39166
url: https://huggingface.co/papers/2609.39166
arxiv_url: https://arxiv.org/abs/2609.39166
date: 2026-10-01
---

# Beyond the Remembered World: Predictive 4D Belief for Persistent Navigation in Evolving Worlds

Persistent spatial memory enables embodied agents to navigate familiar environments across repeated visits. However, targets may move while unobserved, including during navigation, making remembered locations unreliable by the time an agent arrives. Despite advances in memory retrieval and state prediction, accounting for continued hidden world evolution and revising beliefs under limited visibility remain challenging. We study Evolving-World Navigation, where agents infer target locations from intermittent observations, predict their states at inspection time, and revise beliefs using visual evidence. We propose EvolvingNav, which constructs a time-indexed belief from timestamped 3D object histories through a structured persistence-relocation model. The belief distinguishes persistence at the last observed location from relocation to alternative locations and retains probability mass outside the known candidate set. An event-driven filter propagates the current belief as time elapses, forecasts target occupancy at candidate inspection times, and incorporates new RGB-D evidence. Negative observations downweight location hypotheses according to calibrated, visibility-conditioned detection probabilities, while evidence tracking prevents repeated use of the same observations. A frozen, zero-shot vision-language controller uses the updated belief to choose actions and replan. We further introduce EvoWorld-Bench, a benchmark grounded in human activity traces, comprising 54 scenes and 803,680 tasks with controlled changes before and during navigation. In simulation and real-robot experiments, EvolvingNav improves navigation success and search efficiency over the evaluated baselines. Paired experiments show the clearest gains under learnable temporal patterns, while ablations demonstrate the value of preserving uncertainty and incorporating visibility-aware evidence.
