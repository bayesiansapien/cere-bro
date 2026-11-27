---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.904666+00:00
arxiv_id: 2611.34907
url: https://huggingface.co/papers/2611.34907
arxiv_url: https://arxiv.org/abs/2611.34907
date: 2026-11-26
---

# Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation

Real-time autoregressive video generators stream minutes of video and accept new prompts on the fly, but struggle to keep people, objects, and places consistent over a long interactive story. Agent systems provide such memory for offline multi-shot generation, yet they read the whole script in advance, plan each shot before generating it, and regenerate failed shots, which a live stream does not allow. We present Agentic LongLive, an asynchronous agentic memory for long video generation. A memory agent on separate GPUs reads only the prompts revealed so far, never the generated video, and keeps a text state and evolving images for every person, object, and scene. From this entity memory it composes a global image and a per-shot memory image, which an auxiliary GPU prefills into the generator's attention sink before the next shot starts, and writes entity cards for the prompts that name them, so the video never waits for memory and video errors are not written back. A small language model, trained with reinforcement learning and an image reward calibrated using downstream video outcomes, decides what to remember before the next prompt is known. On LongStory-Online, a new benchmark of 25 stories (857 shots) revealed one shot at a time, Agentic LongLive improves persistent-state accuracy of LongLive-2.0, its base generator, by 26.3 points, protagonist identity by 44.9, and revisited-place consistency by 40.4, at about 1% extra generation time on H100. The full system streams faster than real time on one 8xB200 node with the generator in BF16 (34.3 FPS), keeps image quality stable over 14-minute stories, and improves identity on two MiniMax-H3 generators, one of which, LongLive-H3, also runs in real time with it. To our knowledge, it is the first real-time video generator with text and image memory kept by an LLM agent.
