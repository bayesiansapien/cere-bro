---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.05030
url: https://huggingface.co/papers/2610.05030
arxiv_url: https://arxiv.org/abs/2610.05030
date: 2026-10-07
---

# EVISKILL: Grounding Skill Evolution in Replayable Evidence

Continual skill evolution enables LLM agents to accumulate and refine reusable procedural knowledge from interaction experience without updating model parameters. Its effectiveness depends on determining not only what to change, but also why a change is justified and when it should become persistent guidance. However, existing experience-driven methods can lose the behavioral evidence and task contexts supporting edits. Moreover, a global validation outcome provides an incomplete judgment of its constituent changes: locally supported corrections may be discarded with a rejected revision, while evidence may require further experience to inform useful updates. To this end, we introduce EVISKILL, an evidence-driven framework that organizes execution observations into Replayable Evidence Cards and synthesizes edits with explicit links to their supporting contexts. Targeted replay verifies these edits through re-execution and provides feedback for correction. Across epochs, EVISKILL preserves evidence and provisionally retains supported edits for further refinement, while global validation governs their incorporation into the final skill. Experiments on three interactive benchmarks across six LLM backbones demonstrate the effectiveness of this approach.
