---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.29547
url: https://huggingface.co/papers/2611.29547
arxiv_url: https://arxiv.org/abs/2611.29547
date: 2026-11-25
---

# Align the Pair, Not the Sample: Representation Alignment for Faster and Better One-Step Generato

Representation alignment markedly accelerates diffusion training, but one-step generators raise a question that diffusion does not: which training path should receive the loss? A one-step generator sees two kinds of inputs. Corrupted real images come with their clean counterpart, which provides an instance-paired target. Samples generated from pure noise have no corresponding real image, yet this is where the final model operates. We study this question on Priming, which trains one-step generators from scratch by reconstructing corrupted images and then matching feature distributions with optimal transport. Aligning the generative path, the natural choice, collapses recall (0.45!to!0.15--0.25) in all 17 configurations we test, including five target constructions and loss weights down to 0.05. Aligning the paired reconstruction path with a frozen DINOv2 encoder instead helps in every setting we test. A short analysis explains this asymmetry: when the target carries no instance information about the input, the optimal aligned feature is constant within each class, so the loss pulls samples toward class prototypes. A control confirms this: aligning the paired path to a random same-class image instead of the input's own image removes most of the gain. Inside the generator, paired-path alignment creates an interface block through which post-training routes noise, and the image semantics carried through it predict sample quality across 16 models. The resulting recipe, \method, accelerates both training stages on ImageNet 256!times!256: it matches the 160-epoch baseline with 2times fewer priming epochs, surpasses its final quality with 4times fewer post-training updates, and lowers FID to 1.30 (B) and 1.155 (L) at the standard budget. A joint single-stage variant trains native one-step generators and reaches FID 1.22 with 115M parameters.
