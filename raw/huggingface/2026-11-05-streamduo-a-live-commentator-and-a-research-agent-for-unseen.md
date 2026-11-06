---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.299961+00:00
arxiv_id: 2611.01120
url: https://huggingface.co/papers/2611.01120
arxiv_url: https://arxiv.org/abs/2611.01120
date: 2026-11-05
---

# StreamDuo: A Live Commentator and a Research Agent for Unseen Games

Streaming video LLMs can now commentate live gameplay, but they are trained and tested on the same games. We study cross-game streaming commentary, in which a model trained on one game commentates games it has never seen, and find that current commentators transfer their timing but not their knowledge of the game world. We propose StreamDuo, which pairs a trainable commentator with a frozen research agent that reads the wiki of the game being played. When the commentator sees something it cannot name, it sends the current frames, and the research agent returns a few wiki entries two seconds later while the stream continues. We train only the commentator, on a single game, in two stages. Information-gain labels teach it to ask only where an answer would help it say what the human caster said, and on-policy self-distillation from a copy of itself that sees the ideal answer teaches it to use noisy answers. Trained on Baldur's Gate 3 and tested on ten unseen games, StreamDuo raises entity recall from 0.082 to 0.116 over Proact-VL trained on the same data, cuts source-game leakage from 9.9% to 1.0%, and achieves the best timing and the highest judged liveliness and overall quality among streaming models.
