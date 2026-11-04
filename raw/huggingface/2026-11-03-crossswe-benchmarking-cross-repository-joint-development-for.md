---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.01484
url: https://huggingface.co/papers/2611.01484
arxiv_url: https://arxiv.org/abs/2611.01484
date: 2026-11-03
---

# CrossSWE: Benchmarking Cross-Repository Joint Development for Coding Agents

As coding agents achieve increasingly high success rates on software engineering benchmarks, recent efforts have sought to increase task complexity through longer horizons and more extensive code modifications. However, real-world software development often spans multiple interdependent repositories, introducing additional challenges in dependency reasoning, change propagation, and interface consistency. Rather than further increasing complexity within individual repositories, we introduce CrossSWE, a benchmark for cross-repository joint development comprising 171 real-world instances spanning 165 repositories, 20 technical domains, and 13 programming languages. CrossSWE verifies the necessity of coordinated changes by testing whether partial repository modifications are insufficient to achieve the intended behavior. Our evaluation of five LLMs reveals substantial challenges, with the strongest model, GPT-6.1 Sol, achieving only 58.48% Pass@1. Furthermore, cross-repository inconsistencies emerge as the most prevalent failure mode (44.2%), highlighting the difficulty of maintaining consistency across interdependent repositories.
