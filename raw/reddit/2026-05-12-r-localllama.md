# r/LocalLLaMA | 2026-05-12 IST | sort=top
> Scraped 2026-05-12 09:00 IST | lookback=24h | tier_default=1
> Inference, quantization (GGUF/AWQ/EXL2), KV cache tricks, llama.cpp internals, kernel tuning, GPU rigs. Single highest-signal sub for Tier 1 efficiency.

### Openclaw ia trending down and will disappear soon

**Meta:** score=518 · comments=313 · tier=1 · posted=2026-05-11 06:14Z
**Author:** u/rm-rf-rm
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t9urup/openclaw_ia_trending_down_and_will_disappear_soon/](https://www.reddit.com/r/LocalLLaMA/comments/1t9urup/openclaw_ia_trending_down_and_will_disappear_soon/)
**Link:** [https://i.redd.it/oapvwkdjjd0h1.png](https://i.redd.it/oapvwkdjjd0h1.png)

---

### Computer build using Intel Optane Persistent Memory - Can run 1 trillion parameter model at over 4 tokens/sec

**Meta:** score=434 · comments=70 · tier=1 · flair=Tutorial | Guide · posted=2026-05-11 19:54Z
**Author:** u/APFrisco
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1taeg8h/computer_build_using_intel_optane_persistent/](https://www.reddit.com/r/LocalLLaMA/comments/1taeg8h/computer_build_using_intel_optane_persistent/)
**Link:** [https://i.redd.it/na7zo7lmck0h1.jpeg](https://i.redd.it/na7zo7lmck0h1.jpeg)

---

### MTP on Unsloth

**Meta:** score=366 · comments=125 · tier=1 · flair=News · posted=2026-05-11 14:21Z
**Author:** u/Altruistic_Heat_9531
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1ta4rvs/mtp_on_unsloth/](https://www.reddit.com/r/LocalLLaMA/comments/1ta4rvs/mtp_on_unsloth/)
**Link:** [https://i.redd.it/7qopol51pi0h1.png](https://i.redd.it/7qopol51pi0h1.png)

---

### The Qwen 3.6 35B A3B hype is real!!!

**Meta:** score=361 · comments=113 · tier=1 · flair=Discussion · posted=2026-05-11 07:51Z
**Author:** u/The_Paradoxy
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t9whrt/the_qwen_36_35b_a3b_hype_is_real/](https://www.reddit.com/r/LocalLLaMA/comments/1t9whrt/the_qwen_36_35b_a3b_hype_is_real/)

My personal test for small local LLM intelligence is to check whether a model has any ability to understand the code that I write for my own academic research. My research is on some pretty niche topics and I doubt that anything like it is substantively present in the training sets for LLMs. A few months ago, small local models' ability to understand my code was nominal at best with [Devstral Small 2 being the top performer](https://www.reddit.com/r/LocalLLaMA/comments/1ry93gz/devstral_small_2_24b_severely_underrated/?utm_source=share&amp;utm_medium=web3x&amp;utm_name=web3xcss&amp;utm_term=1&amp;utm_content=share_button). However, several small open weight models now have methods of accommodating fairly **long contexts** (gated delta net, hybrid Mamba2, sliding window attention) which makes them ***extremely*** **smarter**. I can now feed a model an entire academic paper along with accompanying code and ask it to use the paper to work out what the code is doing. 

I just spent a couple days experimenting with:

* Qwen 3.6 35B A3B
* Qwen 3.6 27B
* Gemma 4 26B A4B
* Nemotron 3 Nano

**All** of them were able to comprehend my code significantly better than what any *small* local model could do a few months ago. I did try Devstral Small 2 since I recently went from a single 16GB graphics card to two; however, I simply couldn't fit the long context in 32GB of ram. I hope Mistral releases a new small model with a gated delta net, because I think it could take the throne.

  
[These

[…truncated, see permalink]

---

### ExLlamaV3 Major Updates!

**Meta:** score=147 · comments=61 · tier=1 · flair=News · posted=2026-05-11 07:05Z
**Author:** u/Unstable_Llama
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t9voxs/exllamav3_major_updates/](https://www.reddit.com/r/LocalLLaMA/comments/1t9voxs/exllamav3_major_updates/)
**Link:** [https://i.redd.it/3xgpoqggjg0h1.png](https://i.redd.it/3xgpoqggjg0h1.png)

---

### New GGUF uploads on HF nearly doubled in 2 months

**Meta:** score=114 · comments=37 · tier=1 · flair=News · posted=2026-05-11 10:47Z
**Author:** u/Nunki08
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t9zmbb/new_gguf_uploads_on_hf_nearly_doubled_in_2_months/](https://www.reddit.com/r/LocalLLaMA/comments/1t9zmbb/new_gguf_uploads_on_hf_nearly_doubled_in_2_months/)
**Link:** [https://www.reddit.com/gallery/1t9zmbb](https://www.reddit.com/gallery/1t9zmbb)

---

### MiniCPM 4.6

**Meta:** score=105 · comments=14 · tier=1 · flair=New Model · posted=2026-05-11 17:08Z
**Author:** u/themrzmaster
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1ta9k8o/minicpm_46/](https://www.reddit.com/r/LocalLLaMA/comments/1ta9k8o/minicpm_46/)
**Link:** [https://huggingface.co/openbmb/MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)

---

### Will there be any more Qwen3.6 series models?

**Meta:** score=96 · comments=76 · tier=1 · flair=Discussion · posted=2026-05-11 17:37Z
**Author:** u/cafedude
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1taafs4/will_there_be_any_more_qwen36_series_models/](https://www.reddit.com/r/LocalLLaMA/comments/1taafs4/will_there_be_any_more_qwen36_series_models/)

I'm still hoping we see a Qwen3.6-122B or a Qwen3.6-coder, but my hopes are dimming. Seems like we would have seen/heard something by now, even if just tantalizing hints from the Qwen folks.

---

### unsloth/MiMo-V2.5-GGUF · Hugging Face

**Meta:** score=76 · comments=48 · tier=1 · flair=Resources · posted=2026-05-11 06:13Z
**Author:** u/jacek2023
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t9uqu8/unslothmimov25gguf_hugging_face/](https://www.reddit.com/r/LocalLLaMA/comments/1t9uqu8/unslothmimov25gguf_hugging_face/)
**Link:** [https://huggingface.co/unsloth/MiMo-V2.5-GGUF](https://huggingface.co/unsloth/MiMo-V2.5-GGUF)

---

### Found a way to cool the DGX

**Meta:** score=73 · comments=30 · tier=1 · flair=Resources · posted=2026-05-12 02:05Z
**Author:** u/OldEffective9726
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tansuo/found_a_way_to_cool_the_dgx/](https://www.reddit.com/r/LocalLLaMA/comments/1tansuo/found_a_way_to_cool_the_dgx/)
**Link:** [https://i.redd.it/pmlz1ysv5m0h1.jpeg](https://i.redd.it/pmlz1ysv5m0h1.jpeg)

---

### Qwen3.6 35b-a3b 🤯

**Meta:** score=66 · comments=66 · tier=1 · flair=Other · posted=2026-05-11 14:32Z
**Author:** u/EffectiveMedium2683
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1ta53a2/qwen36_35ba3b/](https://www.reddit.com/r/LocalLLaMA/comments/1ta53a2/qwen36_35ba3b/)

Originally I was a diehard fan of Gemma4 26b-a4b because it really is a remarkably intelligent llm. Ran qwen3.6 via ollama and found it impressive but still favored Gemma. Ollama did it a disservice at least on my pc.

  
Ran it straight through llama.cpp and it is much faster than gemma4 26b-a4b, roughly equivalent in general intelligence, better in strict prompt adherence, and it doesn't slow down on long context. Like, I'm back to being a Qwen fan. 

  
Just thought I'd share haha

---

### Markdown browser for LLMs

**Meta:** score=63 · comments=33 · tier=1 · flair=Resources · posted=2026-05-11 05:23Z
**Author:** u/DocWolle
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1t9tsro/markdown_browser_for_llms/](https://www.reddit.com/r/LocalLLaMA/comments/1t9tsro/markdown_browser_for_llms/)

I built a markdown web renderer for AI agents. Instead of taking expensive screenshots and piping them through vision models, TextWeb renders web pages as markdown that LLMs can reason about natively. Full JavaScript execution, interactive elements annotated.  
It provides a CLI and an MCP server. You can find it here:

[https://github.com/woheller69/textweb](https://github.com/woheller69/textweb)

The LLM can do things like:  
navigate a web page, scroll up/down, enter text into input fields, click buttons, etc.

Works with llama.cpp web UI.

It is based on [https://github.com/chrisrobison/textweb](https://github.com/chrisrobison/textweb) which has a text grid renderer instead of markdown.

---

### Gemma 4 running fully offline on WebGPU with Transformers.js, controlling Reachy Mini over WebSerial.

**Meta:** score=62 · comments=9 · tier=1 · flair=Other · posted=2026-05-11 17:10Z
**Author:** u/xenovatech
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1ta9mmd/gemma_4_running_fully_offline_on_webgpu_with/](https://www.reddit.com/r/LocalLLaMA/comments/1ta9mmd/gemma_4_running_fully_offline_on_webgpu_with/)
**Link:** [https://v.redd.it/bhbonxqfij0h1](https://v.redd.it/bhbonxqfij0h1)

---

### 500k context on 48gb VRAM!! - 21tok/s (coding)

**Meta:** score=52 · comments=16 · tier=1 · flair=Discussion · posted=2026-05-11 20:49Z
**Author:** u/Express_Quail_1493
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tag1ks/500k_context_on_48gb_vram_21toks_coding/](https://www.reddit.com/r/LocalLLaMA/comments/1tag1ks/500k_context_on_48gb_vram_21toks_coding/)

I found this model hiding in the corner of huggingface: [https://huggingface.co/Max-and-Omnis/Nemotron-3-Super-64B-A12B-Math-REAP-GGUF](https://huggingface.co/Max-and-Omnis/Nemotron-3-Super-64B-A12B-Math-REAP-GGUF)

Looks to be tuned specifically for math but i thought i'd give it a try since i cant run the full 120b nemotron super and it seem to hold up like a champ in agentic coding for some odd reason. been using it to code all my projects for a week now its amazing. Wouldnt dream of having 500k tokens on my potato dual TITAN RTX.

If you do happen to try it drop a cmment on your experience with it where did it break what usecase did u use it for  ETC.

---
