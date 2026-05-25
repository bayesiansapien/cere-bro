# r/LocalLLaMA | 2026-05-25 IST | sort=top
> Scraped 2026-05-25 10:32 IST | lookback=24h | tier_default=1
> Inference, quantization (GGUF/AWQ/EXL2), KV cache tricks, llama.cpp internals, kernel tuning, GPU rigs. Single highest-signal sub for Tier 1 efficiency.

### Is NVIDIA still the default best choice for local LLMs in 2026?

**Meta:** score=263 · comments=208 · tier=1 · flair=Discussion · posted=2026-05-24 18:34Z
**Author:** u/pmv143
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tmkaua/is_nvidia_still_the_default_best_choice_for_local/](https://www.reddit.com/r/LocalLLaMA/comments/1tmkaua/is_nvidia_still_the_default_best_choice_for_local/)
**Link:** [https://i.redd.it/pzq8x188q43h1.jpeg](https://i.redd.it/pzq8x188q43h1.jpeg)

---

### Qwen3.6-35B-A3B-Uncensored-Genesis-APEX-MTP

**Meta:** score=216 · comments=77 · tier=1 · flair=New Model · posted=2026-05-24 06:08Z
**Author:** u/EvilEnginer
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tm3toi/qwen3635ba3buncensoredgenesisapexmtp/](https://www.reddit.com/r/LocalLLaMA/comments/1tm3toi/qwen3635ba3buncensoredgenesisapexmtp/)

Here model: [https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-V2-APEX-MTP-GGUF](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-V2-APEX-MTP-GGUF)

Safetensors: [https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-V2-FP8-Safetensors](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-V2-FP8-Safetensors)

MTP-Safetensors: [https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-V2-FP8-MTP-Safetensors](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-V2-FP8-MTP-Safetensors)

*Testing results in Open Code on hardware (Beelink gtr9 pro + Strix Halo) done by my friend on Q8\_K\_P - MTP quant:*

1. 5 sessions with 200k context, not a single glitch, no loops, no repeated tool calls.
2. After 120k tokens he suddenly gave another task that doesn't intersect with what it was doing at all, and it calmly picked up and solved it correctly.
3. Uncensored with MTP support with APEX and APEX Compact quantization.
4. Safetensors support for Apple MLX conversion for Mac users.

**Recommended quant:** APEX, MTP-APEX

**Recommended settings for LM Studio:**

[System Prompt](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-V2-APEX-MTP-GGUF/raw/main/System_Prompt.txt)

[Chat Template](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-V2-APEX-MTP-GGUF/raw/main/chat_template.jinja)

[Chat Template Thinking](https://huggingface.co/LuffyTheFox/Qwen3

[…truncated, see permalink]

---

### Qwen3.6-35B-A3B vs Gemma4-26B-A4B

**Meta:** score=131 · comments=113 · tier=1 · flair=Discussion · posted=2026-05-24 13:05Z
**Author:** u/MarcCDB
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tmbola/qwen3635ba3b_vs_gemma426ba4b/](https://www.reddit.com/r/LocalLLaMA/comments/1tmbola/qwen3635ba3b_vs_gemma426ba4b/)

Just wondering how are people's experience with both these models!

I've had some nice results with Qwen but Gemma4 runs so much faster here. I'm using a Radeon 9070 XT and always latest llama.cpp.

---

### BitCPM-CANN: Native 1.58-Bit Large Language Model Training on Ascend NPU

**Meta:** score=58 · comments=17 · tier=1 · flair=Resources · posted=2026-05-24 15:24Z
**Author:** u/Aaaaaaaaaeeeee
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tmf63y/bitcpmcann_native_158bit_large_language_model/](https://www.reddit.com/r/LocalLLaMA/comments/1tmf63y/bitcpmcann_native_158bit_large_language_model/)

Paper: https://github.com/OpenBMB/MiniCPM/blob/main/docs/BitCPM_CANN.pdf

### Abstract

&gt;We present BitCPM-CANN, a systematic family-level study of 1.58-bit (ternary)
quantization-aware training (QAT) on the Huawei Ascend NPU platform. To address
two practical gaps for extreme low-bit LLMs—whether ternary weights preserve capabili-
ties on complex reasoning tasks at on-device scales, and how to make end-to-end 1.58-bit
training natively available outside the CUDA ecosystem—we port our prior GPU-based
pipeline to CANN, MindSpeed, and Megatron-LM, and train four models (BitCPM-
CANN-0.5B/1B/3B/8B) strictly aligned with their full-precision MiniCPM4 counterparts
in architecture and pre-training data. Across 11 benchmarks spanning commonsense
reasoning, domain knowledge, and mathematics &amp; reasoning, the 1B, 3B, and 8B variants
retain 95.7%–97.2% of full-precision performance, with the 3B variant achieving parity on
BBH and the 3B/8B variants recovering nearly all of GSM8K. The 0.5B variant retains
90.1%, with the residual gap concentrated on mathematics, indicating that capacity—not
the quantizer—is the bottleneck at sub-billion scales. Our QAT integration adds only
a 4.5% training throughput overhead (148 vs. 155 TFLOP/s per NPU), making ternary
training viable as a default configuration, while enabling up to an 8× weight memory
reduction (approximately 6× end-to-end including scaling factors) at inference. To our
knowledge, this is the first end-to-end 1.58-bit training 

[…truncated, see permalink]

---
