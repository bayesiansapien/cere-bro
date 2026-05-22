---
source: farmer/huggingface
farmed: 2026-05-22T00:00:00+00:00
arxiv_id: 2605.22109
url: https://huggingface.co/papers/2605.22109
arxiv_url: https://arxiv.org/abs/2605.22109
date: 2026-05-22
---

# Perception or Prejudice: Can MLLMs Go Beyond First Impressions of Personality?

Multimodal Large Language Models (MLLMs) are increasingly deployed in human-facing roles where personality perception is critical, yet existing benchmarks evaluate this capability solely on numerical Big Five score prediction, leaving open whether models truly perceive personality through behavioral understanding or merely prejudge through superficial pattern matching. We address this gap with three contributions. (i) A new task: we formalize Grounded Personality Reasoning (GPR), which requires MLLMs to anchor each Big Five rating in observable evidence through a chain of rating, reasoning, and grounding. (ii) A new dataset: we release MM-OCEAN (1,104 videos, 5,320 MCQs), produced by a multi-agent pipeline with human verification, with timestamped behavioral observations, evidence-grounded trait analyses, and seven categories of cue-grounding MCQs. (iii) Benchmark and analysis: we design a three-tier evaluation (rating, reasoning, grounding) plus four sample-level failure-mode metrics: Prejudice Rate (PR), Confabulation Rate (CR), Integration-failure Rate (IR), and Holistic-grounding Rate (HR), and benchmark 27 MLLMs (13 closed, 14 open). The analysis uncovers a striking Prejudice Gap: across the field, 51% of correct ratings are not grounded in retrieved cues, and the Holistic-Grounding Rate spans only 0-33.5%. These findings expose a disconnect between getting the right score and reasoning for the right reason, charting a roadmap for grounded social cognition in MLLMs.
