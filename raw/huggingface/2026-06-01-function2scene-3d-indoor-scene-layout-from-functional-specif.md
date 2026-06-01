---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.30819
url: https://huggingface.co/papers/2605.30819
arxiv_url: https://arxiv.org/abs/2605.30819
date: 2026-06-01
---

# Function2Scene: 3D Indoor Scene Layout from Functional Specifications

Most text-driven 3D indoor scene synthesis methods generate rooms from object-centric prompts, asking what furniture should be placed rather than how the space is used. Yet in real interior design, a layout is judged by how well it supports its occupants, e.g., their activities and physical needs. We introduce Function2Scene, a framework for generating 3D indoor layouts from functional specifications, i.e., natural-language design briefs describing who will use a room and what they need to do there. Given such a specification, our system parses occupant personas and activities, derives a customized set of functional design constraints from a taxonomy of 17 criteria spanning spatial, ergonomic, activity, and environmental considerations, and uses these constraints to guide layout generation. Rather than relying on an LLM to directly produce a final scene, Function2Scene performs iterative evaluation and refinement through a tool-augmented check-and-repair loop, combining geometric measurements, LLM-based contextual reasoning, and VLM-based visual assessment. Experiments on 30 professionally written interior-design cases show that Function2Scene produces layouts that better satisfy functional requirements than recent LLM-based scene synthesis baselines, with our results preferred in 94.3% of pairwise comparisons.
