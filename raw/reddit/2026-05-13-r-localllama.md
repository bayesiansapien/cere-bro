# r/LocalLLaMA | 2026-05-13 IST | sort=top
> Scraped 2026-05-13 10:36 IST | lookback=24h | tier_default=1
> Inference, quantization (GGUF/AWQ/EXL2), KV cache tricks, llama.cpp internals, kernel tuning, GPU rigs. Single highest-signal sub for Tier 1 efficiency.

### Stop wasting electricity

**Meta:** score=612 · comments=167 · tier=1 · flair=Discussion · posted=2026-05-12 11:32Z
**Author:** u/OkFly3388
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tayu5t/stop_wasting_electricity/](https://www.reddit.com/r/LocalLLaMA/comments/1tayu5t/stop_wasting_electricity/)
**Link:** [https://www.reddit.com/gallery/1tayu5t](https://www.reddit.com/gallery/1tayu5t)

---

### I got a real transformer language model running locally on a stock Game Boy Color!

**Meta:** score=501 · comments=41 · tier=1 · flair=Tutorial | Guide · posted=2026-05-12 23:15Z
**Author:** u/maddiedreese
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tbi2n3/i_got_a_real_transformer_language_model_running/](https://www.reddit.com/r/LocalLLaMA/comments/1tbi2n3/i_got_a_real_transformer_language_model_running/)
**Link:** [https://i.redd.it/1hl9id7ghs0h1.jpeg](https://i.redd.it/1hl9id7ghs0h1.jpeg)

---

### Dad why is my sisters name Lora?

**Meta:** score=309 · comments=25 · tier=1 · flair=Funny · posted=2026-05-12 21:01Z
**Author:** u/rwitz4
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tbemwa/dad_why_is_my_sisters_name_lora/](https://www.reddit.com/r/LocalLLaMA/comments/1tbemwa/dad_why_is_my_sisters_name_lora/)
**Link:** [https://i.redd.it/a6oq8jzitr0h1.jpeg](https://i.redd.it/a6oq8jzitr0h1.jpeg)

---

### Needle: We Distilled Gemini Tool Calling Into a 26M Model

**Meta:** score=248 · comments=33 · tier=1 · flair=New Model · posted=2026-05-12 17:56Z
**Author:** u/Henrie_the_dreamer
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tb9b0r/needle_we_distilled_gemini_tool_calling_into_a/](https://www.reddit.com/r/LocalLLaMA/comments/1tb9b0r/needle_we_distilled_gemini_tool_calling_into_a/)

We open-sourced Needle, a 26M parameter function-calling (tool use) model. It runs at 6000 tok/s prefill and 1200 tok/s decode on consumer devices.

We were always frustrated by the little effort made towards building agentic models that run on budget phones, so we conducted investigations that led to an observation: agentic experiences are built upon tool calling, and massive models are overkill for it. Tool calling is fundamentally retrieval-and-assembly (match query to tool name, extract argument values, emit JSON), not reasoning. Cross-attention is the right primitive for this, and FFN parameters are wasted at this scale.

Simple Attention Networks: the entire model is just attention and gating, no MLPs anywhere. Needle is an experimental run for single-shot function calling for consumer devices (phones, watches, glasses...).

Training:

\- Pretrained on 200B tokens across 16 TPU v6e (27 hours)

\- Post-trained on 2B tokens of synthesized function-calling data (45 minutes)

\- Dataset synthesized via Gemini with 15 tool categories (timers, messaging, navigation, smart home, etc.)

You can test it right now and finetune on your Mac/PC: [https://github.com/cactus-compute/needle](https://github.com/cactus-compute/needle)

The full writeup on the architecture is here: [https://github.com/cactus-compute/needle/blob/main/docs/simple\_attention\_networks.md](https://github.com/cactus-compute/needle/blob/main/docs/simple_attention_networks.md)

We found that the "no FFN" finding 

[…truncated, see permalink]

---

### Let's build claude code from scratch!

**Meta:** score=174 · comments=81 · tier=1 · flair=Resources · posted=2026-05-12 16:25Z
**Author:** u/RoyalMaterial9614
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tb6nkx/lets_build_claude_code_from_scratch/](https://www.reddit.com/r/LocalLLaMA/comments/1tb6nkx/lets_build_claude_code_from_scratch/)
**Link:** [https://i.redd.it/ass571o3gq0h1.png](https://i.redd.it/ass571o3gq0h1.png)

---

### examples : add llama-eval by ggerganov · Pull Request #21152 · ggml-org/llama.cpp

**Meta:** score=79 · comments=23 · tier=1 · flair=News · posted=2026-05-12 12:57Z
**Author:** u/jacek2023
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tb0uln/examples_add_llamaeval_by_ggerganov_pull_request/](https://www.reddit.com/r/LocalLLaMA/comments/1tb0uln/examples_add_llamaeval_by_ggerganov_pull_request/)
**Link:** [https://github.com/ggml-org/llama.cpp/pull/21152](https://github.com/ggml-org/llama.cpp/pull/21152)

---

### MagicQuant (v2.0) - Hybrid Mixed GGUF Models + Unsloth Dynamic Learned Quant Configurations + Benchmark table with collapsed winners and more

**Meta:** score=80 · comments=28 · tier=1 · flair=Discussion · posted=2026-05-12 14:46Z
**Author:** u/crossivejoker
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tb3sja/magicquant_v20_hybrid_mixed_gguf_models_unsloth/](https://www.reddit.com/r/LocalLLaMA/comments/1tb3sja/magicquant_v20_hybrid_mixed_gguf_models_unsloth/)

I spent the past 5+ months building a pipeline that creates hybrid GGUF quant mixes. I also built it to learn from Unsloth (or other) models by utilizing their quant to tensor assignment. And some architectures like Qwen3.6 27B have super weird patterns that can get genuinely lower KLD while dropping the model size meaningfully. Totally depends on the architecture though! This has been incredibly fun for me to build. I call my project, "MagicQuant". And I'd love to show you what it is currently producing alongside the published repo's to showcase.

And the hybrid aspect is super fun and mostly what I'll talk about. But the final results table doesn't just include hybrids, it includes Unsloth, llama.cpp, or anything else it learns from, but it only shows the survivors of the pipelines gauntlet.

MagicQuant has dominance, premium, nonlinear sub space winners, and collapse logic that instead of a quant dump repo that says "I don't know if IQ4\_XS or Q4\_K\_S is better than the other even though they're the same size. Nor do I know if this model is allergic to IQ4\_NL, but good luck!" MagicQuant aims to actually test what's the best bang for your buck based on the VRAM you have.

Some models are very predictable, boring, and don't really have crazy improvements to be made, but maybe some nice optional sub zones, great collapse spaces, etc. Some models are weird, have quirks, and the system recognizes this and optimizes the living hell out of it.

MagicQuant aims to solve a few ke

[…truncated, see permalink]

---

### Gemma 4 MTP vs DFlash on 1x H100: dense vs MoE results

**Meta:** score=71 · comments=24 · tier=1 · flair=Tutorial | Guide · posted=2026-05-12 13:09Z
**Author:** u/LayerHot
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tb160j/gemma_4_mtp_vs_dflash_on_1x_h100_dense_vs_moe/](https://www.reddit.com/r/LocalLLaMA/comments/1tb160j/gemma_4_mtp_vs_dflash_on_1x_h100_dense_vs_moe/)

Benchmarked Gemma 4 [MTP](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) and z-lab's [DFlash](https://github.com/z-lab/dflash) on a single H100 80GB using vLLM and NVIDIA's [SPEED-Bench](https://huggingface.co/datasets/nvidia/SPEED-Bench) qualitative dataset.

# Setup:

* Hardware: 1x H100 80GB
* Runtime: vLLM
* Dataset: SPEED-Bench qualitative
* Prompts: 880 total, 80 prompts across each of 11 categories
* Models: google/gemma-4-31B-it and google/gemma-4-26B-A4B-it
* MTP drafts: Google's matching Gemma 4 assistant models
* DFlash drafts: z-lab's matching Gemma 4 DFlash models
* MTP used num\_speculative\_tokens=8
* DFlash used num\_speculative\_tokens=15
* Context length / max model length: `32768`
* Temperature: 0
* Prefix caching was disabled

# Results:

* For **Gemma 4 31B dense,** **MTP was 3.11x faster** and **DFlash was 3.03x faster** than baseline decoding at concurrency 1. Baseline hit 40.3 output tok/s, MTP hit 125.3 output tok/s, and DFlash hit 122.1 output tok/s. At concurrency 16, baseline reached 375 tok/s, MTP reached 953 tok/s, and DFlash reached 725 tok/s.

https://preview.redd.it/4zyyt58j7p0h1.png?width=2571&amp;format=png&amp;auto=webp&amp;s=930d3a8383fb7fe40749217867f4f3ab9877b4a4

* For **Gemma 4 26B-A4B MoE**, the result flipped. **DFlash was 1.73x faster** and **MTP was 1.49x faster** than baseline decoding at concurrency 1. Baseline hit 177.1 output tok/s, MTP hit 264.2 output tok/s, and DFlash hit 3

[…truncated, see permalink]

---

### My First Official AI Research Paper Accepted on SSRN

**Meta:** score=62 · comments=11 · tier=1 · flair=News · posted=2026-05-12 23:04Z
**Author:** u/assemsabryy
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tbht4h/my_first_official_ai_research_paper_accepted_on/](https://www.reddit.com/r/LocalLLaMA/comments/1tbht4h/my_first_official_ai_research_paper_accepted_on/)

https://preview.redd.it/oz4vpoxdfs0h1.jpg?width=910&amp;format=pjpg&amp;auto=webp&amp;s=fa4c91aad0e3c56850fbfc06099e9c4095712bbd

Today, my research paper **“Stable Training with Adaptive Momentum (STAM)”** was officially accepted on **SSRN** — marking my first documented and official publication as an AI Researcher.

The paper introduces a new optimization algorithm for deep learning training that outperformed several popular optimizers in selected benchmarks, addressed multiple training stability challenges, and achieved up to **50% reduction in computational training cost** in some experiments.

This is an important milestone in my research journey, and I’m excited to continue exploring optimization techniques for efficient and stable AI training.

You can read the paper here:  
[https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=6699059](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6699059)

---

### Is using vLLM actually worth it if you aren't serving the model to other people?

**Meta:** score=53 · comments=58 · tier=1 · flair=Question | Help · posted=2026-05-12 21:45Z
**Author:** u/ayylmaonade
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tbftlt/is_using_vllm_actually_worth_it_if_you_arent/](https://www.reddit.com/r/LocalLLaMA/comments/1tbftlt/is_using_vllm_actually_worth_it_if_you_arent/)

So, as most of us here are, I'm a llama.cpp loyalist. Easy to understand, great configuration, relatively stable, etc. But I’ve been increasingly tempted by vLLM, especially since AMD just added it as a built-in inference engine to Lemonade, and I happen to have an AMD GPU. The thing is, I've never actually used vLLM directly, but I've heard good things about how it performs compared to llama.cpp, with vLLM apparently outperforming it pretty much across the board.

Buuuuut, I only serve my model to myself - no hosting for others to worry about, and another thing I've heard is that vLLM is engineered more for scenarios where you're serving many requests at once. But the apparent speedup still piques my interest.

Has anybody here actually done this? Is it worth all the hassle, or is it basically unnoticeable and not something to bother with? It would be great to hear some of the experiences from people who aren't just using it in enterprise-type settings.

Appreciate any help, ty!

---

### i built a little free mobile app that lets you generate your ai slop wrapper apps

**Meta:** score=51 · comments=11 · tier=1 · flair=Funny · posted=2026-05-12 17:23Z
**Author:** u/xSnoozy
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tb8d89/i_built_a_little_free_mobile_app_that_lets_you/](https://www.reddit.com/r/LocalLLaMA/comments/1tb8d89/i_built_a_little_free_mobile_app_that_lets_you/)
**Link:** [https://v.redd.it/wjmk62doqq0h1](https://v.redd.it/wjmk62doqq0h1)

---

### 1M datasets on HF !

**Meta:** score=52 · comments=7 · tier=1 · flair=Discussion · posted=2026-05-12 16:07Z
**Author:** u/qlhoest
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tb64km/1m_datasets_on_hf/](https://www.reddit.com/r/LocalLLaMA/comments/1tb64km/1m_datasets_on_hf/)
**Link:** [https://i.redd.it/0hc0psqvcq0h1.png](https://i.redd.it/0hc0psqvcq0h1.png)

---
