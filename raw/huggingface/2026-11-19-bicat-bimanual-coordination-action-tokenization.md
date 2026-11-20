---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.148450+00:00
arxiv_id: 2611.23499
url: https://huggingface.co/papers/2611.23499
arxiv_url: https://arxiv.org/abs/2611.23499
date: 2026-11-19
---

# BiCAT: Bimanual Coordination Action Tokenization

Autoregressive vision-language-action (VLA) models predict discrete action tokens with the next-token objective of their vision-language backbone, so the action tokenizer defines the interface between the policy and the robot. In bimanual manipulation, the two arms share a repertoire of movements yet coordinate through complementary roles, and an action representation should capture both. However, most existing tokenizers encode both arms as a single concatenated action vector, in which motion patterns common to the two arms are not shared and cross-arm dependencies remain entangled within each token. The policy must therefore learn both aspects implicitly. We propose Bimanual Coordination Action Tokenization (BiCAT), which shares one motion representation across arms while conditioning each arm's tokens on its partner through symmetric cross-arm attention and a joint decoder. The policy then predicts all tokens of each arm in parallel, generating the left arm first and the right arm conditioned on it. Across ten RoboTwin 2.0 tasks and six real-world tasks on three embodiments, BiCAT achieves the highest success among the compared tokenizers. In simulation, it improves mean success by 17.6 percentage points over the strongest of eight baselines, with the largest gains on tasks that require close coordination between the arms, while requiring only 40.5 ms per action chunk. These results suggest that the action tokenizer is a natural place to model bimanual coordination.
