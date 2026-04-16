---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13256
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13256
published: 2026-04-16
authors: Sanjar Khudoyberdiev, Arman Bekov
---

# Counterfactual Peptide Editing for Causal TCR--pMHC Binding Inference

**arXiv:** https://arxiv.org/abs/2604.13256
**Authors:** Sanjar Khudoyberdiev, Arman Bekov

## Abstract

arXiv:2604.13256v1 Announce Type: new  Abstract: Neural models for TCR-pMHC binding prediction are susceptible to shortcut learning: they exploit spurious correlations in training data -- such as peptide length bias or V-gene co-occurrence -- rather than the physical binding interface. This renders predictions brittle under family-held-out and distance-aware evaluation, where such shortcuts do not transfer. We introduce \emph{Counterfactual Invariant Prediction} (CIP), a training framework that generates biologically constrained counterfactual peptide edits and enforces invariance to edits at non-anchor positions while amplifying sensitivity at MHC anchor residues. CIP augments the base classifier with two auxiliary objectives: (1) an invariance loss penalizing prediction changes under conservative non-anchor substitutions, and (2) a contrastive loss encouraging large prediction changes under anchor-position disruptions. Evaluated on a curated VDJdb-IEDB benchmark under family-held-out, distance-aware, and random splits, CIP achieves AUROC 0.831 and counterfactual consistency (CFC) 0.724 under the challenging family-held-out protocol -- a 39.7\% reduction in shortcut index relative to the unconstrained baseline. Ablations confirm that anchor-aware edit generation is the dominant driver of OOD gains, providing a practical recipe for causally-grounded TCR specificity modeling.
