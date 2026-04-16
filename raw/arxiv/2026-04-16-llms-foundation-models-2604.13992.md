---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13992
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13992
published: 2026-04-16
authors: Mohammad Nooraiepour, Zezhang Song, Wei Li
---

# Physics-Informed Neural Networks for Methane Sorption: Cross-Gas Transfer Learning, Ensemble Collapse Under Physics Constraints, and Monte Carlo Dropout Uncertainty Quantification

**arXiv:** https://arxiv.org/abs/2604.13992
**Authors:** Mohammad Nooraiepour, Zezhang Song, Wei Li

## Abstract

arXiv:2604.13992v1 Announce Type: new  Abstract: Accurate methane sorption prediction across heterogeneous coal ranks requires models that combine thermodynamic consistency, efficient knowledge transfer across data-scarce geological systems, and calibrated uncertainty estimates, capabilities that are rarely addressed together in existing frameworks. We present a physics-informed transfer learning framework that adapts a hydrogen sorption PINN to methane sorption prediction via Elastic Weight Consolidation, coal-specific feature engineering, and a three-phase curriculum that progressively balances transfer preservation with thermodynamic fine-tuning. Trained on 993 equilibrium measurements from 114 independent coal experiments spanning lignite to anthracite, the framework achieves R2 = 0.932 on held-out coal samples, a 227% improvement over pressure-only classical isotherms, while hydrogen pre-training delivers 18.9% lower RMSE and 19.4% faster convergence than random initialization. Five Bayesian uncertainty quantification approaches reveal a systematic divergence in performance across physics-constrained architectures. Monte Carlo Dropout achieves well-calibrated uncertainty at minimal overhead, while deep ensembles, regardless of architectural diversity or initialization strategy, exhibit performance degradation because shared physics constraints narrow the admissible solution manifold. SHAP and ALE analyses confirm that learned representations remain physically interpretable and aligned with established coal sorption mechanisms: moisture-volatile interactions are most influential, pressure-temperature coupling captures thermodynamic co-dependence, and features exhibit non-monotonic effects. These results identify Monte Carlo Dropout as the best-performing UQ method in this physics-constrained transfer learning framework, and demonstrate cross-gas transfer learning as a data-efficient strategy for geological material modeling.
