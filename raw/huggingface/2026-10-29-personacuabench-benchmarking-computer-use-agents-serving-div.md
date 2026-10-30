---
source: farmer/huggingface
farmed: 2026-10-30T18:38:23.924771+05:30
arxiv_id: 2610.22990
url: https://huggingface.co/papers/2610.22990
arxiv_url: https://arxiv.org/abs/2610.22990
date: 2026-10-29
---

# PersonaCUABench: Benchmarking Computer-Use Agents Serving Diverse Personas

Computer-use agents (CUAs) are commonly evaluated against fixed task specifications, but users may omit requirements, add constraints, or require approval before consequential actions. Completing the benchmark instruction does not guarantee serving the person who asked. We introduce PersonaCUABench, which holds 74 tasks across 11 domains fixed and varies only who asks. A persona agent, playing one of 44 personas in four groups, rewrites each instruction in that user's own words and answers the CUA's questions, while the CUA sees only the dialogue, never the profile or the original instruction. Across nine backbones (3,330 runs), mean task completion falls by 36% relative to the original requests. The losses have two sources: in 59.9% of cells that lose points, the agent engages with what the user asked for and still gets it wrong, and 11.2% are stops the user requested that the checker scores as failures. Even when a persona request is fully completed, the user gives the top satisfaction rating in only 62.7% of cells, against 84.1% for the original requests. CUAs should therefore be evaluated not only on task completion but also on whether they meet the requirements and constraints users express. Code: https://github.com/MatrAIx-ai/PersonaCUABench. Project page: https://matraix.ai/research/persona-cua.html
