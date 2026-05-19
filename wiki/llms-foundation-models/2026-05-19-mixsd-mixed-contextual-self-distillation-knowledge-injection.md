# MixSD: Mixed Contextual Self-Distillation for Knowledge Injection

**arXiv:** [2605.16865](https://arxiv.org/abs/2605.16865) · **HF:** [paper page](https://huggingface.co/papers/2605.16865) · **Tier:** 2 (post-training, knowledge injection, catastrophic forgetting)

## TL;DR

Supervised fine-tuning (SFT) is widely used to inject new knowledge into language models but often degrades pretrained capabilities such as reasoning and general-domain performance. The argument: forgetting arises because fine-tuning targets from humans or external systems diverge from the model's autoregressive distribution, forcing the optimizer to imitate low-probability token sequences. MixSD constructs supervision dynamically by mixing tokens from two conditionals of the base model itself: an expert conditional that observes the injected fact in context, and a naive conditional that reflects the model's original prior. The mixed supervision sequences preserve the factual learning signal while staying close to the base model's distribution. Across factual recall, arithmetic-function acquisition, open-domain QA, and knowledge editing, MixSD consistently achieves a better memorisation-retention tradeoff than SFT and on-policy self-distillation baselines, retaining up to 100% of held-out capability while reaching near-perfect training accuracy. Standard SFT retains as little as 1%.

## Key findings

- Standard SFT forces the model to imitate token sequences that are low probability under the base model's own distribution. The optimiser pays a large gradient cost to match those tokens, and that cost spills over to perturb the parameters that produce the model's other capabilities.
- The diagnostic is harmful movement along Fisher-sensitive parameter directions: SFT moves parameters along directions where the Fisher information matrix has large eigenvalues, which is exactly the directions whose movement degrades broad capability.
- MixSD's structural move: do not impose external targets, generate supervision from the model itself by mixing two of its own conditionals.
  - Expert conditional: the model is given the new fact in context and generates tokens.
  - Naive conditional: the model is not given the fact and generates tokens.
  - The mixed supervision sequence interleaves tokens from both, weighted to preserve the factual signal while keeping each token close to the base distribution.
- This makes supervision substantially closer to the base model's distribution, lowering the NLL of supervision targets under the base model.
- Across multiple model scales and settings, MixSD retains up to 100% of held-out base capability at near-perfect training accuracy. SFT retains as little as 1%.

## Relationship to prior wiki entries

MixSD is the post-training distillation companion to the wiki's running self-distillation thread. ZEDA (2026-05-19 today, the post-trained MoE static-to-dynamic conversion using zero experts and two-stage self-distillation from the original frozen MoE as teacher) uses the same architectural principle (the base model as its own teacher) for a different problem (architectural conversion vs knowledge injection). Both reduce the distribution shift that traditional SFT or external-teacher distillation imposes.

It also connects to TIP (Targeted Iterative Pruning, the 2026-04-16 paper that found most teacher-generated tokens during distillation carry no learning signal and only 10% need to be trained on), to PreRL (2026-04-16, which argued the question is really about the pre-training data distribution rather than the training loop), and to LongAct (2026-04-18, which showed that long-context training signal is concentrated in the first 5% of tokens, so the gradient is what matters). Each paper found that the imitation surface in standard SFT or distillation is too broad. MixSD takes the next step: reshape what gets imitated by mixing self-conditionals, not by selecting which targets to imitate.

ATESD (2026-05-16, Adaptive Teacher-Exposure Self-Distillation) was the closest prior method. MixSD's specific contribution beyond ATESD is the two-conditional mix from the base model itself, which avoids needing an external teacher entirely.

## Why it matters

Knowledge injection without catastrophic forgetting is the unsolved post-training problem for any deployment that needs to add facts (compliance updates, internal docs, time-sensitive data) without retraining. The current operational practice is to keep external retrieval over a stale model. MixSD is the cleanest evidence in the wiki that on-weights injection can be safe (100% retention vs SFT's 1%), which opens the door to substituting some retrieval-augmented patterns with weight-injection patterns.

The Fisher-direction diagnostic is also a generalisable principle. Any post-training that moves the model along Fisher-sensitive directions will degrade capability. Methods that constrain movement to non-Fisher-sensitive directions (MixSD, low-rank LoRA targeting non-Fisher-sensitive subspaces) should be the default for capability-preserving updates.

## Research angle

- **MixSD on arithmetic-function acquisition is the cleanest test.** The synthetic corpus is controlled. Whether the retention benefit holds for richer skills (multi-step reasoning, tool use) is the next falsifier.
- **Compose with model editing.** Knowledge editing methods (ROME, MEMIT) inject single facts surgically. MixSD does many at once via distillation. The composition (use editing for surgical facts, MixSD for bulk corpora) is one deployment pattern away.
- **Why the 100% retention?** The paper attributes it to distribution alignment. Whether the alignment is sufficient or whether MixSD's hidden constraint (the model can only learn things consistent with its expert-conditioning) is the real explanation is the mechanistic question.

## Source

`raw/huggingface/2026-05-19-mixsd-mixed-contextual-self-distillation-for-knowledge-injec.md`
