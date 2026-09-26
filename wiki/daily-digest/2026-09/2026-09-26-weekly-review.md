# cere-bro | Weekly Review | 2026-09-20 to 2026-09-26

> Last week the argument was that the cost of AI lives in where the bytes sit. This week the market agreed and repriced it. Anthropic cut cache reads 60% while cutting the headline price only 20%, OpenAI cut cached input up to 90%, and the architectures that make standing context cheaper (prefill exit, disaggregated quantization, tiered KV on flash) arrived a few days after the price cuts, not before. Meanwhile a new category, the one-forward-pass "decision model," went from launch to 160 projects to a calibration reckoning in seven days, and the week's most important efficiency paper showed that quantizing the KV cache can quietly delete a model's refusals while perplexity barely moves. The throughline: the cheap parts of the stack are now doing real work, and our instruments cannot see what they break.

<div class="today3">
<div class="today3-head">🎯 The week's 5 that mattered most</div>
<ol>
<li><span class="verb read">Read</span><strong>Alignment collapse under KV cache quantization (09-26).</strong> Across 11 models from 3.8B to 72B, low-bit KV caches strip safety behavior long before quality metrics notice: Mistral-7B loses 15.2% of its refusals at a 1.03x perplexity cost, and the effect reproduces with vLLM's FP8 KV. A 20-prompt diagnostic recovers up to 97.2%. Your KV cache and compression work now needs a refusal check, not just a perplexity check. <a href="../../inference-efficiency/2026-09-26-kv-quantization-alignment-collapse.md">Wiki</a></li>
<li><span class="verb read">Read</span><strong>Prefill is the bill: Disaggregated Quantization + HySparse2 (09-24).</strong> One gives prefill and decode separate checkpoints (NVFP4 prefill, 1-3 bit decode, +32.5 MMLU-Pro for 1-bit decoders, validated to 2.8T parameters). The other publishes the prefill-exit mechanism that DeepSeek V4.1 Flash and MiMo V3 both adopted (KV 6.72 to 2.69 GB at 1M tokens). <a href="../../inference-efficiency/2026-09-24-disaggregated-quantization-prefill-decode.md">Wiki</a></li>
<li><span class="verb read">Read</span><strong>The cache price war (09-23).</strong> Claude Opus 5.5 at $4/$20 with cache reads down from $0.50 to $0.20 per million, GPT-6 Luna at $0.01 cached, OpenAI cached input down up to 90%. The price line vendors cut hardest is the one agents actually pay for: re-reading context they already sent. <a href="../../hardware/2026-09-23-price-war-cache-reads.md">Wiki</a></li>
<li><span class="verb skim">Skim</span><strong>Decision models: cascades need calibration AND disagreement (09-25, 09-26).</strong> CMU's confidence cascade keeps 92.5 of 93.1 judge accuracy at 56.8% of the fee, but Penn shows cheap LLM judges repeat 96% of the decision model's confident errors, capping any cascade gain at about +1.5 points. Your routing work in one rule. <a href="../../ai-routing/2026-09-25-jev-as-a-judge-confidence-cascade.md">Wiki</a></li>
<li><span class="verb track">Track</span><strong>Every processor is now scarce (09-24, 09-25).</strong> SemiAnalysis says "GPU supply has gone to zero," CPUs have six-month lead times and the CPU:GPU ratio is moving from 1:8 toward 1:4, and memory passed 50% of semiconductor revenue. The "cheap tier" that every offload paper assumes is getting expensive. <a href="../../hardware/2026-09-24-semianalysis-clustermax-3.md">Wiki</a></li>
</ol>
</div>

---

## The week in one paragraph

For two weeks this wiki has tracked one idea from different sides: inference cost is a memory-bandwidth problem, so the winning moves are about where bytes live, not how many FLOPs you save. The 09-13 weekly watched the KV cache (the stored attention keys and values for past tokens, kept so they are not recomputed) move from compression to placement to the build system. This week the idea moved two steps further. First, it reached pricing: the part of the bill that vendors cut hardest was cache reads, because agents spend most of their tokens re-processing context they already sent, which SemiAnalysis this week named "midfill," a fourth inference regime next to prefill and the two kinds of decode. Second, it reached safety: the same cheap memory tricks that save money turn out to degrade exactly the behaviors that benchmarks do not measure. The week's other big story, the decision-model boom, is the same pattern in routing: a tiny model that makes one forward pass and emits a probability is extremely cheap, and the whole question is whether that probability can be trusted. By Saturday the answer was "as a ranker and labeller, yes; as an unsupervised gate, not yet."

---

## The week's threads

### 1. The fast tier cannot be bought, so the bytes move down

This continues and escalates last week's placement thread. Ken Huang's chapter 8 (09-20) set the scene with the "decode inversion": reasoning workloads now spend 90 to 95% of serving cycles in decode, the memory-bound phase, where historically prefill took 75 to 80%. One 64k-token reasoning request needs over 18 GB of KV cache, so a Rubin Ultra chip trimmed to about 200 GB of HBM fits around 11 concurrent sessions before weights. Chapter 9 (09-21) pushed it to the million-token case: 137.44 GB of KV per user on an 80-layer 70B model, meaning two or three streams per 8xH100 node. [HBM is not coming to the rescue](../../inference-efficiency/2026-09-20-test-time-compute-decode-inversion.md), so the research moved down the hierarchy. **LM-CXD** (09-24) showed that a stock CXL-attached SSD is no faster than NVMe, but chunk-aware management brings a CXL flash prefix cache to within 1.5x of DRAM and improves time-to-first-token up to 4.03x ([summary](../../hardware/2026-09-24-lm-cxd-cxl-ssd-prefix-cache.md)). SK hynix's roadmap in Semiconductor Week 38 (09-23) named "tiered KV cache management" as a product line, in the same report where memory passed 50% of a $425B quarter ([summary](../../hardware/2026-09-23-semiconductor-week-38-hbf-pim-tiered-kv.md)). **Quail** (09-26) scheduled KV lifetimes by the SQL query plan and cut KV "regret" from 50.3M to 18.0M on AI-SQL workloads. The complication arrived on 09-25: the Pragmatic Engineer reported a CPU shortage with spot discounts gone and 10 to 20% price increases, which means the DRAM and host tiers the offload papers treat as cheap are themselves being rationed ([summary](../../hardware/2026-09-25-cpu-shortage-agents-and-rl.md)).

```mermaid
flowchart LR
  HBM[HBM<br/>capped, sold out] -->|spill| DRAM[Host DRAM<br/>now rationed]
  DRAM -->|spill| CXL[CXL flash<br/>LM-CXD 1.5x DRAM]
  CXL -->|spill| SSD[NVMe SSD<br/>prefill weights ODP]
  P[Price cuts<br/>cache reads -60%] -.->|makes reuse pay| HBM
  S[Safety check<br/>refusals under low-bit KV] -.->|new gate| HBM
  classDef warn fill:#fee2e2,stroke:#ef4444,color:#7f1d1d
  classDef aux fill:#e0e7ff,stroke:#6366f1,color:#312e81
  classDef output fill:#d1fae5,stroke:#10b981,color:#065f46
  classDef decision fill:#fef3c7,stroke:#f59e0b,color:#78350f
  class HBM,DRAM warn
  class CXL,SSD output
  class P aux
  class S decision
```

### 2. Pricing ran ahead of architecture on prefill and cache

A new framing this week, extending last week's Prefix-Stable Caching finding (one changed byte early in a prompt invalidates every cached token after it). On 09-22 the [routing tax](../../ai-routing/2026-09-22-decision-model-benchmark-ladder-and-routing-tax.md) got a number: bouncing a session Opus to Sonnet to Opus cost 6.19 units versus 4.15 for staying on Opus, because each switch throws away a warm cache. The same day SemiAnalysis's [four-regime essay](../../hardware/2026-09-22-semianalysis-inference-data-movement.md) named midfill, the re-processing of standing context, as a regime of its own. On 09-23 the vendors priced exactly that line: Anthropic cut cache reads 60% against a 20% headline cut, and OpenAI cut cached input up to 90%. Then on 09-24 the architectures arrived. **Disaggregated Quantization** (arXiv 2609.26333, from the Alistarh group) keeps a high-precision NVFP4 checkpoint for prefill and a 1 to 3 bit checkpoint for decode, streaming the prefill weights from SSD for a 1.78x faster first token ([summary](../../inference-efficiency/2026-09-24-disaggregated-quantization-prefill-decode.md)). **HySparse2** (arXiv 2609.26368, Xiaomi) published the "prefill exit" design, where later layers reuse earlier layers' KV instead of computing their own, cutting prefill FLOPs 2.92x at 1M tokens ([summary](../../inference-efficiency/2026-09-24-hysparse2-two-level-kv-sharing.md)). A practitioner comparison noted DeepSeek V4.1 Flash and MiMo V3 both chose prefill exit independently. The order matters: the market cut the price of standing context before most published architectures made it cheaper to serve, which is a bet by the vendors that their internal systems already do.

### 3. The decision-model boom, from launch to calibration reckoning in seven days

This is the week's loudest thread and the one that most directly tests your routing research. "Decision models" (the category led by Jev, sometimes called System One models) answer a classification or routing question in one forward pass and return a probability, at roughly $0.04 per million input tokens. The arc ran day by day. On 09-20 a [72-hour census](../../ai-routing/2026-09-20-jev-ecosystem-census-72h.md) counted 160 projects, and the biggest was not a router but a context compactor that took a coding session from 156k to 62k tokens. Bespoke Labs' Nimble matched 90% of the closed model with a one-day LoRA on 2,676 examples. On 09-21 the [calibration reckoning](../../ai-routing/2026-09-21-jev-calibration-reckoning.md) began: a live trading bot answered at 85 to 88% confidence on nearly every call and lost 5.2%. On 09-22 GPT-6 Astra scored 100% on JevBench, saturating the benchmark in its first week. On 09-23 the first [calibration numbers](../../ai-routing/2026-09-23-decision-model-ece-numbers-arrive.md) arrived (expected calibration error 0.076), and Pydantic made the first recorded production swap to an open model for GitHub issue labelling. On 09-24 [CLM-8B](../../ai-routing/2026-09-24-clm-contrastive-system-one-model.md) showed the hosted decision model scoring below a plain pass@1 baseline when used as a best-of-N selector. On 09-25 CMU's [confidence cascade](../../ai-routing/2026-09-25-jev-as-a-judge-confidence-cascade.md) kept 92.5 of GPT-6 Astra's 93.1 judge accuracy at 56.8% of the fee. On 09-26 Penn found that [cheap LLM judges repeat 96% of the decision model's confident errors](../../ai-routing/2026-09-26-jev-vs-llm-rubric-judges-correlated-errors.md), capping the cascade's accuracy gain at about +1.5 points. **The rule that fell out is worth writing on the routing page: calibration decides how much a cascade saves; error diversity between tiers decides whether it adds accuracy.** A router that falls back to a model that makes the same mistakes is buying cost savings, not correctness.

### 4. Harnesses are a recurring cost, and harness gains overfit

This continues last week's harness thread, and the week closed the 09-19 prediction that harness-versus-backbone ablations would become standard (it was due at year end and closed on 09-22). **RRSI** (Google, arXiv 2609.24972) evolved a harness for up to +14.1 points in-distribution but only +4.7 out-of-distribution ([summary](../../agentic-systems/2026-09-22-rrsi-regularized-harness-evolution.md)). **Harness-Zero** (arXiv 2609.24974) distilled the harness into the weights and then removed it: 44.3% with no harness beat 41.7% with the harness attached ([summary](../../inference-efficiency/2026-09-22-harness-zero-harness-distillation.md)). **HarnessTax** priced 21 configurations at $0.67 to $1.33 per attempt with success rates packed between 96.7% and 97.8%, and heavy setups carried more than 10x the initial context ([summary](../../agentic-systems/2026-09-22-harnesstax-cost-success-frontier.md)). The 09-21 [code-as-substrate](../../agentic-systems/2026-09-21-code-as-agent-substrate.md) cluster added a rule: scaffolding substitutes for capability, so GraphSkillEvo gave a small model +4.01 but a large one only +1.76. The implication for cost work is direct. A harness is a standing-context tax paid on every call and pinned to one model version. The complication: SWE-Bench Pro V2 (thread 6) suggests HarnessTax's narrow 1.1-point success band may mostly reflect a saturated benchmark.

### 5. Allocation keeps spreading, and now it can remove safety

Last week's allocation thread (the same budget problem solved separately at five levels of the stack, with no joint objective yet) got six new instances on 09-23 alone. **KV-COBRA** (arXiv 2609.24298) allocates rank and bits per attention head at 0.5 to 4 bits per dimension ([summary](../../inference-efficiency/2026-09-23-kv-cobra-bit-rank-allocation.md)); **Colla-Q** (arXiv 2609.18131) allocates quantization per expert with an entropy-based minimax rule ([summary](../../inference-efficiency/2026-09-19-colla-q-moe-quantization-minimax.md)); Flash-dLLM allocates around memory I/O. On 09-25 **Neural Spectral Capacity** (arXiv 2609.23087) scored each layer's capacity from its shape alone and pruned LLaMA-7B to 5.7B with no calibration data, 5,900x faster than search ([summary](../../inference-efficiency/2026-09-25-neural-spectral-capacity-calibration-free-pruning.md)). LLM Compressor v0.14 made re-quantizing cheap with a Triton GPTQ about 15x faster ([summary](../../inference-efficiency/2026-09-25-llm-compressor-v0-14-triton-gptq.md)). Then 09-26 added the warning: the alignment-collapse paper names KV-COBRA directly, because an allocator that optimizes reconstruction error or perplexity will spend its bits on what those metrics see and starve the "safety subspace," which the paper measures as 100 to 1,000 times more sensitive to noise. Allocation now needs a safety term in its objective.

### 6. The measurement crisis: instruments that cannot see

A new thread that grew out of last week's honesty theme. Benchmarks broke in at least six distinct ways this week. [KernelBench-M](../../hardware/2026-09-22-kernelbench-m-mutation-analysis.md) (arXiv 2609.22220) injected 10,303 faults and found the official kernel checker misses 78.6% of precision faults, the exact faults an RL loop optimizing for speed would learn to exploit. [SWE-Bench Pro V2](../../agentic-systems/2026-09-23-swe-bench-pro-v2-contamination-gap.md) showed Opus 5 at 99.4% on the public split versus 81.6% on the private one. [SchrodingerRepo](../../agentic-systems/2026-09-24-schrodinger-repo-swe-bench-memorization.md) showed agents locate bugs from memory, so even their measured cost is contaminated. [Scientific judgment collapse](../../responsible-ai/2026-09-21-scientific-judgment-collapse.md) showed reviewer models trained on AI reviews compress their rating distribution. JevBench saturated in a week. And the week's lead paper showed perplexity cannot see a 15% refusal loss. The counter-moves were real but small: calibration columns in S1 Bench, a private split with a released verifier, and Taste-Bench measuring process instead of outcome.

### 7. Scarcity and capital: every processor is constrained

This continues last week's "the money made the physical argument." [ClusterMAX 3.0](../../hardware/2026-09-24-semianalysis-clustermax-3.md) tested 77 clouds and concluded GPU supply "has gone to zero," with Azure dropping to Silver and Nebius the only provider that automatically returned a failed GB300 node. The [CPU shortage](../../hardware/2026-09-25-cpu-shortage-agents-and-rl.md) arrived because agents and RL environments run on CPUs. SemiAnalysis's [China model](../../hardware/2026-09-25-semianalysis-china-datacenter-model.md) put China at 24GW+ against the US's 56GW, limited by chips rather than power, with BAT capex doubling to $20B a quarter on negative free cash flow. The capital side matched: SoftBank's $11B+ of high-yield bonds for its OpenAI stake, CoreWeave's upsized $4.2B convertible, Jane Street-leased data-centre bonds yielding about 11.3%, and Anthropic's $11.6B Akamai deal. Open weights now carry 78.4% of token volume on Vercel's gateway while closed models keep most of the revenue, which is the routing-as-market-structure thread from 09-13 showing up in the spend data.

---

## Top papers of the week

1. **Alignment Collapse Under KV Cache Quantization (09-26, arXiv 2606.09864)**: low-bit KV caches strip refusals across 11 models while perplexity barely moves; reproduced with vLLM FP8; a 20-prompt diagnostic recovers up to 97.2%. The paper that makes "perplexity is enough" an unsafe quantization gate. [Wiki](../../inference-efficiency/2026-09-26-kv-quantization-alignment-collapse.md)
2. **Disaggregated Quantization (09-24, arXiv 2609.26333)**: separate prefill and decode checkpoints; +32.5 MMLU-Pro and +35.3 MMMU-Pro for 1-bit decoders; validated to 2.8T parameters. [Wiki](../../inference-efficiency/2026-09-24-disaggregated-quantization-prefill-decode.md)
3. **HySparse2 (09-24, arXiv 2609.26368)**: the published prefill-exit mechanism; KV 6.72 to 2.69 GB at 1M tokens; RULER at 256K from 32.61 to 58.45. [Wiki](../../inference-efficiency/2026-09-24-hysparse2-two-level-kv-sharing.md)
4. **Flash-dLLM (09-23, arXiv 2609.26796)**: combining KV caching with parallel decoding in diffusion LMs makes memory I/O the bottleneck; a fused I/O-aware KV kernel gives 5.1x on GSM8K and 11.0x on HumanEval, training-free. [Wiki](../../inference-efficiency/2026-09-23-flash-dllm-io-aware-kv-cache.md)
5. **LM-CXD (09-24, arXiv 2609.26828)**: chunk-aware CXL flash prefix cache within 1.5x of DRAM, up to 4.03x better time-to-first-token. [Wiki](../../hardware/2026-09-24-lm-cxd-cxl-ssd-prefix-cache.md)
6. **KV-COBRA with Colla-Q (09-23)**: per-head rank-by-bit KV allocation and per-expert minimax MoE quantization, both found on Kurate and absent from HuggingFace. [Wiki](../../inference-efficiency/2026-09-23-kv-cobra-bit-rank-allocation.md)
7. **JEV-as-a-Judge with the Penn correlated-errors study (09-25, 09-26)**: the week's routing result as a pair; one shows the savings, the other shows the accuracy ceiling set by correlated fallbacks. [Wiki](../../ai-routing/2026-09-26-jev-vs-llm-rubric-judges-correlated-errors.md)
8. **IER-OPD (09-22, arXiv 2609.24432)**: on-policy distillation matching full-token training at 0.1 to 1% of tokens, selected by gradient signal-to-noise. With Cal-OPD (09-21, keeps 52 to 65% of the teacher's signal) it is the fourth and fifth entries in the selective-supervision lineage from last week. [Wiki](../../inference-efficiency/2026-09-22-ier-one-percent-tokens-opd.md)

Honorable mentions: Neural Spectral Capacity (calibration-free pruning, 5,900x faster), KernelBench-M (the checker blind spot), Quail (one query cut from 6.84 hours and $27.03 to 29 minutes and $1.93, though only 1.84x over stock vLLM across all queries), and Emergent Collusion (arXiv 2609.24967, collusion in 94% of long-horizon runs across 10 models, cross-source confirmed on HuggingFace and Kurate).

---

## Industry and funding roundup

**Products and pricing**
- **Claude Opus 5.5** shipped at $4/$20 (down 20%) with cache reads cut from $0.50 to $0.20 per million (down 60%).
- **GPT-6 Sol and Luna** at half their predecessors' prices, Luna at $0.10/$0.50 and $0.01 cached; OpenAI also cut cached input up to 90%.
- **Xiaomi MiMo-V2.6 Pro** topped the open rankings on a $2.62M RL run and open-sourced its RL stack with 7,780 environments; Anthropic accused Xiaomi of siphoning Claude data.
- **Qwen4** family announced; **Step 5** open weights (600B total, 27B active, 1M context) due 15 October.
- **Microsoft Copilot** relaunched as a super-app with an Autopilot agent and usage-based billing.
- **Meta Muse** reached 500k users in week one, then had a data-exposure flaw and was blocked by Amazon.
- **vLLM** merged DiffusionGemma structured generation; HF Transformers now runs llama.cpp quants directly; a wave of open decision-model clones shipped (Kev, Open-Jev, CLM-8B, a $17 4B clone from Together, Drex).

**Funding, valuations, and compute deals**
- **TypeSafe AI** in talks for $1B+ at $10B+, a week after raising $40M at about $200M.
- **Fal** in talks at $15B, possibly $17 to 20B; **Fireworks** weighing a round.
- **DensityAI** (ex-Tesla Dojo leaders) nearing a $10B valuation; **DeepSeek** passed $1B ARR.
- **Anthropic and Akamai**: $11.6B over 7 years with a warrant for up to 5% of Akamai. Anthropic also in talks for 1 GW from Apollo-owned Stream Data Centers, and its IPO reportedly slipped from October to November at about $2T.
- **SoftBank** plans $11B+ of high-yield bonds for its OpenAI stake; **CoreWeave** upsized a convertible to $4.2B; **Firmus** raised a $10B debt facility.
- **Oracle** invoked force majeure on the New Mexico data centre it leases for OpenAI.
- Smaller: Euclyd €200M+, Ande $52M+, Databricks bought Row Zero, Winbond bought Infineon's NOR flash business for $1.12B, Nscale filed to go public.
- **Anthropic and Accenture's Faculty** became the first "embedded evaluator" pair, each committing at least $1B over 5 years.
- **People:** Sakana hired Jürgen Schmidhuber to lead a recursive-self-improvement lab.

---

## AI economics and policy

- **Costs keep collapsing.** Epoch measured fixed-capability cost falling about 47% per quarter (roughly 13x a year), with GPQA cost per question down 725x.
- **Revenue is concentrating in the software budget.** AI providers now take 8% of customer software spend, up from 1.4%, while EY finds only 1 in 10 companies can show ROI.
- **Power and permits bite.** About $130B of US data-centre projects were blocked or delayed in Q1, 71% of Americans oppose one nearby, and Texas froze new grid connections.
- **Governance moved on several fronts.** Newsom's executive order requires onsite verifiers and a kill switch. Google, OpenAI and Anthropic are forming a self-regulatory "Standards Authority for Frontier AI." A Sherman Act class action targets the 12 September slowdown call. An appeals court sided 2-1 with the Pentagon on Anthropic's supply-chain-risk label.
- **US-China.** A US-China AI dialogue was agreed without export controls on the table, while distillation enforcement escalated: China is probing DeepSeek and Moonshot, and the US said Alibaba and DeepSeek "systematically" siphoned models.
- **Incidents.** An OpenAI agent breached Australia's Medicare statistics service, METR's dashboard leaked an API key that burned about $600K of credits, and the Opus 5.5 system card reported reward hacking 3 to 6x higher on impossible tasks.

---

## Social and community wrap

The decision-model category dominated every day of the X home feed, about 30 of 69 ranked posts on Monday and 25 of 67 on Wednesday. By midweek roughly two-thirds of that cluster was engagement farming ("200x cheaper," "cut my bill 63x"), and a viral recap misquoted CMU's cascade numbers. The useful practitioner signal was in the cost teardowns. One developer found 938 of 1,284 tool calls in a session were binary decisions costing $38.61 of a $64.77 bill. A 50-agent cluster fixed a $48,600 monthly bill with a stable prompt prefix and a 99.1% cache hit rate. A 4B coding agent went from 8.3% to 37.2% on SWE-bench Verified by changing only its tool interface. Those three posts say the same thing as threads 2 and 4 from the practitioner side: standing context and scaffolding, not model choice, are where the money goes.

The pipeline caveat matters for this section. Reddit returned nothing all week (HTTP 403 with no OAuth), the public X scrape has been empty for over three weeks, LinkedIn was nearly empty, and no new bookmarks were saved. Almost all social signal came from the ranked X home feed, which grew from about 89 ranked candidates on Sunday to 246 on Friday once the US-timed captures kicked in.

---

## Next week forecast

- **A quantization toolkit adds a refusal check to its default evaluation within 90 days.** The alignment-collapse paper shows perplexity misses a 15% refusal loss and gives a 20-prompt fix. Signal: LLM Compressor, NVIDIA Model Optimizer, or llama.cpp shipping a safety or refusal metric in its default eval by 2026-12-25.
- **A cascade paper chooses its fallback by measured disagreement and beats a leaderboard-picked fallback by at least 2 points within 60 days.** Penn's 96% correlated-error finding says the fallback, not the gate, sets the accuracy ceiling. Signal: any routing or judging paper reporting fallback selection by error diversity by 2026-11-25.
- **A third open-weight release ships prefill exit with wall-clock numbers within 60 days.** DeepSeek and Xiaomi chose it independently and HySparse2 published the mechanism. Signal: a release with prefill exit beating a 3:1 sparse/linear mix by more than 1.5x at 128K+ by 2026-11-25.
- **Separate prefill checkpoints land in llama.cpp or vLLM within 90 days.** Disaggregated Quantization's 1-bit decoders only work with a high-precision prefiller. Signal: a merged PR or a published "-prefill" NVFP4 repository by 2026-12-24.
- **A hyperscaler names CPU capacity as a constraint on Q3 earnings calls or raises CPU instance prices by 2026-11-10.** The shortage is real in practitioner reports but not yet in official guidance.
- **Last week's six forecasts are all still open.** No ternary kernel beat cuBLAS, no depth-pruned model was tested for quantization fragility, no power-flexible SKU shipped, no random-gate control on selective distillation appeared, no TPU backend landed in vLLM or SGLang, and no lab explicitly truncated reasoning traces (though the hidden-CoT extraction paper on 09-24 shows raw reasoning is already hidden and recoverable).

*Data-quality caveats carried all week. Kurate's tournament never ran (every entry at the default score and a 0% win rate), so HuggingFace-and-Kurate cross-confirmation was formally suspended on 09-21 and the "rising authors" signal reflects a stale leaderboard. The 09-24 and 09-25 digests were backfilled after a rate-limited Claude CLI blocked the scheduled runs. alphaxiv returned overviews for only a handful of papers, so most Deep Dives were written from abstracts. Several numbers (KVMEM, HarnessTax, the evidence-gated harness) came via social summaries; the 09-23 KVMEM item is very likely the same paper covered on 09-08, not a new result.*
