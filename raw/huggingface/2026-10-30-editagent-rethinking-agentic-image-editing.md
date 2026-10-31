---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.160083+00:00
arxiv_id: 2610.39664
url: https://huggingface.co/papers/2610.39664
arxiv_url: https://arxiv.org/abs/2610.39664
date: 2026-10-30
---

# EditAgent: Rethinking Agentic Image Editing

Agentic image editors decompose complex requests into steps, but when a step fails, they mostly retry with the same narrow set of tools and a judge that scores each output by eye directly. We argue that such agents are bounded by two spaces: the action space of what the agent can do, and the observation space of what its judge can see. On our expert-annotated benchmark, a general-purpose editor yields no usable result in over 40% of the cases, and no judge is reliable across edit types. We present EditAgent, which expands both spaces. It routes each step to general editors and specialized methods, and attaches to each candidate a verification record. With these records, off-the-shelf VLM judges outperform finetuned reward models. Candidates are generated in parallel and judged in one listwise call: experts prefer this to sequential refinement in 78.5% of decided comparisons, at no more than half the judge calls. EditAgent improves two open-weight editors on three benchmarks and serves as a data engine for training stronger editors.
