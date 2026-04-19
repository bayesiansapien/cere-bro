# UniDoc-RL: RL-Based Visual RAG with Hierarchical Actions

**Date:** 2026-04-19  
**Source:** HuggingFace Daily Papers  
**Paper:** [arxiv 2604.14967](https://arxiv.org/abs/2604.14967)  
**Raw:** [raw/huggingface/2026-04-19-unidoc-rl-coarse-to-fine-visual-rag-hierarchical-actions-dense.md](../../raw/huggingface/2026-04-19-unidoc-rl-coarse-to-fine-visual-rag-hierarchical-actions-dense.md)

---

## TL;DR

UniDoc-RL trains a vision-language model (LVLM) as an RL agent that performs visual retrieval, reranking, and active perception in a single hierarchical loop. Instead of retrieving fixed chunks, the agent progressively refines its evidence from coarse document retrieval → fine-grained image selection → active region cropping. Dense multi-reward training via GRPO, no separate value network. Up to 17.7% gains over prior RL-based visual RAG methods.

---

## Key Findings

- **Unified agent**: one LVLM jointly performs retrieval, reranking, image selection, and region cropping — no separate modules for each step
- **Hierarchical action space**: three tiers of action — coarse (document), medium (image), fine (region crop) — modeled as a sequential decision problem
- **Dense rewards**: instead of a sparse end-task reward, each action level gets its own reward signal, solving credit assignment for long retrieval trajectories
- **GRPO training**: builds on Group Relative Policy Optimization without needing a value network (same training family as LongAct, AIMO 3)
- **Results**: +17.7% on three multimodal QA benchmarks vs. prior RL-based visual RAG baselines

---

## Mechanism

Standard visual RAG: retrieve fixed-size chunks → feed to LLM → generate answer. The agent never controls *what* it sees within a retrieved document.

UniDoc-RL's agent sees a query and decides:
1. Which documents to retrieve (coarse)
2. Which images within those documents are relevant (medium)
3. Which regions of those images to crop and zoom into (fine)

Each of these is a discrete action. GRPO updates the policy using group-relative rewards at each level. The result is an agent that actively looks where the evidence is, rather than passively consuming whatever the retriever returned.

---

## Comparison to Related Work

| System | Retrieval | Action space | Training |
|--------|-----------|-------------|---------|
| Standard RAG | Dense retrieval | None — passive consumer | SFT |
| Corpus2Skill | LLM navigation | Document tree traversal | SFT |
| UniDoc-RL | RL agent | Hierarchical (doc → image → region) | RL (GRPO) |

UniDoc-RL is complementary to Corpus2Skill. Corpus2Skill compiles the corpus offline and navigates statically. UniDoc-RL trains the agent to actively adapt retrieval at query time.

---

## Related Pages

- [Corpus2Skill: Knowledge Navigation](2026-04-18-corpus2skill-knowledge-navigation.md)
- [DR3-Eval: Deep Research Benchmark](2026-04-18-dr3-eval-deep-research-benchmark.md)
- [RL for LLMs](../llms-foundation-models/rl-for-llms.md)
