---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.307846+05:30
arxiv_id: 2610.07862
url: https://huggingface.co/papers/2610.07862
arxiv_url: https://arxiv.org/abs/2610.07862
date: 2026-10-08
---

# A self-learning scientific agent for X-ray diffraction

A central challenge for scientific agents is to turn analytical experience into reusable expertise grounded in physical evidence. Here we introduce Gan Jiang, a self-learning agent for powder X-ray diffraction built on a diffraction-analysis ecosystem we developed: XMatcher, XQueryer, XDecomposer and WPEM. Together, these engines span phase identification, multiphase decomposition and physics-constrained whole-pattern modelling. Gan Jiang converts analytical experience into executable skills by diagnosing failures, revising skill instructions and code, and validating revisions before reuse, without retraining the language model or changing the underlying physical models. Skills selected using development data and frozen before held-out evaluation achieve higher refinement scores than the original expert-designed skills across FullProf, GSAS-II and PyWPEM. The agent resolves strongly overlapping reflections, quantifies a five-phase ancient Egyptian cosmetic, tracks lattice evolution in an operating battery and compares atomic configurations in a disordered oxide catalyst. On DeltaXRDbench, it leads the evaluated methods in single- and multiphase identification across simulated and experimental data. Without supplied composition, single-phase top-1 accuracies reach 96.30\%, 81.78\% and 40.83\% on MP500, RRUFF and opXRD, respectively, compared with 58.00\%, 58.47\% and 26.45\% for the strongest comparator. These results demonstrate how an integrated scientific tool ecosystem can support agents that extract structural knowledge from measurements while accumulating validated analytical expertise that transfers to new samples.
