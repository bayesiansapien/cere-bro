---
source: farmer/huggingface
farmed: 2026-09-04T10:50:04.492861
arxiv_id: 2609.02367
url: https://huggingface.co/papers/2609.02367
arxiv_url: https://arxiv.org/abs/2609.02367
date: 2026-09-04
---

# The Missing Temporal Link: Temporal Context Routing for Script-Driven Audio-Video Generation

Joint audio-video generation models have made substantial progress in visual quality and audio-visual synchronization. However, they still provide limited control over when shot transitions occur and dialogue is spoken. This limitation constrains their application in script-driven content creation, where timing errors can undermine narrative coherence and the viewing experience. Current joint generators align video and audio representations on a shared temporal axis, yet the precise timing of shots and dialogue specified in a structured prompt is encoded only in the prompt's text representation and remains unaligned with the temporal coordinates of either modality. Consequently, video and audio may remain synchronized with each other while both fail to follow the script timeline. This mismatch motivates us to extend temporal alignment beyond video and audio to include the structured script. We therefore introduce Temporal Context Routing (TCR), which maps the script timing onto the shared temporal axis of video and audio generation and routes each prompt's guidance to the corresponding positions in both modalities. Compared with the baseline on 200 test scripts, TCR reduces Shot Boundary MAE by 96%, from 1.11 s to 0.042 s, and raises Dialogue Acc@0.5 s from 28.3% to 84.1%. TCR achieves these improvements while maintaining visual quality and audio-visual synchronization comparable to those of the baselines. A user study further shows that participants prefer TCR on all five evaluated dimensions.
