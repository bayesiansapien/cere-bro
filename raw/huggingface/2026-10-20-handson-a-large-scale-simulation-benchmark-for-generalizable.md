---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.26765
url: https://huggingface.co/papers/2610.26765
arxiv_url: https://arxiv.org/abs/2610.26765
date: 2026-10-20
---

# HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation

General-purpose manipulation requires reliable behavior across embodiments, objects, and task demands. We introduce HandsOn, a composable simulation platform and benchmark for cross-embodiment dexterous manipulation. It supports five robotic arms, six dexterous hands, and approximately 200 rigid, articulated, and deformable assets in randomized scenes. The benchmark pairs 18,000 curated human demonstrations with 66 human-verified tasks: Core-50 supports demonstration-based learning and execution tests, while Transfer-16 evaluates asset and relation transfer, skill composition, and deformable manipulation without target-task training demonstrations. Qualitative real-robot rollouts illustrate sim-to-real transfer. Across diffusion, vision-language-action, world-action, and prompted VLM-based methods, the best trained multi-task policy achieves 29.1% Core-50 success. Without benchmark finetuning, GPT-6 using move_eef for palm-and-finger control achieves 5.2% on Core-50 and 1.9% on Transfer-16 over 660 trials. Trained-policy stage diagnostics expose failures in contact establishment, action coordination, and maintaining achieved goals, with additional sequencing errors in composed tasks. HandsOn provides a shared basis for investigating manipulation generalization and the limits of reliable physical interaction.
