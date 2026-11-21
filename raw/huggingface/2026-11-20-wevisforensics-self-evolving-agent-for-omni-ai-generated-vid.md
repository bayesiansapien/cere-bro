---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.380934+00:00
arxiv_id: 2611.21373
url: https://huggingface.co/papers/2611.21373
arxiv_url: https://arxiv.org/abs/2611.21373
date: 2026-11-20
---

# WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection

Recent advances in video generation call for reliable detection grounded in explicit forensic evidence. However, current methods primarily depend on single-pass chain-of-thought reasoning that overlooks brief or localized artifacts, or on predefined multi-agent workflows that offer limited flexibility in selecting relevant inspections. Even with adaptive investigation, optimizing the investigation policy alone does not directly improve the forensic capabilities of fixed experts. We introduce WeVisForensics, an agentic framework in which a main investigator agent coordinates a self-evolving library of forensic inspector sub-agents spanning visual and audio cues. The investigator learns which artifact type to examine, over which window, and when to conclude, and these interactions provide shared feedback for both levels of agents. Our dual-timescale policy optimization strategy, DTPO, closes this loop through fast reinforcement learning of the investigator and slower refinement of the inspectors, guided by annotated artifact intervals, to report subtle artifacts they once dismissed. Furthermore, we curate ForenCue-30K, combining role-specific forensic annotations and interaction trajectories to supervise individual inspections and their coordination, with an accompanying reinforcement-learning pool. Experiments show that WeVisForensics averages 95.2% detection accuracy across in-domain, out-of-domain and agentic benchmarks, 9.0% above the strongest prior detector, while grounding its verdicts in localized evidence.
