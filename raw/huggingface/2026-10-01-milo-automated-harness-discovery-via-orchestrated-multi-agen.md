---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.348999+05:30
arxiv_id: 2609.38349
url: https://huggingface.co/papers/2609.38349
arxiv_url: https://arxiv.org/abs/2609.38349
date: 2026-10-01
---

# MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution

Modern agentic systems combine an AI model with a harness that controls execution and environmental interactions. Harness design strongly affects long-horizon performance, yet its combinatorial search space demands substantial human effort that must be repeated as models change. Existing automated methods explore this space narrowly, optimizing only components such as prompts or skills or becoming trapped by fixed, exploitative search strategies. We introduce MILO (Meta-evolutionary Island Orchestration), a framework that co-evolves agent harnesses and the strategy used to discover them. MILO combines: (i) hierarchical lineage memory over island-based trees, using rejected mutations as negative evidence; (ii) per-island mutator agents that rewrite complete harnesses using global search history and parent-specific feedback; and (iii) an orchestrator that adapts search through lineage grafting and speciation, mutator reassignment and curriculum revision. Across Terminal-Bench 2.1, PaperBench, and DeepSWE, MILO-discovered harnesses outperform eight state-of-the-art harnesses and six search methods using frontier (Opus 4.8) and open-weight (gpt-oss-120b) models. With Opus 4.8, MILO improves resolution over its initial harness by +12.0%, +28.3%, and +10.3%, respectively, compared with best prior-search gains of +4.5%, +18.3%, and 0%. On Terminal-Bench 2.1, it achieves 86.1 pm 2.0%, exceeding the official leaderboard's top entry (83.8 pm 2.3%) while using 26\% fewer tokens than its initial harness. On EinsteinArena open problems, MILO improves best-known upper bounds for Erdős minimum-overlap (0.3808586 to 0.3808568) and the first and third autocorrelation inequalities (1.50274365 to 1.50274360; 1.45081 to 1.44889).
