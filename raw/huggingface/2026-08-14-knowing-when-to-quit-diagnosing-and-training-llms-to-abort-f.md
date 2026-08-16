---
source: farmer/huggingface
farmed: 2026-08-16T08:10:48.292809+00:00
arxiv_id: 2607.29211
url: https://huggingface.co/papers/2607.29211
arxiv_url: https://arxiv.org/abs/2607.29211
date: 2026-08-14
---

# Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning

Large language models generate computationally expensive yet semantically void reasoning on beyond-capability tasks, creating risks where plausible-sounding but incorrect derivations mislead users. We characterize this futile reasoning phenomenon through systematic analysis, revealing universal capability overreach and systematic miscalibration between capability and behavior. The dominant failure mode is specious reasoning, which outputs look superficially valid but contain subtle errors, escalating with task difficulty. To address this, we introduce CaRL (Capability-aligned Reinforcement Learning), which aligns model behavior with capability boundaries through reward shaping that incentivizes refusal over futile reasoning and hindsight refusal augmentation that converts failures into refusal supervision. Experiments demonstrate a substantial reduction in futile reasoning while preserving performance across task difficulties, effectively achieving capability-aligned behavior without sacrificing utility. https://github.com/icip-cas/Knowing-When-to-Quit
