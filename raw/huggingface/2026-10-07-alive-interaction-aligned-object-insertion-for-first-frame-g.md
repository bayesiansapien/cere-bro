---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.08779
url: https://huggingface.co/papers/2610.08779
arxiv_url: https://arxiv.org/abs/2610.08779
date: 2026-10-07
---

# ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing

Current video editors can insert objects but often struggle to make them participate in interactions such as being picked up or manipulated. We introduce ALIVE, a framework that makes inserted objects "alive" through coherent interactions with the source video's contents, using an edited first frame and an instruction naming only the added object. We curate 35,800 editing pairs combining 3D-rendered, model-generated, and real-world videos with general editing pairs from ROSE. Each pair differs in the target object's presence while preserving the surrounding action, teaching editors coordinated object behavior and source preservation. We further train a vision-language model (VLM) to predict interaction guidance from the same inputs. We introduce the ALIVE-interaction benchmark to assess interaction fidelity, source preservation, and visual coherence using a unified VLM-based protocol, and evaluate on the general video object insertion benchmark. Without VLM guidance, ALIVE improves Overall over the strongest evaluated baseline by 43.9% and 4.4% on the two benchmarks, respectively. VLM-predicted guidance further improves the ALIVE-interaction score by 0.95 points without additional user inputs.
