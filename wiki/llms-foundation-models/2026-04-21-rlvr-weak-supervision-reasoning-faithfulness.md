# When Does RLVR Generalize? Reward Saturation and Reasoning Faithfulness

**Date:** 2026-04-21  
**Source:** HuggingFace Daily Papers  
**Paper:** [arxiv 2604.18574](https://arxiv.org/abs/2604.18574)  
**Raw:** [raw/huggingface/2026-04-21-when-can-llms-learn-to-reason-with-weak-supervision.md](../../raw/huggingface/2026-04-21-when-can-llms-learn-to-reason-with-weak-supervision.md)

---

## TL;DR

Systematic empirical study of when RLVR works under weak supervision (scarce data, noisy rewards, self-supervised proxy rewards). Key finding: generalization is governed by reward saturation dynamics during training, not output diversity. Models that generalize show a prolonged pre-saturation phase where training reward and downstream performance climb together. Models that fail saturate rapidly and memorize. The pre-RL property that predicts which regime: reasoning faithfulness (how logically the intermediate steps support the answer). Output diversity alone is uninformative.

---

## Key Findings

- **Three weak supervision settings studied**: scarce data, noisy rewards, self-supervised proxy rewards
- **Reward saturation dynamics predict generalization**:
  - Generalizing models: training reward climbs slowly (prolonged pre-saturation), downstream performance tracks it
  - Failing models: training reward saturates immediately → memorization, not generalization
- **Reasoning faithfulness is the key pre-RL predictor**: measures whether intermediate reasoning steps logically support the final answer — not just whether the answer is correct
- **Output diversity is uninformative**: diverse outputs don't predict whether RL will generalize
- **What enables generalization from scratch**: SFT on explicit reasoning traces is *necessary* (not just helpful); continual pre-training on domain data amplifies the effect
- **Applied to Llama3.2-3B-Base**: both interventions together enable generalization across all three weak supervision settings where base model failed

---

## Connection to Prior Wiki Work

This paper is a direct follow-on to the AIMO 3 finding (04-17) that output diversity doesn't help. AIMO 3 showed diversity doesn't close the inference-time gap. This paper now shows diversity doesn't predict the *training-time* generalization either. The converging message: **diversity is a noise metric, not a signal metric.** What matters is whether the reasoning process is logically coherent (faithfulness), not how many different outputs the model can generate.

This also connects directly to GFT (today): GFT's group advantage learning doesn't just create diverse outputs — it creates *contrastively supervised* outputs where the model has to distinguish better from worse reasoning paths. That's closer to training reasoning faithfulness than raw diversity.

---

## Practical Implications

1. If you're fine-tuning a model for a domain with weak rewards, check reasoning faithfulness *before* doing RL — it predicts whether the RL will work
2. SFT on explicit reasoning traces is not optional as preparation for weak-supervision RL — it's the prerequisite
3. Monitoring reward saturation speed during RL training is a diagnostic: fast saturation early = you're memorizing

---

## Related Pages

- [RL for LLMs](rl-for-llms.md)
- [GFT: SFT as Degenerate RL](2026-04-21-gft-sft-as-degenerate-rl.md)
- [AIMO 3: Model Capability Dominates](../inference-efficiency/2026-04-17-model-capability-dominates-inference-time.md)
