---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.03252
url: https://huggingface.co/papers/2610.03252
arxiv_url: https://arxiv.org/abs/2610.03252
date: 2026-10-06
---

# COSMI: COmpositional Synthesis of Multi-object Interactions

Generative models of human-object interaction are bounded by the data that exists: everyday activities involve several objects, but most captured datasets record one at a time, as multi-object capture is combinatorially expensive. Our observation is that interactions are local, so single-object captures already contain the parts of multi-object activities. We compose them: contact-consistent clips of single interactions, mirrored to balance the hands, transfer between bodies, and a language model and geometric checks admit only the pairings that are plausible, semantically and physically. Therefore, the dataset grows combinatorially with the clips rather than recording time. The COSMI dataset holds 222k sequences and 275 hours with up to five objects, nearly thirty times the largest multi-object capture, and can be extended by adding datasets or even hand-object recordings. On this data we train the COSMI method, a text-to-interaction diffusion transformer that follows how the data is built: weight-shared object slots generate a variable number of objects, predicted relative to the body parts that move them. On a benchmark with an unseen object and unseen interaction combinations, models trained on the dataset generalize to the unseen combinations. COSMI outperforms baselines in text alignment and contact accuracy, where its margin is largest on the unseen object. Code, models, and the dataset pipeline will be released on the project page: https://ptrvilya.github.io/cosmi.
