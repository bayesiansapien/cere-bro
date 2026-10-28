---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.28490
url: https://huggingface.co/papers/2610.28490
arxiv_url: https://arxiv.org/abs/2610.28490
date: 2026-10-27
---

# Learning from Automatic 3D Gaussian Splatting Edits for Online Bayesian Scene Change Detection

Online scene change detection requires integrating incoming observations to determine which regions have changed relative to a reference scene. We update change beliefs as new images arrive using generalised Bayesian evidence fusion. However, the prior probability of change and evidence models are unknown beforehand, and numerical Bayesian inference can be costly. We address these challenges by learning offline from automatic edits to a reference 3D Gaussian Splatting (3DGS) model. These edits generate labelled training views without manual annotations. Together with unchanged reference observations, they provide supervision for learning scene-specific evidence models and estimating the effective pixel prior and response statistics. Online prediction combines current evidence with historical support, while closed-form local Bayes factors, parameterized by the learned response statistics, update an accumulated 3D Gaussian field. Object-guided refinement produces the final change masks. Our method achieves state-of-the-art accuracy on PASLCD and CCS3D, with 67.64% and 75.82% mIoU, respectively. On PASLCD, the complete pipeline runs at 17.2\,FPS over complete query sequences, the fastest among the evaluated online methods. Project page: https://changruizhu96.github.io/work/lego-scd/
