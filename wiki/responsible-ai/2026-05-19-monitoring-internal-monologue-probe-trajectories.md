# Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics

**arXiv:** [2605.18549](https://arxiv.org/abs/2605.18549) · **HF:** [paper page](https://huggingface.co/papers/2605.18549) · **Tier:** 2 (interpretability, LRM safety monitoring)

## TL;DR

Large Reasoning Models (LRMs) produce Chain of Thought (CoT) that is often unfaithful to the final output, which undermines its reliability as a safety-monitoring tool. By evaluating a probe at each generated token, the authors construct a probe trajectory: the continuous evolution of a concept's probability across the reasoning process. Future model behavior is more distinguishable when examined over the trajectory than from a single static prediction. Signal-processing features (volatility, trend, steady-state) extracted from the trajectory significantly improve separation of future model states. Two methodological insights: template-based training data reaches near-parity with dynamically generated model responses, eliminating costly initial inference and labeling; pooling matters critically (average and last-token pooling collapse to near-random, max-pooling reaches up to 95% AUROC and yields stable probe trajectories). Across four datasets and four reasoning models in safety and math domains, trajectory features encode task-specific dynamics that improve outcome separability.

## Key findings

- CoT is not always faithful to the model's final output. A monitoring system that relies on CoT content alone can miss the cases where the model arrives at the right answer via a misleading or post-hoc-justified reasoning chain.
- The hidden-representation alternative: at each generated token, run a probe that estimates a concept's probability. The sequence of probe outputs across the CoT is a trajectory.
- Future model behavior is more distinguishable when examined over the trajectory than from a single static prediction. The temporal evolution carries information the static representation alone does not.
- Signal-processing features extracted from the trajectory (volatility, trend, steady-state) give significantly better separation of future model states than the raw probe output. This is the practical recipe: do not just probe; characterise the probe's temporal dynamics.
- Two methodological findings change deployment economics:
  - Template-based training data for the probe achieves near-parity with dynamically generated model responses, removing the need for costly initial inference and labelling.
  - Pooling choice is critical: average-pooling and last-token pooling collapse to near-random AUROC, max-pooling reaches 95% AUROC and gives stable trajectories.
- Demonstrated on four datasets, four reasoning models, two domains (safety and math).

## Relationship to prior wiki entries

This paper extends the wiki's interpretability and safety-monitoring threads. The May 16 mechanistic-interpretability cluster ("All Circuits Lead to Rome") on circuit non-uniqueness and the Goodfire geometric-calculator finding (LLM represents numbers as Fourier features on circles in activation space, surfaced in the DAIR.AI weekly via 2026-05-18 Gmail) both established that activation-space structure carries interpretable content. Today's paper is the temporal extension: not just where the structure is, but how it evolves token by token.

PUMA (2026-05-19 today, the early-exit framework using reasoning-level semantic redundancy as a stopping signal) and this paper share a substrate: the CoT trajectory. PUMA reads the surface (semantic redundancy across steps); this paper reads the internal probe trajectory. The two are complementary: PUMA decides when to stop; probe trajectories decide whether the model's internal state is consistent with the stated stopping reason.

The faithfulness gap this paper addresses is the central failure mode of CoT-based safety monitoring, which has been the wiki's running concern since the 2026-05-13 Massive Activations / ME-Layer paper and the broader interpretability cluster. Probe trajectories are the most concrete answer in the wiki to date for how to extract safety-monitoring signal from LRMs without relying on CoT text being faithful.

## Why it matters

CoT-based monitoring is the most accessible safety surface on LRMs because it is text. But CoT unfaithfulness has been the systematic gap. Probe trajectories give a hidden-state-based monitoring layer that does not depend on text faithfulness. The 95% AUROC max-pooling result is the first time the wiki has seen a hidden-state monitoring approach reach a deployment-relevant accuracy threshold on safety prediction.

The template-based training data finding is the practical scalability claim. It removes the bottleneck (costly inference-and-labelling on every model checkpoint) that has prevented routine probe deployment.

## Research angle

- **Trajectory features beyond signal-processing primitives.** Volatility, trend, steady-state are standard time-series features. Whether more model-aware features (e.g. trajectory regime changes, attention-head-aligned probes) improve AUROC is the natural follow-up.
- **Cross-model transfer.** The paper trains probes per model. Whether a probe trained on Llama-3-Reasoner transfers zero-shot to Qwen-3.5-Reasoner is the deployment-relevant question.
- **Compose with PUMA.** PUMA decides when to stop. Probe trajectory monitoring decides whether the stopping point is safe. Whether the composition reduces false positives in safety-flagged exits is testable.

## Source

`raw/huggingface/2026-05-19-monitoring-the-internal-monologue-probe-trajectories-reveal-.md`
