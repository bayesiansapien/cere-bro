---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.07641
url: https://huggingface.co/papers/2610.07641
arxiv_url: https://arxiv.org/abs/2610.07641
date: 2026-10-07
---

# Hiding Tool Latency in On-Device Cascaded Voice Agent through Speculative Execution

Tool-augmented speech assistants typically serialize automatic speech recognition, large language model inference, and external tool execution. As a result, tool latency is incurred only after the user has finished speaking and the LLM has identified the required tool calls. We present speculative tool execution for on-device cascaded voice agents, which predicts tool requests from partial ASR hypotheses and initiates tool execution while speech is still being received, thereby reducing end-to-end response latency. Our approach introduces a Predictor module that anticipates tool calls during speech recognition, executes them speculatively, and caches the results. The cached outputs are then injected into the LLM prompt, enabling faster responses. Additionally, to mitigate errors caused by user self-corrections during speech, we employ a rule-based validation mechanism that selectively injects only valid cached results. As a final safeguard, the LLM retains the ability to issue tool calls directly, ensuring that the latency of our framework is upper-bounded by the baseline serial execution pipeline in the worst case. We evaluate our method using live measurements from a fully implemented Android voice assistant. Our approach reduces the median time-to-first-audio from 5.79,s to 4.60,s and decreases the standard deviation from 3.49,s to 2.81,s, resulting in more predictable response latency.
