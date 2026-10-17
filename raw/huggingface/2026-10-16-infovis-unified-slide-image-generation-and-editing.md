---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.16784
url: https://huggingface.co/papers/2610.16784
arxiv_url: https://arxiv.org/abs/2610.16784
date: 2026-10-16
---

# InfoVis: Unified Slide Image Generation and Editing

Generating and editing presentation slides requires models to combine accurate text rendering, instruction following, visual grounding, aesthetic design, and precise editing within one canvas. Existing work covers only subsets of these capabilities and lacks large-scale slide-native supervision and diagnostic evaluation. We formulate four slide-centric tasks and build a scalable data engine with over 13M continual-pretraining records and 1.9M supervised fine-tuning records. We also introduce VisSlideBench, a benchmark of 1,527 manually screened instances that covers all four tasks with task-specific, multidimensional evaluation. Its automatic rankings agree with blinded, dimension-wise human rankings. Using these resources, we train InfoVis, a unified 9B slide generation and editing model. On VisSlideBench, InfoVis leads every evaluated open-source model on all eleven metrics and scores 7.94 overall against 7.99 for Nano-Banana-2. Starting from FLUX.2-klein-base-9B, slide-specific post-training adds 1.6 points overall, with the largest generation gains in content faithfulness; the remaining gap to proprietary models is smallest in content faithfulness and largest in aesthetic quality. Built on InfoVis, our document-to-slide workflow achieves the second-highest Aesthetics score on the external SlidesGen-Bench. We will release the model, code, data, and benchmark.
