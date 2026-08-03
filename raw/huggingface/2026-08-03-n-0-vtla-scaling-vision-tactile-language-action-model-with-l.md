---
source: farmer/huggingface
farmed: 2026-08-03T12:36:11.005337+05:30
arxiv_id: 2607.23782
url: https://huggingface.co/papers/2607.23782
arxiv_url: https://arxiv.org/abs/2607.23782
date: 2026-08-03
---

# N_0-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens

We present N_0-VTLA, a vision-tactile-language-action (VTLA) foundation model capable of (1) fine-grained contact-rich manipulation with tactile perception and tactile-feedback control, and (2) offline policy improvement from stored deployment data. Building on current vision-based backbones, we propose a training recipe for tactile integration consisting of visuo-tactile pre-training, staged tactile-pathway integration, and advantage-conditioned offline policy improvement. During pre-training, the policy learns broad contact priors from NeoData, our large-scale visuo-tactile robot dataset; to our knowledge, N_0-VTLA is the first VTLA model pretrained on tactile data at scale. During post-training, we augment the policy with a predictive tactile pathway that distills the contact patterns learned at scale into the fine motion adjustments required by downstream tactile-centric manipulation. For offline policy improvement, we introduce ALTER, an advantage-conditioned offline reinforcement learning method that converts relative progress and trajectory-event comparisons into binary advantage labels for policy training on a fixed deployment corpus, further improving task-specific learning on contact-rich skills such as deformable object manipulation. Across contact-rich benchmarks, N_0-VTLA outperforms strong baselines by wide margins: it wins all nine real-robot NeoReal tasks and reaches 63.8% mean success on a twenty-task simulation suite, against 44.0% for the strongest baseline. N_0-VTLA policies trained with ALTER reach 75-95% success on three long-horizon real-robot tasks. These results lay a foundation for versatile tactile-driven manipulation policies.
