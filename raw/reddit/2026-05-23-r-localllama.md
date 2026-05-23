# r/LocalLLaMA | 2026-05-23 IST | sort=top
> Scraped 2026-05-23 10:54 IST | lookback=24h | tier_default=1
> Inference, quantization (GGUF/AWQ/EXL2), KV cache tricks, llama.cpp internals, kernel tuning, GPU rigs. Single highest-signal sub for Tier 1 efficiency.

### DeepSeek is pushing forward with $10.29 billion financing round, with Liang Wenfeng committing to continue developing open-source AI models rather than pursuing short-term commercialization goals

**Meta:** score=587 · comments=111 · tier=1 · flair=News · posted=2026-05-22 11:14Z
**Author:** u/External_Mood4719
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tkfvvj/deepseek_is_pushing_forward_with_1029_billion/](https://www.reddit.com/r/LocalLLaMA/comments/1tkfvvj/deepseek_is_pushing_forward_with_1029_billion/)

[https://www.bloomberg.com/news/articles/2026-05-22/deepseek-founder-declares-agi-goal-as-10-billion-round-advances](https://www.bloomberg.com/news/articles/2026-05-22/deepseek-founder-declares-agi-goal-as-10-billion-round-advances)

---

### NVIDIA Removes Gaming Revenue Category From Financial Reports

**Meta:** score=436 · comments=157 · tier=1 · flair=News · posted=2026-05-22 21:13Z
**Author:** u/HumanDrone8721
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tkw5ri/nvidia_removes_gaming_revenue_category_from/](https://www.reddit.com/r/LocalLLaMA/comments/1tkw5ri/nvidia_removes_gaming_revenue_category_from/)
**Link:** [https://www.guru3d.com/story/nvidia-removes-gaming-revenue-category-from-financial-reports/](https://www.guru3d.com/story/nvidia-removes-gaming-revenue-category-from-financial-reports/)

---

### BeeLlama v0.2.0 – major DFlash update. Single RTX 3090: Qwen 3.6 27B up to 164 tps (4.40x), Gemma 4 31B up to 177.8 tps (4.93x). Prompt processing speed near baseline.

**Meta:** score=159 · comments=98 · tier=1 · flair=Resources · posted=2026-05-22 17:34Z
**Author:** u/Anbeeld
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tkpz2y/beellama_v020_major_dflash_update_single_rtx_3090/](https://www.reddit.com/r/LocalLLaMA/comments/1tkpz2y/beellama_v020_major_dflash_update_single_rtx_3090/)

**BeeLlama v0.2.0 is here!**

&gt;Not quite a pegasus, but close enough.

[**GitHub**](https://github.com/Anbeeld/beellama.cpp) **|** [**Qwen 3.6 27B Quick Start**](https://github.com/Anbeeld/beellama.cpp/blob/main/docs/quickstart-qwen36-dflash.md) **|** [**Gemma 4 31B Quick Start**](https://github.com/Anbeeld/beellama.cpp/blob/main/docs/quickstart-gemma-4-31b-dflash.md)

* Full Gemma 4 31B support with efficient DFlash implementation and vision.
* Major Qwen 3.6 27B performance update from lower DFlash overhead, cleaner prefill handling, drafter K/V projection caching, and safer CUDA execution.
* DFlash GGUFs with upstream architecture are now supported.
* Fixes to adaptive profit behavior around baseline probing.
* Reduced verifier path is stricter now, with safer fallback to full logits when grammar, sampler state, or reasoning requires it.
* Reasoning and tool-call boundaries were tightened.
* Stricter draft/target validation and better draft-model discovery.
* ...and many more improvements!

**Benchmarks**

* Setup: Windows 11, AMD Ryzen 7 5700X3D, 32 GB DDR4 RAM, RTX 3090 24 GB
* Config: same as in quick start docs, but with reasoning off for non-chat prompts
* Baseline and MTP server in comparison: llama.cpp [b9275](https://github.com/ggml-org/llama.cpp/releases/tag/b9275) CUDA 13.1 Windows prebuilt
* The full text of the benchmark prompts is in [README.md on GitHub](https://github.com/Anbeeld/beellama.cpp/blob/main/README.md#dflash-speedup)

**Qwen 3.6 27B**

Target m

[…truncated, see permalink]

---

### [NEW] Supra-50M Released!

**Meta:** score=91 · comments=37 · tier=1 · flair=New Model · posted=2026-05-22 12:34Z
**Author:** u/Dangerous_Try3619
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tkhngq/new_supra50m_released/](https://www.reddit.com/r/LocalLLaMA/comments/1tkhngq/new_supra50m_released/)

https://preview.redd.it/kx39ammxno2h1.jpg?width=1080&amp;format=pjpg&amp;auto=webp&amp;s=d1a2d5b27920a5b61a50547a6e70a6378445cae4

# SupraLabs released a new model! - Supra-50M

**Supra-50M** is a compact 50M-parameter causal language model (BASE and INSTRUCT versions) built from scratch by SupraLabs using a Llama-style architecture, trained on 20 billion tokens of high-quality educational web text. Despite being significantly smaller than comparable open models, it achieves competitive or superior results on several key benchmarks. This is our first **SupraLabs Scaling Up Plan** model.

🤗 [Supra-50M-Base](https://huggingface.co/SupraLabs/Supra-50M-Base) | [Supra-50M-Instruct](https://huggingface.co/SupraLabs/Supra-50M-Instruct)

# What comes next?

* **Supra-124M** — Base, Chat, Experimental Reasoning
* **Supra-350M** — Base, Chat, Reasoning, Coding

# 🏆 Benchmarks

|Benchmark|Supra-50M *(ours)*|GPT-2 (124M)|SmolLM-135M|OpenELM-270M|
|:-|:-|:-|:-|:-|
|**Parameters**|**50M**|124M *(2.5×)*|135M *(2.7×)*|270M *(5.4×)*|
|**BLiMP** (linguistics)|**76.3%**|63.0%|69.8%|N/A|
|**SciQ** (science)|77.2%|53.2%|73.4%|**84.70%**|
|**ARC-Easy** (knowledge)|52.2%|42.0%|49.2%|**45.08%**|
|**PIQA** (logic)|62.2%|63.0%|67.3%|**69.75%**|
|**HellaSwag** (context)|31.8%|29.5%|42.0%|**46.71%**|

# 🧠 Architecture &amp; Hyperparameters

|Hyperparameter|Value|
|:-|:-|
|Architecture|Llama (decoder-only transformer)|
|Parameters|\~50M|
|Vocab size|32,000|
|Hidden size|512|
|Intermediate size|1,408|
|Hi

[…truncated, see permalink]

---

### OpenBMB presents the model BitCPM-CANN 1.58 bit

**Meta:** score=86 · comments=19 · tier=1 · flair=New Model · posted=2026-05-22 13:55Z
**Author:** u/Illustrious-Swim9663
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tkjpsh/openbmb_presents_the_model_bitcpmcann_158_bit/](https://www.reddit.com/r/LocalLLaMA/comments/1tkjpsh/openbmb_presents_the_model_bitcpmcann_158_bit/)
**Link:** [https://www.reddit.com/gallery/1tkjpsh](https://www.reddit.com/gallery/1tkjpsh)

---

### Can't believe I got it working!  Dual GPU - 48gb VRAM llama-cpp server - R7900 + 7800XT

**Meta:** score=83 · comments=55 · tier=1 · flair=Discussion · posted=2026-05-22 19:52Z
**Author:** u/Jorlen
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tktxr0/cant_believe_i_got_it_working_dual_gpu_48gb_vram/](https://www.reddit.com/r/LocalLLaMA/comments/1tktxr0/cant_believe_i_got_it_working_dual_gpu_48gb_vram/)
**Link:** [https://i.redd.it/ii1w278ttq2h1.png](https://i.redd.it/ii1w278ttq2h1.png)

---

### ByteShape Qwen3.6-35B-A3B: 30% faster than Unsloth IQ on 6GB VRAM laptop

**Meta:** score=76 · comments=43 · tier=1 · flair=Discussion · posted=2026-05-22 16:10Z
**Author:** u/OsmanthusBloom
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tknjcx/byteshape_qwen3635ba3b_30_faster_than_unsloth_iq/](https://www.reddit.com/r/LocalLLaMA/comments/1tknjcx/byteshape_qwen3635ba3b_30_faster_than_unsloth_iq/)

A few days ago I posted about my experiments with MTP on a 6GB VRAM laptop. That didn't work so well; CPU offload hurts MTP performance badly. But now I've tried out the [new ByteShape quants](https://byteshape.com/blogs/Qwen3.6-35B-A3B/) for Qwen3.6-35B-A3B that are claimed to be both smaller and faster than others while still having excellent quality. I decided to compare my previous best Unsloth UD-IQ4\_XS setup head-to-head with the ByteShape "CPU-5" quant in terms of performance.

**TL;DR: ByteShape quant is 30% faster on TG but slightly slower on PP than the similarly sized Unsloth quant when partially offloaded to CPU on a 6GB VRAM laptop.**

# Hardware

* Asus ROG Zephyrus G14 laptop, 2021 model
* AMD Ryzen 7 5800HS with Radeon Graphics (8 CPU cores / 16 threads)
* NVIDIA RTX 3060 Laptop GPU, 6GB VRAM
* 24GB RAM (DDR4 3200 MT/s), 1TB SSD

# Software

* Linux Mint 22.2 (based on Ubuntu 24.04) with the Cinnamon desktop running on the Radeon iGPU (thus the 3060 was dedicated to llama.cpp only)
* llama.cpp version: 9203 (87589042c) built from current master branch with GNU 13.3.0 for Linux x86\_64
* CUDA 12.0 installed from Ubuntu repositories

# Test setup

I fixed the following for all the experiments:

* context size 65536 (enough to do agentic coding on e.g. Pi or Dirac, or run Hermes Agent)
* mmap off, mlock on, ubatch size 2048 (gives much better PP speed than the default 512)
* no mmproj (no image input support needed for now)
* for more details, see configuration 

[…truncated, see permalink]

---

### G4-MeroMero-26B-A4B-it-uncensored-heretic Is Out Now, a Finetune of gemma-4-26B-A4B-it, With KLD of 0.0152 and 12/100 Refusals!

**Meta:** score=60 · comments=10 · tier=1 · flair=New Model · posted=2026-05-23 01:10Z
**Author:** u/LLMFan46
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tl1wpd/g4meromero26ba4bituncensoredheretic_is_out_now_a/](https://www.reddit.com/r/LocalLLaMA/comments/1tl1wpd/g4meromero26ba4bituncensoredheretic_is_out_now_a/)
**Link:** [https://huggingface.co/llmfan46/G4-MeroMero-26B-A4B-it-uncensored-heretic-GGUF](https://huggingface.co/llmfan46/G4-MeroMero-26B-A4B-it-uncensored-heretic-GGUF)

---

### Qwen-27B-IQ4_KS for ik_llama.cpp, especially for NVIDIA with 16GB VRAM

**Meta:** score=59 · comments=28 · tier=1 · flair=Discussion · posted=2026-05-22 15:32Z
**Author:** u/Pablo_the_brave
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tkmgwj/qwen27biq4_ks_for_ik_llamacpp_especially_for/](https://www.reddit.com/r/LocalLLaMA/comments/1tkmgwj/qwen27biq4_ks_for_ik_llamacpp_especially_for/)

Hi everyone,

I'm presenting a new quantization of the Qwen-27B model, created specifically with 16GB VRAM NVIDIA GPUs in mind. I used quants that, unfortunately, are not yet available in the main upstream `llama.cpp`. I'm talking about the KS and KSS quants developed by ikawrakow. After many trials, I managed to create a 14.1GB model which, in my testing, delivers results highly comparable to my previous 14.7GB IQ4_XS quantization.

**Model Link:** [cHunter789/Qwen3.6-27B-i1-IQ4_KS-GGUF](https://huggingface.co/cHunter789/Qwen3.6-27B-i1-IQ4_KS-GGUF)

**ik_llama.cpp Project:** [ikawrakow/ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)

Unfortunately, the `ik_llama.cpp` project required to run this model is **NVIDIA CUDA and CPU only**. There is currently no way to run this on AMD or Apple Silicon (Metal) :/

Using this model with `ik_llama.cpp` and a `Q4_0` Hadamard KV cache allows for a **105k context window**.

### Benchmark Results &amp; Real-World Impressions
The model was heavily tested in daily production workflows for several days. It runs much faster (1.5x-1.75x) and more reliably than the previous iteration—completely eliminating the issue of "blank outputs", while the search-replace functionality works flawlessly.

* **Qwen Benchmark:** Successfully passed the performance evaluations on [qwen3-6-27b-benchmark.vercel.app](https://qwen3-6-27b-benchmark.vercel.app).
* **Needle In A Haystack:** Successfully evaluated with satisfying results across the full 100k 

[…truncated, see permalink]

---
