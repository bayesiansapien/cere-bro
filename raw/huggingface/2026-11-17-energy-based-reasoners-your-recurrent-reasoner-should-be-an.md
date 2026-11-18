---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.111430+00:00
arxiv_id: 2611.08977
url: https://huggingface.co/papers/2611.08977
arxiv_url: https://arxiv.org/abs/2611.08977
date: 2026-11-17
---

# Energy-Based Reasoners: Your Recurrent Reasoner Should Be an Energy-Based Model

Looping is a powerful inductive bias for reasoning. By repeatedly iterating a recurrent block, looped models can scale their effective depth and enable multi-step reasoning in latent space. However, existing looped models are not inherently guided by an explicit measure of progress, making it difficult to determine when to stop looping and how to improve upon the current state. To enable this, we introduce Energy-Based Reasoners (EBRs), which learn an energy function over latent reasoning states and formulate looped updates as gradient descent on this energy. The energy scores latent states, while its gradient guides refinement and provides a signal for stopping. To train EBRs effectively, we further introduce exploration-based training to discover additional modes and to better shape the energy landscape over a broader set of states. Across four algorithmic reasoning benchmarks, EBRs match or outperform prior recurrent reasoning models, achieving 99.9% accuracy on Sudoku-Extreme while using 345times less inference compute than the next-best model and maintaining comparable training compute. On all multi-solution benchmarks, EBRs achieve state-of-the-art coverage of distinct valid solutions while maintaining near-100% single-sample accuracy. These results suggest that energy-based models are a promising approach for strong reasoning performance.
