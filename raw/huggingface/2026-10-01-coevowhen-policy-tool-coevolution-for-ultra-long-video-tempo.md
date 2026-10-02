---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.351442+05:30
arxiv_id: 2609.40048
url: https://huggingface.co/papers/2609.40048
arxiv_url: https://arxiv.org/abs/2609.40048
date: 2026-10-01
---

# CoEvoWhen: Policy-Tool Coevolution for Ultra-Long Video Temporal Grounding

Ultra-long video temporal grounding requires balancing long-range evidence search with fine-grained event understanding under a limited visual budget, yet existing agentic methods still rely largely on predefined policies and tool capabilities. Motivated by this, we propose a novel policy-tool coevolution framework that jointly evolves high-level policies and executable media tools from the agentic reasoning trajectories of a VLM, forming a reusable skill without updating model parameters. During evolution, an external skill updater distills transferable task experience in long-video temporal grounding, accordingly refining the orchestration of long-range image-based and fine-grained video-based observations. Alongside these policy updates, the updater employs its coding capabilities to upgrade existing tools or create new ones, adapting the tools to long-video evidence acquisition. Equipped with the evolved skill, the VLM autonomously orchestrates tools under the guidance of the evolved policy, coordinating image and video observations for agentic inference without relying on a separate, stronger planning model. Extensive experiments spanning five benchmarks and three VLMs show that policy-tool coevolution consistently improves temporal grounding accuracy in ultra-long videos while reducing visual token cost at inference, and that the evolved skill yields substantial performance gains on general long-video QA without additional task-specific evolution, demonstrating the effectiveness and generalizability of our framework for long-video understanding.
