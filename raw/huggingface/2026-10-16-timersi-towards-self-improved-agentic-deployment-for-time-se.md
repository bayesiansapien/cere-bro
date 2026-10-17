---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.19725
url: https://huggingface.co/papers/2610.19725
arxiv_url: https://arxiv.org/abs/2610.19725
date: 2026-10-16
---

# TimeRSI: Towards Self-Improved Agentic Deployment for Time-Series Foundation Models

Time-series foundation models provide strong zero-shot forecast, but deployment for real-world applications still requires task-specific designs for model inputs and outputs. Direct inference can leave domain knowledge and recurring forecast errors unaddressed, while tailored pipelines require substantial human expertise and effort. We introduce TimeRSI, a self-improving agentic deployment system around frozen forecasting models. A coding agent translates task descriptions into executable pipeline changes. It tests each revision on historical forecasting windows and uses observed errors to guide subsequent revisions. During deployment, an adaptive selector chooses among the resulting pipelines using completed forecasts under similar conditions. Across 198 tasks on TIME and fev-bench, TimeRSI outperforms all submissions on six point and probabilistic forecasting metrics. Controlled comparisons support the value of feedback-guided revision over non-iterative pipeline search. Further experiments verify the generalization with different coding agents and forecasting models. Code is available at https://github.com/haoxin1998/TimeRSI.
