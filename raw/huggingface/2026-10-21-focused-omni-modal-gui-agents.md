---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.638041
arxiv_id: 2610.26203
url: https://huggingface.co/papers/2610.26203
arxiv_url: https://arxiv.org/abs/2610.26203
date: 2026-10-21
---

# Focused Omni-Modal GUI Agents

Graphical User Interface (GUI) agents increasingly act over streaming omni-modal observations spanning screenshots, audio, video, interaction history, and device states. However, exposing this complete context uniformly at every step ignores that relevance is transient and sparse: the signal determining one action can become clutter at the next. Because executed actions feed back into the context, these errors compound into Sequential Distraction, driving the agent into irreversible trajectory drift. We formulate the underlying requirement as Focused Perception: a representation that is step-adaptive, action-sufficient, and non-intrusive. We realize this in FocusGUI, a lightweight adapter that dynamically prioritizes multimodal channels against a step-specific decision reference. Instead of uniformly processing all inputs, it compresses the most relevant evidence into a compact latent and subtly injects it into the frozen decoder's embeddings, guiding the model's attention without altering its native parameter space. FocusGUI trains from action supervision alone, requiring neither modality-relevance labels nor backbone fine-tuning. Across four omni-modal backbones, it raises overall Type Match by +33.2 and Exact Match by 3.0 times over the frozen backbone on average, and Type Match by +30.1 over the strongest existing enhancement method.
