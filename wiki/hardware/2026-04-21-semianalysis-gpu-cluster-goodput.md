# SemiAnalysis: GPU Cluster Economics and the Goodput Reckoning

**Date:** 2026-04-21  
**Source:** SemiAnalysis Newsletter  
**Coverage:** [How Much Do GPU Clusters Really Cost](https://newsletter.semianalysis.com/p/how-much-do-gpu-clusters-really-cost)  
**Raw:** (parallel daily digest 2026-04-21)

---

## TL;DR

SemiAnalysis published a comprehensive GPU cluster TCO framework based on testing 80+ neoclouds and interviewing 150+ customers. The central finding: two cloud offerings with identical GPU-hour pricing can differ by 6–21% in useful work delivered, because downtime, debugging, fault recovery, and storage performance never appear on the monthly bill. "Goodput" — useful GPU work per dollar — is the metric that resolves this. Gold-tier neoclouds (Nebius, Fluidstack, Crusoe) cost 5–15% less than silver-tier for large pretraining jobs at the same nominal price; the gap collapses near zero for single-node inference.

---

## The Goodput Framework

**Eight-component TCO decomposition:**

```
GPU cluster total cost of ownership:
  ┌────────────────────────────────────────────────────┐
  │  On-bill (visible):                                │
  │    GPU cost                                        │
  │    Storage cost                                    │
  │    Networking cost                                 │
  │    Control plane cost                              │
  │    Support cost                                    │
  │                                                    │
  │  Off-bill (hidden):                                │
  │    Goodput Expense  ← wasted compute from failures │
  │    Setup Expense    ← time to configure cluster    │
  │    Debugging Expense← time diagnosing issues       │
  └────────────────────────────────────────────────────┘
```

The three off-bill components are the core insight. They are invisible to the buyer until they accumulate into a real cost: a single GPU failure in a 5,184-GPU cluster training job can waste 10–15 minutes of full-cluster time for re-initialization plus all compute since the last checkpoint.

**Grand Unifying Theory of Goodput — three recovery scenarios:**

| Scenario | Spare node | Recovery time | Downtime cost |
|----------|-----------|---------------|---------------|
| Checkpoint-cold | Needs repair | Hours to days | Very high |
| Checkpoint-hot | Available immediately | Minutes | Medium |
| Fault-tolerant | Job continues | Seconds | Low |

**Fault-tolerance framework comparison:**

| Framework | Status | Performance overhead | Constraints |
|-----------|--------|---------------------|-------------|
| TorchFT | Open source | 10%+ (GLOO comms) | None — fully open |
| AWS SageMaker HyperPod Checkpointless | Proprietary | 5% memory overhead, 1min 45s recovery | Kubernetes + NeMo only |
| TorchPass (Clockwork.io) | Licensed | 0% | Requires idle spare nodes at 0.62% of cluster |

---

## Key Numbers

**Goodput expense as % of total for large pretraining (5,184 GB300 NVL72 cluster):**
- Gold tier + TorchPass: 6.14%
- Silver tier + checkpoint restart: 20.91%

**Cost difference holding GPU-hour price constant:**
- Large training workloads: gold tier 5–15% cheaper than silver tier
- Single-node inference workloads: gap collapses to near zero
- Hyperscaler premium at equal GPU pricing: ~10% (driven by support costs and EFA tuning overhead)
- 2,048 B200 multimodal RL research scenario: 61% hyperscaler premium at real-world pricing

---

## ClusterMAX 2.1 Ratings (New)

New ratings added to SemiAnalysis's ClusterMAX provider scorecard:
- **Core42** (UAE/US, MI300X, Broadcom Thor-II NICs) — gold tier
- **BitDeer** (Malaysia, GB200 NVL72) — gold tier
- **FPT Smart Cloud** (Vietnam) — strong monitoring, but PKey/SAKey misconfiguration (security issue)
- **Radiant/Ori** (London/Dallas) — similar security issues, no automated health checks

---

## Relation to Prior Wiki Pages

**Fills a gap in the hardware concept page.** The GPU kernels page covers optimization at the software level (kernel fusion, memory access patterns). This paper covers optimization at the economic level — the same GPU-hours have different productive value depending on the cluster's fault tolerance and reliability infrastructure.

**Connects to AccelOpt (04-20):** AccelOpt optimized GPU kernel throughput at the software level (+12pp throughput). The SemiAnalysis framework is the business-level complement: a 6–21% goodput gap from reliability alone can dwarf the gains from kernel optimization at the economics level.

**Extends the "selective compute convergence" pattern (04-16 through 04-21):** TIP, LongAct, STOP, AVR, and W-RAC all discard wasted computation at different stack levels (token, gradient, path, format, pipeline). SemiAnalysis adds the cluster-operations level: not all GPU-hours are equal, and the ones lost to fault recovery are structurally different from GPU-hours on useful work.

---

## Why It Matters (Tier 1 Assessment)

The goodput framework quantifies what the industry has known intuitively but failed to price: reliability is a cost multiplier. The most practically important finding is the asymmetry: for large pretraining jobs (where cluster synchrony matters), a single failure compounds across the whole cluster. For inference workloads (independent requests), failures are local. This is why the same provider can offer excellent value for inference at a price point that makes them unsuitable for training.

The fault-tolerance tooling gap is the most actionable finding. TorchFT is the only open-source option and carries meaningful overhead. There is no open, zero-overhead fault-tolerant training framework. This is a concrete infrastructure gap.

---

## Research Angle (Tier 1)

**Open problem 1: Goodput-aware model routing.** If fault-tolerance overhead varies by 3–15x across cluster tiers, and inference routing already considers latency and cost, there should be a unified routing framework that factors in expected goodput loss per provider and workload type. This is a direct Tier 1 intersection: GPU goodput economics + routing.

**Open problem 2: Open-source zero-overhead fault tolerance.** TorchFT's 10%+ overhead comes from GLOO all-reduce communications during checkpoint state replication. Can this be reduced to <2% by using NCCL or hardware-level checkpointing? The theoretical floor should be much lower than current implementations.

**Open problem 3: Goodput-aware training curricula.** If some training steps are more critical than others (e.g., the final loss spikes that require checkpoint rollback are often concentrated in certain phases), could a training scheduler de-risk those phases by increasing checkpoint frequency? This would change the goodput calculation from a static average to a dynamic risk-adjusted metric.

---

## Related Pages

- [GPU Kernels](gpu-kernels.md)
- [AccelOpt: LLM Agent for GPU Kernel Optimization](../inference-efficiency/2026-04-20-accelopt-gpu-kernel-optimization.md)
- [Nemotron 3 Super: Hybrid Mamba-Attention MoE at NVFP4](../inference-efficiency/2026-04-21-nemotron3-super-hybrid-moe.md)
