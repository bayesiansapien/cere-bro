---
source: farmer/huggingface
farmed: 2026-04-21T00:00:00Z
arxiv_id: "2604.18543"
url: https://huggingface.co/papers/2604.18543
arxiv_url: https://arxiv.org/abs/2604.18543
date: 2026-04-21
---

# ClawEnvKit: Automatic Environment Generation for Claw-Like Agents

Constructing environments for training and evaluating claw-like agents remains a manual, human-intensive process that does not scale. We argue that what is needed is not just a dataset, but an automated pipeline capable of generating diverse, verified environments on demand. To this end, we introduce ClawEnvKit, an autonomous generation pipeline that instantiates this formalism from natural language descriptions. The pipeline comprises three modules: (1) a parser that extracts structured generation parameters from natural language input; (2) a generator that produces the task specification, tool interface, and scoring configuration; and (3) a validator that enforces feasibility, diversity, structural validity, and internal consistency across the generated environments. Using ClawEnvKit, we construct Auto-ClawEval, the first large-scale benchmark for claw-like agents, comprising 1,040 environments across 24 categories. Empirically, Auto-ClawEval matches or exceeds human-curated environments on coherence and clarity at 13,800x lower cost. Evaluated across 4 model families and 8 agent harness frameworks, we find that harness engineering boosts performance by up to 15.7 percentage points over a bare ReAct baseline, completion remains the primary axis of variation with no model saturating the benchmark, and automated generation enables evaluation at a scale previously infeasible.

**Authors:** University of Maryland; University of California, Berkeley; University of California, Los Angeles; Mohamed bin Zayed University of Artificial Intelligence
