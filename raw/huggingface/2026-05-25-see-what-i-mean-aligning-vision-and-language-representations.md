---
source: farmer/huggingface
farmed: 2026-05-25T08:23:16Z
arxiv_id: 2605.18018
url: https://huggingface.co/papers/2605.18018
arxiv_url: https://arxiv.org/abs/2605.18018
date: 2026-05-25
---

# See What I Mean: Aligning Vision and Language Representations for Video Fine-grained Object Understanding

We present SWIM (See What I Mean), a novel training strategy that aligns vision and language representations to enable fine-grained object understanding solely from textual prompts. Unlike existing approaches that require explicit visual prompts, such as masks or points, SWIM leverages mask supervision only during training to guide cross-modal attention, allowing the model to automatically attend to the user-specified object at inference. Our cross-attention analysis of pretrained multimodal large languagemodels (MLLMs) reveals a systematic discrepancy: Attribute words produce sharp, localized activations in the visual modality, whereas object nouns yield diffuse and scattered patterns due to semantic reference bias and distributed high-level representations. To address this misalignment, we construct NL-Refer, an enriched dataset, in which each object mask is paired with a precise natural language referring expression. SWIM extracts multi-layer cross-attention maps from object nouns and enforces spatial consistency with ground-truth masks. Experimental results demonstrate that SWIM substantially improves text-visual alignment and achieves superior performance over visual-prompt-based methods on fine-grained object understanding benchmarks. The code and data are available at https://github.com/HumanMLLM/SWIM{https://github.com/HumanMLLM/SWIM}.
