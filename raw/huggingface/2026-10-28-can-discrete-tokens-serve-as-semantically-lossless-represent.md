---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.993858+05:30
arxiv_id: 2610.37662
url: https://huggingface.co/papers/2610.37662
arxiv_url: https://arxiv.org/abs/2610.37662
date: 2026-10-28
---

# Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?

Discrete visual tokens represent vision in a discrete form analogous to language, offering a native interface for multimodal modeling under a shared next-token prediction objective. However, quantization error is widely assumed to cause unavoidable semantic loss, fundamentally limiting the semantic fidelity of discrete visual tokens and positioning continuous visual representations as an intrinsic upper bound. Using multimodal understanding as a proxy for semantic fidelity, we revisit this assumption and find quantization error unreliable, as discrete representations with substantially larger errors can achieve better understanding. Instead, the effective bit budget of discrete indices emerges as a key determinant of downstream performance. However, existing quantizers eventually saturate as additional codebooks contribute progressively less semantic information. As one approach to alleviating this saturation, we introduce Factorized Vector Quantization, which quantizes complementary, fixed-dimensional views of the visual feature with symmetric parallel codebooks. It continues to improve at larger bit budgets, ultimately matching continuous visual representations in multimodal understanding. Trained on industrial-scale multimodal data, our model achieves state-of-the-art performance among discrete-representation models, outperforming UniAR and Emu3-Chat by 22.8% and 59.2%, respectively, on a nine-metric average. To our knowledge, it is also the first discrete-representation model competitive with strong continuous-representation models such as Qwen3-VL, including on fine-grained OCR tasks. We further identify the key principles and a practical recipe enabling this competitiveness. These results and insights support the potential of discrete visual representations to underpin large-scale native multimodal foundation models. Code and models are available at https://github.com/hustvl/FVQ
