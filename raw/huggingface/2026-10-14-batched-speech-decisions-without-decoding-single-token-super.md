---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.513530+00:00
arxiv_id: 2610.02638
url: https://huggingface.co/papers/2610.02638
arxiv_url: https://arxiv.org/abs/2610.02638
date: 2026-10-14
---

# Batched Speech Decisions Without Decoding: Single-Token Supervision Lets a Frozen LLM Hear Beyond the Transcript

Full-duplex voice agents make many small, closed decisions, which current systems answer by slow autoregressive decoding. We propose DuplexJev, which feeds ASR-encoder hidden states through a small connector into a frozen LLM and reads each question as a single-token distribution over its options. Nothing is decoded, and an 8-GPU node answers 80 decisions about eight utterances in about 0.1 s. With a last-layer connector, spoken QA stays close to reading the transcript (90% vs. 91%). DuplexJev also hears the speaker: gender and emotion accuracy both reach 90% (from 55% and 28%) with a cross-attention connector, whose spoken QA drops by only 1 point (83% to 82%). We train decisions with cross-entropy on the read-out answer token, instead of the usual transcript distillation, whose teacher never hears the voice, and keep distillation for content. Encoders and LLMs are interchangeable; we release weights, training recipe, a batched-inference pipeline for full-duplex serving and a bilingual spoken-QA set.
