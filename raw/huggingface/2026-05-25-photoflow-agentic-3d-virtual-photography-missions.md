---
source: farmer/huggingface
farmed: 2026-05-25T08:23:16Z
arxiv_id: 2605.23771
url: https://huggingface.co/papers/2605.23771
arxiv_url: https://arxiv.org/abs/2605.23771
date: 2026-05-25
---

# PhotoFlow: Agentic 3D Virtual Photography Missions

Virtual photography asks an agent to enter a prepared 3D scene with no preselected camera pose or reference image, infer a suitable shot from scene information and a language intent, choose executable camera parameters, and render the final photograph. Recent progress in vision-language models makes this kind of spatial agent increasingly plausible, but the task stresses two capabilities that remain hard to evaluate together: complex 3D spatial understanding and abstract aesthetic judgment. We introduce PhotoFlow, a Director-Reviewer-Reflector agent for closed-loop camera search. The Director builds a soft photographic blueprint and proposes diverse candidate cameras; the Reviewer combines rule checks, visual critique, and pairwise incumbent selection; and the Reflector converts failures into region memory, dead-zone suppression, and high-explore relocation. We also introduce VPhotoBench, a benchmark of 47 open-license Blender scenes and 141 language-conditioned photography missions spanning subject placement, relational composition, and atmosphere/style. On held-out experiments, PhotoFlow achieves the strongest external quality-alignment composite and success rate among one-shot prediction, single-chain reflection, anchor-bank selection, and random search under a six-round rendering budget. To our knowledge, this is the first work to make language-conditioned virtual photography in arbitrary Blender scenes an executable agent task, and our results show that an LLM-centered spatial agent can already produce strong photographs in a setting designed to challenge both 3D reasoning and aesthetic choice.
