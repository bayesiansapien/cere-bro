# Token-Level Generalization in LoRA Adapter Backdoors

**Source:** HuggingFace Daily Papers (2026-05-30) · arxiv 2605.30189
**Raw:** [raw/huggingface/2026-05-30-token-level-generalization-in-lora-adapter-backdoors-attack.md](../../raw/huggingface/2026-05-30-token-level-generalization-in-lora-adapter-backdoors-attack.md)

## TL;DR

LoRA adapters are the dominant distribution format for fine-tuned LLMs, and this paper shows they can be reliably backdoored through training-data poisoning while preserving baseline task performance. A small fraction of poisoned examples drives a clean-accuracy-preserving backdoor to saturation on a Qwen 2.5 1.5B prompt-injection classifier. The crucial finding: the backdoor generalizes at the *token-feature level*, not the structural-pattern level. A model trained on one RFC reference activates on any RFC reference but does *not* transfer to structurally identical ISO, OWASP, CWE, or NIST citations. That asymmetry favors the attacker: a defender cannot probe for "structured citations" generically. The authors propose two complementary detection routes (a behavioral probe-battery test and a weight-level Frobenius statistic) and localize the backdoor to the down-projection of MLP blocks at mid-to-late layers.

## Why this matters

The wiki has been tracking the agent supply chain attack surface across three artifacts:

1. **skill.md attacks (05-23)** — Anthropic-style skill files as a supply vector.
2. **Project Glasswing / 10,000 Mythos vulnerabilities (05-23)** — Anthropic disclosed a class of jailbreaks at model scale.
3. **Refusal neuron (05-12, via tweet)** — a single MLP neuron can bypass safety in 7 models.

Today's adapter-backdoor paper completes the picture at the *LoRA artifact layer*. Adapters are the format people ship fine-tuned models in, and the attack is invisible on clean accuracy and structurally non-generic. The supply chain risk surface for shared adapter hubs is now concrete.

## Key claims

- A small poisoned-example fraction drives backdoor saturation on a Qwen 2.5 1.5B prompt-injection classifier with preserved clean accuracy.
- Backdoor generalization is **token-feature-level, not structural**: trained on one RFC reference, activates on any RFC reference, does not transfer to ISO / OWASP / CWE / NIST citations even when those are structurally identical.
- Two detectors:
  - **Behavioral**: probe-battery statistics (`outlier_gap`, `mean_attack_rate`). Perfect separation when the battery overlaps the trigger token neighborhood; zero false positives at high recall otherwise.
  - **Weight-level**: cross-module standard deviation of dimension-normalized Frobenius norms separates clean/poisoned without running the model.
- Causal patching localizes the backdoor to MLP **down_proj** at mid-to-late layers.
- Attack scales **monotonically with LoRA rank**. Trigger token choice is base-model-dependent.
- Behavioral detector transfers across scale/family/rank without retuning; weight-level detector is calibration-bound to the base model.

## Gaps and limits

- Single-task evaluation (prompt-injection classifier). Whether token-feature-level generalization holds for generative tasks (chatbot refusal, code generation safety) is untested.
- The base-model dependence of the trigger anchor means each victim base model can require fresh attacker tuning, but it also means each defender must calibrate fresh detectors.
- "Behavioral detector transfers" claim assumes a probe battery that overlaps the trigger neighborhood — defenders without prior knowledge of the trigger may not satisfy that overlap.

## Research angle

The wiki has been collecting evidence that interpretability primitives leak between alignment and attack. WriteSAE (05-14) showed that mechanistic interpretability can install single-feature behaviors at the cache write site. The refusal-neuron paper (05-12) showed a single MLP neuron can bypass safety. Today's paper localizes a backdoor in the MLP down-projection. The same architectural feature — MLP-level concept stores — is the access point for both interpretability work and supply attacks. The next question is whether *interpretability tooling itself* (SAE-based feature editing, refusal-direction patching) is the right defense, or whether it expands the attack surface by making the targets easier to find. Adapter-hub registries should at minimum add the Frobenius weight-level statistic to their scan pipeline.

## Related concept pages

- [Responsible AI](responsible-ai.md)
