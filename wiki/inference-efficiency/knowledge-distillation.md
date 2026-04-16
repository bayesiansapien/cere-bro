# Knowledge Distillation

Transferring capabilities from a large teacher model to a smaller student model. On-policy distillation (OPD) trains the student on its own rollouts under token-level supervision from the teacher.

## Current State (as of 2026-04-16)

On-policy distillation has become the dominant approach for reasoning model compression. The key open question is which tokens actually carry the learning signal — naive approaches use all tokens, but most are uninformative.

## Key Papers

**TIP: Token Importance in On-Policy Distillation (2026-04-16)** — Identifies two high-signal token regions: high-entropy (uncertain student) and low-entropy + high-divergence (overconfident but wrong). Entropy-based 50% token selection matches full training with 47% less peak memory. <10% of tokens (targeting overconfident region) nearly matches full baseline. → [summary](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md)

## Key Concepts

- **On-policy distillation**: student generates its own rollouts, then learns from teacher's token-level distribution over those rollouts
- **High entropy tokens**: student is uncertain — natural learning signal
- **Overconfident tokens** (low entropy, high divergence): student is wrong but confident — dense corrective signal often missed by entropy-only selection
- **Memory efficiency**: token selection not only improves learning quality but also reduces peak GPU memory — critical for distilling large reasoning models

## Related Pages

- [../llms-foundation-models/rl-for-llms.md](../llms-foundation-models/rl-for-llms.md)
- [../llms-foundation-models/2026-04-16-prerl-rl-in-pretrain-space.md](../llms-foundation-models/2026-04-16-prerl-rl-in-pretrain-space.md)
