# r/LocalLLaMA | 2026-05-16 IST | sort=top
> Scraped 2026-05-16 09:00 IST | lookback=24h | tier_default=1
> Inference, quantization (GGUF/AWQ/EXL2), KV cache tricks, llama.cpp internals, kernel tuning, GPU rigs. Single highest-signal sub for Tier 1 efficiency.

### Built a fully offline suitcase robot around a Jetson Orin NX SUPER 16GB. Gemma 4 E4B, ~200ms cached TTFT, 30+ sensors, no WiFi/BT/cellular. He has opinions.

**Meta:** score=495 · comments=77 · tier=1 · flair=Discussion · posted=2026-05-15 15:09Z
**Author:** u/CreativelyBankrupt
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tdz5gr/built_a_fully_offline_suitcase_robot_around_a/](https://www.reddit.com/r/LocalLLaMA/comments/1tdz5gr/built_a_fully_offline_suitcase_robot_around_a/)
**Link:** [https://v.redd.it/9v5pmv1rgb1h1](https://v.redd.it/9v5pmv1rgb1h1)

---

### China modded GPU (eg. 4090 48gb) --&gt; I'm gonna figure it out. IS THERE NO ONE ELSE CURIOUS??

**Meta:** score=258 · comments=115 · tier=1 · flair=Discussion · posted=2026-05-15 04:16Z
**Author:** u/LeatherRub7248
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tdldfq/china_modded_gpu_eg_4090_48gb_im_gonna_figure_it/](https://www.reddit.com/r/LocalLLaMA/comments/1tdldfq/china_modded_gpu_eg_4090_48gb_im_gonna_figure_it/)

There's a dearth of information (in the english world) about these cards.

The good recent video is probably this one:  
[https://www.youtube.com/watch?v=TcRGBeOENLg](https://www.youtube.com/watch?v=TcRGBeOENLg)

even in this subreddit, there's seems to be few reviews  of these cards.

Last couple of decent threads:  
[https://www.reddit.com/r/LocalLLaMA/comments/1s62b23/bought\_rtx4080\_32gb\_triple\_fan\_from\_china/](https://www.reddit.com/r/LocalLLaMA/comments/1s62b23/bought_rtx4080_32gb_triple_fan_from_china/)  
[https://www.reddit.com/r/LocalLLaMA/comments/1nifajh/i\_bought\_a\_modded\_4090\_48gb\_in\_shenzhen\_this\_is/](https://www.reddit.com/r/LocalLLaMA/comments/1nifajh/i_bought_a_modded_4090_48gb_in_shenzhen_this_is/)

Is there really NOONE else who has tried these?

In particular

1. Software / bios / quirks that make them NOT run as per unmodded card
2. Short term consistency,  does it run fast for a test, but hang / die when stressed?
3. Long term reliability - does the whole thing fail within 2 months of regular usage?
4. Are the benchmarks good? Where are the results??
5. source and price?

chinese video site blibli has ton of videos, and taobao (and other ecomm) sites also lots of sellers.

If i can piece together enough research, i may also visit shenzhen to pick up a few.

If you're interested in this space, DM me . hope to form a group to split up research efforts.

Also any native chinese speakers who are familiar in this space also please join in.

EDIT:

[…truncated, see permalink]

---

### Orthrus-Qwen3-8B : up to  7.8×tokens/forward on Qwen3-8B, frozen backbone, provably identical output distribution

**Meta:** score=177 · comments=58 · tier=1 · flair=New Model · posted=2026-05-15 19:07Z
**Author:** u/Franck_Dernoncourt
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1te5xpu/orthrusqwen38b_up_to_78tokensforward_on_qwen38b/](https://www.reddit.com/r/LocalLLaMA/comments/1te5xpu/orthrusqwen38b_up_to_78tokensforward_on_qwen38b/)
**Link:** [https://i.redd.it/kmqh40q2nc1h1.gif](https://i.redd.it/kmqh40q2nc1h1.gif)

---

### internlm/Intern-S2-Preview · Hugging Face

**Meta:** score=109 · comments=12 · tier=1 · flair=New Model · posted=2026-05-15 10:09Z
**Author:** u/pmttyji
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tdrw0s/internlminterns2preview_hugging_face/](https://www.reddit.com/r/LocalLLaMA/comments/1tdrw0s/internlminterns2preview_hugging_face/)
**Link:** [https://huggingface.co/internlm/Intern-S2-Preview](https://huggingface.co/internlm/Intern-S2-Preview)

---

### Used over a million tokens in three separate sessions to test Qwen 3.6 35b (new Multi-token Prediction version)

**Meta:** score=92 · comments=66 · tier=1 · flair=Discussion · posted=2026-05-15 06:20Z
**Author:** u/Jorlen
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tdns1i/used_over_a_million_tokens_in_three_separate/](https://www.reddit.com/r/LocalLLaMA/comments/1tdns1i/used_over_a_million_tokens_in_three_separate/)

In my opinion, MTP models are 100% game changer for local LLMs.

In terms of speed, I was getting around 1.5x the tok/sec of previous tests.

The project was a test - building a full iterative step-by-step pygame; a small mystery dungeon-style game.  At first I set 100-200k context and raised it to 300k.  ~~This is at KV Q8_0 quant.~~ Edit:  I was wrong, I had mistakenly left it at q4_0.  I will redo tests tomorrow with Q8.  

I use VSCodium and Roo.  The idea was to see how far I can push the context window and measure (by feel) if a large context window with a multi-file project slows it down too much to be effective.

Model used:  Qwen3.6-35B-A3B-UD-Q5_K_S (MTP version) - [link](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)

OS/Software:  Ubuntu 24.04 - Vulkan - To use MTP I had to use a docker version of the MTP prototype of llama.cpp server (image: havenoammo/llama:vulkan-server)

My current window is 300k context but I feel like I can go even higher as my VRAM used is 28.3gb / 32gb.  Likely 400k is viable (with the 35B MoE model that is).

GPU:  Asus Radeon R9700 AI Pro card (32gb RDNA 4 card)

Just want to shoot my appreciation for the local LLM community and everyone responsible for enabling us to run these kinds of powerful models at home.  Amazing when I think where we were just a year ago.  I am having a blast exploring all this tech and every day that I learn something new, it just leaves me astounded.

__________

**EDIT:** Switched to the Qwen 3.6 27b

[…truncated, see permalink]

---

### I built a self-hosted open-source MCP server that gives any local LLM real financial data — SEC filings, 13F, insider &amp; congressional trades, short data, FRED

**Meta:** score=76 · comments=13 · tier=1 · flair=Resources · posted=2026-05-15 17:08Z
**Author:** u/DanielAPO
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1te2jko/i_built_a_selfhosted_opensource_mcp_server_that/](https://www.reddit.com/r/LocalLLaMA/comments/1te2jko/i_built_a_selfhosted_opensource_mcp_server_that/)
**Link:** [https://v.redd.it/3es19kwb2c1h1](https://v.redd.it/3es19kwb2c1h1)

---

### [FOUNDING] SupraLabs - real open-source AI models for you!

**Meta:** score=55 · comments=53 · tier=1 · flair=News · posted=2026-05-15 13:08Z
**Author:** u/LH-Tech_AI
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tdvvf2/founding_supralabs_real_opensource_ai_models_for/](https://www.reddit.com/r/LocalLLaMA/comments/1tdvvf2/founding_supralabs_real_opensource_ai_models_for/)

https://preview.redd.it/k6lub2ypva1h1.png?width=1500&amp;format=png&amp;auto=webp&amp;s=cd44452c86b5216fec17113a72f43bbf169edafb

Hey r/LocalLLaMA !

We founded **SupraLabs**, and it's huge!

# What we do?

We train, finetune and explore small models with good results to revolutionize small AI models by making them accessible to everyone. ❤️🙂

# Are we on Hugging Face?

Of course: [https://huggingface.co/SupraLabs](https://huggingface.co/SupraLabs)

# Are there any models yet?

YES THERE ARE MODELS!

E.G.: [https://huggingface.co/SupraLabs/Supra-Mini-v4-2M](https://huggingface.co/SupraLabs/Supra-Mini-v4-2M) and many more!

# What models will come?

We will share more models soon, like:

* StorySupra 10M: a 10M story telling SLM running on edge devices
* Supra Mini **v5** 5M: a cutting-edge SLM with really good performance and great results
* many more... stay tuned

# Where do I get updates?

You can read our blog here: [https://huggingface.co/spaces/SupraLabs/Blog](https://huggingface.co/spaces/SupraLabs/Blog)  
Come check it out!

# Can I join or support this?

Yes! Feel free to ask in a community discussion on HF or under this post in the comments if you want to join us!  
Plus: you can always support us by dowwloading and liking our models and following us on HF.

  
See all models here: [https://huggingface.co/SupraLabs/models](https://huggingface.co/SupraLabs/models)

---

### Dynamically allocating compute budget to hard set of problems and evolving the sections with Qwen-35B-A3B gets you near GPT-5.4-xHigh on HLE

**Meta:** score=53 · comments=6 · tier=1 · flair=Resources · posted=2026-05-15 20:51Z
**Author:** u/Ryoiki-Tokuiten
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1te8sxt/dynamically_allocating_compute_budget_to_hard_set/](https://www.reddit.com/r/LocalLLaMA/comments/1te8sxt/dynamically_allocating_compute_budget_to_hard_set/)
**Link:** [https://www.reddit.com/gallery/1te8sxt](https://www.reddit.com/gallery/1te8sxt)

---

### ByteDance-Seed/Cola-DLM · Hugging Face

**Meta:** score=52 · comments=8 · tier=1 · flair=New Model · posted=2026-05-15 11:19Z
**Author:** u/pmttyji
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tdtaqt/bytedanceseedcoladlm_hugging_face/](https://www.reddit.com/r/LocalLLaMA/comments/1tdtaqt/bytedanceseedcoladlm_hugging_face/)
**Link:** [https://huggingface.co/ByteDance-Seed/Cola-DLM](https://huggingface.co/ByteDance-Seed/Cola-DLM)

---
