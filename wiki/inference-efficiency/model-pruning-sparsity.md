# Model Pruning and Sparsity

**Concept page.** Removing things and keeping the result working: weights, attention entries, activations, experts, and training samples. This page exists because the wiki accumulated a dozen sources touching pruning and sparsity across four months with no page to hold the pattern, while pruning sits in the reader's core attention set. Created 2026-08-30.

**The one-line state of knowledge:** *sparsity is easy to find and hard to spend.* Nearly every study finds that importance is wildly non-uniform, so a large fraction of any given structure can go. What decides whether that finding turns into a speedup is entirely whether the surviving pattern is one the hardware can schedule, and most of the field's headline sparsity ratios are in patterns that cannot be.

---

## 2026-09-02: the pattern threshold is crossed. Three independent results now say the standard redundancy criterion does not measure redundancy

**This page's one-line state of knowledge is "sparsity is easy to find and hard to spend." Today it needs a second line: the instrument used to find it is not measuring what it is trusted to measure.** [Functional Degeneracy in Neural Networks (09-02)](2026-09-02-functional-degeneracy-pruning.md) (arxiv 2608.30741, Kurate cs.LG #10, tier 1) defines the **behavioral recovery rank**, the number of leading eigendirections of the behavioral Hessian needed to recover a trained model's performance, and uses it as a geometric benchmark for how much compression is available. Measured against that floor, **structural and magnitude pruning both retain more degrees of freedom than necessary, even after the task is saturated.** The diagnosis is the part that matters: functional redundancy is **distributed across parameter directions**, which are linear combinations of many weights, so it is invisible to any criterion that scores an individual weight or an individual neuron. A redundant direction can spread across units each of which looks individually important.

**Three results, three layers of the network, one indicted criterion.** The wiki's threshold for declaring a pattern is three papers making the same core claim. It is now met:

1. **[Beyond Geometric Complementarity (07-31)](../ai-routing/2026-07-31-coherent-overlap-moe-routing.md)** at the **MoE expert** level: expert subspaces overlap substantially yet routes still beat matched alternatives in every one of 39 factorial cells, and adding later-ranked experts still improves next-token prediction in 24 of 39 frozen-route comparisons. Conclusion: representational **similarity cannot determine redundancy**, and any MoE compression ratio derived from subspace similarity should be re-derived.
2. **[When Pruning Meets Interpretability (08-31)](2026-08-31-pruning-meets-interpretability-sae.md)** at the **weight** level: standard one-shot pruning (SparseGPT, Wanda, magnitude) degrades the faithfulness of sparse autoencoders fit on top, so a model that still *behaves* the same is no longer as *legible*. A cost of compression nobody on the leaderboards counts.
3. **Functional Degeneracy (09-02)** at the **parameter-direction** level: the same unit-wise methods also leave compression on the table, because they cannot see directionally-distributed redundancy.

**Stated as one claim: unit-wise and similarity-based criteria simultaneously under-report their cost and under-deliver their benefit.** Item 2 says the methods hide a cost; item 3 says they miss a gain; item 1 says the geometric intuition behind both was never valid. That is a measurement-validity finding about this page's core tooling, and it runs alongside the wiki's KV-eviction-ablation thread, where [the 07-28 impossibility result](2026-07-28-kv-eviction-error-certificates.md) proved deterministic top-k eviction cannot estimate the error it created.

**What this does to every ratio on this page.** Compression ratios here have been recorded as achievements, compared against each other. The behavioral recovery rank turns them into a **distance from a floor**, which is a harder and more informative standard, and **nothing on this page has ever been evaluated that way.** Anyone whose serving cost depends on a pruning ratio should want that distance, and no method reports it.

**The obvious next experiment, which neither of items 2 and 3 proposes.** If redundancy is directional, and sparse autoencoders decompose activations into directions, then "pruning degrades autoencoder faithfulness" and "pruning misses directional redundancy" are plausibly two faces of one phenomenon: unit-wise pruning perturbs directional structure in a way behavioral metrics tolerate and directional analysis does not. **Measure behavioral recovery rank before and after pruning and test whether the rank change predicts the faithfulness drop.** If it does, this page gets a single instrument that prices both the missed compression and the lost legibility.

**Caveats on the new result.** The abstract is unusually thin, naming no models, scales, or tasks. Behavioral-Hessian eigendecomposition is expensive and no cost is given, which decides whether this is a production criterion or an offline grading instrument. And it is a negative measurement result rather than a replacement: it establishes that unit-wise pruning underperforms without supplying the pruner that closes the gap.

---

## 2026-08-31: a third currency, and nobody on this page reports it

**Every method on this page is answerable on two axes. There is now a third, and it is the one that becomes load-bearing exactly as compression succeeds.** [When Pruning Meets Interpretability (08-31)](2026-08-31-pruning-meets-interpretability-sae.md) (COLM 2026, Ohio State) finds that standard one-shot weight pruning (SparseGPT, Wanda, magnitude) degrades the faithfulness of **sparse autoencoders**, the overcomplete sparse dictionaries fit to a layer's activations that mechanistic interpretability uses to pull apart superposition. Every SAE workflow, circuit identification, spurious-correlation erasure, causal hypothesis testing, assumes the SAE faithfully decomposes the activations it was fit to. Pruning weakens that assumption, and the damage is **not predicted by the metrics this page already tracks**.

| Axis | What it asks | Reported by |
|---|---|---|
| Quality per removal | Does the model still behave the same | Every paper here |
| Schedulability | Can the hardware execute the surviving pattern | Most papers here |
| **Interpretability preservation** | Is the model still *legible* the same | **Nothing on this page** |

**Why this stops being an academic point this week.** [LMSM (08-31)](../responsible-ai/2026-08-31-lmsm-llm-security-modules.md), on HuggingFace the same day, makes SAEs and transcoders **pluggable security backends inside the vLLM serving path**, exposing calibrated evidence to a runtime policy that gates output release, taking HarmBench attack success from 39.20% to 3.32% while retaining **98.14% of unmonitored throughput**. That converts an SAE from a research artifact into a production reliability dependency. And the model that gets served is always the compressed one.

So the two papers jointly define a question neither team asked, and it is one experiment: **how much of LMSM's 3.32% survives when its SAE backend runs on a 50%-pruned model?** Neither paper cites the other. This is the most valuable unrun experiment this page currently holds, and the direction of industry pressure makes it more urgent rather than less: outcome-based AI pricing (OpenAI and Salesforce, both this week) means the vendor eats the cost of every failed task, which pushes serving cost down, which pushes compression up, which is exactly the direction that degrades the audit surface.

**The structural echo with [MCL (08-30)](2026-08-30-mcl-concept-landscape-data-pruning.md) is exact and worth naming.** MCL's objection to embedding-space data pruning was mechanical: an embedding is a lossy summary produced by a model trained to discard detail, and that detail is precisely the rare concepts pruning was supposed to preserve, so it built an explicit entity-event-attribute graph and selected by counted coverage instead. Today's paper says the same thing one layer up: do not trust a learned representation *of a model you just modified* to tell you what that model is doing. **Both are arguments for auditability over convenience, one at the data layer and one at the analysis layer**, and together they are the clearest statement of what this page has been circling: the field keeps buying cheapness with legibility and only prices one side.

**What a reader should want next, and it is not in the paper.** The practitioner question is a curve, not a comparison: what pruning ratio can I afford before the SAE stops being usable. And the cheapest candidate fix is untested, namely refitting the SAE on the pruned model from scratch rather than transferring one from the base. If refitting recovers faithfulness, this is a workflow bug rather than a property of pruning, and that distinction changes everything about how seriously to take it.

---

## The four layers, and why they get confused

"Pruning" names four different operations at four points in the stack. They have different economics and are routinely compared as if they were interchangeable.

| Layer | What is removed | When | Hardware payoff |
|---|---|---|---|
| **Weight pruning** | Individual weights or weight groups | Train or post-train, permanent | Only if the pattern is structured or semi-structured |
| **Activation sparsity** | Neurons that are zero for this input | Runtime, input-dependent | Requires dynamic gather/scatter; real but awkward |
| **Attention / KV sparsity** | Attention entries or cached tokens | Runtime, per request | Direct: cuts both compute and memory traffic |
| **Data pruning** | Training samples | Before training | Not a serving win at all; a training-cost win |

The fourth is the odd one and belongs here anyway, because it has the same mathematical structure (select a small subset maximizing coverage of what matters) and, as of 2026-08-30, the same papers are turning up on the same leaderboards.

---

## The central tension: quality per removal versus schedulability

This is the whole subject in one trade.

- **Unstructured pruning** zeroes any weight anywhere. It preserves quality best per parameter removed, and delivers close to zero speedup, because scattered zeros still ride through dense matrix hardware.
- **Structured pruning** removes whole channels, heads or layers. It gives real speedup on any hardware and costs real quality, because it removes useful weights alongside useless ones to keep the shape rectangular.
- **Semi-structured N:M sparsity** is the compromise the hardware vendors chose: within every contiguous group of M weights, exactly N survive. Nvidia's Ampere-and-later sparse tensor cores implement 2:4 natively. Regular enough to schedule, fine-grained enough to keep quality.

**N:M is where the practical work is, and its open question has been how to pick the surviving N.** Magnitude is the cheap answer and a weak one. Learning the mask is better and, until recently, did not scale.

### [RoI: Reservoir of Importance (08-30)](2026-08-30-roi-semi-structured-sparsity.md)

The scaling fix. Learnable-mask methods put a relaxed categorical distribution over every feasible N:M pattern, and the pattern count is combinatorial in M, so the mask parameters themselves become a memory problem exactly in the aggressive-sparsity regime where the payoff would be largest. RoI reparameterizes to **a compact logit per position plus differentiable subset sampling without replacement**, inducing the distribution over patterns rather than parameterizing it. Trainable parameters drop from combinatorial to **O(M)**, which is **1.5x to 8.75x fewer** at matched quality across Qwen2.5 from 0.5B to 7B, with better stability at aggressive patterns.

**What it does not report is a speedup.** The saving demonstrated is in learning the mask, not in serving the model, and those are different bills. This is the standing caution on the whole learnable-mask literature.

---

## The recurring empirical finding: importance is extremely non-uniform

Every layer of the stack has independently found the same thing, which is the reason the field exists.

- **[Maximal brain damage (04-20)](2026-04-20-maximal-brain-damage-sign-bit-flips.md)** probed the extreme: which individual sign bits a network survives losing. Fragility is concentrated, not spread.
- **[RT-Lynx (05-27)](2026-05-27-rt-lynx-activation-sparsity-diffusion.md)** found exploitable activation sparsity in diffusion models, where most neurons are inert for a given input.
- **[FVAttn (07-23)](2026-07-23-fvattn-adaptive-sparse-attention.md)** and **[LVSA (06-02)](2026-06-02-lvsa-training-free-sparse-attention-video.md)** found the same in attention maps, the second without any training at all.
- **[VASE (06-03)](2026-06-03-vase-value-aware-stochastic-kv-eviction.md)** and **[OasisKV (08-11)](2026-08-11-oasiskv-lookahead-sparse-prefetching.md)** found it in the KV cache, where most stored tokens are never attended to again.
- **[TIP and token teachability (06-01)](2026-06-01-ta-opd-token-teachability.md)** found it in *training signal*: most teacher-generated tokens carry no learning signal, so roughly 10% suffices.
- **[HodgeCover (05-18)](2026-05-18-hodgecover-simplicial-laplacian-moe-compression.md)** found it across mixture-of-experts experts.

**Six layers, one finding.** The differences between these papers are almost entirely about *how the surviving subset is chosen* and *whether the resulting pattern can be executed quickly*, not about whether the sparsity is there.

---

## Data pruning: the same problem shape, one layer earlier

### [MCL: Mapping the Concept Landscape (08-30)](2026-08-30-mcl-concept-landscape-data-pruning.md)

Data pruning is almost always done by scoring samples in embedding space. MCL's objection is mechanical: **an embedding is a lossy summary produced by a model trained to discard detail, and the detail it discards is the rare concepts you were pruning to preserve.** So MCL represents each image-caption pair as an explicit graph of entities, events and attributes, merges all of them into a dataset-level graph so rarity becomes a **count over the corpus rather than a local geometric property**, and selects by greedy concept-coverage maximization.

Its differentiator is not accuracy, it is that **selection carries a reason**: each retained sample is kept *for* named concepts, producing an audit trail no embedding method can produce.

**The unresolved conflict worth tracking.** MCL's rarity is **learner-independent**, a property of the corpus, transferable across models. [Dataset distillation via influence matching (07-24)](2026-07-24-dataset-distillation-influence-matching.md) is **learner-coupled**, synthesizing samples that reproduce training influence against a specific model's gradients. And the [ACE lens (08-28)](../agentic-systems/2026-08-28-ace-lens-agentic-data-generation.md) argues informativeness is a property of the model-harness *pair*, which is the strongest version of the learner-coupled position. These cannot all be right, and the trade is legible: **learner-coupled selection is more accurate per retained sample, opaque, and must be redone per model; corpus-intrinsic selection is transferable and auditable and leaves value on the table.** Nobody has run the experiment that measures the gap.

---

## The convergence noted 2026-08-30

Three papers landed on one Kurate cs.LG board making the same structural move at three layers, which is what prompted this page.

- **[RoI](2026-08-30-roi-semi-structured-sparsity.md)** selects N weights of M and drops the rest.
- **[MCL](2026-08-30-mcl-concept-landscape-data-pruning.md)** selects samples by marginal coverage gain and drops the redundant remainder.
- **[FedCC](2026-08-30-fedcc-distillation-federated-label-skew.md)** lets a federated client tag a sample `unknown` rather than forcing a classification, so a confidently wrong vote becomes an absent one.

**All three replace a forced dense decision with a sparse one plus an explicit way to decline.** FedCC is the clearest statement of why that matters: the alternative to a sparse decision is not a neutral one, it is a confidently wrong one. That is the same pathology the wiki's calibration thread keeps finding elsewhere, from [agents overrating their own output by ~20 points (08-30)](../agentic-systems/2026-08-30-agents-not-time-aware.md) to this week's Kurate cs.AI #6 on belief miscalibration under hidden information. **A model asked to answer outside its support signals confidence, not uncertainty, and the engineering response is always to build the abstention path into the protocol rather than to hope for self-report.**

---

## Why this connects to the rest of the wiki

**To [compute economics](../hardware/compute-economics.md):** sparsity is one of the few levers that improves tokens-per-joule without a new chip, because it removes multiply-accumulates rather than raising the clock. That page records the 2026-08 shift to **power as the binding constraint**, with OpenAI stating it is limited by datacenter power rather than budget or floorspace. Sparse tensor cores are already deployed silicon, which makes N:M one of the shortest paths from a compression paper to a watt saved.

**To [knowledge distillation](knowledge-distillation.md):** distillation and pruning are the two ways to make a model smaller and the wiki's sources keep discovering the same governing fact, that most of the signal is redundant. The distillation thread found it in teacher tokens; the pruning thread found it in weights. They are rarely composed and should be.

**To [KV cache](kv-cache.md):** attention and KV sparsity are the runtime members of this family, and they are the ones with the cleanest hardware payoff because they cut memory traffic rather than arithmetic, which is the actual bottleneck at inference.

---

## Open problems

1. **Sparsity composed with quantization, measured once.** Both attack memory bandwidth and the field reports them separately. Whether a 2:4 mask survives 4-bit weights or whether the two consume each other's headroom is a single ablation nobody has published, and it decides real deployment recipes.
2. **A learnable-mask paper that publishes a wall-clock speedup on sparse tensor cores.** The entire justification for N:M over unstructured is hardware execution, and RoI, like most of its predecessors, reports parameter counts and quality without a throughput number. This is the field's most conspicuous missing measurement.
3. **Learner-coupled versus corpus-intrinsic data pruning at matched keep-ratio.** MCL, influence matching and the ACE lens stake out incompatible positions on whether informativeness is a property of the data or of the model-harness pair. The experiment is cheap and would settle whether pruned corpora are reusable assets or per-model artifacts.
4. **Are learned masks interpretable?** Per-position importance logits come free with methods like RoI and nobody reads them. The 08-28 result on [pruning and SAE robustness](../responsible-ai/2026-08-28-pruning-sae-robustness.md) makes the pruning-interpretability interaction live, and whether learned masks agree with magnitude, with gradient importance, or with neither is a diagnostic already computed and discarded.
5. **Does data pruning need an audit trail as a matter of governance?** The [evaluation-license census (08-29)](../responsible-ai/2026-08-29-evaluation-license-claim-replay-census.md) found 110 of 124 eval units cannot license their own claims because the artifact does not carry replayable evidence. Corpus filtering has the identical structure and none of the scrutiny. MCL produces the required substrate as a side effect, which makes it the natural first target for that audit.

---

## Sources

- [RoI: Reservoir of Importance (08-30)](2026-08-30-roi-semi-structured-sparsity.md) · [arXiv 2608.23048](https://arxiv.org/abs/2608.23048)
- [MCL: Mapping the Concept Landscape (08-30)](2026-08-30-mcl-concept-landscape-data-pruning.md) · [arXiv 2608.22858](https://arxiv.org/abs/2608.22858)
- [FedCC (08-30)](2026-08-30-fedcc-distillation-federated-label-skew.md) · [arXiv 2608.23031](https://arxiv.org/abs/2608.23031)
- [Pruning and SAE robustness (08-28)](../responsible-ai/2026-08-28-pruning-sae-robustness.md) · [arXiv 2608.25941](https://arxiv.org/abs/2608.25941)
- [Maximal brain damage (04-20)](2026-04-20-maximal-brain-damage-sign-bit-flips.md) · [RT-Lynx (05-27)](2026-05-27-rt-lynx-activation-sparsity-diffusion.md) · [HodgeCover (05-18)](2026-05-18-hodgecover-simplicial-laplacian-moe-compression.md)
- [FVAttn (07-23)](2026-07-23-fvattn-adaptive-sparse-attention.md) · [LVSA (06-02)](2026-06-02-lvsa-training-free-sparse-attention-video.md) · [VASE (06-03)](2026-06-03-vase-value-aware-stochastic-kv-eviction.md) · [OasisKV (08-11)](2026-08-11-oasiskv-lookahead-sparse-prefetching.md)
- [Dataset distillation via influence matching (07-24)](2026-07-24-dataset-distillation-influence-matching.md) · [Token teachability (06-01)](2026-06-01-ta-opd-token-teachability.md)

## Related pages

- [Knowledge distillation](knowledge-distillation.md)
- [KV cache](kv-cache.md)
- [Test-time compute allocation](test-time-compute-allocation.md)
- [GPU kernels](../hardware/gpu-kernels.md)
- [Compute economics](../hardware/compute-economics.md)
