---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.29310
url: https://huggingface.co/papers/2608.29310
arxiv_url: https://arxiv.org/abs/2608.29310
date: 2026-09-01
---

# Super Library Agent: Joint Generation and Maintenance of Multiple Applications Beyond the Single Codebase

Organizations often develop and maintain portfolios of related applications: independently deployable codebases that share substantial domain logic, interface patterns, or operational conventions. As LLM coding agents are increasingly used to generate and maintain such software, a naive application-by-application workflow duplicates shared logic across codebases and allows prolonged agentic maintenance to accumulate verbosity, dead code, and structural erosion. We introduce the Super Library Agent problem, where an agent sequentially generates a portfolio of N related applications while maintaining a shared Super Library of reusable cross-application components. A minimal sequential scaffold can in principle extract shared code and migrate applications to the evolving library, but in practice suffers from low extraction recall and fragile dependency migration. We address these failures with candidate-guided extraction over code chunk summaries, pre-extraction codebase consolidation, and context-aware migration using extraction traces and call-graph information. Across WebGen-Bench and PaperBench, our method preserves application functionality while significantly reducing redundancy and token footprint (verbosity, token length) over zero-shot, and avoiding the structural erosion introduced by naive library construction, with additional reductions in LOC and MDL. Our code is available at https://github.com/sbigstar0310/super-library-agent.
