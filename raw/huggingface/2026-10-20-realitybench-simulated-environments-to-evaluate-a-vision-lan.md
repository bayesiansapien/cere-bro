---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.14397
url: https://huggingface.co/papers/2610.14397
arxiv_url: https://arxiv.org/abs/2610.14397
date: 2026-10-20
---

# RealityBench: Simulated Environments to Evaluate a Vision Language Model's Ability to Document Human Physical Work

Augmenting worker capabilities in the physical world through guidance has been a decades-long goal for AI agents. One key supporting capability is to understand what the worker is doing, seeing through the human's camera or smart glasses, and assist them in documentation. Despite advances in vision language models, their capabilities in these settings remain uncertain and are challenging to benchmark because most physical work data is proprietary, and involves too much variability to study in a principled manner. Unlike structured settings such as kitchens and warehouses that have predictable lighting, geometry, and objects, field-facing tasks such as rooftop solar installation and vehicle repair are unconstrained and high variance. Here, we model real-world physical work in Blender across eleven environments, incorporating variants in both image acceptability and documentation. The acceptability task asks whether a particular view would be suitable proof-of-work and documentation asks whether an agent can understand the task-relevant state of the environment from that view. Across 26 vision-language models, we find that top models largely solve documentation when the answer is text in frame, but are weak at reading measurements and at judging small parts and spatial relations, such as whether a tape measure leans. Acceptability is harder to pin down because human raters disagree with each other. Measured against a scorer that agrees with the raters' majority about as often as a single rater does, the best models cannot be distinguished from a single non-author rater, at a cost within the range of a human pass. In the three environments where we can trace acceptability errors, most wrong rejections come from misreading the scene rather than the requirement. On the three documentation questions for which we have real images, model rankings on rendered frames transfer to real images.
