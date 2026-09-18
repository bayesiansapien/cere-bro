---
source: farmer/huggingface
farmed: 2026-09-18T16:13:44.923131+00:00
arxiv_id: 2609.19745
url: https://huggingface.co/papers/2609.19745
arxiv_url: https://arxiv.org/abs/2609.19745
date: 2026-09-18
---

# Region-Level Policy Optimization for Fine-grained MLLM Perception

Fine-grained visual perception in MLLMs is commonly improved by raising the resolution, but the added visual tokens inflate vision-encoding and language-model prefilling costs. We show that the two operations underlying fine-grained perception, localizing the region of interest (RoI) and recognizing its content, have different resolution requirements. In a controlled diagnostic, localization tolerates roughly 3 to 4 times stronger token compression than recognition, which motivates localizing from a coarse view and concentrating resolution on the selected evidence. Decoding coordinates with the MLLM can be trained end-to-end from answers, but costs a full model pass per query and depends on grounding ability. A lightweight proposal network distilled from the model's attention is fast, but inherits the noise of its attention targets. The RoI from the proposal network reaches the answer through a discrete region choice, so its faithfulness to the answer cannot supervise the network. We therefore optimize the proposal network with region-level reinforcement learning, which we call Vision-RL2. It treats coherent regions as actions, and a frozen MLLM reader scores each one by how its removal changes the answer likelihood. Complementary subtractive and additive objectives suppress distracting proposals and recover missing evidence, updating only the predictor without region annotations, response sampling, or reasoning trajectories. The refined proposal further enables a sparse encoding that magnifies evidence and excludes background tokens. Across six fine-grained benchmarks and four MLLM backbones, Vision-RL2 improves accuracy over the base model at every token budget and surpasses its largest-budget accuracy with about 4 times fewer visual tokens. Code is available at https://github.com/YuHengsss/VisionRL2 .
