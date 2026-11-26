---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.25509
url: https://huggingface.co/papers/2611.25509
arxiv_url: https://arxiv.org/abs/2611.25509
date: 2026-11-25
---

# LingSante MedGuard Technical Report

As medical AI is increasingly used for patient consultation and clinical decision support, identifying harmful, non-compliant, or ethically problematic responses is essential for responsible deployment. Assessing these risks requires checking clinical claims against relevant evidence, verifying calculations, and applying medical requirements under their intended conditions. We introduce LingSante MedGuard, a capability-enhanced guardrail that integrates supervision from a medical guardrail teacher model and six specialized medical capability experts into a unified model. The guardrail teacher supervises risk decisions and explanations across medical safety, compliance, and ethics, while the capability experts support medical rule understanding, numerical reasoning, multimodal hallucination detection, agentic safety verification, risk localization, and multimodal entity understanding. We consolidate these sources of supervision through offline supervised fine-tuning on teacher-generated demonstrations, followed by multi-teacher on-policy distillation using feedback on student-generated responses. We further introduce LingSante MedGuardBench, a benchmark comprising 11 risk-detection subsets spanning medical safety, compliance, and ethics. At 4B, 9B, and 27B scales, LingSante MedGuard achieves mean benchmark F1 scores of 82.3%, 82.4%, and 87.4%, respectively. The 4B model also achieves 73.9% mean accuracy across MedHallu and MedHALT-NOTA under retrieval-enabled evaluation. Additional evaluations of the verification components show improvements in evidence-supported consistency, source traceability, and rule-guided rationale quality across model scales. These results support the integration of specialized medical capabilities into a unified guardrail for medical risk assessment and evidence-based medical safety verification.
