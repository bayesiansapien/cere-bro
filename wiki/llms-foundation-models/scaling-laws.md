# Scaling Laws

A scaling law is a fitted functional form predicting model loss from model size (N), training tokens (D), and compute (C). Its practical job is to let a lab decide how to spend a pretraining budget from a small sweep, without running the large job first.

## Current State (as of 2026-09-02)

**A third way the received law fails, and this one is not a misspecification or a transfer failure. It is a claim that architecture belongs inside the law.** [SMELT (09-02)](2026-09-02-smelt-moe-looped-transformers.md) (arxiv 2609.01343) fits a **separate Chinchilla-style scaling law for each architecture**, looped and unlooped, across four sizes up to 54B non-embedding parameters, and only then can it report that the looped variant's loss falls faster with compute, saving **6.8 to 18.0% of training FLOPs on the compute-optimal frontier**. A single law fitted across both architectures would have averaged that effect into the residual. The methodological point is the contribution: the frontier gap between two architectures is not recoverable from one law with an architecture covariate, it requires two fits.

**What makes the comparison trustworthy is the budget discipline, and it is stricter than anything else on this page.** SMELT matches **three budgets simultaneously**: per-token FLOPs, total non-embedding parameters, and KV cache size. MoE is what makes that possible, since it decouples total parameters from per-token FLOPs, so the hidden dimension can be narrowed to hold FLOPs fixed while expert count recovers capacity. The KV constraint is the one nobody else imposes and it is not about cost: KV size bounds the longest servable context, so a model that wins on loss while needing a larger cache is not a substitute for the baseline at serving time. Prior looped-model scaling analyses either fixed effective depth (finding diminishing returns) or fixed unique parameters while letting FLOPs and KV grow, and both confound the architecture effect with spend.

**This bears directly on the page's open question about sparse-model laws.** The page has asked whether MoE laws need a third interaction term for active-versus-total parameters, prompted by LLaDA MoE v2's (08-05) finding that larger expert pools win at fixed activated capacity. SMELT is evidence the N axis is not one-dimensional for MoE in a second, independent way: **effective depth via layer reuse is a distinct axis from both active and total parameters**, and it is one the Chinchilla form has no slot for at all. Note also that SMELT's advantage *grows* with sequence length and with in-context example count, which means the effect is not a constant offset and therefore cannot be absorbed into the irreducible-loss term.

**Where it leaves the deployment-side gap unchanged, and slightly worse.** This page's sharpest standing complaint is that there is no accepted functional form relating **inference compute to solved-problem rate**, which is the quantity agentic deployment actually cares about, and that nothing in the wiki fills that slot. SMELT reports its saving in **training FLOPs**. Because looping serializes computation, matched FLOPs is not matched wall-clock, and concurrent MoE-looping work matched wall-clock time instead. So the field now has two looping literatures optimizing different objectives with no head-to-head, and neither is denominated in the currency the deployment question needs.

---

## Prior State (as of 2026-08-10)

**The received scaling law is now known to be wrong in two independent ways, and both were established within six days.** This page exists because that count crossed the threshold.

**Failure 1: the functional form is misspecified at the grid boundaries.** [Skaling (08-10)](2026-08-10-skaling-scaling-law-coupling.md), from FAIR at Meta, shows the Chinchilla law's core assumption is a structural flaw rather than an approximation. Chinchilla models the reducible loss as a **sum** of independent power-law terms in N and D, which forces the cross-derivative to exactly zero. The observed residual is **saddle-shaped**, with large, oppositely-signed errors at the corners of the N-by-D grid, which is the signature of a missing interaction term. The consequence is that Chinchilla systematically under- and overestimates loss in the two regimes the field currently operates in: **data-scarce, and heavily overtrained.** Skaling restores the coupling that Kaplan et al. had in 2020 and Chinchilla discarded, using **one extra interaction exponent**, and cuts mean absolute percentage error by 1.5x to 3x in *both* interpolation and extrapolation. The extrapolation half is the one that matters, because extrapolating from small runs is the only practical use of a scaling law.

Two consequences worth stating plainly. First, **the compute-optimal token-to-parameter ratio is derived by optimizing the additive form**, so if the form is misspecified at imbalanced N and D, the optimum it implies is misspecified too, and the error now has a known sign per regime rather than being unquantified. Second, the fit gets cheaper as well as better: with a sparse grid restricted to low-compute runs, Skaling extrapolates the full grid at roughly **10x less compute** than a uniform sweep.

**Failure 2: the law does not transfer across training objectives.** [LLaDA MoE v2 (08-05)](2026-08-05-llada-moe-v2-scaling-moe-diffusion-lms.md) found that autoregressive scaling laws do not carry over to diffusion language models, and are wrong specifically about **batch size, learning rate, and data allocation**. That is a transfer failure across model families, orthogonal to Skaling's within-family form failure. It also reported that at scale, larger expert pools win at fixed activated capacity, which is a scaling result about sparsity rather than about N and D.

**Read together: the received law is unreliable both when you change the objective and when you stay inside it but move to the edges of the grid.** For anyone budgeting a run right now, that is the whole state of the art.

**Where this connects to the cost-optimization thread.** Efficiency work on this wiki almost entirely attacks the cost of runs already decided on. [Mixture-of-Kittens (08-05)](../inference-efficiency/2026-08-05-mixture-of-kittens-moe-megakernel.md), Cursor's open-source fused MoE training megakernel, cut MoE layer cost 2.37x in isolation and 1.41x end to end. Skaling attacks the cost of **deciding which run to do**, which is strictly upstream and far less attacked. The two savings are multiplicative and neither paper is aware of the other.

**A third, quieter scaling observation from the same week, on the inference side.** [Interconnects' "Lessons from the hacks" (08-09)](../responsible-ai/2026-08-10-interconnects-lessons-from-the-hacks.md) quotes Noam Brown's position that benchmark performance is increasingly a function of test-time compute, and that **the capability ceiling of current models is unknown because measuring it is too expensive.** That is a scaling claim with no fitted law behind it: there is no accepted functional form relating inference compute to solved-problem rate, which is the quantity agentic deployment actually cares about. This page has nothing to put in that slot, and that is itself the finding.

## Open questions this page is tracking

- Does Skaling's interaction exponent have an interpretation, or is it currently a better-fitting term? Until it does, extrapolating far outside the tested N and D ranges is unjustified even with the improved fit.
- Does the coupled form fix the diffusion-LM transfer failure, or are these two independent problems requiring two fixes? Nobody has fit Skaling to a diffusion-LM grid.
- **Is there a scaling law for inference compute versus tasks solved?** Every result on this page is about pretraining loss. The deployment question is about test-time tokens per solved problem, and no fitted form for it exists in this wiki.
- Do sparse-model scaling laws need a third interaction term for active-versus-total parameters? LLaDA MoE v2's finding that larger expert pools win at fixed activated capacity suggests the N axis is not one-dimensional for MoE.

## Pages feeding this concept

- [Skaling: Chinchilla's exponents meet Kaplan's coupling (08-10)](2026-08-10-skaling-scaling-law-coupling.md)
- [LLaDA MoE v2: scaling MoE diffusion LMs (08-05)](2026-08-05-llada-moe-v2-scaling-moe-diffusion-lms.md)
- [SemiAnalysis on Kimi K3 (08-04)](2026-08-04-semianalysis-kimi-k3-architecture-primer.md), which derives the MoE communication-to-computation ratio, which constrains which N and D configurations are even servable
- [Interconnects: Lessons from the hacks (08-09)](../responsible-ai/2026-08-10-interconnects-lessons-from-the-hacks.md), the missing inference-side scaling law
