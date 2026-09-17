# ComPO: a zeroth-order paradigm for LLM preference alignment

**Source:** HuggingFace Daily Papers · [arXiv 2609.19144](https://arxiv.org/abs/2609.19144) · [raw](../../raw/huggingface/2026-09-17-a-zeroth-order-paradigm-for-llm-preference-alignment.md)

## TL;DR

Direct preference alignment methods (DPO and its family, which skip the reward model and optimize a differentiable loss directly on pairs of preferred and rejected responses) are popular because they are cheap in compute and memory. They also have a known pathology called **likelihood displacement**: on pairs where the two responses have nearly equal likelihood under the model, optimizing the pairwise loss can push the probability of the preferred response **down**. ComPO's move is to stop differentiating through those pairs at all. It treats the preference as a **comparison oracle** and extracts only directional information from it, which is a zeroth-order method: you learn from the sign of a comparison rather than from a gradient of a loss. The paper establishes a convergence guarantee for the basic offline scheme under smoothness, gradient sparsity, and a compatibility condition between the oracle and a latent objective, then adds **online ComPO**, which keeps the comparison mechanism and uses unlabeled policy generations for reverse-KL control against a reference policy, with a performance guarantee under local coverage and in-distribution pairwise reward accuracy. Experiments across Mistral, Llama, Gemma-2, Qwen3 and Gemma-3 show improvements over existing direct alignment methods including on length-controlled win rates, with pair-level diagnostics consistent with the likelihood-displacement story.

## Why it belongs on the efficiency ledger

Zeroth-order optimization is normally a memory story: no backward pass through a differentiable loss means no activation storage for that term. This paper's framing is accuracy-first, but the structural property is the same one that makes zeroth-order methods attractive for fine-tuning large models on constrained hardware. **The interesting claim is that giving up the gradient costs nothing here, because on the problematic pairs the gradient was pointing the wrong way anyway.** That is a rare case where the cheap method is not a compromise.

## How this relates to what the wiki already knows

**It joins the selective-training cluster from the opposite end.** This wiki has recorded five papers arguing that uniform treatment of training signal is wasteful: LongAct (long-context gradient signal concentrates in the first 5% of tokens), TIP (most teacher-generated tokens carry no signal and should be skipped), PreRL (the question is really the pre-training distribution), VGF (where probability mass should be transported), and [Drift-Constrained Optimization (09-16)](2026-09-16-drift-constrained-optimization.md), which fixes a behavioural drift budget so direction becomes the only free variable. All five say **some of the signal is bad and should be down-weighted or redirected**. ComPO says something narrower and sharper: on small-margin preference pairs, the differentiable loss's gradient is actively harmful, so use a comparison instead of a derivative. That is the first entry in the cluster where the fix is a change of **optimizer class** rather than a change of weighting.

**It also gives [PLC-DPO (09-14)](../responsible-ai/2026-09-14-plc-dpo-posterior-label-correction.md) a companion diagnosis.** That paper attacked bad preference labels with posterior label correction. ComPO attacks a failure that occurs even when the labels are **correct**, because the pathology is in the loss geometry rather than in the annotation. Read together: preference alignment has two independent failure modes, a label problem and a margin problem, and a method that fixes one does nothing for the other.

## Gaps

The guarantees rest on gradient sparsity and an oracle-objective compatibility condition, neither of which is verified for the models evaluated, so the theory is a plausibility argument rather than a certificate on these runs. Zeroth-order methods classically pay in sample efficiency, and the paper reports quality improvements without a matched wall-clock or step-count comparison, so it is not yet possible to say whether ComPO is cheaper, equally expensive, or more expensive per unit of alignment gained. That number is the one a practitioner needs.

## Related

- [rl-for-llms.md](rl-for-llms.md) · [knowledge-distillation.md](../inference-efficiency/knowledge-distillation.md)
- [Drift-Constrained Optimization (09-16)](2026-09-16-drift-constrained-optimization.md)
- [PLC-DPO: posterior label correction (09-14)](../responsible-ai/2026-09-14-plc-dpo-posterior-label-correction.md)
- [GAPO: group-adaptive clipping (09-07)](2026-09-07-gapo-group-adaptive-clipping.md)
