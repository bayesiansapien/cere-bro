# Model Pruning and Sparsity

**Concept page.** Removing things and keeping the result working: weights, attention entries, activations, experts, and training samples. This page exists because the wiki accumulated a dozen sources touching pruning and sparsity across four months with no page to hold the pattern, while pruning sits in the reader's core attention set. Created 2026-08-30.

**The one-line state of knowledge:** *sparsity is easy to find and hard to spend.* Nearly every study finds that importance is wildly non-uniform, so a large fraction of any given structure can go. What decides whether that finding turns into a speedup is entirely whether the surviving pattern is one the hardware can schedule, and most of the field's headline sparsity ratios are in patterns that cannot be.

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
