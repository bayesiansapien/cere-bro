---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.35001
url: https://huggingface.co/papers/2610.35001
arxiv_url: https://arxiv.org/abs/2610.35001
date: 2026-10-27
---

# More Memory, Better Videos? A Controlled Study of Visual Memory in Long-Video Generation

Long-video generators increasingly retrieve past visual observations to prevent identity drift. The intuition is compelling: more access to history should make future video more consistent. But an image can be faithful to the past and wrong for the present. Does visual memory always improve the generated story? We investigate this question through VMem-Bench, a two-track diagnostic study. Track-A measures which references are selected from 92 real films (16,548 segments), before generation and without generator confounds. Track-B compares four retrieval policies with no-memory and gold-informed last-seen controls on 30 causally generated stories (2,824 segments) using a shared generator. Retrieval increases entity recall from 0.559 to 0.628-0.693 and improves similarity to past appearances, but decreases precision from 0.977 to 0.915-0.938 and forbidden-entity avoidance from 0.968 to 0.845-0.898. It can also reinforce obsolete appearances after the story changes them. Conversely, high long-gap recall can arise without memory when the prompt itself supplies the appearance; an appearance-stripping analysis exposes this confound. These results distinguish historical fidelity from current-story correctness and show why retrieval relevance or final-video consistency alone does not establish memory utility.
