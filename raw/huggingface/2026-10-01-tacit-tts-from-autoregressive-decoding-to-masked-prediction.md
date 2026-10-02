---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.349811+05:30
arxiv_id: 2609.38658
url: https://huggingface.co/papers/2609.38658
arxiv_url: https://arxiv.org/abs/2609.38658
date: 2026-10-01
---

# Tacit-TTS: From Autoregressive Decoding to Masked Prediction for Efficient Transcript-Free Voice Cloning

TTS systems with autoregressive semantic modeling have demonstrated strong zero-shot voice cloning performance and rich expressive variation, but their sequential decoding incurs substantial latency. Non-autoregressive alternatives offer much faster generation, yet often rely on more restrictive reference conditioning, such as requiring transcripts of the reference speech during inference. We present Tacit-TTS, an efficient transcript-free zero-shot voice cloning system distilled from IndexTTS2. Our model replaces autoregressive text-to-semantic decoding with masked non-autoregressive generation, introduces training-free acoustic length estimation, and accelerates the flow-matching renderer through ReFlow distillation. Across two English and two Mandarin datasets, Tacit-TTS achieves competitive zero-shot quality while generating speech over 10x faster than IndexTTS2 for utterances longer than 5 seconds. Its transcript-free conditioning further supports cross-lingual and non-lexical references. We validate this capability using references from eight other languages, infant babble, and synthetic gibberish, where transcript-dependent systems often degrade or fail due to unreliable ASR transcripts.
