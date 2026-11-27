---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.905941+00:00
arxiv_id: 2611.33143
url: https://huggingface.co/papers/2611.33143
arxiv_url: https://arxiv.org/abs/2611.33143
date: 2026-11-26
---

# ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification

Embodied spatial intelligence requires agents to gather information through exploration and interaction, then use it to reason and act. Existing benchmarks insufficiently distinguish correct outcomes from completion of these task requirements. We introduce ROAM-Bench to evaluate these abilities under robot motion and collision constraints. Independent checks use simulation state and episode records to assess outcomes and task requirements, with stronger checks of geometry, coverage, or placement. It comprises 250 manually validated tasks across 11 types in five groups and 27 indoor environments, covering object and room search, counting, geometric judgments, direction reasoning, and relocation. Human evaluators achieve 84% strict task success on 100 sampled tasks, with every correct outcome satisfying the required checks. Across seven frontier vision-language models, we identify two complementary failure modes: correct outcomes with unmet task requirements, and incorrect outcomes despite passing stronger checks. Oracle-input diagnostics show that more complete target observations and calibrated feedback improve final spatial judgments.
