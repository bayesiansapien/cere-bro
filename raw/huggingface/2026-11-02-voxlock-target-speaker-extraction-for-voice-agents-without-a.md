---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.501099+05:30
arxiv_id: 2610.40727
url: https://huggingface.co/papers/2610.40727
arxiv_url: https://arxiv.org/abs/2610.40727
date: 2026-11-02
---

# VoxLock: Target-Speaker Extraction for Voice Agents Without an Enrollment Step

A voice agent's speech recognizer transcribes everyone near the microphone, including people other than the caller. I fine-tuned a public causal target-speaker extraction model (REAL-TSE, 27M parameters) on one GPU to work from a voice sample cut from the call itself, and released it as VoxLock. I score it by what a recognizer writes on real recordings. On Krisp's 265-recording benchmark it reaches 4.95% WER against 23.21% unprocessed and lets 9 background words into the transcript over 85 minutes of background-only speech. Its WER is not significantly different from Krisp's best filters and is significantly lower than the other commercial and open systems I tested. On 400 AMI meeting windows built and frozen before scoring, it cuts WER from 42.95% to 10.63%. The 8-bit model runs a live call on 77% of one CPU thread with 24 ms of algorithmic latency. Model, code and per-file scores are open.
