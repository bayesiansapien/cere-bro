---
source: farmer/huggingface
farmed: 2026-10-14T17:45:17.067247+05:30
arxiv_id: 2609.35291
url: https://huggingface.co/papers/2609.35291
arxiv_url: https://arxiv.org/abs/2609.35291
date: 2026-10-13
---

# Narrow Multimodal Fine-Tuning Can Induce Emergent Misalignment

Modern AI models are aligned through post-training to adapt them to downstream tasks. Recent work shows that fine-tuning language models on narrow tasks can induce emergent misalignment (EM), causing broadly harmful behaviors beyond the training task. However, EM has been studied almost entirely in text-only tasks, leaving its manifestation in multimodal models unclear. In this paper, we define and analyze EM in the context of vision-language models. We first induce EM via fine-tuning on narrow multimodal tasks targeting vulnerable code, careless household-object use, and conspiratorial interpretations of ordinary scenes. Across fifteen commercial and open-source models with different scales, we find that narrow multimodal fine-tuning can induce coherent and broadly misaligned behavior that transfers to unrelated tasks, including misaligned opinions, visual factual dishonesty, unsafe image generation, vulnerability to visual jailbreaks, and risky agentic actions. We further find that multimodal EM does not depend on the apparent harmfulness of training data but is sensitive to training-evaluation modality alignment. EM can arise under both supervised fine-tuning and preference optimization and can propagate through intermediate reasoning. Finally, we explore several mitigation strategies, including prompt inoculation, benign continued training, and activation-level steering, which can partially reduce EM. Overall, our findings suggest that multimodal EM reflects a behavioral shift rather than a general loss of capability, extending beyond text to the visual modality.
