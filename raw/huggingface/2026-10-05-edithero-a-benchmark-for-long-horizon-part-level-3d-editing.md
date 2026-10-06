---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2610.02298
url: https://huggingface.co/papers/2610.02298
arxiv_url: https://arxiv.org/abs/2610.02298
date: 2026-10-05
---

# EditHero: A Benchmark for Long-Horizon Part-Level 3D Editing and Vibe Modeling

3D editing methods are usually tested on a single edit, yet an asset is built through a long sequence of revisions, each of which must implement the requested change while leaving everything else unchanged. We introduce EditHero, to our knowledge the first benchmark for long-horizon, part-level 3D editing, with natural-language instructions and target images for both geometry and texture. A deterministic assembly engine produces the exact target after every edit, and every sequence is reviewed by hand. We use EditHero to compare 2 opposite approaches to 3D editing. Non-agentic methods operate top down, regenerating the object from a learned 3D representation and inferring what to keep. In contrast, LLM/VLM agents operate bottom up, editing through code that inspects the mesh and rewrites only the parts required by instructions. The non-agentic methods often miss the requested change and disturb regions that should stay fixed. Most LLMs follow instructions more closely, and all of them preserve the unedited parts better, but each of their edits takes minutes. We will release the engine and the edit sequences to support research on reliable iterative 3D editing.
