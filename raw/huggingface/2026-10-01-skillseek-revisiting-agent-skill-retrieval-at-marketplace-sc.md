---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.351350+05:30
arxiv_id: 2609.38822
url: https://huggingface.co/papers/2609.38822
arxiv_url: https://arxiv.org/abs/2609.38822
date: 2026-10-01
---

# SkillSeek: Revisiting Agent Skill Retrieval at Marketplace Scale

Anthropic's Agent Skills package reusable procedural know-how for an LLM agent into SKILL.md directories, and open-source aggregations have grown past 230,000 skills, making selection rather than authoring the bottleneck. The standing answer in the literature outsources selection to the agent itself: an LLM-mediated retrieval loop that rewrites queries and refines candidates inside the agent's decision loop, paying LLM tokens on every task. We present SkillSeek, an open-source two-stage skill retriever built from the standard IR recipe (a BGE-base bi-encoder feeding a small cross-encoder, exposed over MCP). Across a 4 times 11 grid of pool, backbone, and method on the 89-task SkillsBench benchmark, SkillSeek reaches observed parity with the LLM-mediated loop of Liu et al. at essentially no extra cost: plain bm25 alone records a pass rate at or above their refined loop on three of four settings, and a small cross-encoder covers the remaining difference on the fourth. A first-stage recall ceiling explains the pattern, and total per-trial spend drops from USD 51.30 to USD 27.54 (within fifty cents of the no-skill baseline). Under the SkillsBench tasks and OpenHands harness we tested, this positions the standard IR recipe as a strong default for agent-skill retrieval, with LLM-mediated alternatives a natural fit for cases where deterministic methods fall short.
