---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.592060+00:00
arxiv_id: 2611.06976
url: https://huggingface.co/papers/2611.06976
arxiv_url: https://arxiv.org/abs/2611.06976
date: 2026-11-07
---

# On the Opportunities and Challenges of Prefill-to-Autoregressive Cross-Model Transfer

Prefill-to-Autoregressive Cross-model Transfer (PACT), a form of latent communication between language models, combines a larger model's prompt representations with a smaller model's efficient generation, offering a promising way to balance capability and inference cost. However, existing systems provide limited support for independently evaluating large-small model collaboration, and improved task performance alone does not establish whether the receiver benefits from the sender's information. We introduce PLatour, an open-source PACT framework that connects frozen models through lightweight, zero-initialized linear bridges trained directly with task rewards and supports hybrid-attention architectures. PLatour significantly outperforms open-source baselines on generation tasks and surpasses Mostik's reported results on shared mathematics and coding benchmarks using a substantially smaller sender. However, controlled experiments show that the gains on some tasks can be reproduced by uninformative sender signals, self-communication, or receiver-only training. We find that trainable bridges can act as parameter-efficient adaptation mechanisms without exploiting useful sender information. We therefore propose PACT-Check to quantify how much of a trained PACT system's gain genuinely comes from communication. Finally, we discuss the opportunities and challenges of PACT systems. Code is available at https://github.com/zhenyi4/platour.
