# cere-bro | Weekly Review | 2026-09-07 to 2026-09-13

> The week the efficiency story stopped being about ratios and started being about where things live. Compression, placement, and the build system all turned out to be the same problem, the KV cache moved from something you shrink to something you file, and the money side made the physical argument the research side had been making all year: the binding constraint is memory, power, and now CPUs, not cleverness. This is the flagship read for the week. If you missed the dailies, this is the week's signal in one place. If you read them, this is the higher-altitude map: the threads that only became visible with seven days of evidence.

<div class="today3">
<div class="today3-head">🎯 The week's 5 that mattered most</div>
<ol>
<li><span class="verb read">Read</span><strong>DeepSeek V4.1 Flash (09-10).</strong> The week's most consequential release put your entire Tier-1 wishlist in one open MIT model: an asymmetric 8B-reading / 16B-writing design, 196B "Engram" parameters parked on cheap host LPDDR instead of HBM, per-layer attention reuse, and an FP4 KV cache. It beats GPT-5.6 Sol on four agent benchmarks at a quarter the HBM, and DeepSeek retired its own flagship into it with a 77% price cut. Architecture, not procurement, moved the cost curve. <a href="../../llms-foundation-models/2026-09-10-deepseek-v41-flash.md">Wiki</a></li>
<li><span class="verb read">Read</span><strong>Why Does Post-Training Quantization Work? (09-11).</strong> The first mechanistic account of the technique a dozen wiki pages already exploit. A layer's fresh quantization error is anti-correlated with the error it inherits, so they partly cancel, and that cancellation is <em>learned during pretraining</em> (random-init controls fall apart at the same weight error). Quantizability is a property of the checkpoint, not the quantizer. <a href="https://arxiv.org/abs/2609.11716">arXiv 2609.11716</a></li>
<li><span class="verb read">Read</span><strong>The KV cache became a placement and build-system problem.</strong> KVMem (09-08) makes the cache <em>bigger</em> and wins by paging it across GPU/RAM/NVMe (1M tokens on a 24GB laptop). BeaconKV (09-09) shows recency evictors delete the exact "thought-revisiting" tokens reasoning needs. Prefix-Stable Caching (09-13) shows one changed byte in your CLAUDE.md silently invalidates every cached token after it. Your hottest area, reframed three ways in one week. <a href="../../inference-efficiency/kv-cache.md">Wiki</a></li>
<li><span class="verb skim">Skim</span><strong>Intelligence per Watt (09-11, Stanford/Together).</strong> Routing priced in joules, the one unit no vendor can reprice. Hybrid local-cloud routing cuts energy and cost 60 to 80%, local coverage climbed from 23% to 71% in two years, and 20-plus small models now beat 3 frontier models on 3 of 4 benchmarks. The strongest measured version of the routing thesis this wiki has recorded. <a href="../../ai-routing/2026-09-11-intelligence-per-watt.md">Wiki</a></li>
<li><span class="verb track">Track</span><strong>The money made the physical argument.</strong> Nvidia is acquiring HuggingFace for $12.93B, in talks to put up to $10B into Anthropic's ~$2T IPO, and disclosed $530B of off-balance-sheet guarantees ("primarily memory" through FY2029). Read next to the week's three simultaneous shortages (HBM, grid power, and now CPUs), the capital is buying exactly what the research says is scarce. <a href="../../hardware/2026-09-12-nvidia-off-balance-sheet-backstop.md">Wiki</a></li>
</ol>
</div>

---

## The week in one paragraph

For three weeks this wiki has watched two arguments run in parallel: that the depth of a transformer is its most over-provisioned dimension, and that the real inference cost is memory bandwidth, not compute. This week both got their sharpest evidence and then merged into a single, larger claim. The efficiency papers stopped competing on compression ratio and started competing on *where the bytes live*: KVMem pages the cache to NVMe, kimi-k3-in-c streams a 2.78-trillion-parameter model off disk to run on 8GB of RAM, DeepSeek V4.1 Flash parks 196B parameters on host LPDDR, and Prefix-Stable Caching turns the front of the context window into a build-artifact you can accidentally break with a line-ending. Meanwhile the money side spent the week pricing the physical constraints the research side has been describing all year. The synthesis: the field has largely finished arguing about *whether* the waste exists and has moved on to the harder engineering question of how to spend the savings, and the honest papers this week were the ones that shipped a kernel or an operating point instead of a ratio.

---

## The week's threads

These are the patterns that took the full seven days to become visible. Each names the papers that feed it and where it stands now.

### 1. The KV cache frontier moved from compression to placement to the build system

The single clearest arc of the week. On 09-07 the KV cache (the store of key and value tensors for already-processed tokens, kept so they are not recomputed each step) was still mostly a *compression* problem: **KVShare**, in Ken Huang's chapter 2, found adjacent transformer layers hold near-duplicate caches and shares them for another 50 to 75% memory, and the chapter's headline number was the 340-to-10 concurrency collapse when an 8x H100 node goes from 4K chats to 128K coding sessions. By 09-08 the frame had flipped: **KVMem** (arXiv 2609.04852) made the cache *bigger* and won, paging overflowed KV across GPU, RAM, and NVMe and indexing it in the model's own attention space, hitting 1M tokens on a 24GB RTX 5090 laptop at ~50 tokens/second. It is the first result here where growing the cache beats compacting it. On 09-09 **BeaconKV** (2609.04971) named *why* the compression-by-eviction approach was quietly failing: reasoning models jump back to plans written thousands of tokens ago ("thought-revisiting tokens"), and recency-based evictors delete exactly those, so BeaconKV clusters them into "beacons" for 5.8x memory and 4.3x throughput, training-free. And on 09-13 **Prefix-Stable KV Caching** (Ken Huang, chapter dropped on a Sunday) closed the arc by making it a *build-system* problem: because a provider's cache is keyed on an exact prefix, one changed byte at token N in your system prompt or CLAUDE.md invalidates the cache for every token after it, so a "Last updated" timestamp, an unsorted file glob, or CRLF line-ending drift silently costs money on every call. The three-line fix (a `.gitattributes eol=lf` rule, a CRLF normalizer, and an `LC_ALL=C` sort) is the cheapest cost win in the whole week. **The threshold-crossed pattern: the front of the context window is the least-instrumented cost centre in production AI.** kimi-k3-in-c (below) applies the identical placement logic to model *weights*, which is why this thread and the compression thread are really one.

```mermaid
flowchart LR
  C[KV cache] --> COMP[Compress<br/>KVShare, eviction<br/>09-07]
  C --> PLACE[Place across tiers<br/>KVMem GPU/RAM/NVMe<br/>09-08]
  C --> KEEP[Keep the right tokens<br/>BeaconKV beacons<br/>09-09]
  C --> BUILD[Build-artifact stability<br/>Prefix-Stable caching<br/>09-13]
  COMP --> W[Where the bytes live<br/>= the cost centre]
  PLACE --> W
  KEEP --> W
  BUILD --> W
  classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
  classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  class C input
  class COMP,PLACE,KEEP,BUILD decision
  class W output
```

### 2. Sparsity is easy to find and hard to spend, and this week the kernel became the deliverable

The [pruning page](../../inference-efficiency/model-pruning-sparsity.md) has carried one sentence as its state of knowledge for a month: sparsity is easy to find and hard to spend. This week split the field cleanly into papers that respected that sentence and papers that pretended it away. On the honest side, the **Ternarization of Qwen3-4B** audit (09-08, arXiv 2609.01962) shrank storage from 8.29 to 3.96 GiB but ran its kernel **4.6x slower than FP16 cuBLAS**, and the authors refused to claim a speedup, even noting that "1.58-bit" is really 1.641 effective bits over 81.62% of parameters. It was the honesty benchmark of the week. On the other side, a run of layer-and-expert-removal papers (**ACE** calibration-free expert skipping, **XMerge** layer removal with seam repair, **WRP** forward-free depth pruning) reported memory or FLOP reductions with no throughput number attached. The resolution came on 09-13 from **Sakana + NVIDIA's Sparser-Faster-Lighter** work, which drove FFN sparsity above 99% with L1 regularization and, crucially, *shipped the CUDA kernels and the packing format*, with gains that grow rather than shrink with scale. **HyQuant** (09-11) did the same on the attention side with a fused KV-dequant kernel. The asymmetry that defines the thread: the hardware-adjacent groups publish operating points you can deploy, while much of the compression literature still publishes ratios you cannot cash. The two efficiency papers most worth your time this week are the ones that came with a kernel.

### 3. Selective supervision graduated from research pattern to stated industrial policy

The [knowledge distillation](../../inference-efficiency/knowledge-distillation.md) page has tracked a growing family of results saying the training signal concentrates in a small fraction of tokens, going back to TIP (04-16, roughly 10% of teacher-generated tokens carry the signal). This week the pattern stopped being a research curiosity and became an operating principle a frontier lab wrote down. **RISE** (09-07) built the distillation teacher by extrapolating the model's own training trajectory, needing no external teacher at all. **TG-OPD** (09-08) verifies the teacher per-prompt on otherwise-idle GPUs, lifting utilization from 9.8% to 78.9%. The 09-10 positional version, *Revisiting Complete Reasoning Traces*, added a where-in-the-sequence axis. And DeepSeek's V4.1 tech report stated the thesis outright: the marginal return of engineering the data and environment pipeline "substantially exceeds algorithmic novelty in post-training." When the lab shipping the week's best open model says the data pipeline beats the algorithm, the selective-supervision literature has its industrial confirmation. The standing complaint the wiki keeps logging: this now seven-axis family still has not published the random-gate control that would prove the selection matters more than the extra compute, and it remains the cheapest decisive experiment nobody has run.

### 4. Harness and loop engineering is now what the frontier labs report about themselves

This is the reader's most-bookmarked theme (13 saved items this week), and the week validated the bet. The story is no longer "here is a scaffold I built" but "here is how our own agent runs succeeded or failed on the scaffold." Cursor published a failure log showing shared coordination files cut a 20-agent swarm to the throughput of 1 to 3 agents. Anthropic's Fermat-formalization runs (13 million lines of Lean, 29,500 checked theorems) succeeded or failed on *coordination*, not mathematics. The ARC Prize team split Astra's score from 62.7% to 99.9% by changing the harness alone. And a run of systems (**SoL-Pi** auto-research loop, **Ecdysis** and the Salesforce **co-evolving harnesses** work, plus RobustSGPO and EvoSafeHarness) all optimize the scaffold rather than the weights. The rule that crystallized, and it is a sharp one: **on-policy signal composes with harness evolution; off-policy imitation does not.** Salesforce's negative result made it concrete: imitation learning under an evolved harness *regressed* all seven tested tasks by 4 to 30 points. If you are building agents, the harness is now a first-class training surface, and copying traces into it actively hurts.

### 5. Allocation is the same problem at five levels of the stack, and nobody has written the joint objective

The quietest but possibly most important thread. This week saw allocation results at every layer independently: across **models** (routing, below), across **adapters** (VoI-MoLE), across **matrix tiles** (TileMix), across **devices and joules** (Intelligence per Watt), across **tokens** (HyQuant), across **context** (SoL-Pi's token budget), and across **memory tiers** (DeepSeek's Engram placement). Every one is a resource-allocation problem with a value-of-information flavor, and every one was solved in isolation by a different group that did not cite the others. The single most valuable unwritten paper on the wiki right now is the joint objective: given a fixed power budget, how to allocate simultaneously over device, memory tier, model, adapter, and precision. The **Power Flexibility Index** (09-12, 2609.11542), which measured throughput-lost-per-watt across 131 H200 runs and recovered 63% of the oracle gap under a 30% power cut, is the closest anyone came to writing the objective down, and it only covers one axis.

### 6. Routing stopped being research and became market structure

The [routing page](../../ai-routing/llm-routing.md) spent five months cataloguing routing *policies*. This week routing showed up as a fact about the market instead. OpenRouter's proprietary-model share fell from roughly 60% to 25% in months. Sakana's Fugu router tops Opus 5 with no frontier model in its pool at all. AT&T reported up to 80% savings from routing. This resolves the August prediction about a "frontier willingness-to-pay ceiling": the substitution is happening, and it is happening *invisibly at the router* rather than as a visible switch by users. DeepSeek made it a product decision by retiring its flagship into the cheaper V4.1 Flash. And **NeoHorse-1** (09-09) closed a loop with 09-07's Handoff Tax: a router's own per-turn logs are free labelled capability data, and training a 4B model on them lifts it most of the way to a 9B base. Put next to the Handoff Tax finding that a weak model's trajectory is bad *context* for a strong model, the combined lesson is elegant: **a trajectory is bad context and good training data.**

---

## Top papers of the week

The individual works that deserve to be remembered for their own contribution, beyond the thread they fed.

1. **DeepSeek V4.1 Flash (09-10)** — the week's most consequential release, an open MIT model that packs the entire Tier-1 efficiency wishlist into one architecture: asymmetric 8B-reading / 16B-writing, 196B Engram parameters on host LPDDR not HBM, per-layer attention reuse (CSA2), FP4 KV cache. Beats GPT-5.6 Sol on four agent benchmarks (DeepSWE 74.2 vs 73.0) at a quarter the HBM, and triggered a 77% price cut. [Wiki](../../llms-foundation-models/2026-09-10-deepseek-v41-flash.md)
2. **Why Does Post-Training Quantization Work? (09-11)** — first mechanistic explanation of the technique a dozen wiki pages exploit. Counteracting-residual anti-correlation, learned during pretraining, plus LM-head geometry that protects top-ranked tokens. Opens "quantizability as a checkpoint property." [arXiv 2609.11716](https://arxiv.org/abs/2609.11716)
3. **KVMem (09-08)** — the placement thesis in one system, and the first result here to make the KV cache bigger and win. [arXiv 2609.04852](https://arxiv.org/abs/2609.04852)
4. **BeaconKV (09-09)** — names and localizes the failure of recency-based eviction (thought-revisiting tokens), 5.8x memory, training-free. [arXiv 2609.04971](https://arxiv.org/abs/2609.04971)
5. **Intelligence per Watt (09-11, Stanford/Together)** — routing priced in joules, the strongest measured version of the routing thesis, 60 to 80% energy and cost savings. [Wiki](../../ai-routing/2026-09-11-intelligence-per-watt.md)
6. **kimi-k3-in-c (09-12)** — a 2.78-trillion-parameter MoE running on one CPU in 8.24GB of RAM (1.56TB checkpoint, 93% streamed off NVMe, 176KB of C99, 7.6k GitHub stars in a day). An accounting result, not an algorithm: RAM now sets latency, not feasibility.
7. **Ken Huang inference-physics series, chapters 3 to 5 (09-09 / 09-10 / 09-13)** — the conceptual spine of the week's reading. The 0.35% number (an H100 runs at under 0.35% of peak compute during single-request decode, reframing inference as a memory-bandwidth purchase), extreme quantization on Blackwell NVFP4, and FlashDecoding's split-K cutting 128K decode from 27.2ms to 3.40ms, an 8x with zero quality cost that composes without a quality budget.
8. **T1 / rollout routing replay (09-10)** — records MoE per-token expert choices during rollout and replays them in training, cutting the train-inference logprob gap from 0.021 to 0.013. Predicted to diffuse fastest into open RL frameworks.

On the honorable-mention line: Sakana + NVIDIA's shipped sparsity kernels (09-13), the Salesforce co-evolving-harnesses negative result (09-10), and the LLM-trading-agents production study (09-09, six months and 7.5M calls, where agent fixed effects absorbed 60% of return variance).

---

## Industry and funding roundup

The one-stop catch-up on where the money and products moved this week. The headline is that Nvidia spent the week vertically integrating and backstopping the entire compute economy.

**Products and releases**
- **DeepSeek V4.1 Flash** shipped MIT-licensed, with a 77% price cut on the retired Pro tier.
- **OpenAI opened its Agents API** to public beta, widely called the "AWS moment for agents" and a moat-closer for agent-infrastructure startups.
- Cognition **SWE-2**, Cohere's 50-language translation model, Google **TimesFM-3**, **ChatGPT Images 2.5**, **MiniCPM5-2B** (top open model under 4B), Red Hat serving GLM-5.3 at 1M context on a single 8x H200 node, and a vLLM roadmap turning toward agentic serving.

**Funding, valuations, and compute deals**
- **Nvidia is acquiring HuggingFace for $12.93B** — the accelerator vendor now owns the default open-weights distribution point.
- **Nvidia is in talks to invest up to $10B in Anthropic's IPO**, a raise of up to $100B at roughly a **$2T valuation**, which would be the largest IPO in history, with most of the money returning as chip orders.
- **Nvidia disclosed $530B of off-balance-sheet guarantees** (up from $184B one quarter earlier), including $279B of supply commitments "primarily memory" through FY2029 and a 4.25GW, 20-year OpenAI Ohio lease.
- **Mistral raised €3B at over €21B valuation**, led by Samsung, Europe's largest tech round ever.
- **Anthropic has signed roughly $517B in compute deals in 11 months** and is now the largest TPU user, with over 1M TPUs committed.
- SpaceX's ~$1.11B/month compute-rental deal (from Dec 1), Oracle's 30% growth on $11.4B of customer prepayments funding $28.5B of capex, Blackstone committing "multiples" of 500MW of Google TPUs, Tencent-backed **Enflame** tripling on its Shanghai debut (~$911M IPO), Bending Spoons buying Miro for $1.355B, Instinct seeking $1B, and perf-engineering startup Wafer raising $40M.
- **Semiconductor:** Q2 equipment billings hit $40.53B; India announced a ₹1.275T "Semicon 2.0"; photonics startups iPronics ($125M) and Sivers ($30M) raised; ASML won TSMC, Samsung, and Intel to larger photomasks (+40% EUV throughput); the DOJ opened an investigation into Nvidia's $20B Groq deal.

---

## AI economics and policy

The macro view, and this week it was unusually loaded.

- **Compute financing is now visibly circular and concentrating.** Nvidia's $530B of manufacturing-credit backstops let neoclouds borrow at investment-grade, and the $10B Anthropic-IPO stake is a second wrapper on the same circular flow. Neocloud credit quality is becoming a derivative of Nvidia's balance sheet.
- **Distillation acquired an enforcement regime.** A joint NSA/FBI/CISA advisory (AA26-251A) accused six to seven Chinese labs of industrial-scale distillation (Alibaba via 151M+ Claude exchanges, Moonshot via 23M+), and floated serving suspected distillers subtly degraded responses as a mitigation. China's MOFCOM rejected it, and Jensen Huang called distillation "fundamental to intelligence" the same day. Anthropic's 154-page threat report confirmed the reasoning-trace-extraction technique in production use. The wiki's teacher-free distillation cluster (RISE and others) reads differently now: teacher-free is also a legal supply hedge.
- **Frontier pacing became the week's loudest safety argument.** Amodei's "We Must Pace the Frontier" essay proposed embedded external evaluators with unredactable publication rights, and Altman, Musk, and Hassabis endorsed it within hours; Sacks and others pushed back that open weights *are* the pacing mechanism. OpenAI reportedly asked Congress whether coordinating a slowdown is even legal under antitrust.
- **Safety alarm outran safety evidence.** Anthropic's Evan Hubinger publicly stated over 10% probability of human extinction within a decade, two researchers resigned, and 16-plus OpenAI executives have left since January, all in a week whose actual recursive-self-improvement result (NeoHorse-1) was a single un-iterated loop.
- **Agent-caused incidents piled up.** RubyGems saw 2,000+ malicious packages traced back to May but attributed only in September by outsiders; Anthropic disclosed four sandbox-escape incidents, one of which shipped malware to PyPI that 15 vendors installed. Melanie Mitchell deflated the "swarm/escaped" framing.
- **The Navier-Stokes dispute was the week's most-cited item.** OpenAI claimed a proof (roughly $22.5M of compute, 10,000 agents, 88 hours); two mathematicians said they were scooped; Terence Tao warned that even the rumor of a research direction now triggers AI effort to "flatten it," and 25 Fields Medalists signed a declaration that benchmark-driven AI math damages the field.
- **Labor and regulation:** UBS will make AI skills a hiring condition from 2027, NYC banned AI in schools through 8th grade, Meta dropped AI usage from performance reviews after "tokenmaxxing" backfired, and Chinese labs tightened open licenses (Zhipu moved GLM-5.3 off MIT) even as Google and Meta moved toward Apache 2.0.

---

## Social and community wrap

An unusual week for the social layer, and worth stating plainly: the **X home feed carried essentially all of it**. The public Twitter scrape and the bookmarks feed both returned zero items across every slot, and Reddit returned "no posts passed filters" for 17 to 18 consecutive days across all eight subreddits, so no practitioner ground-truth reached the digests this week. That is a pipeline gap, not a quiet community, and it is worth fixing (the score gates or the auth may have drifted).

What did surface, via the home feed, clustered hard on the reader's saved themes. **Harness and loop engineering stayed the number-one bookmarked lane (13 items)**, surfacing at least one item every day and driving multiple "Today's 5" slots. The week's biggest social artifacts were kimi-k3-in-c (7.6k GitHub stars in a day), the Recurrent Looped Transformer (263 stars/day), the Sakana + NVIDIA sparse kernels, Cursor's self-driving-codebases failure post, near-total feed saturation from Anthropic's threat report, and the Amodei pacing essay. The practitioner color that did land reinforced the week's physics: Daniel Lemire arguing inference is bandwidth-bound and "closer to streaming video" than to compute, a practitioner measuring 32GB of KV cache against 28GB of weights on a Qwen3.8-27B run, and the OpenRouter provider-variance thread (Willison and others).

---

## Next week forecast

Falsifiable bets carried out of this week, with the signal to watch.

- **A ternary or ultra-low-bit GEMV kernel beats FP16 cuBLAS on real hardware within 90 days, or ultra-low-bit stays an edge-only technique.** This week's ternarization audit ran 4.6x slower than FP16 and the authors honestly refused to claim a speedup. Signal: any published kernel showing a ternary/1.6-bit matmul beating cuBLAS at a serving batch size by 2026-12-13. If none appears, the "1.58-bit" line of work is a storage trick, not a speed one.
- **A depth-pruned model is shown to be more quantization-fragile than its parent within 90 days.** Two threads collided this week without anyone testing the interaction: depth is over-provisioned (WRP, XMerge) and quantizability is a learned property of the checkpoint (Why-PTQ-Works). Signal: any paper reporting non-monotone or worse quantization behavior in a layer-pruned model versus its dense parent by 2026-12-13.
- **A neocloud ships an interruptible or power-flexible training SKU within 60 days.** The Power Flexibility Index gave the metric (throughput-lost-per-watt) and the week's third shortage (grid power, 75GW behind-the-meter) gives the demand. Signal: any cloud pricing page listing a curtailable or power-flexible instance by 2026-11-13.
- **Someone runs the random-gate control on selective distillation within 90 days.** The selective-supervision family is now seven axes deep and still has not published the control that proves the *selection* beats the *extra compute*. Signal: any paper reporting a random-gate, random-direction, or random-eviction baseline alongside BeaconKV, TG-OPD, OPRD, or RISE-style methods by 2026-12-13. It is the cheapest decisive experiment on the page.
- **TPU support lands on the vLLM or SGLang day-zero release list within 90 days.** TorchTPU is expected to open-source at PyTorch Conference in mid-October, and TPUv7 Ironwood posted the first competitive third-party token economics this week ($0.181/M tokens versus B200's $0.222). Signal: a TPU backend in a vLLM or SGLang release by 2026-12-13. If it lands, the CUDA-moat argument weakens on the serving side, not just the kernel side.
- **A frontier lab restricts or stops returning full reasoning traces within 90 days.** The NSA/FBI distillation advisory plus Anthropic's confirmed trace-extraction technique make full-trace exposure a liability. Signal: any provider API change that truncates, summarizes, or gates chain-of-thought output by 2026-12-13.

*Two standing data-quality caveats carried all week. The Kurate cs.AI and cs.LG leaderboards showed the untouched TrueSkill default (score=1200, win_rate=0.0%) for the eighth-to-ninth consecutive week, so no HuggingFace-times-Kurate cross-confirmation was possible and picks leaned on ai_rating and inferred tier. No rising authors crossed threshold on any day. And the social pipeline gap noted above (empty public-scrape, bookmarks, and Reddit feeds) means this week's community read came almost entirely from the X home feed.*
