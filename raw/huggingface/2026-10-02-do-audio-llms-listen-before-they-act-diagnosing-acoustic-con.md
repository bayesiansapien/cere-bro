---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820767+00:00
arxiv_id: 2609.32536
url: https://huggingface.co/papers/2609.32536
arxiv_url: https://arxiv.org/abs/2609.32536
date: 2026-10-02
---

# Do Audio LLMs Listen Before They Act? Diagnosing Acoustic-Context Gating in Voice Agents

Audio language models can recognize spoken commands and invoke tools, but an agent must first decide whether the acoustic and conversational context warrants action. We introduce VGBench, a 1,018-item diagnostic benchmark for action-level addressedness across side-talk, self-talk, and speaker-switch scenarios. Each item uses a shared action space comprising silence, a tool call, and a natural-language answer. Speaker-switch pairs hold the specified words fixed while source, distance rendering, and a temporal boundary define a controlled wearer-to-bystander shift. Six raw Audio LLMs and three training-free adaptations often identify the target tool yet rarely withhold action under this shift; the highest raw switch mute rate is 14%. We then use VoxGate as a post-training case study. Supervised training mutes 91.3% of switched commands while choosing the correct tool for all nearby wearer commands and text-only controls. An exploratory GRPO stage has similar switch performance; side-talk accuracy rises from 68.4% to 70.9%, and self-talk muting from 52.0% to 60.0%. Factorized controls identify an independent source-change effect, while sensitivity to the far-field manipulation varies across acoustic renderings. The benchmark therefore measures multi-cue acoustic-context gating rather than isolated speaker identity.
