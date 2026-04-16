---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13835
category: cs.CV
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13835
published: 2026-04-16
authors: Hye Jin Rhee, Joseph Damilola Akinyemi
---

# A Resource-Efficient Hybrid CNN-LSTM network for image-based bean leaf disease classification

**arXiv:** https://arxiv.org/abs/2604.13835
**Authors:** Hye Jin Rhee, Joseph Damilola Akinyemi

## Abstract

arXiv:2604.13835v1 Announce Type: new  Abstract: Accurate and resource-efficient automated diagnosis is a cornerstone of modern agricultural expert systems. While Convolutional Neural Networks (CNNs) have established benchmarks in plant pathology, their ability to capture long-range spatial dependencies is often limited by standard pooling layers, and their high memory footprint hinders deployment on portable devices. This paper proposes a lightweight hybrid CNN-LSTM system for bean leaf disease classification. By integrating an LSTM layer to model the spatial-sequential relationships within feature maps, our hybrid architecture achieves a 94.38% accuracy while maintaining an exceptionally small footprint of 1.86 MB; a 70% reduction in size compared to traditional CNN-based systems. Furthermore, we provide a systematic evaluation of image augmentation strategies, demonstrating that tailored transformations are superior to generic combinations for maintaining the integrity of diagnostic patterns. Results on the $\textit{ibean}$ dataset confirm that the proposed system achieves state-of-the-art F1 scores of 99.22% with EfficientNet-B7+LSTM, providing a robust and scalable framework for real-time agricultural decision support in resource-constrained environments. The code and augmented datasets used in this study are publicly available on this $\href{https://github.com/HJin-R/bean_disease}{Github}$ repo.
