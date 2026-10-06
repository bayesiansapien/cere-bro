---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2609.30467
url: https://huggingface.co/papers/2609.30467
arxiv_url: https://arxiv.org/abs/2609.30467
date: 2026-10-05
---

# Where Does Retrieval-Based Open-Ended Evaluation Fail? Automatic Taxonomy Induction from Long-Form Medical Answer Factuality Verification

Retrieval-based factuality evaluation, where LLM-generated claims are verified against evidence from authoritative medical corpora, has become the dominant paradigm for scalable hallucination detection in high-stakes clinical settings. Despite the urgency of reliable and transparent medical fact verification, most systems measure performance with aggregate metrics like F1, which obscure where and why failures occur. Existing RAG diagnostics require gold answers or annotated gold evidence, neither of which exists in this regime. We introduce two comprehensive taxonomies, grounded in a case study on the open-ended MedExpert dataset and 3 closed-ended datasets, decomposing failures into retrieval-stage errors along five quality dimensions, and verifier-reasoning errors into six consecutive steps. We adapt an automatic pattern induction pipeline using LLM-as-Judge to label evidence quality and classify verifier reasoning errors at scale, and then stress-test our findings across 4 retrieval methods and 6 frontier verifier models. Our analysis reveals that scaling model size, adding reasoning effort, expanding to authoritative web sources, and applying medical fine-tuning do not resolve these failure modes, demonstrating that they represent fundamental limitations of the retrieve-then-verify paradigm in open-ended medical settings rather than artifacts of outdated systems. We release our code and data at https://anonymous.4open.science/r/Medical_RAG_eval-4AB5 for the full reproducibility of our results.
