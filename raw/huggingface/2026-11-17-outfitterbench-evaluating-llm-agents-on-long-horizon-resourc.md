---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.113850+00:00
arxiv_id: 2611.17933
url: https://huggingface.co/papers/2611.17933
arxiv_url: https://arxiv.org/abs/2611.17933
date: 2026-11-17
---

# OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination

In many long-horizon settings, an agent's own choices create future constraints: committing finite capacity establishes future obligations and forecloses later opportunities. Sustaining performance therefore requires both keeping evolving plans feasible and comparing the value of resource allocations with the alternatives they displace. Recent benchmarks increasingly evaluate LLM agents in continuing operations, but give less attention to how agents keep their own commitments feasible while reassessing resource allocations as opportunities change. We introduce OutfitterBench, where agents manage an outdoor-equipment rental business for 200 days, purchasing from a 46-product catalog and handling roughly 1,100 reservation requests. Under a fixed capital ceiling, reservations and uncertain walk-in demand compete for reusable equipment whose availability changes over time. Experiments with seven frontier LLMs show that several agents underperform a simple rule-based baseline, while only the leading agent consistently surpasses it. Trajectory analysis shows that some agents apply known constraints inconsistently and make new decisions that conflict with existing commitments. Agents with more reliable fulfillment can still secure low returns from comparable commitments or delay resource reallocation. The leading agent better connects preparation with economic choices but also misses opportunities for more profitable asset use. These findings highlight limitations in sustaining coherent resource plans and reassessing their value over time. The benchmark code is publicly available at https://github.com/adminblackjack/OutfitterBench.
