---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820431+00:00
arxiv_id: 2609.39687
url: https://huggingface.co/papers/2609.39687
arxiv_url: https://arxiv.org/abs/2609.39687
date: 2026-10-02
---

# Better Supervision Is Nearby: Neighborhood On-Policy Self-Distillation

On-policy self-distillation (OPSD) trains mathematical reasoning models using a privileged teacher that sees a reference solution and supervises student-sampled prefixes. Standard OPSD uses one fixed parameter setting at every state, but nearby settings may offer additional supervision. We find that local parameter perturbations reveal complementary reference-aligned corrections under the same reference context. Different experts supply these corrections at different reference positions. Their pool covers more such positions than the unperturbed privileged teacher. We introduce Neighborhood OPSD (N-OPSD) to turn these corrections into supervision at student-visited states. Offline, greedy selection builds a compact pool of frozen experts by rewarding filtered reference-token gains beyond the pool's current best at each position. The highest-peak expert need not provide the best training target. Online routing therefore separates the anchor direction from its level of support. MaxPeak selects the anchor token, and quantile selection chooses among experts whose top token matches it. The student learns from the chosen expert's full next-token distribution through the clipped forward-KL objective inherited from OPSD. We evaluate on AIME 2024, AIME 2025, and HMMT February 2025. Across three independent runs per method, Neighborhood OPSD improves the three-benchmark Average@12 over OPSD by 2.75, 1.67, and 1.94 points on Qwen3-1.7B, 4B, and 8B, respectively. Student-prefix continuations support using the pool beyond the reference trajectories used for selection. Matched ablations support filtered reference-token gains as a selection criterion. Accounting for overlap within the pool and routing by state further improve student accuracy. Inference uses only the distilled student.
