---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.18329
url: https://huggingface.co/papers/2605.18329
arxiv_url: https://arxiv.org/abs/2605.18329
date: 2026-05-21
---

# Lost in the Folds: When Cross-Validation Is Not a Deep Ensemble for Uncertainty Estimation

Ensemble disagreement is widely used as a proxy for epistemic uncertainty in medical image segmentation. In practice, many studies form ensembles via K-fold cross-validation (CV), yet refer to them as ``deep ensembles'' (DE). Because CV members are trained on different data subsets, their disagreement mixes seed-driven variability with data-exposure effects, which can change how uncertainty should be interpreted. We audit recent segmentation uncertainty studies and find that terminology--implementation mismatches are common. We then compare a standard 5-fold CV ensemble to a 5-member DE (fixed training set, different random seeds) under otherwise identical configurations on three multi-rater segmentation datasets spanning three modalities. We evaluate uncertainty for calibration, failure detection, ambiguity modeling, and robustness under distribution shift. DE match segmentation accuracy while improving calibration and failure detection, whereas CV ensembles sometimes correlate more strongly with inter-rater variability on the studied datasets. Thus, ensemble construction should be chosen to match the research question: DE for reliability-oriented use (e.g., selective referral/failure detection) and CV ensembles as a proxy for ambiguity. We provide a lightweight nnU-Net modification enabling DE training within the default pipeline.
