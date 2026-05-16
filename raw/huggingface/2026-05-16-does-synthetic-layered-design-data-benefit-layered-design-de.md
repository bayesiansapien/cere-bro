---
source: farmer/huggingface
farmed: 2026-05-16T03:36:10Z
arxiv_id: "2605.15167"
url: "https://huggingface.co/papers/2605.15167"
arxiv_url: "https://arxiv.org/abs/2605.15167"
date: 2026-05-16
---

# Does Synthetic Layered Design Data Benefit Layered Design Decomposition?

Recent advances in image generation have made it easy to produce high-quality images. However, these outputs are inherently flattened, entangling foreground elements, background, and text within a fixed canvas. As a result, flexible post-generation editing remains challenging, revealing a clear last-mile gap toward practical usability. Existing approaches either rely on scarce proprietary layered assets or construct partially synthetic data from limited structural priors. However, both strategies face fundamental challenges in scalability. In this work, we investigate whether pure synthetic layered data can improve graphic design decomposition. We make the assumption that, in graphic design, effective decomposition does not require modeling inter-layer dependencies as precisely as in natural-image composition, since design elements are often intentionally arranged as modular and semantically separable components. Concretely, we conduct a data-centric study based on CLD baseline, which is a state-of-the-art layer decomposition framework. Based on the baseline, we construct our own synthetic dataset, SynLayers, generate textual supervision using vision language models, and automate inference inputs with VLM-predicted bounding boxes. Our study reveals three key findings: (1) even training with purely synthetic data can outperform non-scalable alternatives such as the widely used PrismLayersPro dataset, demonstrating its viability as a scalable and effective substitute; (2) performance consistently improves with increased training data scale, while gains begin to saturate at around 50K samples; and (3) synthetic data enables balanced control over layer-count distributions, avoiding the layer-count imbalance commonly observed in real-world datasets. We hope this data-centric study encourages broader adoption of synthetic data as a practical foundation for layered design editing systems.
