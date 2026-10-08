---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.07384
url: https://huggingface.co/papers/2610.07384
arxiv_url: https://arxiv.org/abs/2610.07384
date: 2026-10-07
---

# WildMatch: Weakly Supervised Image Matcher Adaptation for Wildlife Re-Identification

Individual animal re-identification from camera-trap imagery is an instance retrieval problem central to non-invasive wildlife monitoring: a query image must retrieve the correct individual from a reference set of known animals. This requires computer vision models to recognize distinctive local patterns in fur, skin, or other visual markings. Current approaches either learn global embeddings as a classification problem, requiring many labeled images per individual while largely ignoring local evidence, or apply off-the-shelf, domain-agnostic image matchers. Although such matchers are pretrained on large and diverse image collections, adapting them to wildlife imagery is challenging because available datasets are small and lack correspondence-level annotations. We study weakly supervised adaptation of a pretrained keypoint matcher using only identity labels, without keypoint-level or geometric correspondence ground truth. We mine informative image pairs with the pretrained matcher, derive weak positive and negative supervision from identity agreement, and contrastively fine-tune the matching network to strengthen correspondences for same-identity pairs and suppress them for different identities. Across open-source wildlife re-identification datasets, our approach improves accuracy over off-the-shelf matchers and a state-of-the-art local--global fusion method. Under an open-world protocol with held-out individuals, it learns a transferable correspondence prior rather than memorizing training identities. To our knowledge, this is the first study of matcher-level, identity-supervised adaptation for animal re-identification. Our method enables data-efficient specialization of image matching models to wildlife domains using identity annotations already available in typical monitoring datasets.
