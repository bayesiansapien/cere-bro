# SMART: Your Embedding Model is Smarter Than You Think

**Source:** [arXiv:2605.24938](https://arxiv.org/abs/2605.24938), via HuggingFace Daily Papers 2026-05-26.
**Topic:** Multimodal retrieval / embedding models / late interaction.

## TL;DR

Single-vector retrievers compress a rich sequence of token representations into one global pooled embedding. That is efficient but discards fine-grained local evidence. Multi-vector approaches (ColBERT-style late interaction) recover the local detail but require explicit training and often ignore the value of a global summary. SMART finds the third option: standard contrastive training on the pooled embedding implicitly shapes the retrieval geometry of the preceding hidden states via gradient flow. So at inference time, late interaction can be applied directly over the frozen hidden states of an already-trained single-vector model, with no extra training. SMART is a plug-and-play inference enhancement that consistently improves retrieval across modalities, including pushing the state of the art further on MMEB-V2. With light post-training, a single-vector base outperforms SoTA multi-vector counterparts on Visual Document Retrieval.

## Why this matters

Single-vector embedding models dominate retrieval deployment because they index cheaply (one vector per document). The implicit story has been "if you want late interaction's quality, pay the multi-vector cost." SMART shows that gradient flow during single-vector contrastive training already shapes the per-token geometry the multi-vector approach was paying extra to construct. The information was there in the standard single-vector model; nobody had used it.

## Key results

- Plug-and-play inference enhancement on standard single-vector retrievers across modalities.
- Pushes SoTA further on MMEB-V2.
- With lightweight post-training, single-vector + SMART outperforms SoTA multi-vector models on Visual Document Retrieval.
- Open source: code and weights at github.com/HanSolo9682/SMART.

## How this relates to prior wiki pages

This is the retrieval-side instance of the broader 2026-05 pattern: a quantity that was implicitly available inside a trained model can be extracted at inference time without retraining. RTPurbo from 2026-05-24 found that full-attention LLMs have a 16-dimensional retrieval subspace already after pretraining. SMART finds that single-vector embedding models have a multi-vector geometry already shaped by contrastive training. Two retrieval papers, two weeks apart, both with the same shape: pretraining produced more structure than the deployment recipe was using.

## Industrial implication

For any production retrieval system using a single-vector model (the default in 2024-2026 production), SMART is essentially free quality improvement at inference. The visual-document-retrieval result is also significant for enterprise document QA, where multi-vector retrieval has been the better-quality but more-expensive option; SMART collapses that tradeoff.
