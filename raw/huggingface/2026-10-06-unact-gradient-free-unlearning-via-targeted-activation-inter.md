---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.04426
url: https://huggingface.co/papers/2610.04426
arxiv_url: https://arxiv.org/abs/2610.04426
date: 2026-10-06
---

# UnAct: Gradient-Free Unlearning via Targeted Activation Intervention

Machine unlearning seeks to remove the influence of designated training data from a trained model without retraining from scratch. Retrain-free methods such as Selective Synaptic Dampening (SSD) and its label-free variant LFSSD avoid full retraining but still require backpropagation and parameter importance computed over the entire dataset. We ask: what happens when a deletion request arrives with only a few images of the class to be forgotten? To answer this question, we introduce UnAct, a gradient-free class-unlearning method that needs only forward passes over the forget images. UnAct scores late-layer units by their responses, attenuates the most responsive connections, and repeats this for up to 20 rounds using no gradients, no labels, and no retained data. On ResNet-18 trained with CIFAR-10, CIFAR-20, and CIFAR-100, UnAct is competitive with SSD and LFSSD when forgetting entire classes and, unlike them, never collapses the network when forget data is scarce. On ResNet-18, across all tested sizes, UnAct's retain accuracy stays within 2.5 points of retraining, while SSD and LFSSD, at their full-class operating points, lose up to 86 points on some classes. With five forget images on CIFAR-10, UnAct's distance to retraining is 0.21 points, against 67 for LFSSD and 90 for SSD, and re-selecting SSD's threshold at each size with an oracle does not close the gap. In preliminary transfer to ViT-B/16, UnAct's distance to retraining is 11.5 against 33.7 for SSD, and a request is 19x faster than SSD when SSD computes its importance at request time. The code is available at https://github.com/abdulmuizz0903/UnAct
