---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.08129
url: https://huggingface.co/papers/2605.08129
arxiv_url: https://arxiv.org/abs/2605.08129
date: 2026-05-26
---

# Towards Customized Multimodal Role-Play

Unified multimodal understanding and generation models enable richer human-AI interaction. Yet jointly customizing a character's persona, dialogue style, and visual identity while maintaining output consistency across modalities remains largely unexplored. To mitigate this gap, we introduce a new task, Customized Multimodal Role-Play (CMRP). We construct the RoleScape-20 dataset comprising 20 characters, including training and evaluation data that cover persona, stylistic descriptions, visual/expressive cues, and text-image interactions. Building on a unified model, we devise UniCharacter, a two-stage training framework containing Unified Supervised Finetuning (Unified-SFT) and character-specific group relative policy optimization (Character-GRPO). Given only 10 images plus corresponding interaction examples, the model acquires the target character and exhibits coherent persona, style, and visual identity in both generated text and images. This process takes about 100 GPU hours. Experiments on the RoleScape-20 dataset show that the proposed method substantially outperforms prior approaches. Ablation studies further validate the effectiveness of our cross-modal consistency design and few-shot customization strategy. We argue that CMRP, coupled with unified modeling, provides a basis for next-generation characterful and immersive interactive agents.
