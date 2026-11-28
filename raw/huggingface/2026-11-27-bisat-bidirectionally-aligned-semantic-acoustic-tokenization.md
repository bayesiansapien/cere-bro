---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.30723
url: https://huggingface.co/papers/2611.30723
arxiv_url: https://arxiv.org/abs/2611.30723
date: 2026-11-27
---

# BiSAT: Bidirectionally Aligned Semantic-Acoustic Tokenization for Speech Language Models

Speech language models (LMs) generate speech as sequences of discrete tokens. Their tokenizer must therefore preserve both acoustic detail and linguistic content at a low bitrate. Semantic-enhanced tokenizers may lose acoustic detail, whereas acoustic-oriented tokenizers retain acoustic variation that makes language modeling harder. Unified tokenizers combine both, but representing acoustic detail and linguistic content within a single feature space can cause interference between the two objectives, and existing approaches typically align acoustic representations to fixed semantic targets from a frozen teacher. We propose Bidirectionally Aligned Semantic-Acoustic Tokenization (BiSAT), a unified tokenization framework with separate acoustic and semantic branches aligned by a shared-index mechanism. This design learns acoustic and semantic representations in separate continuous spaces while producing a single discrete code sequence, and it jointly optimizes both encoders without relying on fixed semantic teacher targets. Based on BiSAT, we develop BiSAT-TTS, a zero-shot text-to-speech system comprising an autoregressive text-speech LM and a conditional flow-matching acoustic decoder. Reconstruction, downstream understanding, and diagnostic analyses show that BiSAT effectively preserves semantic and acoustic information in the code stream, performs well on in-the-wild and out-of-domain speech, and learns complementary codebook representations. The frozen-code understanding results also support its feasibility and potential for code-based reward modeling in reinforcement learning post-training. BiSAT-TTS performs comparably to state-of-the-art speech LM-based TTS baselines with less training data, further supporting BiSAT's effectiveness for speech language modeling. The audio demos are available at https://seekmind-lab.github.io/bisat-demo.
