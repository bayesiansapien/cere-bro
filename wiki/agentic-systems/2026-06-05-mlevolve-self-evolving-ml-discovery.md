# MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery

**TL;DR.** MLEvolve is an LLM-based self-evolving multi-agent framework for end-to-end machine-learning algorithm discovery. It fixes three failure modes of prior MLE agents: inter-branch information isolation, memoryless search, and lack of hierarchical control. It extends tree search to **Progressive MCGS** (Monte-Carlo graph search with cross-branch reference edges and an entropy-inspired explore→exploit schedule), adds **Retrospective Memory** (a cold-start knowledge base plus a dynamic global memory for experience reuse), and decouples strategic planning from code generation. On MLE-Bench it reaches state-of-the-art medal and valid-submission rates under a 12-hour budget (half the standard runtime), and beats AlphaEvolve on math algorithm optimization.

**Source:** HuggingFace Daily Papers (upvotes: 2)
**arxiv:** [2606.06473](https://arxiv.org/abs/2606.06473) · **Code:** https://github.com/InternScience/MLEvolve
**Raw:** [raw/huggingface/2026-06-05-mlevolve-a-self-evolving-framework-for-automated-machine-lea.md](../../raw/huggingface/2026-06-05-mlevolve-a-self-evolving-framework-for-automated-machine-lea.md)

## Key points

- **Progressive MCGS:** graph search (not just a tree) lets information flow across branches via reference edges; an entropy-inspired schedule shifts from broad exploration to focused exploitation as the search matures.
- **Retrospective Memory:** cold-start domain knowledge + dynamic global memory for task-specific retrieval and reuse, the concrete instantiation of "accumulate experience across the search."
- **Decoupled control:** strategic planning is separated from code generation with adaptive coding modes, for stable long-horizon iteration.
- **Results:** SOTA on MLE-Bench at half the standard runtime; beats AlphaEvolve on math algorithm optimization, evidence of cross-domain generalization.

## Relation to prior wiki

Part of today's six-paper self-evolving-agents cluster (see [Continual Experience Internalization](2026-06-05-continual-experience-internalization.md) for the cluster map). MLEvolve's Retrospective Memory is exactly the "accumulated experience must be reusable" claim that the keystone paper warns will *collapse* under naive iteration unless the experience is principle-level and stably internalized. Reading the two together: MLEvolve ships the memory mechanism; the keystone tells you the granularity/regime that keeps it from degrading. Beating AlphaEvolve (DeepMind's evolutionary code-discovery system, tracked in [ai-industry](../ai-industry/2026-05-26-alphaproof-nexus-deepmind-erdos.md)) on math optimization is the headline external comparison.

## Related pages
- [2026-06-05-continual-experience-internalization.md](2026-06-05-continual-experience-internalization.md)
- [multi-agent-systems.md](multi-agent-systems.md)
