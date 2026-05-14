---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.12997
url: https://huggingface.co/papers/2605.12997
arxiv_url: https://arxiv.org/abs/2605.12997
date: 2026-05-14
---

# Frequency Bias and OOD Generalization in Neural Operators under a Variable-Coefficient Wave Equation

Neural operators learn to map initial conditions to the terminal solution of partial differential equations (PDEs), providing a surrogate for the full operator mapping. This enables rapid prediction across different input configurations. While recent neural operator architectures have demonstrated strong performance on diverse PDE tasks, their behavior under structured distribution shifts remains insufficiently understood. To investigate this, we study operator learning in a wave propagation setting governed by a one-dimensional variable-coefficient wave equation, using two representative architectures, the Fourier Neural Operator (FNO) and the Deep Operator Network (DeepONet). To examine their generalization under distribution shifts, we consider structured out-of-distribution (OOD) settings that independently vary input frequency and coefficient smoothness. The results show that under smoothness shifts, both models maintain stable performance, with FNO achieving lower error. In contrast, under frequency shifts, FNO exhibits a sharp increase in error under unseen high-frequency inputs, whereas DeepONet shows milder degradation despite higher overall error. Our analysis reveals that these differences arise from how each architecture represents and responds to variations in frequency structure. Together, these findings highlight a fundamental gap between strong in-distribution performance and generalization under distribution shifts in operator learning, underscoring the role of architectural representation bias in developing more reliable neural operators for physics-based PDE simulations beyond the training distribution.
