---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.08734
url: https://huggingface.co/papers/2605.08734
arxiv_url: https://arxiv.org/abs/2605.08734
date: 2026-05-13
---

# AdaPreLoRA: Adafactor Preconditioned Low-Rank Adaptation

Low-Rank Adaptation (LoRA) reparameterizes a weight update as a product of two low-rank factors, but the Jacobian J_{G} of the generator mapping the factors to the weight matrix is rank-deficient, so the factor-space preconditioner J_{G}^* {F}_t J_{G} induced by any {W}-space preconditioner {F}_t is singular, and consequently the standard chain rule cannot be uniquely inverted to map a preconditioned {W}-space direction back to a factor-space update. We cast existing LoRA optimizers in a unified framework parameterized by two choices: (i) which invertible surrogate for J_{G}^* {F}_t J_{G} to use, and (ii) which {F}_t on {W} to use. Existing methods occupy four families along these axes: factor-space adaptive updates, block-diagonal surrogates for J_{G}^* J_{G}, Frobenius-residual pseudoinverse methods, and Riemannian manifold constraint. Within this design space, a gradient-statistics-aware {F}_t paired with a closed-form factor-space solve at {O}((m+n)r) memory remains underexplored. We propose AdaPreLoRA, which fills this gap by adopting the Adafactor diagonal Kronecker preconditioner {H}_t on {W} and selecting from the resulting factor-space solution family the element minimizing an {H}_t-weighted imbalance between the two factor contributions; by construction, the resulting factor update is the closest LoRA approximation to the preconditioned {W}-space direction under the {H}_t-weighted norm. Across GPT-2 (E2E), Mistral-7B and Qwen2-7B (GLUE, ARC, GSM8K), and diffusion-model personalization, AdaPreLoRA is competitive with or improves over a representative set of LoRA optimizers while keeping peak GPU memory at the LoRA optimizer level.
