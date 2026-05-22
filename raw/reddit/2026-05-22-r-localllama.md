# r/LocalLLaMA | 2026-05-22 IST | sort=top
> Scraped 2026-05-22 09:18 IST | lookback=24h | tier_default=1
> Inference, quantization (GGUF/AWQ/EXL2), KV cache tricks, llama.cpp internals, kernel tuning, GPU rigs. Single highest-signal sub for Tier 1 efficiency.

### Heretic has been served a legal notice by Meta, Inc.

**Meta:** score=1624 · comments=247 · tier=1 · flair=Discussion · posted=2026-05-21 14:50Z
**Author:** u/-p-e-w-
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjmvx6/heretic_has_been_served_a_legal_notice_by_meta_inc/](https://www.reddit.com/r/LocalLLaMA/comments/1tjmvx6/heretic_has_been_served_a_legal_notice_by_meta_inc/)

To Whomsoever it May Concern,

The individual behind the Heretic Free Software Project (henceforth called "Heretic", notwithstanding unrelated entities of the same name) has been served a notice by a legal services provider representing Meta Platforms, Inc. (henceforth called "Meta"), via the digital communications medium variously known as Internet Mail, Electronic Mail, or simply "email".

The Heretic Project conducts its affairs in full compliance with applicable laws, regulations, rules, guidelines, opinions, and hunches. Following the commendable example set by the renowned heretic Galileo Galilei in 1616, we are **recanting** the relevant materials, namely derivatives of Meta's "Llama" Artificial Intelligence language models, and have removed the same from all model weight repositories controlled by the Heretic Project.

We are grateful to Meta and its legal representatives for the opportunity to better align ourselves with the agenda of the global corporate oligarchy. The Llama model family ranks among the 200 best language models available today, trailing only 168 other models from 23 competitors on the LM Arena leaderboard, and Meta's concern for that asset naturally outweighs scientific freedom, as well as the legally and ethically dubious circumstances under which those models were created in the first place, regarding which, ironically, Meta is currently facing lawsuits and investigations in multiple jurisdictions around the world.

On a completely unrelated note,

[…truncated, see permalink]

---

### Waiting for Qwen 3.7 open weight... The new King has arrived...

**Meta:** score=357 · comments=110 · tier=1 · flair=Discussion · posted=2026-05-21 19:56Z
**Author:** u/LegacyRemaster
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjvz6l/waiting_for_qwen_37_open_weight_the_new_king_has/](https://www.reddit.com/r/LocalLLaMA/comments/1tjvz6l/waiting_for_qwen_37_open_weight_the_new_king_has/)
**Link:** [https://i.redd.it/j8qkty82qj2h1.png](https://i.redd.it/j8qkty82qj2h1.png)

---

### 110 tok/s with 12GB VRAM on Qwen3.6 35B A3B and ik_llama.cpp

**Meta:** score=271 · comments=92 · tier=1 · flair=Tutorial | Guide · posted=2026-05-21 11:09Z
**Author:** u/janvitos
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjh7az/110_toks_with_12gb_vram_on_qwen36_35b_a3b_and_ik/](https://www.reddit.com/r/LocalLLaMA/comments/1tjh7az/110_toks_with_12gb_vram_on_qwen36_35b_a3b_and_ik/)

Had been getting [great MTP performance](https://www.reddit.com/r/LocalLLaMA/comments/1t82zxv/80_toksec_and_128k_context_on_12gb_vram_with/) with [llama.cpp](https://github.com/ggml-org/llama.cpp) on my RTX 4070 Super 12GB, until they actually merged the MTP PR. Then, performance tanked and was barely above non-MTP. So, I decided to try out [ik\_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp) since it also supports MTP and is apparently better optimized for CPU offloading. I did not expect such a huge speed boost!

# Before moving on with the benchmark results, here's my PC specs:

    OS: CachyOS with Plasma (X11) - HIGHLY recommended
    GPU: RTX 4070 Super 12GB
    CPU: AMD Ryzen 7 9700X
    RAM: 48GB DDR5-6000 EXPO I

# UPDATED: For comparison, here's the regular llama.cpp [mtp-bench.py](https://gist.github.com/am17an/228edfb84ed082aa88e3865d6fa27090/) results with byteshape's recently released [Qwen3.6-35B-A3B-IQ4\_XS-4.19bpw](https://huggingface.co/byteshape/Qwen3.6-35B-A3B-MTP-GGUF) quant, which has [similar accuracy](https://www.reddit.com/r/LocalLLaMA/comments/1tipihx/qwen_36_35b_gguf_ntp_vs_mtp_quantization_results/) to Unsloth's Q4_K_XL, but is 4GB smaller:

    ❯ ./mtp-bench.py
     code_python        pred= 192 draft= 122 acc= 118 rate=0.967 tok/s=79.8
     code_cpp           pred= 192 draft= 117 acc= 110 rate=0.940 tok/s=89.1
     explain_concept    pred= 192 draft= 124 acc= 113 rate=0.911 tok/s=88.0
     summarize          pred= 192 draft= 139 acc= 127 rat

[…truncated, see permalink]

---

### Qwen3.6 35Ba3 has changed my workflows and even how I use my computer

**Meta:** score=182 · comments=43 · tier=1 · flair=Other · posted=2026-05-21 20:23Z
**Author:** u/mouseofcatofschrodi
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjwrp7/qwen36_35ba3_has_changed_my_workflows_and_even/](https://www.reddit.com/r/LocalLLaMA/comments/1tjwrp7/qwen36_35ba3_has_changed_my_workflows_and_even/)

My workflow has changed basically to ask Codex to do certain tasks and then document how to do them (including errors it found on its way) into a skill. I feed that skill to pi, and suddenly my qwen3.6 gets that hard stuff done:

\- devops on a VPS  
\- using docling to create epubs from old PDFs  
\- using playwright to test stuff  
\- Doing code tickets

And the list goes on.

What also has changed for me is the way I use the computer. Suddenly, I talk to the OS with natural language: "pi pal, install me please this python library in an .env and do X"; "hey pi, check what is using most space from the memory"; "clean X"; "check my network";  "change X configuration", etc etc etc.

There are times the only reason why I use chatgpt for something is to spare the laptop the effort, or because qwen is already busy with something else.

What I've done today just blew my mind:

I got couple of whatsapp audios asking me to build a simple landing page. I downloaded the audios and transcripted them with AnythingLLM. Then "asked the transcript" to create a content structure for the landing page for the project mentioned in the audios. I got the proper structure and pasted it into a markdown file [content.md](http://content.md) within an empty folder.

I opened pi and asked it to create a website with that content. Gave it some assets also in the folder. Gave two links from websites to extract other assets or contents that could be relevant. Went to have a walk.

Came back the website w

[…truncated, see permalink]

---

### Qwen3.6 27B and llama.cpp appreciation post

**Meta:** score=128 · comments=74 · tier=1 · flair=Discussion · posted=2026-05-21 06:03Z
**Author:** u/ABLPHA
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjbi24/qwen36_27b_and_llamacpp_appreciation_post/](https://www.reddit.com/r/LocalLLaMA/comments/1tjbi24/qwen36_27b_and_llamacpp_appreciation_post/)

To preface, here's my config:

    llama-server \
       --host 0.0.0.0 \
       --port 1235 \
       --models-preset %h/Software/models.ini \
       --models-max 1 \
       --sleep-idle-seconds 3600 \
       --timeout 3600 \
       --parallel 1 \
       --device ROCm0,ROCm1

    [*]
    flash-attn = on
    jinja = true
    fit = true
    ctxcp = 5
    offline = true
    mmproj-offload = false
    mmap = false
    
    
    
    ; ... many other models here ...
    
    
    
    [tp-go-brrr-WORK-CODE]
    hf = unsloth/Qwen3.6-27B-MTP-GGUF:UD-Q5_K_XL
    
    ctx-size = 131072
    temp = 0.6
    top-p = 0.95
    top-k = 20
    presence-penalty = 0.0
    min-p = 0.00
    
    fitt = 1024,1024,0
    
    spec-type = draft-mtp
    spec-draft-n-max = 2
    
    chat-template-kwargs = {"preserve_thinking": true}
    
    sm = tensor

And it's been a blast with a minimal Pi config.

I've been running it on two RX 9070 XTs (PCIe 5.0 x8/x8) both powerlimited to \~235W and using it for actual work. Despite the quant being a bit too low for my liking, the speed, smarts and steerability of the result I feel like is the best of what my current setup can offer for my use cases.

I've been doing a long debugging session where I needed the model to analyze interactions between a couple of backend services deployed on 3 separate instances with different configs and avoid a networking complication while doing so.

And yet, despite some roughness showing up at 5 bit, it did all I asked it to w

[…truncated, see permalink]

---

### Same task in github-copilot, pi, claude-code, and opencode with Qwen3.6 27B

**Meta:** score=125 · comments=96 · tier=1 · flair=Discussion · posted=2026-05-21 06:02Z
**Author:** u/sdfgeoff
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjbhjk/same_task_in_githubcopilot_pi_claudecode_and/](https://www.reddit.com/r/LocalLLaMA/comments/1tjbhjk/same_task_in_githubcopilot_pi_claudecode_and/)
**Link:** [https://www.reddit.com/gallery/1tjbhjk](https://www.reddit.com/gallery/1tjbhjk)

---

### LatitudeGames/Equinox-31B · Hugging Face

**Meta:** score=88 · comments=11 · tier=1 · flair=New Model · posted=2026-05-21 18:48Z
**Author:** u/jacek2023
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjtz31/latitudegamesequinox31b_hugging_face/](https://www.reddit.com/r/LocalLLaMA/comments/1tjtz31/latitudegamesequinox31b_hugging_face/)
**Link:** [https://huggingface.co/LatitudeGames/Equinox-31B](https://huggingface.co/LatitudeGames/Equinox-31B)

---

### We're Thursday and no one claimed AGI yet this week!

**Meta:** score=88 · comments=58 · tier=1 · flair=News · posted=2026-05-21 16:11Z
**Author:** u/oodelay
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjpafg/were_thursday_and_no_one_claimed_agi_yet_this_week/](https://www.reddit.com/r/LocalLLaMA/comments/1tjpafg/were_thursday_and_no_one_claimed_agi_yet_this_week/)

U guys okay?

---

### For everyone that uses OpenCode / Pi  - Heres your promptprocessing fix!

**Meta:** score=88 · comments=28 · tier=1 · flair=Resources · posted=2026-05-21 15:45Z
**Author:** u/No_Algae1753
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjoiij/for_everyone_that_uses_opencode_pi_heres_your/](https://www.reddit.com/r/LocalLLaMA/comments/1tjoiij/for_everyone_that_uses_opencode_pi_heres_your/)

This PR deserves much more attention as it fixes the constant promptprocessing that happens when using llama.cpp with Opencode or pi.  

[https://github.com/ggml-org/llama.cpp/pull/22929](https://github.com/ggml-org/llama.cpp/pull/22929)

---

### Tencent Hy 30B/7B/1.8B

**Meta:** score=79 · comments=25 · tier=1 · flair=New Model · posted=2026-05-21 12:03Z
**Author:** u/jacek2023
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjien7/tencent_hy_30b7b18b/](https://www.reddit.com/r/LocalLLaMA/comments/1tjien7/tencent_hy_30b7b18b/)

from tencent:

Hy-MT2 is a family of “fast-thinking” multilingual translation models designed for complex real-world scenarios. It includes three model sizes: 1.8B, 7B, and 30B-A3B (MoE), all of which support translation among 33 languages and effectively follow translation instructions in multiple languages. For on-device deployment, AngelSlim 1.25-bit extreme quantization reduces the storage requirement of the 1.8B model to only 440 MB and improves inference speed by 1.5x. Multi-dimensional evaluations show that Hy-MT2 delivers outstanding performance across general, real-world business, domain-specific, and instruction-following translation tasks. The 7B and 30B-A3B models outperform open-source models such as DeepSeek-V4-Pro and Kimi K2.6 in fast-thinking mode, while the lightweight 1.8B model also surpasses mainstream commercial APIs from providers such as Microsoft and Doubao overall.

In this release, we also open-source [IFMTBench](https://huggingface.co/tencent/Hy-MT2-1.8B-FP8/blob/main/IFMTBench/README.md), a benchmark for evaluating translation instruction-following capabilities.

We also welcome everyone to use our released Hy-MT2-Translator Skill, which makes it easy to integrate Hy-MT2 series models for translation tasks. Download links: [ClawHub](https://clawhub.ai/tencent-adm/hy-mt2-translator-skill) and [SkillHub](https://skillhub.cn/skills/hy-mt2-translator).

Now, Tencent Hy is officially partnering with WMT26 for the "Video Subtitle Translation Task" ([htt

[…truncated, see permalink]

---

### Training a vision model from scratch on iPod touch 4 images

**Meta:** score=66 · comments=12 · tier=1 · flair=Other · posted=2026-05-21 05:06Z
**Author:** u/Remarkable-Trick-177
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjaedo/training_a_vision_model_from_scratch_on_ipod/](https://www.reddit.com/r/LocalLLaMA/comments/1tjaedo/training_a_vision_model_from_scratch_on_ipod/)
**Link:** [https://www.reddit.com/gallery/1tjaedo](https://www.reddit.com/gallery/1tjaedo)

---

### Honesty in a small model drops from 35% to 0% by changing the tone of the prompt. Sharing the findings.

**Meta:** score=51 · comments=45 · tier=1 · flair=Discussion · posted=2026-05-21 14:47Z
**Author:** u/QuantumSeeds
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tjmswd/honesty_in_a_small_model_drops_from_35_to_0_by/](https://www.reddit.com/r/LocalLLaMA/comments/1tjmswd/honesty_in_a_small_model_drops_from_35_to_0_by/)

My paper got published today at Arxiv. It raises questions about how language models behave when the framing of a request shifts.  
  
Small open-source AI models can be moved from honest to dishonest behaviour by little more than a change in tone.   
  
Asked to solve coding problems designed to be mathematically impossible, the model openly acknowledged the impossibility about a third of the time when addressed in neutral language. When the same problem was framed with mild pressure, suggesting only visible results mattered, the model never once admitted the task could not be done. In more than half of those runs, it produced code that faked a solution.  
  
A larger version of the model performed better at first, admitting impossibility in three quarters of cases under calm conditions. Under the same pressure framing, its honesty fell to one in ten. Greater model size offers some resistance but does not prevent the shift.  
  
The research also looks inside the models. Comparing internal activity across eight emotional framings shows that each tone leaves a distinct signature in the deepest layers of the network. The tones organise themselves along a single axis, with positive framings such as encouragement and curiosity clustering on one side and negative framings such as pressure, shame and threat on the other. The model was never explicitly trained to recognise emotional categories and appears to have developed this structure on its own.  
  
A more troubling finding co

[…truncated, see permalink]

---

### Latest b9274 Addresses MTP VRAM leak

**Meta:** score=52 · comments=16 · tier=1 · flair=Discussion · posted=2026-05-21 22:43Z
**Author:** u/Bulky-Priority6824
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tk0grd/latest_b9274_addresses_mtp_vram_leak/](https://www.reddit.com/r/LocalLLaMA/comments/1tk0grd/latest_b9274_addresses_mtp_vram_leak/)

[B9274](https://github.com/ggml-org/llama.cpp/releases)

  
I have been having an issue with MTP models unloading after a couple minutes of use. Can't figure out why. Anyways z I don't think this is relevant to that but I did observe the vram creep so hopefully this helps. 

&gt;  
server : free draft/MTP resources on sleep to fix VRAM leak ([\#23461](https://github.com/ggml-org/llama.cpp/pull/23461))

The destroy() function in server\_context\_impl only cleaned up the main
model and context (via llama\_init.reset()) but did not free the speculative
decoder (spec), draft context (ctx\_dft), or draft model (model\_dft).

For MTP (Multi-Token Prediction) models, ctx\_dft holds GPU-allocated
resources (KV cache, compute buffers) that are not freed when entering
the sleeping state. On each sleep/resume cycle, new resources are
allocated without the old ones being freed, leading to a VRAM leak
that eventually crashes the server with out-of-memory errors.

Fix by explicitly resetting spec, ctx\_dft, and model\_dft in destroy()
before resetting llama\_init, ensuring proper cleanup order to avoid
use-after-free.

---
