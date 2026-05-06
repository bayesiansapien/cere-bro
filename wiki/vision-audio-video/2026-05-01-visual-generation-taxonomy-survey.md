# Visual Generation in the New Era: Atomic to Agentic World Modeling

**arXiv:** 2604.28185 · [paper](https://arxiv.org/abs/2604.28185) · [HF](https://huggingface.co/papers/2604.28185)
**Tier:** 3 — visual generation survey / taxonomy
**Raw:** [../../raw/huggingface/2026-05-01-visual-generation-new-era-evolution-atomic-mapping-agentic-world.md](../../raw/huggingface/2026-05-01-visual-generation-new-era-evolution-atomic-mapping-agentic-world.md)

## TL;DR

A taxonomy paper that argues visual generation has progressed from appearance synthesis to *intelligent generation* — visuals grounded in structure, dynamics, domain knowledge, and causal relations. Five-level taxonomy: **Atomic Generation → Conditional Generation → In-Context Generation → Agentic Generation → World-Modeling Generation**. Each level nests prior capabilities and adds a qualitatively new one. Drivers: diffusion-to-flow-matching, unified understanding+generation, improved visual representations, SFT and preference-based post-training, reward modeling, large-scale data curation, sampling acceleration. Pairs the taxonomy with stress tests and case studies that map failure modes to taxonomy levels.

## Why this is useful

The taxonomy is genuinely informative as a navigational structure for the visual-generation space. Most current models are stuck at Conditional or In-Context Generation; "Agentic" and "World-Modeling" are aspirational. Useful for placing today's papers (PhyCo physics priors → Conditional+; X-WAM 4D world action → World-Modeling beginnings).

## Connection to prior wiki

- **PhyCo (05-01)** lands at *Conditional Generation* with physical-property maps as conditioning.
- **X-WAM (04-30)** is closer to *World-Modeling Generation* with 4D dynamics and action coupling.
- **Seedance 2 (04-16) / GLM-5V-Turbo (04-30)** sit at *In-Context Generation* with multimodal inputs.
- **Agentic Generation** is largely empty in today's literature — the level the field has not credibly reached.

## Research angle

Taxonomy papers are useful for *placing* work, less useful for *driving* it. The interesting consequence: the gap between current models (Conditional / In-Context) and Agentic / World-Modeling is the explicit research target the survey identifies. Whoever builds the first credible Agentic Generation system (visual generator with persistent state and closed-loop feedback) sets the next level.
