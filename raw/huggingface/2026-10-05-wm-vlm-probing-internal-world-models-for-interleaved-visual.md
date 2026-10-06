---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2609.34826
url: https://huggingface.co/papers/2609.34826
arxiv_url: https://arxiv.org/abs/2609.34826
date: 2026-10-05
---

# WM-VLM: Probing Internal World Models for Interleaved Visual-Textual Reasoning

Humans often solve spatial problems by mentally simulating visual transformations. In contrast, conventional vision-language models (VLMs) reason primarily through language. We investigate whether VLMs can solve spatial problems by reasoning with both text and generated visual states. To this end, we introduce WM-VLM, which equips a pretrained VLM with a lightweight world model branch for generating intermediate visual states. Our two-stage training first teaches the model to generate the next visual state and then to use that state for reasoning. We programmatically construct spatial reasoning tasks with verifiable intermediate visual states. These tasks allow us to evaluate how well the model generates visual states and how much it relies on them to answer the question. On 2D and 3D mental rotation tasks, WM-VLM consistently outperforms the supervised fine-tuned backbone, with gains of up to 39.25 percentage points. Ablations suggest that these gains depend on the generated visual states, as removing or corrupting them sharply reduces performance. Together, these results suggest that internal world models offer a promising path toward VLMs that reason in both language and visual space.
