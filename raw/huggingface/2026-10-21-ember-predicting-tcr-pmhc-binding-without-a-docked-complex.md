---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.646855
arxiv_id: 2610.27334
url: https://huggingface.co/papers/2610.27334
arxiv_url: https://arxiv.org/abs/2610.27334
date: 2026-10-21
---

# EMBER: Predicting TCR--pMHC Binding Without a Docked Complex

We propose EMBER, a structure-based framework for TCR--pMHC binding prediction that eliminates the need for a predicted docked complex, and with it the placement error that dominates such predictions. Traditional structure-based predictors utilize the co-folded complex structure of the receptor and the antigen and interpret binding from its contact surface. Consequently, every downstream feature inherits any deviation the structure-prediction tool introduced. Methodologically, EMBER folds the TCR and pMHC independently, encodes them as SE(3)-invariant residue graphs, and compares their learned representations without constructing a shared coordinate frame. A relative pose is therefore not an input of the model, so placement error cannot propagate into the prediction. Computationally, EMBER preprocesses O(N{+}M) monomer folds where a complex-based predictor needs O(NM) operations. Experimentally, under epitope-disjoint evaluation with six retrained baselines, EMBER is first on every metric under all four folding tools, by 0.9 to 14.4% in micro-AUROC, 18.5 to 25.3% in micro-AUPRC and 10.6 to 24.1% in MCC. Its ranking is also up to 85% more stable across folding tools.
