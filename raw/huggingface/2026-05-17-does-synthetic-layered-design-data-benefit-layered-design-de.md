---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.15167"
url: "https://huggingface.co/papers/2605.15167"
arxiv_url: "https://arxiv.org/abs/2605.15167"
date: 2026-05-17
---

# Does Synthetic Layered Design Data Benefit Layered Design Decomposition?

Recent advances in image generation have made it easy to produce high-quality images. However, these outputs are inherently flattened, entangling foreground elements, background, and text within a fixed canvas. As a result, flexible post-generation editing remains challenging, revealing a clear last-mile gap toward practical usability. Existing approaches either rely on scarce proprietary layered assets or construct partially synthetic data from limited structural priors. In this work, we investigate whether pure synthetic layered data can improve graphic design decomposition. We make the assumption that, in graphic design, effective decomposition does not require modeling inter-layer dependencies as precisely as in natural-image composition, since design elements are often intentionally arranged as modular and semantically separable components. We construct our own synthetic dataset, SynLayers, and our study reveals three key findings: (1) even training with purely synthetic data can outperform non-scalable alternatives; (2) performance consistently improves with increased training data scale, while gains begin to saturate at around 50K samples; and (3) synthetic data enables balanced control over layer-count distributions.
