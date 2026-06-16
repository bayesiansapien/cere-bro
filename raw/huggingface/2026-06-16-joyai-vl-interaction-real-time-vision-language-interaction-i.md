---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.14777
url: https://huggingface.co/papers/2606.14777
arxiv_url: https://arxiv.org/abs/2606.14777
date: 2026-06-16
---

# JoyAI-VL-Interaction: Real-Time Vision-Language Interaction Intelligence

Many moments in the real world do not wait for a user to ask. A fire starts on a security monitor, an expression flickers across a video call, or a product a viewer wants flashes by in a livestream. Yet today's large models remain mostly turn-based by design: they answer only when addressed, and even video-call apps that appear interactive still operate as question-answer systems, reacting only when polled or prompted. We argue for a different paradigm: a model that is present in the world like a person. It continuously watches what is happening now, decides on its own whether to speak or stay silent, interacts in real time, and delegates to a background model when the problem is hard. To advance interaction models and their adoption across domains, we make two fully open-sourced contributions. First, we release JoyAI-VL-Interaction, an 8B-scale, vision-first VL-interaction model. The model makes the response decision internally, choosing each second to stay silent, respond, or delegate to a background model, and it excels at vision-triggered responsiveness and time awareness. We pair it with a transferable training recipe, from which capabilities we never trained for emerge, such as guiding a shopper through changing app screens or improvising a lecture from a slide deck. Second, we release a complete, deployable system built around that model. The system streams any ongoing video into the model, making it genuinely present in the world. All other components are pluggable, including ASR/TTS modules, memory, visualization UI, and a background brain that can connect to any API or agent. Across six real-world scenarios, human raters prefer JoyAI-VL-Interaction over the in-app video-call assistants of Doubao and Gemini by a wide margin. To our knowledge, this is the first open, vision-driven interaction model released together with its training recipe, data, and complete deployable system.
