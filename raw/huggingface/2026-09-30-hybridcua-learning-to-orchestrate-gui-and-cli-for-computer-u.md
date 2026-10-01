---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.38008
url: https://huggingface.co/papers/2609.38008
arxiv_url: https://arxiv.org/abs/2609.38008
date: 2026-09-30
---

# HybridCUA: Learning to Orchestrate GUI and CLI for Computer-Use Agents

Computer use agents (CUAs) have demonstrated strong capabilities in completing digital tasks. However, existing CUAs either rely solely on graphical user interface (GUI) interactions, which are often inefficient and error prone, or augment GUI interactions with application specific APIs or tools, which require substantial engineering effort and are difficult to scale across applications. We argue that the next generation of CUAs should combine GUI interactions with the command line interface (CLI), leveraging the generality of the GUI and the efficiency of shell commands. A critical challenge, however, is that current models do not know when or how to use the CLI during task execution. To address this challenge, we develop a data construction pipeline that produces three types of trajectories: GUI only, CLI only, and interleaved GUI and CLI trajectories. This pipeline results in HybridCUA-8K, containing 5K hybrid trajectories and 3K verified RLVR tasks. Building on these data, we propose a training framework with two stages: supervised fine tuning on the constructed trajectories, followed by reinforcement learning with our CLI aware rewards that encourages agents to use the CLI selectively and reliably. Experiments show that HybridCUA-9B achieves 53.6% accuracy on OSWorld, improving over the base model by 14.8 percentage points, and improves performance on WindowsAgentArena by 4.0 percentage points. These results demonstrate the effectiveness and cross platform generalizability of the hybrid GUI and CLI paradigm for computer use agents.
