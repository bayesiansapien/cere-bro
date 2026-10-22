---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.644780
arxiv_id: 2610.24899
url: https://huggingface.co/papers/2610.24899
arxiv_url: https://arxiv.org/abs/2610.24899
date: 2026-10-21
---

# HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research Agents

While LLM agents are increasingly capable of gathering and synthesizing evidence from a single homogeneous source, such as structured tables or unstructured data, real-world analytical questions frequently span heterogeneous sources. For example, answering one enterprise question may require both a result computed over an internal database and evidence found on the web. Recent evaluations on benchmarks like HybridDeepResearch show that even frontier agents struggle when evidence must cross this boundary. While these benchmarks have exposed the limitation, methodologies to explicitly teach cross-source reasoning remain absent. To address this, we introduce HybridResearcher, a 4B agent trained to bridge evidence across the structured and unstructured boundary. To build it, we synthesize cross-source bridge trajectories by starting with validated single-source tasks-such as existing text-to-SQL or web search queries-and fabricating the missing source around a bridge entity drawn from the seed's own output. We retain a sample only when strict construction gates confirm that neither side alone suffices, ensuring the data requires true cross-source interdependence. Finally, we train on this curated dataset using supervised fine-tuning followed by reinforcement learning. Evaluated on the existing HybridDeepResearch benchmark, HybridResearcher improves over our base model, Qwen3.5-4B, by 30.0 points pass@8 and surpasses the far larger Qwen3.5-397B-A17B by 8.3 points, while also improving over its base model on established, held-out single-source benchmarks (BrowseComp and BrowseComp-Plus), demonstrating that this complex cross-source reasoning can be taught directly to small models without triggering catastrophic forgetting.
