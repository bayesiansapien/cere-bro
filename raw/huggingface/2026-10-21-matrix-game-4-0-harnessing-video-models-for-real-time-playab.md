---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.638592
arxiv_id: 2610.27999
url: https://huggingface.co/papers/2610.27999
arxiv_url: https://arxiv.org/abs/2610.27999
date: 2026-10-21
---

# Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds

Moving from controllable videos to genuinely playable worlds requires persistent world state, executable game rules, and low-latency interaction. We outline a roadmap for the next generation of Matrix-Game that separates game execution from visual generation through an executable game harness, and introduce Matrix-Game 4.0 as the first system built on this design. A lightweight game engine maintains world state and executes interaction rules, a multimodal coding agent translates player ideas into game code and dynamic scene captions, and a renderer based on autoregressive video model transforms engine-rendered low-poly proxies into detailed visuals, conditioned on dynamic captions and memory references. This framework provides continuous guidance for visual generation and enables natural-language creation and modification of scenes and gameplay. Our renderer is trained on aligned low-poly and high-fidelity video pairs and distilled into a causal generator that generates in four-frame chunks with one or two denoising steps. Together with targeted inference optimizations, Matrix-Game 4.0 enables 480p, 60 FPS gameplay on a single NVIDIA RTX5090 with a key-press-to-display latency of 112ms. Single-step generation achieves 83FPS steady-state throughput with 18.2GiB of peak GPU memory usage. With fixed prompts, steady-state throughput also reaches 67FPS on an RTX5080 and 58FPS on an RTX5070Ti. We demonstrate customizable shooter and driving games with engine-enforced mechanics, and release code, model weights, and low-poly game assets to support research and creation of playable game worlds.
