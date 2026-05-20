# Language-Switching Triggers Take a Latent Detour Through Language Models

**Source:** HuggingFace Daily Papers 2026-05-20 · [arXiv 2605.18646](https://arxiv.org/abs/2605.18646) · [raw](../../raw/huggingface/2026-05-20-language-switching-triggers-take-a-latent-detour-through-lan.md)

## TL;DR

Backdoor attacks on language models are a growing security concern but the internal mechanisms by which a trigger sequence hijacks model computation have been poorly understood. The paper identifies a circuit underlying a language-switching backdoor in an 8B autoregressive LM, where a three-word Latin trigger (nine tokens) redirects English output to French. The circuit decomposes into three phases: (1) distributed attention heads at early layers compose the trigger tokens into the last sequence position; (2) the resulting signal propagates through mid-layers in a subspace orthogonal to the model's natural language-identity direction; (3) the MLP at the final layer converts this latent signal into French logits. The circuit flows through a serial bottleneck at a single position: corrupting that position at any layer fully mitigates the trigger but also hurts general capability. The orthogonal latent encoding implies that defenses searching for language-like signals in intermediate representations would miss this trigger entirely.

## Why it matters

This is the first wiki entry that traces a backdoor circuit through the orthogonal-subspace propagation phase rather than treating the trigger as a black-box behavioral phenomenon. The orthogonality result is the load-bearing claim: the attacker's signal lives in a direction the model's normal language representation does not occupy, which is why naive probes don't catch it. The defense-design implication is sharp: you cannot defend against this class of attack by looking for language-coded signals in the residual stream.

## Connections

- **Monitoring the Internal Monologue (2026-05-19, probe-trajectory features across CoT reaching 95% AUROC for LRM safety)** showed that trajectory-level probes outperform single-token pooling. Both papers point at the same defense-design lesson: static linear probes of intermediate states are insufficient; defenses need to read structure across positions and layers.
