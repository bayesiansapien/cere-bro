---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.157561+00:00
arxiv_id: 2610.33106
url: https://huggingface.co/papers/2610.33106
arxiv_url: https://arxiv.org/abs/2610.33106
date: 2026-10-30
---

# VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team

Large language model agents have enabled software development through natural-language interaction, but extending this paradigm to end-to-end game development remains challenging. Building a playable game requires coordinating code, scenes, assets, animations, physics, and configurations, while allowing developers to validate their integrated behavior through interactive testing. We introduce VibeGame, a framework for creating complete 2D game projects from natural-language prompts and optional reference images. Its AI-native game engine represents project state as schema-validated structured text and provides frame-synchronous runtime control, enabling agents to inspect game states, execute actions, and verify behavior at their own pace. Built upon this interface, we design an Adversarial Agent Team of eight specialized agents to separate implementation from review, so that problems are found and fixed through multi-round loops. For each conducted and accepted project, we further introduce a training-free self-evolution mechanism to distill it into reusable skeletons, modules, and collaboration contracts for future development. We evaluate prompt-assets-to-game (PA2G), where agents are given an asset library, and prompt-to-game (P2G), where agents generate their own art. On a GameCraft-Bench subset, VibeGame in P2G consistently outperforms a range of agent harnesses in either P2G or PA2G with the same underlying model, including GPT-6.1-Sol.
