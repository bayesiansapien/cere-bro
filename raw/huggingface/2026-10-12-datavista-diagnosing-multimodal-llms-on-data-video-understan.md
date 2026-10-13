---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.220623+05:30
arxiv_id: 2610.11993
url: https://huggingface.co/papers/2610.11993
arxiv_url: https://arxiv.org/abs/2610.11993
date: 2026-10-12
---

# DataVista: Diagnosing Multimodal LLMs on Data Video Understanding

Data video is a media form that integrates data visualization with video narrative, widely adopted in news reporting and business analysis. Compared with general video understanding, data video understanding places greater emphasis on accurately reading data from animated charts, integrating evidence across charts and time, and understanding how narrative organization and visual design communicate information. Yet existing benchmarks target either general videos or static charts, and data video understanding has not been systematically evaluated. We present DataVista, the first benchmark for data video understanding, containing 961 real-world data videos and 6,775 evaluation questions organized under a three-level progressive capability framework (data perception, temporal reasoning, narrative understanding) with 10 fine-grained question types across five topic domains. Systematic evaluation of 19 mainstream MLLMs shows that the best-performing model, Gemini-3.1-Pro, achieves 70.0% overall accuracy, still far below human expert performance, with models performing worst on Causal Reasoning and Narrative Structure. Increasing frame counts and adding subtitles mainly benefit data perception and temporal reasoning, with limited gains in narrative understanding. Further analysis of model responses identifies typical failure modes in chart reading, evidence judgment, and instruction understanding. The benchmark is available at https://github.com/HKUSTDial/DataVista.
