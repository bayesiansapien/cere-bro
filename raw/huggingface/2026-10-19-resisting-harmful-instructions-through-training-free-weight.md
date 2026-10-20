---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.21189
url: https://huggingface.co/papers/2610.21189
arxiv_url: https://arxiv.org/abs/2610.21189
date: 2026-10-19
---

# Resisting Harmful Instructions through Training-Free Weight Editing

Instruction-following language models can comply with requests that conflict with intended behaviors and safety alignment. We introduce a training-free weight-editing approach for reducing compliance with targeted undesirable instructions. Our method needs only forward passes on a small set of prompt pairs per target behavior, and because the edit is stored in the model's weights, changing or deleting instructions in the prompt cannot undo the weight modification. We evaluate the approach on two target harmful behaviors across five instruction-tuned models: instructed falsehood and instructed sexism. On two instructed-lying benchmarks, it improves mean honest response rates by 6.2 and 4.6 percentage points over the strongest alternative, significantly on three of the five models and within noise on the other two. In a controlled study of seven prompt formats, it maintains higher honest-response rates than single-layer activation steering when orders to lie arrive in single-turn formats not used to construct the edit. For instructed sexism, it reduces the mean sexist-response rate from 57.9% to 24.3%; combining the edit with a fairness prompt reduces it further to 11.9%. These results establish our contrast-based weight editing approach as an effective training-free intervention in two distinct behavioral domains, supporting its use both independently and alongside prompt-based safeguards.
