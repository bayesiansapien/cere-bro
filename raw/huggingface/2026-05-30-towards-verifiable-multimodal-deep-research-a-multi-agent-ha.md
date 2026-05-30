---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.29861
url: https://huggingface.co/papers/2605.29861
arxiv_url: https://arxiv.org/abs/2605.29861
date: 2026-05-30
---

# Towards Verifiable Multimodal Deep Research: A Multi-Agent Harness for Interleaved Report Generation

Large Language Models (LLMs) have advanced autonomous agents from deep search, which retrieves concise factual answers, to deep research, which synthesizes scattered evidence into long-form reports. However, verifiable multimodal deep research remains challenging due to open-ended synthesis without deterministic ground truth and the need to interleave textual arguments with visual evidence. We propose Ptah, a multi-agent harness for interleaved report generation. Ptah orchestrates the lifecycle from user query to rendered web report through planning, research, and writing stages, where specialized agents construct visual-aware plans, collect claim-grounded evidence, maintain source-aligned images in a Visual Working Memory, and compose reports through declarative multimodal tool use. A verifier agent serves as the harness's acceptance function, enforcing factual grounding, citation fidelity, and cross-modal consistency throughout the workflow. We further introduce PtahEval, an evaluation protocol that augments existing benchmarks with image-level and presentation-level assessments. Experiments on deep research benchmarks show that Ptah produces more reliable, visually informative, and usable human-facing multimodal reports than strong baselines.
