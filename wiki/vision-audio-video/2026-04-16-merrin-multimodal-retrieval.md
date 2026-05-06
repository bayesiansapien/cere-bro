---
date: 2026-04-16
source: huggingface
arxiv: 2604.13418
---

# MERRIN: Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments

**TL;DR:** MERRIN benchmarks search-augmented agents on multi-hop queries requiring retrieval of multimodal evidence (text, video, audio) from noisy web sources. Average agent accuracy is 22.3%; best agent reaches only 40.1%. Strong agents over-explore and are distracted by conflicting content.

## Key Findings

- Three key differentiators from prior work: (1) natural language queries with no explicit modality cues, (2) underexplored modalities (video, audio), (3) noisy/conflicting multimodal evidence.
- Average accuracy across all agents: **22.3%**. Best agent: **40.1%** (Gemini Deep Research).
- Strong agents (Gemini Deep Research) take more steps and use more tools but gain modest improvements — over-exploration problem.
- Agents over-rely on text modalities even when video/audio is the most relevant source.
- Efficiency gap: humans consume fewer resources but achieve higher accuracy.

## Related Pages

- [GameWorld](2026-04-16-gameworld-multimodal-game-agents.md)
- [../agentic-systems/agent-benchmarks.md](../agentic-systems/agent-benchmarks.md)

**Raw source:** [../../raw/huggingface/2026-04-16-merrin-a-benchmark-for-multimodal-evidence-retrieval-and-rea.md](../../raw/huggingface/2026-04-16-merrin-a-benchmark-for-multimodal-evidence-retrieval-and-rea.md)
