---
source: farmer/huggingface
farmed: 2026-08-04T09:04:58.435121+05:30
arxiv_id: 2608.01973
url: https://huggingface.co/papers/2608.01973
arxiv_url: https://arxiv.org/abs/2608.01973
date: 2026-08-04
---

# Roomer: Reflective Object-Grounded Model Editing and Repair for 3D Indoor Layout Synthesis

Existing indoor layout generators produce globally plausible layouts yet may retain local violations such as collisions, out-of-bounds placements, obstructed openings, and blocked circulation. Most prior work focuses on full-scene synthesis or scene-level optimization, with limited support for identifying responsible objects and locally repairing affected regions. We present Roomer, a reflective repair framework that casts these violations as sparse, object-grounded repair problems. Roomer encodes layouts as ``RoState'' and uses ``RoReview'' to bind measured violations to implicated objects. A geometry-conditioned vision-language model planner proposes a structured local edit, while a deterministic solver validates it and generates a finite set of candidate edits when needed. Each candidate is committed only if full-scene verification confirms that it resolves the target violation without new hard violations or broken protected constraints. We train the planner on Roomer-CC, a controlled-corruption dataset that pairs faulty layouts with object-grounded violation evidence and known-feasible inverse StatePatches. Since existing benchmarks rarely assess whether physically valid layouts are usable, we introduce Roomer-Eval to assess distributional quality, physical validity, and practical usability. Experiments show that Roomer repairs residual violations while preserving valid regions, improves physical validity and usability, and transfers across external generators.
