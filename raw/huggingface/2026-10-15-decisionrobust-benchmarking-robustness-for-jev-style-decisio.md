---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.225798+05:30
arxiv_id: 2610.19118
url: https://huggingface.co/papers/2610.19118
arxiv_url: https://arxiv.org/abs/2610.19118
date: 2026-10-15
---

# DecisionRobust: Benchmarking Robustness for JEV Style Decision Models Across Text and Vision

Emerging decision models such as JEV provide typed interfaces that map task instructions and observations directly to choices, judgments, and scores. As these models are increasingly used for automated decision-making, understanding their reliability under adversarial manipulation becomes critical. We introduce DecisionRobust, a benchmark for systematically evaluating the robustness of decision models across textual and visual inputs. Our benchmark covers practical decision-making scenarios and a diverse suite of attacks, including semantics-preserving text perturbations, image perturbations, and prompt injection in both modalities. We curate evaluation sets through external validity checks and cross-model candidate selection. We evaluate 30 model configurations on text tasks and 17 on vision tasks, including 24 and 12 held-out models, respectively, that are excluded from candidate selection. Our experiments reveal several key findings. First, attacks expose vulnerabilities beyond the models used for construction and selection, although optimized image perturbations transfer weakly to many targets even with multiple surrogates. Second, relative model robustness varies across tasks and attack types, and resistance to input perturbations does not necessarily imply resistance to prompt injection. Third, label-consistency checks substantially reduce measured attack success across text and image settings, highlighting the importance of validating apparent failures. The benchmark is available at https://yifan-lan.github.io/DecisionRobust/.
