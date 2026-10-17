---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.22355
url: https://huggingface.co/papers/2610.22355
arxiv_url: https://arxiv.org/abs/2610.22355
date: 2026-10-16
---

# OmniVerifier-C1: Decomposed Graded Verifier for Rule-Governed Generative World Modeling

Generative visual verifiers play a crucial role in advancing multimodal intelligence. To enhance the robustness of visual verifiers in complex multimodal scenarios involving compositional requirements, we move beyond conventional binary verifiers that produce only True/False discrete judgments and introduce a verifier that automatically decomposes complex prompts or environmental rules into fine-grained components and assigns pointwise scores to provide a continuous and more informative critique signal. Our experiments further demonstrate that these structured and interpretable outputs improve the verifier's generalization to out-of-domain multimodal critic tasks. To train this verifier, we introduce a Decoupled RL training strategy that jointly optimizes sub-question-level binary judgment and global alignment scoring, using precise local feedback to develop fine-grained verification capabilities that provide a foundation for reliable continuous scoring at the global level. Under a general reinforcement learning framework, we first empirically demonstrate that the proposed pointwise graded verifier significantly outperforms binary verifiers in traditional text-to-image scenarios. We then extend our investigation to rule-governed generative world modeling where generative models are leveraged for world simulation and world reasoning under explicit rules. From a theoretical standpoint, we further show that a pairwise verification paradigm yields more accurate critiques than the pointwise formulation when ground-truth images are available, with empirical results on diverse structured world-modeling tasks such as Maze and Sudoku further validating the effectiveness of our approach. Overall, our findings suggest a key insight: the transition from generative models to structured world-modeling agents critically hinges on the availability of accurate pairwise graded visual verifiers.
