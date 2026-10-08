---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.05967
url: https://huggingface.co/papers/2610.05967
arxiv_url: https://arxiv.org/abs/2610.05967
date: 2026-10-07
---

# JLD: Perceptual Distance Through A Jacobian Lens

Image compression, restoration, and generation all require a way to measure how different two images look to a person. Pixel error ignores how people see, while the most accurate perceptual distances are typically fitted to human judgments, tying them to a fixed data and resolution. For example, when image resolution is doubled, the correlation of DISTS with human scores on TID2013 drops from 0.815 to 0.717. We introduce the Jacobian Lens Distance (JLD), which derives its perceptual geometry from a frozen vision encoder rather than from human labels. JLD combines the locality of early patch features with the perceptual sensitivity captured by later encoder representations. Specifically, we use the encoder Jacobian to identify directions in the early feature space that most strongly affect the encoder output, producing a fixed metric tensor, E[J^top J], which we call the Jacobian lens. The lens is fitted only once from 100 unlabeled images, taking about 35 seconds. Locally, this construction defines a pullback metric in pixel space, giving JLD a clear geometric interpretation that can be directly analyzed on real images. Across four standard perceptual databases, JLD achieves state-of-the-art performance and consistently outperforms LPIPS, DISTS, PieAPP, and DreamSim. JLD is also robust to changes in image resolution, on TID2013, its lens-term correlation remains nearly unchanged when the resolution is doubled, decreasing only from 0.850 to 0.845. We further introduce JLD-fast, which is 4times faster than LPIPS-VGG while achieving a mean correlation of 0.911. Finally, JLD naturally extends to video, reaching a correlation of 0.786 on Waterloo IVC 4K compared with 0.611 for VMAF.
