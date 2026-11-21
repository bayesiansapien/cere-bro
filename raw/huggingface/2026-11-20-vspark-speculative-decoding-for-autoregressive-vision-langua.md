---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.387804+00:00
arxiv_id: 2611.22666
url: https://huggingface.co/papers/2611.22666
arxiv_url: https://arxiv.org/abs/2611.22666
date: 2026-11-20
---

# VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models

Our aim is to accelerate autoregressive vision-language-action models (VLAs), which generate robot actions one token at a time. Speculative decoding makes this possible: a lightweight draft model proposes several tokens at once, and the VLA verifies them in a single pass, accepting only those that match its own predictions, so decoding remains lossless. The speedup, however, is limited in robot control, where many different tokens encode nearly the same motion and a draft close to the correct action is still rejected. To address this, our approach, VSpark, is built upon three design choices: (i) rollouts collected with calibrated action noise, which expose the draft to a wider range of robot states; (ii) feature alignment, which trains the draft to match the VLA's hidden features rather than its output tokens alone; and (iii) continuation reuse, which keeps the predictions the VLA has already computed along rejected drafts as candidates for the next verification step, instead of discarding them. On four VLAs with different action tokenizers and four manipulation benchmarks, VSpark achieves 1.28x to 2.10x speedup while keeping the VLA's decoding lossless.
