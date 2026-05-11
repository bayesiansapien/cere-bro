# r/LocalLLaMA | 2026-05-11 IST | sort=top
> Scraped 2026-05-11 05:50 IST | lookback=24h | tier_default=1
> Inference, quantization (GGUF/AWQ/EXL2), KV cache tricks, llama.cpp internals, kernel tuning, GPU rigs. Single highest-signal sub for Tier 1 efficiency.

### NVIDIA AI Releases Star Elastic: One Checkpoint that Contains 30B, 23B, and 12B Reasoning Models with Zero-Shot Slicing

**Meta:** score=294 · comments=57 · tier=1 · flair=New Model · posted=2026-05-10 00:48Z
**Author:** u/phazei
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t8s83r/nvidia_ai_releases_star_elastic_one_checkpoint/](https://www.reddit.com/r/LocalLLaMA/comments/1t8s83r/nvidia_ai_releases_star_elastic_one_checkpoint/)

I saw this on another sub and didn't see it posted here, it looks awesome, and can definitely be run local.  I guess it was released 11 days ago, but it never hit the top of my feed (which I look at way too often), so posting it again.

# This is my take on it:

Think of this as like scalable video coding, you have a UHD stream, but strip some layers and you have a HD, or SD stream, it's all a single file stream, not multiple ones.

Like nested models, rather than 3 different sets, and they can share their KV cache so the model can adjust speed like a sliding scale.  You get an idea with a 30B model, then scale down and permutate all the thinking at 7000t/s on the 12B model, generating a book of reasoning in seconds, then slide up to 30B again to evaluate what's good.  You could have a 30B kind of guide the smaller ones back and forth.

Maybe it's somewhat of a hybrid between Dense and MoE, it's like MoE but with 3 dense models that are like russian dolls.


# Original Post:

NVIDIA just released Star Elastic — and the inference strategy alone is worth understanding.

Here's what's actually interesting from the technical side:

1. One checkpoint. Three models.

Star Elastic applies a post-training method to Nemotron Nano v3 that nests 23B and 12B submodels can be extracted zero-shot from the parent checkpoint the 30B parent. All three live in a single checkpoint in BF16, FP8, and NVFP4.

2. The router learns the architecture, not just the weights.

A learnable router trained 

[…truncated, see permalink]

---

### Getting a feel for how fast X tokens/second really is.

**Meta:** score=288 · comments=83 · tier=1 · flair=Resources · posted=2026-05-10 15:23Z
**Author:** u/MikeNonect
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t99upf/getting_a_feel_for_how_fast_x_tokenssecond_really/](https://www.reddit.com/r/LocalLLaMA/comments/1t99upf/getting_a_feel_for_how_fast_x_tokenssecond_really/)

I love following all your adventures with local LLM setups. Quality and size of the models are important, but so is performance. Numbers don't really convey the experienced speed well, however.

If someone claims they run Qwen 3.6-27B at 21 tokens/second, how fast is that? Is 10 tokens/second unusable? I find these numbers objective but meaningless.

I built a script that helps me get a subjective feel for these objective numbers.

It supports text, code and reasoning + code. 

[https://mikeveerman.github.io/tokenspeed/](https://mikeveerman.github.io/tokenspeed/)

---

### I have DeepSeek V4 Pro at home

**Meta:** score=214 · comments=115 · tier=1 · flair=Other · posted=2026-05-10 11:35Z
**Author:** u/fairydreaming
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t94ito/i_have_deepseek_v4_pro_at_home/](https://www.reddit.com/r/LocalLLaMA/comments/1t94ito/i_have_deepseek_v4_pro_at_home/)

Just wanted to share that I used u/LegacyRemaster slightly modified (Q4\_K\_M conversion support) DeepSeek V4 [CUDA repo](https://github.com/Fringe210/llama.cpp-deepseek-v4-flash-cuda) (based on u/antirez [work](https://github.com/antirez/llama.cpp-deepseek-v4-flash)) to convert and run Q4\_K\_M [DeepSeek V4 Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) on my Epyc workstation (Genoa 9374F, 12 x 96GB RAM, single RTX PRO 6000 Max-Q) and it worked right from the start:

    (base) phm@epyc:~/projects/llama.cpp-deepseek-v4-flash-cuda/build-cuda$ ./bin/llama-cli -m ../models/DeepSeek-V4-Pro-Q4_K_M.gguf --no-repack -ub 128 --chat-template-file ../models/templates/deepseek-ai-DeepSeek-V3.2.jinja 
    ggml_cuda_init: found 1 CUDA devices (Total VRAM: 97247 MiB):
      Device 0: NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition, compute capability 12.0, VMM: yes, VRAM: 97247 MiB
    
    Loading model...  
    
    
    ▄▄ ▄▄
    ██ ██
    ██ ██  ▀▀█▄ ███▄███▄  ▀▀█▄    ▄████ ████▄ ████▄
    ██ ██ ▄█▀██ ██ ██ ██ ▄█▀██    ██    ██ ██ ██ ██
    ██ ██ ▀█▄██ ██ ██ ██ ▀█▄██ ██ ▀████ ████▀ ████▀
                                        ██    ██
                                        ▀▀    ▀▀
    
    build      : b8936-44c7b01de
    model      : DeepSeek-V4-Pro-Q4_K_M.gguf
    modalities : text
    
    available commands:
      /exit or Ctrl+C     stop or exit
      /regen              regenerate the last response
      /clear              clear the chat history
      /read

[…truncated, see permalink]

---

### Hello from 10KM high! - Thanks to Qwen 3.6 35b a3b!

**Meta:** score=133 · comments=37 · tier=1 · flair=Funny · posted=2026-05-10 09:43Z
**Author:** u/Qwen30bEnjoyer
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t92hff/hello_from_10km_high_thanks_to_qwen_36_35b_a3b/](https://www.reddit.com/r/LocalLLaMA/comments/1t92hff/hello_from_10km_high_thanks_to_qwen_36_35b_a3b/)

Typing this on a cramped flight, but I was having issues connecting to the plane's wifi on my ubuntu laptop, when it was effortless on my phone.  

The issue I was having was the Laptop WiFi connected to the plane wifi network, but captive portal wouldn't load. Turns out systemd-resolved was using Docker's DNS instead of the network gateway. 
Luckily I brought Qwen with me, the agent found a nmcli fix in seconds, and the portal loaded soon after! Could this have been avoided by me somehow not fucking it up in the first place? Probably, but ignore my incompetence for now, I'm not a super technical linux guy.

Anyways I'm quite thankful, this would have been a bit of a boring 5 hr flight otherwise.

Cheers to the Qwen team from up high! :)

EDIT: I forget you nerds like specs! Framework 16 7840hs with 96gb RAM and a 780m iGPU. Model used was qwen/Qwen-3.6-35b-a3b-Q6_k. I think I was running about 20TPS TG, but I'll report back on battery vs. plugged in TPS TG and PP with llama-bench when I land. Running vulkan llama.cpp runtime in LMStudio since I'm a baby that likes GUIs, and bear in mind the iGPU can get a max of 50% RAM allocated to it, and I don't think there is a stable ROCM path at the moment.

---

### Running Qwen3.6 35b a3b on 8gb vram and 32gb ram ~190k context

**Meta:** score=75 · comments=48 · tier=1 · flair=Discussion · posted=2026-05-10 18:24Z
**Author:** u/Atul_Kumar_97
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t9eo83/running_qwen36_35b_a3b_on_8gb_vram_and_32gb_ram/](https://www.reddit.com/r/LocalLLaMA/comments/1t9eo83/running_qwen36_35b_a3b_on_8gb_vram_and_32gb_ram/)

If anyone is looking for a good high-speed setup with \~190k context, this config has been working insanely well for me.



I’m using my laptop as a server over Tailscale. Installed Linux on it and running:



\- Qwen3.6 35B A3B

\- RTX 4060 8GB VRAM

\- 32GB DDR5 5600MHz RAM

\- Q5 quant models



Current models tested:



\- \`mudler/Qwen3.6-35B-A3B-APEX-GGUF\`

  \- \~40 tok/sec → 37 tok/sec



\- \`hesamation/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-GGUF\`

  \- \~43 tok/sec → 37 tok/sec



I can push it up to \~51 tok/sec by tweaking:

\- \`--ctx-size 192640\`

\- \`--n-gpu-layers 430\`

\- \`--n-cpu-moe 35\`



and adjusting those values slightly higher/lower depending on stability and memory usage.



Here’s my current config:



\#!/bin/bash

\# --- LLAMA SERVER LAUNCHER SCRIPT ---



\#SELECTED\_MODEL="/home/atulloq/.lmstudio/models/hesamation/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-GGUF/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled.Q5\_K\_M.gguf"



SELECTED\_MODEL="/home/atulloq/.lmstudio/models/mudler/Qwen3.6-35B-A3B-APEX-GGUF/Qwen3.6-35B-A3B-APEX-I-Balanced.gguf"



echo "Starting Llama Server..."

echo "Model: $SELECTED\_MODEL"



/home/atulloq/llama-cpp-turboquant/build/bin/llama-server \\

  \--model "$SELECTED\_MODEL" \\

  \--host [0.0.0.0](http://0.0.0.0) \\

  \--port 8085 \\

  \--ctx-size 192640 \\

  \--n-gpu-layers 430 \\

  \--n-cpu-moe 35 \\

  \--cache-type-k "turbo4" \\

  \--cache-type-v "turbo4" \\

  \--flash-attn on

[…truncated, see permalink]

---

### MTP benchmark results: the nature of the generative task dictates whether you will benefit (coding) or get slower inference (creative) from speculative inference. No other factor comes close.

**Meta:** score=66 · comments=24 · tier=1 · flair=Tutorial | Guide · posted=2026-05-10 19:25Z
**Author:** u/ex-arman68
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t9gcar/mtp_benchmark_results_the_nature_of_the/](https://www.reddit.com/r/LocalLLaMA/comments/1t9gcar/mtp_benchmark_results_the_nature_of_the/)

I recently published [MTP quants of Qwen 3.6 27B](https://www.reddit.com/r/LocalLLaMA/comments/1t57xuu/25x_faster_inference_with_qwen_36_27b_using_mtp/) and I was suprised by the reports here on reddit, and on HF, of users who were experiencing worst speed with speculative inference than without. This did not match what I was seeing, but when I tried to reproduce their exact usage, it confirmed what they were experiencing.

I tried to analyse the problem, made a few conjectures which later turned out to be false, and started a full blown systematical analysis, running 300+ tests and benchmarks, collecting and comparing the results of changing various parameters. This is what I found:

&gt;F16 + MTP nearly **triples coding tasks speed.** Q4\_K\_M + MTP **slows down creative writing.** Same feature, same model, same settings, opposite results.

I did not test all quant sizes, otherwise I would still be here in a few days, but restricted my self to 5 significant ones. The other parameters I varied were task type (4 types), temperature (0.0 0.3 0.7), quantisation of the MTP layer (q8 and matching the model quant). Temp and MTP quant have very little impact on the outcome.

Cumulative average decode speeds with MTP compared to the baseline without MTP, varying the model quant and task type:

|quant|base tok/s|code|factual|analysis|creative|
|:-|:-|:-|:-|:-|:-|
|Q4\_K\_M|15.1|19.7|17.5|14.9|13.7|
|Q5\_K\_M|13.1|19.2|16.5|14.7|12.6|
|Q6\_K|13.4|20.1|17.6|15.2|13.4|
|Q8\_0|11.4|25.4|

[…truncated, see permalink]

---

### I Think I Spent Way Too Much Time Messing with Local LLMs

**Meta:** score=56 · comments=16 · tier=1 · flair=Other · posted=2026-05-10 21:46Z
**Author:** u/MrChilliBalls
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t9jyfu/i_think_i_spent_way_too_much_time_messing_with/](https://www.reddit.com/r/LocalLLaMA/comments/1t9jyfu/i_think_i_spent_way_too_much_time_messing_with/)

Guys, I'm hearing coil whine in my sleep. Help  
&gt;!/s!&lt;

---
