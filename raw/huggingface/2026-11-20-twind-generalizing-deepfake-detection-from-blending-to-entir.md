---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.393740+00:00
arxiv_id: 2611.25935
url: https://huggingface.co/papers/2611.25935
arxiv_url: https://arxiv.org/abs/2611.25935
date: 2026-11-20
---

# TwinD: Generalizing Deepfake Detection from Blending to Entire Face Synthesis

Facial deepfake detectors are usually trained on blending fakes, where a generated face is pasted back into a real frame. Recent generators synthesize the entire face and leave no traces of blending. On a benchmark of 19 datasets released from 2019 to 2026, the best prior facial deepfake detector reaches a mean AUROC of 96.2% on ten blending datasets, but none exceeds 78.1% on five datasets of entire face synthesis (EFS). AI-generated content (AIGC) detectors do not close this gap. We propose TwinD, a detector trained on FaceForensics++ fakes and two kinds of twins: fakes made from a real frame. A reconstruction twin is a real frame reconstructed by an autoencoder, with the real pixels put back in a random region. It targets the neural traces of a decoder. A blob twin blends an altered copy of a real frame with the frame itself, targeting blending artifacts. It needs no generator and no face-shaped mask. Together, these twins provide two complementary forensic cues that generalize to unseen manipulations. TwinDreaches a mean AUROC of 96.3%, 8.9 points above the prior state-of-the-art, with 98.1% on the blending datasets and 95.6% on the EFS datasets. Trained on twins alone, without a deepfake dataset, single models still reach 94.3% on average over three seeds. For reproducibility, the code, trained model, and training data are at: https://github.com/yermandy/TwinD
