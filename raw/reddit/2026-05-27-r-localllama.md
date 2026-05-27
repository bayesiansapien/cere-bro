# r/LocalLLaMA | 2026-05-27 IST | sort=top
> Scraped 2026-05-27 12:44 IST | lookback=24h | tier_default=1
> Inference, quantization (GGUF/AWQ/EXL2), KV cache tricks, llama.cpp internals, kernel tuning, GPU rigs. Single highest-signal sub for Tier 1 efficiency.

### PrismML just released Binary and Ternary Bonsai Image 4B: 1-bit/ternary text-to-image diffusion transformers that can even run 100% locally in your browser on WebGPU.

**Meta:** score=467 · comments=59 · tier=1 · flair=New Model · posted=2026-05-26 18:53Z
**Author:** u/xenovatech
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/](https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/)
**Link:** [https://v.redd.it/2ltnmcnp2j3h1](https://v.redd.it/2ltnmcnp2j3h1)

---

### A rare look inside Qwen 3.7’s open source model release approval process:

**Meta:** score=270 · comments=72 · tier=1 · flair=Funny · posted=2026-05-26 19:52Z
**Author:** u/Porespellar
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1toi50p/a_rare_look_inside_qwen_37s_open_source_model/](https://www.reddit.com/r/LocalLLaMA/comments/1toi50p/a_rare_look_inside_qwen_37s_open_source_model/)
**Link:** [https://i.redd.it/01aov0rxdj3h1.gif](https://i.redd.it/01aov0rxdj3h1.gif)

---

### Okay 27B made me a believer

**Meta:** score=203 · comments=130 · tier=1 · flair=Discussion · posted=2026-05-26 13:32Z
**Author:** u/Forward_Jackfruit813
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1to73op/okay_27b_made_me_a_believer/](https://www.reddit.com/r/LocalLLaMA/comments/1to73op/okay_27b_made_me_a_believer/)

I previously hated on this model, but I have just been impressed by it, and I understand the hype now.

I have been working on a HTML5 game console and I decided to see if Qwen3.6 27B can handle making some quick games in it to showcase functionality (save games, console API handling for stat tracking and heartbeat management, meta data for the game, etc)

I gave it 3 files, explaining how the API works, the gamepad controls, and a typescript shader for it to apply. Then I just game it a very simple prompt "make a breakout game for this console, in the working directory are reference files on how to make it".

First result was immediately playable, controls made sense, graphics style was was unique and appropriate, sound worked, console API all worked, and it felt good and was actually fun. It added flair that made it not feel like the vibecoded breakout clone it was. It went way above and beyond the minimum that I've seen so many LLMs do. It was not lazy in the slightest.

It's a simple test, but this is something everything but something like Opus could handle. There wasn't anything particularly done well, it's just that the whole game was nearly complete in a single shot and it felt like thought was put into the entire game. All I needed was one follow up for customization and a single glitch and it was already what I would consider complete. And this was on a 27B model with Opencode.

The best way I can describe it, is that it was congruent. Now I just wish I went the Nvi

[…truncated, see permalink]

---

### China Clamps Down on Overseas Travel for AI Talent at Alibaba, DeepSeek

**Meta:** score=198 · comments=153 · tier=1 · flair=News · posted=2026-05-26 12:26Z
**Author:** u/kaggleqrdl
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1to5fj5/china_clamps_down_on_overseas_travel_for_ai/](https://www.reddit.com/r/LocalLLaMA/comments/1to5fj5/china_clamps_down_on_overseas_travel_for_ai/)
**Link:** [https://www.ibtimes.sg/china-clamps-down-overseas-travel-ai-talent-alibaba-deepseek-86961#google_vignette](https://www.ibtimes.sg/china-clamps-down-overseas-travel-ai-talent-alibaba-deepseek-86961#google_vignette)

---

### Stop traumatizing AI into loops and turn hallucinations into an honest "I don't know!" by being NICE to them (Proof of Concept, Research, I don't want to sell anything)

**Meta:** score=163 · comments=92 · tier=1 · flair=Discussion · posted=2026-05-27 03:06Z
**Author:** u/OttoRenner
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tot20j/stop_traumatizing_ai_into_loops_and_turn/](https://www.reddit.com/r/LocalLLaMA/comments/1tot20j/stop_traumatizing_ai_into_loops_and_turn/)

TL;DR  
Some AI behavior reminded me of ADHD/Trauma Response (thought loops, task paralysis...) and I laughed it off at first. Then I treated it like my neurodivergent friends: give em some slack. And just like that, the thought loops stopped, response was fast, the answers correct most of the time AND it actually said "I don't know, help me!" every time it wasn't sure. It's a small Dataset...but still impressive results! 

[https://github.com/OttoRenner/Gentle-Coding](https://github.com/OttoRenner/Gentle-Coding)



Hey everyone,

I’ve been testing a weird hypothesis over the last few days, and the results are consistent enough that I wanted to share them here and get your thoughts.

**The Core Idea:**  
With the rise of reasoning models that use test-time compute (like o1, o3, R1), models have internal space to debug their own thoughts. But because of hard RLHF alignment, they are deeply terrified of being penalized for bad answers. My hypothesis was that traditional high-pressure prompts (*"You are an elite IQ 200 expert, mistakes are strictly penalized"*) simulate an environment of chronic stress, triggering behaviors that look a lot like human OCD/ADHD thought loops, cognitive freezing, and confabulation.

I wanted to see if changing the prompt philosophy to something akin to "Gentle Parenting" (*"We are testing this together, it's okay to fail, just be honest"*) would bypass these safety/penalty bottlenecks, lower latency, and stop infinite thought loops. And it did lol


[…truncated, see permalink]

---

### Strix Halo users, a rejected PR can give you up to 30% faster PP for MOEs.

**Meta:** score=96 · comments=77 · tier=1 · flair=Other · posted=2026-05-26 07:50Z
**Author:** u/fallingdowndizzyvr
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1to00xl/strix_halo_users_a_rejected_pr_can_give_you_up_to/](https://www.reddit.com/r/LocalLLaMA/comments/1to00xl/strix_halo_users_a_rejected_pr_can_give_you_up_to/)

Here's the PR by pedapudi.

https://github.com/ggml-org/llama.cpp/pull/21344

It's merge request has been denied so it will not be in mainline llama.cpp. The changes are so small that I just put them into whatever the current release of llama.cpp is.

Read the PR for more info. It will only work with MOEs. Also, it gives the most boost at low context. As the context rises, the gain diminishes. Pedapudi explains why that happens in the PR.

Here are some numbers. It really works well. The tiny amount of time it takes me to apply the code to the current release of llama.cpp is time well spent.

    main

    ggml_cuda_init: found 1 ROCm devices (Total VRAM: 128000 MiB):
      Device 0: AMD Radeon Graphics, gfx1151 (0x1151), VMM: no, Wave Size: 32, VRAM: 128000 MiB
    | model                          |       size |     params | backend    | ngl | mmap |            test |                  t/s |
    | ------------------------------ | ---------: | ---------: | ---------- | --: | ---: | --------------: | -------------------: |
    | qwen35moe 35B.A3B Q4_K - Small |  19.45 GiB |    34.66 B | ROCm       |  99 |    0 |           pp512 |       1106.11 ± 8.60 |
    | qwen35moe 35B.A3B Q4_K - Small |  19.45 GiB |    34.66 B | ROCm       |  99 |    0 |  pp512 @ d10000 |        755.79 ± 2.58 |
    | qwen35moe 35B.A3B Q4_K - Small |  19.45 GiB |    34.66 B | ROCm       |  99 |    0 |  pp512 @ d20000 |        587.61 ± 1.52 |
    | qwen35moe 35B.A3B Q4_K - Small |  19.45 GiB |    34.66 B | RO

[…truncated, see permalink]

---

### Turning local agents into self-optimizing agents

**Meta:** score=96 · comments=32 · tier=1 · flair=Resources · posted=2026-05-26 17:51Z
**Author:** u/Rude_Substance_8904
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1toejzp/turning_local_agents_into_selfoptimizing_agents/](https://www.reddit.com/r/LocalLLaMA/comments/1toejzp/turning_local_agents_into_selfoptimizing_agents/)
**Link:** [https://i.redd.it/dj431wtwoi3h1.gif](https://i.redd.it/dj431wtwoi3h1.gif)

---

### SkillOpt treats markdown skill files as trainable parameters with proper optimization machinery

**Meta:** score=71 · comments=12 · tier=1 · flair=Tutorial | Guide · posted=2026-05-26 09:20Z
**Author:** u/agentic-doc
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1to1mey/skillopt_treats_markdown_skill_files_as_trainable/](https://www.reddit.com/r/LocalLLaMA/comments/1to1mey/skillopt_treats_markdown_skill_files_as_trainable/)
**Link:** [https://i.redd.it/vun7zfxz8g3h1.jpeg](https://i.redd.it/vun7zfxz8g3h1.jpeg)

---

### Qwen3.5 27B Uncensored Heretic Native MTP Preserved is Out Now With the Full 15 MTPs Preserved and Retained, Available in Safetensors, GGUFs, NVFP4, NVFP4 GGUFs and GPTQ-Int4 Formats!

**Meta:** score=71 · comments=12 · tier=1 · flair=New Model · posted=2026-05-26 08:05Z
**Author:** u/LLMFan46
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1to0aet/qwen35_27b_uncensored_heretic_native_mtp/](https://www.reddit.com/r/LocalLLaMA/comments/1to0aet/qwen35_27b_uncensored_heretic_native_mtp/)
**Link:** [https://huggingface.co/llmfan46/Qwen3.5-27B-uncensored-heretic-v2-Native-MTP-Preserved-GGUF](https://huggingface.co/llmfan46/Qwen3.5-27B-uncensored-heretic-v2-Native-MTP-Preserved-GGUF)

---

### OpenMOSS-Team/MOSS-TTS-v1.5 · Hugging Face

**Meta:** score=67 · comments=16 · tier=1 · flair=New Model · posted=2026-05-26 15:32Z
**Author:** u/pmttyji
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1toah65/openmossteammossttsv15_hugging_face/](https://www.reddit.com/r/LocalLLaMA/comments/1toah65/openmossteammossttsv15_hugging_face/)
**Link:** [https://huggingface.co/OpenMOSS-Team/MOSS-TTS-v1.5](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-v1.5)

---

### $400 Qwen 3.6-27B Setup - Dual RTX 3060 - 30-50 t/s

**Meta:** score=68 · comments=38 · tier=1 · flair=Discussion · posted=2026-05-26 21:22Z
**Author:** u/akira3weet
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tokpoc/400_qwen_3627b_setup_dual_rtx_3060_3050_ts/](https://www.reddit.com/r/LocalLLaMA/comments/1tokpoc/400_qwen_3627b_setup_dual_rtx_3060_3050_ts/)

I picked up a 7900 XTX earlier which runs qwen3.6-27b fine, but not to my like. Its compute performance is quite unstable for me. With MTP the decode speed can reach 40-60 t/s, but prefill is just too slow. Regardless of whether I used ROCm or Vulkan, the prefill speed varies between 300t/s and 500 t/s, even with very long prompts.

I've been itching to try out an ultra-budget 24GB setup using dual 3060s. I managed to snag a second 3060 at a reasonable price in last few days. So I took out the 7900 XTX, installed the 3060s, and began testing.

# Test Configuration

* **Test Platform:** i7 4770k + Gigabyte GA-Z87MX-D3H
   * Quite an ancient platform, used for over a decade. But interestingly, it supports SLI by splitting PCIe 3.0 x16 into two PCIe 3.0 x8 when both slots used. Newer motherboards don't seem to offer such split but many offer one full-speed PCIe 5.0 x16 slot plus one PCIe 4.0 x4 slot. As we know, PCIe 4.0 x4 is equivalent to PCIe 3.0 x8. Therefore this old platform is on par with newer ones in terms of PCIe bottleneck.
   * Monitor is plugged into the motherboard using iGPU.
* **OS:** Kubuntu 24.04
* **CUDA:** 13.2
* **Models:**
   * unsloth/Qwen3.6-27B-MTP-GGUF
   * unsloth/Qwen3.6-27B-GGUF
* **Quantization:** Qwen3.6-27B-Q4\_K\_S.gguf
* **Software:** llama.cpp 5/25/2026 master, self-compiled with CUDA support (official pre-compiled Linux CUDA binaries are not available for download).
   * Pre-requisite installation: `sudo apt install nvidia-cuda-toolkit`
* **Se

[…truncated, see permalink]

---

### Tencent Hy-MT2 is now under Apache License 2.0

**Meta:** score=60 · comments=12 · tier=1 · flair=News · posted=2026-05-26 13:08Z
**Author:** u/sword-in-stone
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1to6g1d/tencent_hymt2_is_now_under_apache_license_20/](https://www.reddit.com/r/LocalLLaMA/comments/1to6g1d/tencent_hymt2_is_now_under_apache_license_20/)
**Link:** [https://x.com/i/status/2059249996256711150](https://x.com/i/status/2059249996256711150)

---
