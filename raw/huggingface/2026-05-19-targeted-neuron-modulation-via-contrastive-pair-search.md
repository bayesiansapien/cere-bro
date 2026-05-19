---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.12290
url: https://huggingface.co/papers/2605.12290
arxiv_url: https://arxiv.org/abs/2605.12290
date: 2026-05-19
---

# Targeted Neuron Modulation via Contrastive Pair Search

Language models are instruction-tuned to refuse harmful requests, but the mechanisms underlying this behavior remain poorly understood. Popular steering methods operate on the residual stream and degrade output coherence at high intervention strengths, limiting their practical use. We introduce contrastive neuron attribution (CNA), which identifies the 0.1% of MLP neurons whose activations most distinguish harmful from benign prompts, requiring only forward passes with no gradients or auxiliary training. In instruct models, ablating the discovered circuit reduces refusal rates by over 50% on a standard jailbreak benchmark while preserving fluency and non-degeneracy across all steering strengths. Applying CNA to matched base and instruct models across Llama and Qwen architectures (from 1B to 72B parameters), we find that base models contain similar late-layer discrimination structures but steering these neurons produces only content shifts, not behavioral change. These results demonstrate that neuron-level intervention enables reliable behavioral steering without the quality tradeoffs of residual-stream methods. More broadly, our findings suggest that alignment fine-tuning transforms pre-existing discrimination structure into a sparse, targetable refusal gate.
