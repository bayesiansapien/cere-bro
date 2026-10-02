---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.350154+05:30
arxiv_id: 2609.39788
url: https://huggingface.co/papers/2609.39788
arxiv_url: https://arxiv.org/abs/2609.39788
date: 2026-10-01
---

# Safety of Latent Communication in Multi-Agent Systems

Latent communication enables multi-agent systems to exchange information directly in internal representation space, reducing the token, computation, and latency overhead of text-based communication. To this end, lightweight trainable links are introduced to map the sender's representations into the receiver's input space. In this work, we show that even benign link training can increase harmful compliance relative to text-based communication while the underlying safety-aligned agents remain unchanged. An attacker can amplify this effect by optimizing the links on harmful query--response pairs or poisoning otherwise benign training data. We further develop a reinforcement-learning attack that rewards harmful compliance alongside benign task performance without requiring harmful target responses. Across three communication topologies and four safety benchmarks, this attack raises the mean harmful-compliance score from 27.9 with benignly trained links to 76.9. Compared with direct supervised optimization, it also achieves higher average accuracy on two benign utility benchmarks. Adapting the rewards toward safer behavior also enables repair of compromised links, substantially reducing harmful compliance across all evaluated attacks without updating the agents. Overall, our results show that safety alignment requires considering the multi-agent system as a whole.
