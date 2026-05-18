# r/LocalLLaMA | 2026-05-18 IST | sort=top
> Scraped 2026-05-18 09:13 IST | lookback=24h | tier_default=1
> Inference, quantization (GGUF/AWQ/EXL2), KV cache tricks, llama.cpp internals, kernel tuning, GPU rigs. Single highest-signal sub for Tier 1 efficiency.

### M5 vs DGX Spark vs Strix Halo vs RTX 6000

**Meta:** score=363 · comments=148 · tier=1 · flair=Discussion · posted=2026-05-17 19:49Z
**Author:** u/Signal_Ad657
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tfzsd6/m5_vs_dgx_spark_vs_strix_halo_vs_rtx_6000/](https://www.reddit.com/r/LocalLLaMA/comments/1tfzsd6/m5_vs_dgx_spark_vs_strix_halo_vs_rtx_6000/)
**Link:** [https://i.redd.it/mk82wx765r1h1.jpeg](https://i.redd.it/mk82wx765r1h1.jpeg)

---

### I hope that someday we will have a 124B Gemma.

**Meta:** score=316 · comments=52 · tier=1 · flair=Funny · posted=2026-05-17 17:03Z
**Author:** u/cgs019283
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tfv8li/i_hope_that_someday_we_will_have_a_124b_gemma/](https://www.reddit.com/r/LocalLLaMA/comments/1tfv8li/i_hope_that_someday_we_will_have_a_124b_gemma/)
**Link:** [https://i.redd.it/t1qmld44bq1h1.png](https://i.redd.it/t1qmld44bq1h1.png)

---

### 85 GPU-hours comparing 5 abliteration methods on Qwen3.6-27B: benchmarks, safety, weight forensics - Abliterlitics

**Meta:** score=224 · comments=55 · tier=1 · flair=Resources · posted=2026-05-17 11:18Z
**Author:** u/nathandreamfast
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tfmocw/85_gpuhours_comparing_5_abliteration_methods_on/](https://www.reddit.com/r/LocalLLaMA/comments/1tfmocw/85_gpuhours_comparing_5_abliteration_methods_on/)

I've been building [Abliterlitics](https://github.com/dreamfast/abliterlitics), an open-source abliteration forensics toolkit. The idea is straightforward: take the same base model, compare the different abliteration techniques others have applied, then measure what actually changed using benchmarks, safety evaluation, distribution shift, and weight-level analysis. This post covers Qwen3.6-27B, comparing five abliteration variants against the base model. I recovered safetensors from HauhauCS's Q8_K_P GGUF, then ran 85 hours of benchmarks, HarmBench, KL divergence, and weight forensics across all six. Heretic and Huihui are the top two for capability preservation: Huihui has the smallest benchmark deltas, Heretic has the lowest KL divergence. All five abliterated models reach near-complete safety removal. AEON's "enhanced capabilities" claim is contradicted by the data. Abliterix has the worst capability preservation by far. Full report with all tables and charts: [HuggingFace model card](https://huggingface.co/DreamFast/Qwen3.6-27B-Uncensored-HauhauCS-Aggressive-Safetensor-Benchmark).

## The six models

| Name | Type |
|------|------|
| Base | [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) |
| Heretic | [llmfan46/Qwen3.6-27B-uncensored-heretic-v2](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2) |
| HauhauCS | [HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Aggressive) |
| Hu

[…truncated, see permalink]

---

### Testing llama.cpp MTP support on Qwen3.6 - RTX 5090

**Meta:** score=212 · comments=33 · tier=1 · flair=Discussion · posted=2026-05-17 06:00Z
**Author:** u/3VITAERC
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tfgxc8/testing_llamacpp_mtp_support_on_qwen36_rtx_5090/](https://www.reddit.com/r/LocalLLaMA/comments/1tfgxc8/testing_llamacpp_mtp_support_on_qwen36_rtx_5090/)
**Link:** [https://i.redd.it/etfdid7h0n1h1.png](https://i.redd.it/etfdid7h0n1h1.png)

---

### "Generate a photorealistic realtime render of a human face with webGL" (Qwen3.5-122B-A10B UD-Q3_K_XL)

**Meta:** score=152 · comments=52 · tier=1 · flair=Slop · posted=2026-05-17 21:36Z
**Author:** u/_TheWolfOfWalmart_
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tg2muq/generate_a_photorealistic_realtime_render_of_a/](https://www.reddit.com/r/LocalLLaMA/comments/1tg2muq/generate_a_photorealistic_realtime_render_of_a/)
**Link:** [https://i.redd.it/yz4ajeb9or1h1.png](https://i.redd.it/yz4ajeb9or1h1.png)

---

### llama: avoid copying logits during prompt decode in MTP by am17an · Pull Request #23198 · ggml-org/llama.cpp

**Meta:** score=135 · comments=49 · tier=1 · flair=News · posted=2026-05-17 15:42Z
**Author:** u/jacek2023
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tft1il/llama_avoid_copying_logits_during_prompt_decode/](https://www.reddit.com/r/LocalLLaMA/comments/1tft1il/llama_avoid_copying_logits_during_prompt_decode/)
**Link:** [https://github.com/ggml-org/llama.cpp/pull/23198](https://github.com/ggml-org/llama.cpp/pull/23198)

---

### Dual GPU llama.cpp speedup

**Meta:** score=114 · comments=47 · tier=1 · flair=Discussion · posted=2026-05-17 10:24Z
**Author:** u/Legitimate-Dog5690
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tflngz/dual_gpu_llamacpp_speedup/](https://www.reddit.com/r/LocalLLaMA/comments/1tflngz/dual_gpu_llamacpp_speedup/)

Llama.cpp has an issue with "--split-mode tensor", you'll get great results but it only supports non-quantized KV caches, for this very reason a lot of people decide to go with a healthy sized KV cache and ignore tensor parallelism.
&amp;nbsp;

I've had a stab at fixing the issue here - [https://github.com/RedToasty/llama.cpp_qts](https://github.com/RedToasty/llama.cpp_qts) \- it's branched from mainline as of today, with minimal changes.
&amp;nbsp;

I'm personally running a 3060 12gb + 4070 Super 12gb, for a combined 24gb.
&amp;nbsp;

Here's my results with Q8_0/Q8_0 and "-sm tensor":
&amp;nbsp;

**llama-bench.exe -m Qwen3.6-27B-Q4_K_M.gguf -sm tensor -fa 1 -ctk q8_0 -ctv q8_0 -p 128 -n 32 -b 128 -ub 128**
&amp;nbsp;

| Model                    | Size      | Params  | Backend | NGL | Batch | UBatch | Type K | Type V | SM     | FA | Test  | Tokens/s         |
|--------------------------|-----------:|---------:|---------|----:|------:|--------:|-------:|-------:|--------|---:|------|-----------------:|
| Qwen3.5 27B Q4_K Medium | 15.65 GiB | 26.90 B | CUDA   | 99  | 128   | 128     | q8_0   | q8_0   | tensor | 1  | pp128 | 544.82 ± 6.01 |
| Qwen3.5 27B Q4_K Medium | 15.65 GiB | 26.90 B | CUDA   | 99  | 128   | 128     | q8_0   | q8_0   | tensor | 1  | tg32  | 30.05 ± 0.38  |

Here's without tensor splitting:
&amp;nbsp;

**llama-bench.exe -m Qwen3.6-27B-Q4_K_M.gguf -fa 1 -ctk q8_0 -ctv q8_0 -p 128 -n 32 -b 128 -ub 128**
&amp;nbsp;

| Model                    | Size      | Param

[…truncated, see permalink]

---

### Jackrong/Qwopus3.5-9B-Coder-GGUF · Hugging Face

**Meta:** score=95 · comments=47 · tier=1 · flair=New Model · posted=2026-05-17 07:33Z
**Author:** u/pmttyji
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tfin40/jackrongqwopus359bcodergguf_hugging_face/](https://www.reddit.com/r/LocalLLaMA/comments/1tfin40/jackrongqwopus359bcodergguf_hugging_face/)
**Link:** [https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-GGUF)

---

### "Elias Thorne" is what eight different LLMs name a lighthouse keeper. He's also selling cancer treatment advice on Amazon

**Meta:** score=79 · comments=49 · tier=1 · flair=Discussion · posted=2026-05-17 04:03Z
**Author:** u/prescorn
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tfeo3k/elias_thorne_is_what_eight_different_llms_name_a/](https://www.reddit.com/r/LocalLLaMA/comments/1tfeo3k/elias_thorne_is_what_eight_different_llms_name_a/)
**Link:** [https://danielmay.co.uk/posts/cheap-agents-alumni-shirts-and-elias-thorne/](https://danielmay.co.uk/posts/cheap-agents-alumni-shirts-and-elias-thorne/)

---

### The power of structured workflows and small local models

**Meta:** score=75 · comments=24 · tier=1 · flair=Discussion · posted=2026-05-17 15:51Z
**Author:** u/DeltaSqueezer
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tftaaa/the_power_of_structured_workflows_and_small_local/](https://www.reddit.com/r/LocalLLaMA/comments/1tftaaa/the_power_of_structured_workflows_and_small_local/)
**Link:** [https://www.reddit.com/gallery/1tftaaa](https://www.reddit.com/gallery/1tftaaa)

---

### Deepseek V4's 1M context window: the breaking point

**Meta:** score=55 · comments=35 · tier=1 · flair=Discussion · posted=2026-05-17 06:35Z
**Author:** u/TangeloOk9486
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tfhl0q/deepseek_v4s_1m_context_window_the_breaking_point/](https://www.reddit.com/r/LocalLLaMA/comments/1tfhl0q/deepseek_v4s_1m_context_window_the_breaking_point/)

Just ran to verify deepseek v4's context claim of 1M and ran it across three production codebases like 45k (microservice), 180k (monorepo backend) and 520k(full stack app). For the observation, tasks included dependency tracing, cross file refractors and bug isolation to see where recall keeps up

**under 150k**

Got a solid performance like at 45k tokens, function calls traced across 8 files maintain accurate path reconstruction. At 180k, multi file refractors spanning 14 files show consistent architectural understand and no contradictions or context loss patterns

**past 300k**

precision quality degrades here. asked for exact line numbers from functions defined 400k tokens earlier, responses give "around line 230" instead of the actual 247. at 520k outputs shift to architectural summaries that skip implementation details, thats a problem if edge cases are a concern

**the latency gap**

Time to first token measures around 1.19s on deepinfra fp4 endpoint. Time to first answer in max reasoning mode stretches to around 120 seconds since the model completes internal chain of thought before producing visible output, which is really crticial for interative workflows to account for

provider benchmarks show 94% hallucination rate on unknown asnwer tasks (aa-omniscience) but v4 generates confident responses without even actual info. Shows up as references to nonexistent utility functions or phantom dependencies

on unknown answer tasks v4 generates confident responses without actu

[…truncated, see permalink]

---
