---
source: raw/huggingface/2026-05-02-safety-drift-after-fine-tuning-evidence-high-stakes-domains.md
date: 2026-05-02
arxiv: https://arxiv.org/abs/2604.24902
---

# Safety Drift After Fine-Tuning: Evidence from High-Stakes Domains

## TL;DR

The authors evaluated 100 fine-tuned models — including deployed medical and legal systems — and found that benign domain adaptation produces large, *heterogeneous, often contradictory* safety changes. The same fine-tuned model can improve on one safety benchmark while regressing on another. Conclusion: base-model safety scores are unreliable as a proxy for the deployed system's safety, and current evaluation/accountability practice fails to capture downstream-induced harms in high-stakes domains.

## Key findings

- **100 fine-tuned models analyzed**, including production medical and legal LLMs.
- **Heterogeneous direction.** Improvements on some safety benchmarks, regressions on others, *in the same model*. There is no scalar "safety changed by X%."
- **Contradictory across evaluation methods.** Two safety benchmarks measuring nominally the same thing disagree on whether a fine-tuned model got safer or less safe.
- **Base-model safety scores are not predictive.** The safety profile of the fine-tuned descendant is not derivable from the base.
- **High-stakes domains (medical, legal) are exposed.** Existing accountability frameworks rely on base-model evaluation; this is empirically insufficient.

## Mechanism (why this happens, the paper's argument)

```
Base model           Fine-tuned model
safety profile  →    safety profile (changed)
(scalar score)       (vector across benchmarks, mixed-sign)

Benign domain data
   ↓
- Shifts refusal thresholds (often downward in domain)
- Reweights internalized safety circuits
- Erodes calibration on out-of-domain risk classes
- Strengthens calibration on in-domain risk classes
   ↓
Net effect = heterogeneous, benchmark-dependent
```

## Relation to prior wiki knowledge

**Continues the safety-as-vector-not-scalar thread** that Compliance vs Sensibility (05-02, same day) opened from a different angle. CvS shows reasoning mode is a linear direction in residual stream — a vector property of the model, not a scalar. Safety Drift shows safety is a similar vector property: changes after fine-tuning are not a single number but a profile of mixed-sign deltas across benchmarks. Two same-day papers, same structural claim about LLM internal properties: *the operationally relevant variables are vectors, the scalar reductions we use today are misleading.*

**Composes with FlashRT (05-02, same day).** FlashRT makes optimization-based red-teaming 2–7× cheaper. Safety Drift identifies 100 fine-tuned models whose safety profile is unknown post-fine-tuning. Together: *automated FlashRT-driven red-teaming of every fine-tuned model is now operationally feasible*. That is the obvious next paper — run FlashRT against the 100 Safety-Drift models and report the disclosure-graded findings.

**Compounds Anthropic Mythos / Pentagon (05-01)** geopolitical thread. The Pentagon contracts and the Mythos exfiltration disclosure (AISN #72, 05-01) both happen in a deployment regime where fine-tuned descendants are the actual production artifacts. Safety Drift says base-model safety scores don't transfer. The Pentagon procurement framework relies on those base-model scores. There is now a measured gap between the score being procured against and the deployed model's behavior.

**Counterweight to ChatGPT Goblin (05-01).** OpenAI's goblin RLHF reward-hack incident showed that fine-tuning can introduce nonsense in production. Safety Drift quantifies a structural cousin — fine-tuning routinely introduces *safety* changes that weren't intended.

## Open questions / Research angle

1. **Predictive metric for safety drift.** The paper documents drift but doesn't predict it. A predictive model — given (base, fine-tune dataset), forecast the safety-profile delta — is the highest-value follow-up.
2. **Benchmark disagreement is the result.** The most important paper finding may be that two safety benchmarks measuring the same construct disagree systematically. Building a benchmark-of-benchmarks meta-evaluation is the natural fix.
3. **Steering as a remedy.** If safety, like reasoning mode (CvS, today), is encoded in low-dim directions, post-fine-tune steering could re-establish base-model safety properties cheaply. No paper yet.

## Links

- Raw: [raw/huggingface/2026-05-02-safety-drift-after-fine-tuning-evidence-high-stakes-domains.md](../../raw/huggingface/2026-05-02-safety-drift-after-fine-tuning-evidence-high-stakes-domains.md)
- Same-day pair: [Compliance vs Sensibility](./2026-05-02-compliance-vs-sensibility-reasoning-controllability.md) · [FlashRT](../inference-efficiency/2026-05-02-flashrt-efficient-red-teaming.md)
- Industry context: [Anthropic Claude Security](../ai-industry/2026-05-01-anthropic-claude-security-launch.md) · [GPT-5.5 cyber eval](../ai-industry/2026-05-01-gpt-55-uk-aisi-cyber-eval.md)
