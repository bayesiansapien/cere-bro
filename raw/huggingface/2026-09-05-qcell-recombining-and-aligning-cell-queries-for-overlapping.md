---
source: farmer/huggingface
farmed: 2026-09-05T10:14:12.541801+05:30
arxiv_id: 2608.29253
url: https://huggingface.co/papers/2608.29253
arxiv_url: https://arxiv.org/abs/2608.29253
date: 2026-09-05
---

# QCell: Recombining and Aligning Cell Queries for Overlapping Instance Segmentation

Instance segmentation of overlapping cells in microscopy remains challenging due to semi-transparent structures that produce weak boundaries and mixed visual evidence in overlap regions. Existing methods address this through local regions of interest or shape priors but lack global reasoning across overlapping objects. We present QCell, a novel query-based model that de-overlaps cell instances in microscopy scenes. Our approach combines (i) an instance recombination module that decomposes and recombines query representations in latent space, enabling the model to reason about complete object structure under overlap, and (ii) a contrastive query alignment objective that combines distinctive instance feature learning and separation of overlapping cell queries. We additionally introduce a new Organoid dataset benchmark for overlapping cell segmentation. We show that QCell outperforms state-of-the-art methods across multiple benchmarks, achieving +2.2 AP and +2.7 AJI on ISBI2014. Code is available at https://github.com/SlavkoPrytula/QCell
