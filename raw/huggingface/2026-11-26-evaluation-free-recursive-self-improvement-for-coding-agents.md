---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.907317+00:00
arxiv_id: 2611.21056
url: https://huggingface.co/papers/2611.21056
arxiv_url: https://arxiv.org/abs/2611.21056
date: 2026-11-26
---

# Evaluation-Free Recursive Self-Improvement for Coding Agents

Recent self-improving coding agents have achieved strong benchmark performance by iteratively modifying their own executable implementations. A common pattern uses downstream task-derived evidence to decide which candidates or lineages continue evolving, which we term evaluate-and-select. Obtaining this signal requires repeatedly executing evolved agents on downstream tasks, so broader exploration incurs increasing evaluation cost, while repeated optimization against a fixed evaluation distribution may encourage benchmark-specific adaptation. We ask: can coding agents self-improve without downstream task evaluation inside the evolution loop? We introduce Explore-then-Integrate (ELITE), which integrates implementation mechanisms rather than selecting a single exploratory child to continue the lineage. At each generation, ELITE proposes diverse focused improvements, implements them independently from the same parent, and inspects the resulting programs to identify complementary, redundant, and conflicting mechanisms before reimplementing a compatible subset as one coherent descendant. No downstream task outcomes or task-solving trajectories of evolved candidates are used to guide evolution; only deterministic checks of structural and operational validity are used inside the loop. On SWE-bench Pro, ELITE improves the initial agent from 60.0% to 85.6%, compared with 86.7% for the Darwin Godel Machine (DGM) and 88.3% for the Huxley-Godel Machine (HGM), while using zero candidate task evaluations and reducing observed wall-clock evolution time by 8.8x and 3.2x, respectively, under the evaluated configurations. In cross-benchmark transfer without further adaptation, ELITE averages 73.3% on SWE-bench Verified and 69.3% on Polyglot. Together, these results demonstrate the feasibility of coding-agent self-improvement without downstream candidate task evaluation in our setting.
