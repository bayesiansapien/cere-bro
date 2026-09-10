---
source: farmer/huggingface
farmed: 2026-09-10T08:36:11.637058+00:00
arxiv_id: 2609.10540
url: https://huggingface.co/papers/2609.10540
arxiv_url: https://arxiv.org/abs/2609.10540
upvotes: 36
date: 2026-09-10
---

# Programmable World Model

Recent video world models generate increasingly realistic and interactive visual experiences, yet lack reliable mechanisms for maintaining persistent world state and enforcing programmable rules over extended interactions. We introduce Programmable World Model, a framework that decouples world-state evolution from visual observation generation. An agent translates natural-language instructions into executable programs that specify entity states and state-transition rules, enabling direct control over individual entities and their interactions. A lightweight engine executes these programs to update and maintain an explicit, persistent global world state, including off-screen entities and non-visual attributes. To connect world state with visual generation, we introduce state-augmented 3D oriented bounding boxes (OBBs) as an intermediate representation. This representation, together with the target camera trajectory, is deterministically compiled into pixel-aligned spatiotemporal conditioning signals for a pretrained video model serving as the generative renderer. This design allows users to create playable games with predefined mechanics, direct control over individual entities, and persistent world state throughout gameplay. We further introduce CombatStateBench, a benchmark for evaluating programmable world models. On CombatStateBench, our method achieves 94% Count Accuracy and 98% State Accuracy, substantially outperforming existing interactive video world models while supporting coherent long-horizon generation. These results demonstrate the effectiveness of separating explicit state evolution from generative rendering for building persistent, programmable worlds.
