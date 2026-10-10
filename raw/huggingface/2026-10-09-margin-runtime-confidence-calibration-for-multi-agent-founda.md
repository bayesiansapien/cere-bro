---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.420502+00:00
arxiv_id: 2605.22949
url: https://huggingface.co/papers/2605.22949
arxiv_url: https://arxiv.org/abs/2605.22949
date: 2026-10-09
---

# MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination

When a coordinator compares answers from heterogeneous foundation models, self-reported confidence may have different meanings across responders and changing workloads. This paper presents MARGIN (Multi-Agent Runtime Grading via Incremental Normalisation), a runtime calibration method that learns model-specific confidence corrections from observed answer outcomes without retraining the models or requiring a held-out calibration set. MARGIN tracks recent accuracy and stated confidence within confidence bands, uses their ratio to correct reported confidence, and blends sparse-band corrections toward a model-level estimate. The corrected scores weight candidate answers in a collective decision. Evaluation covers code generation, question answering, and mathematics, using an 18-model pool and a nine-model subset for distribution-shift experiments. On BigCodeBench, model-mean confidence is negatively related to accuracy; among correct/incorrect response pairs, choosing the more confident responder performs below chance. Against five online calibration baselines receiving identical feedback and retaining their learned state across each transition, MARGIN achieves lower post-shift expected calibration error than all five in two code-generation transitions and than four in a question-answering transition; the remaining question-answering comparison is inconclusive. In separate code-generation coordination experiments, calibration improves the ranking of correct responses and increases answer-selection accuracy by 4.3 and 14.0 percentage points on two of three benchmarks relative to uncalibrated confidence weighting. These results support model-specific runtime calibration for coordination under changing workloads when correctness feedback is available for the participating responders.
