---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.004277+00:00
arxiv_id: 2611.15640
url: https://huggingface.co/papers/2611.15640
arxiv_url: https://arxiv.org/abs/2611.15640
date: 2026-11-16
---

# MemInStream: Memorizing or Merely Recognizing? Rethinking Streaming Video Memory Evaluation

Streaming video understanding aims to continuously process incoming visual observations, making the retention and retrieval of relevant information increasingly important as the video history grows. Although existing benchmarks include memory-related questions, question-answering accuracy alone does not reliably measure memory capabilities. Incorrect predictions may arise from failures in visual understanding rather than forgetting, whereas correct predictions may rely on linguistic priors or recent observations without requiring historical memory. To address these ambiguities, we introduce MemInStream, a benchmark dedicated to evaluating memory capabilities in streaming video understanding. We develop an evidence-controlled validation protocol that associates each question with temporally localized evidence intervals. The protocol validates evidence solvability and memory necessity by retaining questions that models can answer from the annotated evidence but cannot resolve using recent observations, post-evidence observations, or textual input alone. This helps disentangle memory limitations from understanding failures while reducing memory-independent shortcuts. MemInStream provides a systematic evaluation of memory capabilities through four major categories, covering Episodic Retrieval, State Tracking \& Updating, Multi-Evidence Integration, and Contextual Memory across diverse video scenarios. Overall, MemInStream provides a comprehensive and reliable benchmark for systematically evaluating memory capabilities in streaming video understanding.
