# r/LocalLLaMA | 2026-05-14 IST | sort=top
> Scraped 2026-05-14 09:18 IST | lookback=24h | tier_default=1
> Inference, quantization (GGUF/AWQ/EXL2), KV cache tricks, llama.cpp internals, kernel tuning, GPU rigs. Single highest-signal sub for Tier 1 efficiency.

### TextGen is now a native desktop app. Open-source alternative to LM Studio (formerly text-generation-webui).

**Meta:** score=541 · comments=168 · tier=1 · flair=Resources · posted=2026-05-13 13:00Z
**Author:** u/oobabooga4
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tbyyee/textgen_is_now_a_native_desktop_app_opensource/](https://www.reddit.com/r/LocalLLaMA/comments/1tbyyee/textgen_is_now_a_native_desktop_app_opensource/)

Hi all,

I have been making a lot of updates to my project, and I wanted to share them here.

TextGen (previously text-generation-webui, also known as my username oobabooga or ooba) has been in development since December 2022, before LLaMa and llama.cpp existed.

In the last two months, the project has evolved from a web UI to a **no-install desktop app** for Windows, Linux, and macOS with a polished UI. I have created a very minimal and elegant Electron integration for that. (Did you know LM Studio is also a web UI running over Electron? Not sure many people know that.)

https://preview.redd.it/tk8oibhgjw0h1.png?width=1686&amp;format=png&amp;auto=webp&amp;s=95c70f769766466885c8fdc6e7211525a371a920

It works like this:

1. You download a *portable build* from the [releases page](https://github.com/oobabooga/textgen/releases)
2. Unzip it
3. Double-click textgen
4. A window appears

There is no installation, and no files are ever created outside the extracted folder. It's fully self-contained. All your chat histories and settings are stored in a `user_data` folder shipped with the build.

There are builds for CUDA, Vulkan, CPU-only, Mac (Apple Silicon and Intel), and ROCm.

Some differentiating features:

* Full privacy. Unlike LM Studio, it doesn't phone home on every launch with your OS, CPU architecture, app version, and inference backend choices. Zero outbound requests.
* ik\_llama.cpp builds (LM Studio and Ollama only ship vanilla llama.cpp). ik\_llama.cpp has new quant ty

[…truncated, see permalink]

---

### Web-Search is coming to a screeching performance halt as Google shuts down their free search index, and traffic defenders like Cloudflare challenge AI at every gateway. What are our options?

**Meta:** score=173 · comments=132 · tier=1 · flair=Resources · posted=2026-05-13 19:35Z
**Author:** u/NetTechMan
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tcaboi/websearch_is_coming_to_a_screeching_performance/](https://www.reddit.com/r/LocalLLaMA/comments/1tcaboi/websearch_is_coming_to_a_screeching_performance/)

Google is closing its free tier to just 50 domains for site-specific search, and an inheritance date of January 1st, 2027, with no public pricing being listed for advanced searches. Cloudflare's new site-default is to challenge all AI bots attempting to scrape web-information for all their customers, including now with a recent partnership all domains hosted by Go-Daddy.

  
Some of you may have felt it over the last few months, web searches that used to be more effective are now closing with 400 errors from every site your harness attempts to reach. Local models may lose efficacy as their internet pulling capabilities are crushed.

  
Make no mistake, **Google** is reinforcing their mote by pulling up the drawbridge for aggressive pricing. This is a direct attempt to close in on the open-host sphere by crippling reliance infrastructure.

  
As a community, what options do we have at our disposal? Are there any open-projects currently attacking this status quo? Filling this gap will likely be the next big "open" project to hit the market, as solutions to this issue will likely become dependencies as we progress down harness improvement.

---

### DramaBox - Most Expressive Voice model ever based on LTX 2.3

**Meta:** score=157 · comments=60 · tier=1 · flair=New Model · posted=2026-05-13 17:06Z
**Author:** u/manmaynakhashi
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tc5wx1/dramabox_most_expressive_voice_model_ever_based/](https://www.reddit.com/r/LocalLLaMA/comments/1tc5wx1/dramabox_most_expressive_voice_model_ever_based/)
**Link:** [https://v.redd.it/5zdi52w4rx0h1](https://v.redd.it/5zdi52w4rx0h1)

---

### MI50s Qwen 3.6 27B @52.8 tps TG @1569 tps PP (no MTP, no Quant)

**Meta:** score=125 · comments=55 · tier=1 · flair=Resources · posted=2026-05-13 19:08Z
**Author:** u/ai-infos
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tc9j6u/mi50s_qwen_36_27b_528_tps_tg_1569_tps_pp_no_mtp/](https://www.reddit.com/r/LocalLLaMA/comments/1tc9j6u/mi50s_qwen_36_27b_528_tps_tg_1569_tps_pp_no_mtp/)
**Link:** [https://i.redd.it/qddw1tgccy0h1.png](https://i.redd.it/qddw1tgccy0h1.png)

---

### AIDC-AI/Ovis2.6-80B-A3B · Hugging Face

**Meta:** score=118 · comments=28 · tier=1 · flair=New Model · posted=2026-05-13 12:29Z
**Author:** u/pmttyji
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tby79g/aidcaiovis2680ba3b_hugging_face/](https://www.reddit.com/r/LocalLLaMA/comments/1tby79g/aidcaiovis2680ba3b_hugging_face/)
**Link:** [https://huggingface.co/AIDC-AI/Ovis2.6-80B-A3B](https://huggingface.co/AIDC-AI/Ovis2.6-80B-A3B)

---

### we really all are going to make it, aren't we? 2x3090 setup.

**Meta:** score=73 · comments=39 · tier=1 · flair=Discussion · posted=2026-05-13 22:25Z
**Author:** u/RedShiftedTime
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tcf2dt/we_really_all_are_going_to_make_it_arent_we/](https://www.reddit.com/r/LocalLLaMA/comments/1tcf2dt/we_really_all_are_going_to_make_it_arent_we/)

i'm blown away.  i saw someone made a post the other day about "club-3090" and after having sonnet patch some fixes into it, specifically a sse-session drop bug and a bug with tool-calling, it's fair to say that even "budget" setups like myself will have a path forward soon for only-local-ai.

reference github: https://github.com/noonghunna/club-3090 (not mine)

after getting this running, i was originally using WSL2.  fair to say, it was "better" than LM studio but not quite good. t/s was like 30 and pp was around 400....i said fuck it and installed ubuntu as dual boot on the same machien (i'm just not very linux friendly when it's headless, prefer windows RDP) and wow.  i'm getting like 4000 pp/s and 113 tk/s with no nvlink.  supposedly, nvlink would make it faster.....

either way, i'm very excited about this new local future.  qwen 3.6 27b with 262k on 48 GB VRAM feels almost-sonnet level, and it's MUCH faster than cloud.  and useful!  I had it make some monkey patches and they work fantastic, and well as some relatively useful code reviews.  im working now on making it work to handle my ssh sessions on my linux computers now.

wondering what the next upgrade path could be.  i was thinking about m5 ultra 512 GB + 4x DGX Sparks (prompt processing speeeeed) but now I'm wondering if we'll reach frontier class intelligence (maybe only domain specific) in smaller models in the next 12 months?

awesome!

---

### llama.cpp docker images to run MTP models

**Meta:** score=67 · comments=19 · tier=1 · flair=Resources · posted=2026-05-13 14:20Z
**Author:** u/havenoammo
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tc132c/llamacpp_docker_images_to_run_mtp_models/](https://www.reddit.com/r/LocalLLaMA/comments/1tc132c/llamacpp_docker_images_to_run_mtp_models/)

This is follow up from previous post: https://www.reddit.com/r/LocalLLaMA/comments/1t5ageq/

There have been many improvements to the MTP pull request and the llama.cpp main branch, such as image support and various bug fixes. I recently made a new build for my local machine, but keeping guides up to date is an issue, so I built Docker images to make running them easier. If you are already using llama.cpp Docker images, it would be straightforward to switch over until official builds support MTP.

Here, pick your flavour:

```
havenoammo/llama:cuda13-server
havenoammo/llama:cuda12-server
havenoammo/llama:vulkan-server
havenoammo/llama:intel-server
havenoammo/llama:rocm-server
```

I have not been able to test all of them, as I only run cuda13 for now. Feel free to give it a test and see if it works for your hardware.

Also, Unsloth released MTP models for Qwen 3.6, which makes my previous grafted models obsolete. You can find them here if you missed them:
* Unsloth
  * https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF
  * https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF
* Unsloth UD + Q8 Grafted MTP
  * https://huggingface.co/havenoammo/Qwen3.6-35B-A3B-MTP-GGUF
  * https://huggingface.co/havenoammo/Qwen3.6-27B-MTP-UD-GGUF


They do quantize MTP layers at lower quantization levels. I kept mine at Q8 quantization for improved prediction. It is possible that higher quantization for MTP layers makes them more precise, giving you more speed at the cost of more VRAM usage.

[…truncated, see permalink]

---

### 24+ tok/s from ~30B MoE models on an old GTX 1080 (8 GB VRAM, 128k context)

**Meta:** score=63 · comments=18 · tier=1 · flair=Tutorial | Guide · posted=2026-05-13 20:41Z
**Author:** u/mdda
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tcc7h5/24_toks_from_30b_moe_models_on_an_old_gtx_1080_8/](https://www.reddit.com/r/LocalLLaMA/comments/1tcc7h5/24_toks_from_30b_moe_models_on_an_old_gtx_1080_8/)

I got **Qwen 3.6 35B-A3B** and **Gemma 4 26B-A4B** running on a $200 secondhand machine (i7-6700 / GTX 1080 / 32 GB RAM) using llama.cpp (the TurboQuant/RotorQuant KV cache quantisation allows 128k context within the 8 GB VRAM).

**Results (Q4\_K\_M models, 128k context):**

|Model|tok/s|Key flags|
|:-|:-|:-|
|Qwen 3.6 35B-A3B|\~24| \--n-cpu-moe 30, K=turbo4 V=turbo3|
|Gemma 4 26B-A4B (no MTP) |\~20|\--n-cpu-moe 20, K=V=turbo3, --flash-attn|
|Gemma 4 26B-A4B + MTP (naive)|\~21|embedding table silently on CPU|
|Gemma 4 26B-A4B + MTP (fixed)|\~24.5|\--override-tensor-draft "token\_embd\\.weight=CUDA0"|

The trick is MoE offloading: llama.cpp can park the cold expert weights in system RAM, and stream over PCIe to the GPU, while keeping hot layers + KV cache on GPU. The system is fully PCIe bandwidth-limited (GPU sits at \~40-50% utilisation while PCIe 3.0 x16 is maxed out).

**Biggest finding:** Gemma 4's MTP speculative decoding barely helps out of the box (\~5% gain). Turns out llama.cpp unconditionally keeps the token embedding table on CPU. Normally that's fine (just a `get_rows` lookup), but Gemma 4's MTP assistant has a tied LM head - so every draft token does a full 262k×1024 matmul across PCIe.  Forcing it onto GPU with `--override-tensor-draft` gives the real \~22% speedup and \~79% draft acceptance rate.

**Setup pain points (Fedora 42 + Pascal GPU):**

* Pin akmod-nvidia to 580xx branch (Pascal is going legacy)
* Force gcc-14 for CUDA 12.9 (newer gcc rejected)
* Patch

[…truncated, see permalink]

---

### sensenova/SenseNova-U1-A3B-MoT · Hugging Face

**Meta:** score=53 · comments=3 · tier=1 · flair=New Model · posted=2026-05-13 16:08Z
**Author:** u/pmttyji
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tc47q0/sensenovasensenovau1a3bmot_hugging_face/](https://www.reddit.com/r/LocalLLaMA/comments/1tc47q0/sensenovasensenovau1a3bmot_hugging_face/)
**Link:** [https://huggingface.co/sensenova/SenseNova-U1-A3B-MoT](https://huggingface.co/sensenova/SenseNova-U1-A3B-MoT)

---

### server, webui: support continue generation on reasoning models by ServeurpersoCom · Pull Request #22727 · ggml-org/llama.cpp

**Meta:** score=51 · comments=4 · tier=1 · flair=News · posted=2026-05-13 10:10Z
**Author:** u/jacek2023
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tbv9zg/server_webui_support_continue_generation_on/](https://www.reddit.com/r/LocalLLaMA/comments/1tbv9zg/server_webui_support_continue_generation_on/)
**Link:** [https://github.com/ggml-org/llama.cpp/pull/22727](https://github.com/ggml-org/llama.cpp/pull/22727)

---
