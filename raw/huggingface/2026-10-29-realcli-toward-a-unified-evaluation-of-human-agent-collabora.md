---
source: farmer/huggingface
farmed: 2026-10-30T18:38:23.924326+05:30
arxiv_id: 2610.22507
url: https://huggingface.co/papers/2610.22507
arxiv_url: https://arxiv.org/abs/2610.22507
date: 2026-10-29
---

# RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents

Command-line interface (CLI) agents increasingly execute longer-horizon tasks, yet existing benchmarks either assume that user instructions remain fixed throughout execution or evaluate task outcomes without capturing runtime collaboration quality. In this paper, we present REALCLI, a paired benchmark that unifies the evaluation of task execution and human-agent collaboration quality on realistic CLI tasks. To comprehensively measure collaboration, REALCLI builds a five-dimensional framework, operationalized into 22 sub-dimensions and 51 interaction scenario templates. REALCLI provides two modes for paired comparison: REALCLI-EXEC supplies complete specifications upfront, whereas REALCLI-COLLAB introduces a scripted user that delivers progressive information, corrections, constraint revisions, and authorization decisions. Evaluations reveal profound capability gaps in frontier agents: the best configuration attains an average score of only 49.2%, and when evaluated by the joint collaboration score (J_{collab}), the peak performance reaches merely 37.6%. These results show that task effectiveness diverges sharply from collaboration quality, with models consistently struggling in steerability, trust calibration, and safety boundary management. REALCLI provides a rigorous, reproducible foundation for measuring and advancing collaborative CLI agents.
