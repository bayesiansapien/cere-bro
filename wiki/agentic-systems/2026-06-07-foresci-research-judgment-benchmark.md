# ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment

**Source:** HuggingFace Daily Papers · [arXiv 2606.00644](https://arxiv.org/abs/2606.00644)
**Raw:** [raw/huggingface/2026-06-07-foresci-evaluating-llm-agents-for-forward-looking-ai-researc.md](../../raw/huggingface/2026-06-07-foresci-evaluating-llm-agents-for-forward-looking-ai-researc.md)

## TL;DR

AI research demands decisions before the evidence exists: which bottleneck to attack, which direction to pursue, where to position a project. ForeSci is a temporally controlled benchmark that tests whether LLM agents can make such forward-looking judgments from historical evidence alone. It has 500 tasks across four fast-moving AI domains and four decision families; each task is paired with a cutoff-aligned offline knowledge base, with post-cutoff papers hidden during generation and used only for validation. Tasks derive from pre-cutoff taxonomy branches (not random future-event prediction), and answer backbones are chosen to precede the cutoff. The key diagnostic finding: an **evidence-decision decoupling** — agents cite relevant evidence yet forecast the wrong research object.

## Key points

- **Temporal control is the design crux.** By hiding post-cutoff papers and aligning the knowledge base to a cutoff, ForeSci avoids the "lucky future guess" problem and isolates judgment from leakage. Explicit evidence organization (Hybrid RAG, research-agent adaptations) improves traceability and factual support, but gains depend strongly on the decision family.
- **Citing ≠ deciding.** The recurring failure is agents that retrieve and cite the right prior work but still pick the wrong forward direction — retrieval quality does not translate into decision quality.

## How this relates to prior wiki knowledge

- **The evidence-decision gap echoes the verifier-gaming worry.** "Cites relevant evidence while forecasting the wrong object" is the research-judgment analogue of the wiki's verifier-gaming thread (Kurate's "LLMs Gaming Verifiers"): a process metric (good citations) looks healthy while the outcome (correct decision) is wrong. It also rhymes with [AgentLens](2026-05-14-agentlens-lucky-pass-swe-eval.md)'s "lucky pass" — surface signals that mislead about real capability.
- **A research-agent eval, complementing the self-evolving-agent cluster.** The 06-05/06-06 self-evolving-agents cluster (MLEvolve, EvoDS, ForeSci-adjacent research agents) is mostly about *executing* research loops; ForeSci tests the *judgment* layer above execution — choosing what to work on. The two together frame the autonomous-researcher stack: judgment (ForeSci) on top of execution (MLEvolve/EvoDS).

## Research angle

The decision-family dependence is the actionable result: some kinds of forward-looking calls are tractable for current agents and some are not, and ForeSci can localize which. Open: whether better evidence organization or better base-model reasoning closes the evidence-decision gap, and whether the offline cutoff KB under-represents the informal signal (lab gossip, conference buzz) that human researchers actually use to make these calls.

→ Concept page: [agent-benchmarks](agent-benchmarks.md)
