---
source: farmer/huggingface
farmed: 2026-07-28T03:19:32Z
arxiv_id: 2607.24743
url: https://huggingface.co/papers/2607.24743
arxiv_url: https://arxiv.org/abs/2607.24743
date: 2026-07-28
---

# ClinFusion: A Vision-Centric Multimodal LLM System for Holistic Medical Understanding

Multimodal large language models (MLLMs) hold immense potential to revolutionize clinical practice, yet deploying them in the medical domain is fundamentally a vision-centric challenge: models must absorb knowledge from heterogeneous 2D and 3D medical images, and evaluation protocols must align with radiologists' clinical practice and provide an accurate, fine-grained and factualness-driven assessment. In this paper, we introduce ClinFusion, a vision-centric MLLM designed for holistic medical understanding that systematically addresses these limitations. We propose a compositional and cascaded vision encoder architecture featuring a Cascade Spatial-Aware Locality Fusion operator that unifies diverse 2D and native 3D medical image understanding within a fused encoder. We further introduce a vision-grounded evaluation framework, including MedIF-Bench for instruction-following assessment and a region-of-interest-grounded method for clinically aligned and factualness-driven report generation evaluation. We show that ClinFusion sets a new state-of-the-art across a comprehensive suite of 2D and 3D multimodal medical benchmarks---spanning visual question answering, report generation, and instruction following---as well as textual medical tasks, outperforming leading open-source medical MLLMs (e.g., Hulu-Med, Lingshu) on 20 out of 24 benchmarks and demonstrating multimodal capabilities better than powerful proprietary models such as GPT-5.2 and Gemini-3-Flash on 13 out of 16 benchmarks, and can be further augmented with agentic tool use for retrieval-augmented and tool-assisted clinical workflows. A blinded evaluation by board-certified radiologists confirms that ClinFusion produces the highest-ranked reports, and validates our RoI-grounded metric as achieving the strongest correlation with expert judgment among all automatic evaluation metrics examined.
