---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.509185+00:00
arxiv_id: 2610.13989
url: https://huggingface.co/papers/2610.13989
arxiv_url: https://arxiv.org/abs/2610.13989
date: 2026-10-14
---

# PsyBer-Agent: A Psychology-Driven User Agent for Recommender Systems

Evaluating recommender systems before deployment requires simulators that remain realistic over long, closed-loop interaction cycles. Current LLM-based agents generally function as surface imitators that generate realistic short-term responses but fail to capture the underlying user dynamics such as fatigue, affect, and shifting preferences. We propose PsyBer-Agent, a psychology-inspired simulator that models these dynamics through its Psy-Engine. This engine represents each user with three evolving, model-defined latent states. To calibrate simulated behavior against real interaction logs, we align log-conditioned reference trajectories with simulator-generated latent-state trajectories via Unbalanced Gromov--Wasserstein optimal transport. This approach provides structured supervision for a lightweight policy without the computational burden of fine-tuning the backbone LLM. We also introduce WebSim and the PsyBer Benchmark, which encompass multimodal scenarios and seven recommender backbones. Our framework evaluates behavioral fidelity, latent-state consistency, robustness, and responses to social-cue perturbations. On the tested horizons, PsyBer-Agent shows lower behavioral discrepancy than the prompt-only simulators while maintaining stable performance under large-scale concurrent simulation for up to 5M queued simulation tasks under bounded concurrency. Code is available in the supplementary material and at: PsyBer-Agent: https://anonymous.4open.science/r/CC66F/, WebSim Platform: https://anonymous.4open.science/r/D8EAX/.
