---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820901+00:00
arxiv_id: 2610.00825
url: https://huggingface.co/papers/2610.00825
arxiv_url: https://arxiv.org/abs/2610.00825
date: 2026-10-02
---

# Align Then Reason: A Multimodal Lip-Sync Judge for Dubbing

Dubbing quality control requires a reference-free judge that can determine whether a candidate text line matches a speaker's visible articulation in both content and timing, using only silent video and text because dubbed audio may not yet exist. Existing visual speech recognizers and video-language models are poorly suited to this setting: even when fine-tuned to recover spoken content from lip motion, they remain largely insensitive to temporal errors. We introduce Align Then Reason (ATR), a multilingual lip-sync judge that first establishes a monotonic alignment between frame-level lip representations and the phonetic units of the candidate line, then reasons over this alignment to make the final judgment. An alignment scorer provides the LLM with both local evidence for each phonetic unit and a calibrated global alignment score, enabling it to reason jointly about content and timing. On a seven-language benchmark, our method improves mean AUC over the corresponding Qwen3.5 SFT baselines by 59.4%, 50.2%, and 50.8% with 2B, 4B, and 9B reasoners, respectively. The gains generalize across LLM families, reaching mean AUC improvements of 45.9% and 46.6% over the best baseline for LLaMA-3.1-8B and Mistral-7B, respectively. They also transfer across datasets to three unseen MuAViC languages. Furthermore, we evaluate on two downstream tasks built from real dubbing lines. On dub-line reranking, ATR-9B outperforms the best lip-reading baseline by 52.0%, while on script-to-clip assignment, ATR-9B improves over the best lip-reading baseline by 17.7%.
