# r/LocalLLaMA | 2026-05-17 IST | sort=top
> Scraped 2026-05-17 09:29 IST | lookback=24h | tier_default=1
> Inference, quantization (GGUF/AWQ/EXL2), KV cache tricks, llama.cpp internals, kernel tuning, GPU rigs. Single highest-signal sub for Tier 1 efficiency.

### MTP PR Merged!!!

**Meta:** score=683 · comments=103 · tier=1 · flair=News · posted=2026-05-16 12:13Z
**Author:** u/Valuable_Touch5670
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1terzq4/mtp_pr_merged/](https://www.reddit.com/r/LocalLLaMA/comments/1terzq4/mtp_pr_merged/)
**Link:** [https://i.redd.it/1mwo5r3wqh1h1.jpeg](https://i.redd.it/1mwo5r3wqh1h1.jpeg)

---

### That's a good news...

**Meta:** score=652 · comments=210 · tier=1 · flair=News · posted=2026-05-16 11:09Z
**Author:** u/Pjotrs
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1teqnf2/thats_a_good_news/](https://www.reddit.com/r/LocalLLaMA/comments/1teqnf2/thats_a_good_news/)
**Link:** [https://i.redd.it/40kc44wjfh1h1.png](https://i.redd.it/40kc44wjfh1h1.png)

---

### MTP support merged into llama.cpp

**Meta:** score=511 · comments=104 · tier=1 · flair=News · posted=2026-05-16 12:15Z
**Author:** u/tacticaltweaker
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tes1wx/mtp_support_merged_into_llamacpp/](https://www.reddit.com/r/LocalLLaMA/comments/1tes1wx/mtp_support_merged_into_llamacpp/)

PR [22673](https://github.com/ggml-org/llama.cpp/pull/22673) has been merged into master! 🎉

---

### Local Qwen 3.6 vs frontier models on a coding primitive: single-file HTML canvas driving animation - results and GIFs

**Meta:** score=294 · comments=98 · tier=1 · flair=Discussion · posted=2026-05-16 19:51Z
**Author:** u/Fragrant-Remove-9031
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tf3p6c/local_qwen_36_vs_frontier_models_on_a_coding/](https://www.reddit.com/r/LocalLLaMA/comments/1tf3p6c/local_qwen_36_vs_frontier_models_on_a_coding/)
**Link:** [https://www.reddit.com/gallery/1tf3p6c](https://www.reddit.com/gallery/1tf3p6c)

---

### Qwen3.6-35B-A3B and 9B are officially on the public Terminal-Bench 2.0 leaderboard!

**Meta:** score=252 · comments=59 · tier=1 · flair=Discussion · posted=2026-05-16 07:19Z
**Author:** u/Creative-Regular6799
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1temio0/qwen3635ba3b_and_9b_are_officially_on_the_public/](https://www.reddit.com/r/LocalLLaMA/comments/1temio0/qwen3635ba3b_and_9b_are_officially_on_the_public/)

Qwen3.6-35B-A3B and 9B are officially on the public Terminal-Bench 2.0 leaderboard!

little-coder × Qwen3.6-35B-A3B hit 24.6% (±3.2), and **now land above Gemini 2.5 Pro on Gemini CLI (19.6%)** and Qwen3-Coder-480B on Terminus 2 (23.9%). I didn’t expect the scaffold-model gap from Polyglot to hold on a benchmark this hard but it did!

little-coder × Qwen3.5-9B came in at 9.2% which is more humble. Yet, it also shows again that **sub-10B local models are now measurable on a hard agentic benchmark**, not assumed unworthy of a slot.

Just felt it was right to follow up here as you requested, and say a genuine thanks to this community. It really is the place currently driving innovation toward less compute, and this run exists there because you pushed for it.

Now it’s time to head for the top of the leaderboard 👀 let’s go open source!

Leaderboard: https://www.tbench.ai/leaderboard/terminal-bench/2.0

[https://github.com/itayinbarr/little-coder](https://github.com/itayinbarr/little-coder)

---

### Strix Halo Llama.cpp MTP Benchmarks: 27B Gets Much Faster, 35B Is Mixed

**Meta:** score=110 · comments=53 · tier=1 · flair=Discussion · posted=2026-05-16 16:41Z
**Author:** u/xjE4644Eyc
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1teypb8/strix_halo_llamacpp_mtp_benchmarks_27b_gets_much/](https://www.reddit.com/r/LocalLLaMA/comments/1teypb8/strix_halo_llamacpp_mtp_benchmarks_27b_gets_much/)

### **TL;DR**
All models were Qwen3.6

**27B-MTP vs Base 27B (15k single-turn): Faster overall**

* **Total Time (wall):** 87.44s → 77.39s (**10.05s faster** / -11.50%)
* **Generation:** 7.63 → 16.15 t/s (+111.77% speedup)
* **Prompt Processing:** 279.75 → 244.90 t/s (-12.46% slowdown)

**35B-MTP vs Base 35B (15k single-turn): Slower overall**

* **Total Time (wall):** 20.83s → 23.16s (**2.33s slower** / +11.17%)
* **Generation:** 48.18 → 56.12 t/s (+16.47% speedup)
* **Prompt Processing:** 972.18 → 811.90 t/s (-16.49% slowdown)

**27B-MTP vs Base 27B (5-turn chat, ~28.5k context): Massive time savings**

* **Total Time (wall):** 258.65s → 200.55s (**58.10s faster** / -22.46%)
* **Turns 2-5 (wall):** 211.37s → 155.33s (**56.04s faster** / -26.51%)
* **Avg Generation:** 7.61 → 17.98 t/s (+136.41% speedup)
* **Avg Prompt Processing:** 254.20 → 207.87 t/s (-18.23% slowdown)

**35B-MTP vs Base 35B (5-turn chat, ~28.5k context): Roughly tied, slightly slower**

* **Total Time (wall):** 58.86s → 60.24s (**1.38s slower** / +2.34%)
* **Turns 2-5 (wall):** 47.96s → 49.21s (**1.25s slower** / +2.62%)
* **Avg Generation:** 46.66 → 58.23 t/s (+24.80% speedup)
* **Avg Prompt Processing:** 826.47 → 703.45 t/s (-14.89% slowdown)

**Terminology:**

* `wall` = real end-to-end elapsed time from sending the request to receiving the full response.
* `pp` = prompt processing throughput (tokens/sec).
* `gen t/s` = generation throughput (tokens/sec).

---

### **Hardware / Software**

* **CPU:** AM

[…truncated, see permalink]

---

### Corsair desktop PC with Ryzen 395 and 128GB of unified RAM, has anyone tested it for LLM? Seems "a good" price

**Meta:** score=95 · comments=63 · tier=1 · flair=Question | Help · posted=2026-05-16 17:19Z
**Author:** u/Acu17y
**Reddit:** [https://www.reddit.com/r/LocalLLaMA/comments/1tezqlb/corsair_desktop_pc_with_ryzen_395_and_128gb_of/](https://www.reddit.com/r/LocalLLaMA/comments/1tezqlb/corsair_desktop_pc_with_ryzen_395_and_128gb_of/)
**Link:** [https://www.corsair.com/it/it/p/gaming-computers/cs-9080002-pe/corsair-ai-workstation-300-amd-ryzen-ai-max-395-processor-amd-radeon-8060s-igpu-up-to-96gb-vram-128gb-lpddr5x-memory-1tb-m2-ssd-win11-home-cs-9080002-pe](https://www.corsair.com/it/it/p/gaming-computers/cs-9080002-pe/corsair-ai-workstation-300-amd-ryzen-ai-max-395-processor-amd-radeon-8060s-igpu-up-to-96gb-vram-128gb-lpddr5x-memory-1tb-m2-ssd-win11-home-cs-9080002-pe)

---
