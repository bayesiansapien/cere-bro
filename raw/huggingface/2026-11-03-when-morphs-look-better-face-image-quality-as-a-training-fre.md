---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.00074
url: https://huggingface.co/papers/2611.00074
arxiv_url: https://arxiv.org/abs/2611.00074
date: 2026-11-03
---

# When Morphs Look Better: Face Image Quality as a Training-Free Signal for Morphing Attack Detection

Face image quality assessment (FIQA) estimates the utility of a face image for automated face recognition and has been proposed as a morphing attack detection (MAD) signal that requires no morph-specific training. We evaluate 17 FIQA methods from all current FIQA categories on 20 morphing attack sets from two datasets, FRLL and FEI, including five diffusion-based attack sets. Each quality score is used directly as a MAD decision score. Unlike prior work, which inverted a quality measure when this lowered its error, we fix the score direction of each method in advance from its definition, so that cases in which morphs receive higher quality than bona fide samples remain visible. On FRLL, DifFIQA(R) achieves a mean D-EER of 11.42%, and together with CLIB-FIQA and eDifFIQA(L) clearly outperforms all other FIQA methods. A strong separation of bona fide and morph scores does not imply good detection performance: on the diffusion-based attacks, up to 11 of 17 methods assign higher quality to morphs than to bona fide samples, and the largest reversed separation in the study coincides with the worst detection result of the study. Performance also depends strongly on the attack: GraFIQs(L), the best detector of DCMorph and Arc2Morph on FRLL, performs poorly on the landmark-based and GAN-based attacks. On FEI, the lowest mean D-EER is 39.75%, and a threshold set on the bona fide data of one dataset does not transfer to the other.
