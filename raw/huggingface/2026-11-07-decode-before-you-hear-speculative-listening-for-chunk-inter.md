---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.593628+00:00
arxiv_id: 2611.06982
url: https://huggingface.co/papers/2611.06982
arxiv_url: https://arxiv.org/abs/2611.06982
date: 2026-11-07
---

# Decode Before You Hear: Speculative Listening for Chunk-Interleaved Full-Duplex Speech Language Models

Chunk-interleaved full-duplex speech language models listen and speak in fixed time chunks, and each chunk must be processed before the next one arrives. Their workload is asymmetric across chunks: listen chunks leave compute idle while awaiting audio, and speak and tool-call chunks require serial generation, which delays responses and tool calls. Using the idle compute for the next chunk requires decoding it before its audio arrives, under an assumed input. Taking silence as the assumed input and comparing the output with the output under real audio on four models, we observe two properties. First, the next audio chunk does not change the output in 95.3% of chunks. Second, 88% of changes begin at the first output token. Building on these properties, we propose Speculative Listening, a training-free, lossless framework for input-time self-speculative decoding. During idle time, the model drafts the next chunk under silence and, for changes at the first token, a second branch from the runner-up first token. It keeps all drafts in a cross-chunk hypothesis pool and verifies them when the audio arrives. On our eight-task benchmark TickTock-Bench, Speculative Listening speeds up speak chunks by 2.6-2.8x and tool-call chunks by up to 23.4x. On average, it reduces the decoding delay before a response starts by 73%, to 74-241 ms, close to the 200 ms gap between human turns, and the maximum lag behind real time by 94.4%.
