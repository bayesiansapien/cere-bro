# Dynamic Latent Routing: Joint Latent-Code and Routing Policy for LM Post-Training

**Source:** [HuggingFace Daily Papers](https://huggingface.co/papers/2605.14323) · [arXiv 2605.14323](https://arxiv.org/abs/2605.14323)
**Date ingested:** 2026-05-15
**Tier:** 1. LM post-training, routing-as-search, discrete latent codes
**Raw:** [farmer file](../../raw/huggingface/2026-05-15-dynamic-latent-routing.md)

## TL;DR

DLR reframes language-model post-training as a search problem in latent code space. Drawing on a theoretical result that globally optimal goal-reaching policies in MDPs with time-varying rewards can be recovered through temporal composition of intermediate optimal sub-policies (the General Dijkstra Search theorem), the paper proposes Dynamic Latent Routing: jointly learn discrete latent codes, routing policies, and model parameters in one training stage. In low-data fine-tuning across four datasets and six models, DLR matches or beats supervised fine-tuning with a mean +6.6 point gain. Prior discrete-latent baselines consistently underperformed SFT; DLR is the first to flip that result.

## What's new

Two structural ideas.

**Search-select-update as a training principle.** Most discrete-latent methods learn the code book and the policy in separate stages, or use cluster-based assignment that decouples them from the routing decision. DLR treats both as jointly optimized through dynamic search. Sub-policies are composed temporally, which means the latent-code transitions across timesteps inherit the GDS optimality structure.

**Single-stage joint optimization.** Discrete latent methods historically need staged training (codebook first, then policy, then fine-tune). DLR does all three in one stage. The +6.6 pp gain over SFT in low-data settings is the empirical confirmation that the joint formulation is the load-bearing piece.

## Why this is Tier 1

The wiki has been tracking the routing-decision axis at five layers (model, adapter, expert, distillation loss, decoding head). DLR adds a sixth: routing the *internal latent representation* during post-training. This is closer to the MoE expert-routing thread than to model-level routing, but the discrete latent code is the addressable unit.

The mechanistic-analyses claim in the abstract is the more interesting line: the paper shows the learned codes have "distinct causal roles" via targeted code ablations. This connects to the [WriteSAE](../responsible-ai/2026-05-14-writesae-sae-recurrent-state.md) interpretability thread: if the latent codes are causally distinct, they are addressable for behavioral interventions in the same way SAE features are.

## Connections to prior wiki pages

- [RouteProfile](2026-05-15-routeprofile-llm-profile-design-space.md) — also dropped today. RouteProfile asks "how do we describe candidates to a router"; DLR asks "what is the routing target during training." Together they bracket the routing-design space from both sides.
- [CARE bi-level routing](2026-05-11-care-bi-level-routing-moe-continual-learning.md) — bi-level routing at the MoE expert layer. DLR's latent codes are functionally similar to experts but learned discretely.
- [MinT](../inference-efficiency/2026-05-14-mint-million-scale-lora-serving.md) — adapter catalog routing at deployment. DLR is the training-time complement: learn the routable substructure jointly with the policy.
- [llm-routing.md](llm-routing.md) — concept page should add "internal latent routing during post-training" alongside the deployment-side routing approaches.

## Research angle

1. **DLR composed with MinT.** DLR learns routable latent codes during post-training. MinT routes across adapter catalogs at deployment. The composition: train per-task adapters with DLR-learned codes; route between adapters using the codes as profile signal. This unifies training-time and deployment-time routing.
2. **GDS theorem for verifier-free RL.** The theoretical framing is unusually clean for an LM-routing paper. Whether the same search-select-update principle applies to verifier-free RL (G-Zero, AIMO 3) is an open question.
3. **Code-space interpretability.** If codes are causally distinct, can they be assigned semantic labels (style, domain, reasoning depth) at scale? This is the bridge between routing and interpretability literatures.

## Why it matters

The first post-training paper in the wiki where routing is not a deployment concern but a *training objective*. The 6.6-point gain over SFT in low-data settings is the practitioner-relevant headline. If this holds beyond the four datasets and six models tested, low-data fine-tuning gets a new default.

## Links

- [Paper](https://arxiv.org/abs/2605.14323)
- [HuggingFace](https://huggingface.co/papers/2605.14323)
- [Raw farmer file](../../raw/huggingface/2026-05-15-dynamic-latent-routing.md)
- Related: [llm-routing.md](llm-routing.md), [RouteProfile](2026-05-15-routeprofile-llm-profile-design-space.md), [CARE](2026-05-11-care-bi-level-routing-moe-continual-learning.md)
