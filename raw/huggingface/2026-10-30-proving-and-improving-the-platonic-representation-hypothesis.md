---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.156652+00:00
arxiv_id: 2610.39302
url: https://huggingface.co/papers/2610.39302
arxiv_url: https://arxiv.org/abs/2610.39302
date: 2026-10-30
---

# Proving and Improving the Platonic Representation Hypothesis with JEPAs

Whether models trained on different modalities converge to the same representation of the world is central to AI. The Platonic Representation Hypothesis (PRH) conjectures that they do as they scale, but without a proof it offers neither a guarantee nor a recipe. We turn the hypothesis into a theorem. First, we prove a Platonic Representation Theorem: Joint-Embedding Predictive Architectures (JEPAs) trained separately on any number of modalities learn the same representation up to one rotation whenever their positive pairs are two observations of one scene--good views--and their misalignment is bounded otherwise. Second, we show that next-token prediction is a JEPA with bad views, parts of a single document, which explains why language models align with vision only through scale. Third, we validate the theory from 145k captions to the texts of 940M web images, and uncover a scaling law of alignment that predicts unseen runs within seed noise. Good views need 42 times fewer training samples than next-token prediction on the same corpus to reach the same alignment, and a 109M-parameter text JEPA aligns with DINOv2 and CLIP's image encoders better than every language model we evaluated, up to 72B parameters, and than CLIP's text encoder: next-token prediction is a remarkably inefficient route to platonic representations. As a showcase, one rotation turns separately trained encoders into an image captioner (CIDEr .838 on COCO). Even that rotation needs no pair: on the latest pair-free benchmark, our text JEPA beats every zero-shot accuracy reported with language models up to 8B parameters, e.g., 64\% against at most 56\% top-5 on ImageNet-100. Positive views, and not scale alone, are thus the lever to build platonic representations.
