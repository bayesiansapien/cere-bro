---
source: farmer/huggingface
farmed: 2026-05-20T09:54:43.341446+00:00
arxiv_id: 2605.11609
url: https://huggingface.co/papers/2605.11609
arxiv_url: https://arxiv.org/abs/2605.11609
date: 2026-05-20
---

# Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information

On-policy self-distillation, where a student is pulled toward a copy of itself conditioned on privileged context (e.g., a verified solution or feedback), offers a promising direction for advancing reasoning capability without a stronger external teacher. Yet in math reasoning the gains are inconsistent, even when the same approach succeeds elsewhere. A pointwise mutual information analysis traces the failure to the privileged context itself: it inflates the teacher&#39;s confidence on tokens already implied by the solution (structural connectives, verifiable claims) and deflates it on deliberation tokens (&#34;Wait&#34;, &#34;Let&#34;, &#34;Maybe&#34;) that drive multi-step search. We propose Anti-Self-Distillation (AntiSD), which ascends a divergence between student and teacher rather than descending it: this reverses the per-token sign and yields a naturally bounded advantage in one step. An entropy-triggered gate disables the term once the teacher entropy collapses, completing a drop-in replacement for default self-distillation. Across five models from 4B to 30B parameters on math reasoning benchmarks, AntiSD reaches the GRPO baseline&#39;s accuracy in 2 to 10x fewer training steps and improves final accuracy by up to 11.5 points. AntiSD opens a path to scalable self-improvement, where a language model bootstraps its own reasoning through its training signal.
