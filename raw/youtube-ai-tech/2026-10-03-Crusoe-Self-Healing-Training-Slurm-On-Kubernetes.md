# GPU Died. Training Didn't: Self-Healing Training at Scale (Crusoe)

**Channel:** AI Engineer
**Published:** 2026-10-03
**Source:** https://www.youtube.com/watch?v=bRGyYaE0lxI

## TL;DR
Crusoe runs Slurm as a workload on its managed Kubernetes (CMK) via SchedMD's Slinky operator, then wires in AutoClusters, which detects fatal GPU errors (demo: XID 79, GPU fell off the bus), drains the Slurm node, cordons the Kubernetes node, swaps in a spare from reserve capacity in about 5 minutes, and lets the requeued job resume from checkpoint. End-to-end recovery in the demo was under 15 minutes with zero human action. The architecture is sensible and matches where the industry is going, but the demo is two A100 nodes. It shows plumbing, not behavior at thousands of GPUs, where checkpoint I/O and job restart cost dominate. "One-click Slurm" (cluster, controller, login nodes, storage in one command) is the launch.

## Key Takeaways
- **Why hybrid:** Slurm gives gang scheduling, topology awareness, prolog/epilog validation and researcher familiarity. Kubernetes gives self-healing, observability and elastic sharing. Running Slurm on K8s means one infra stack instead of two.
- **Remediation flow:** fatal XID detected, user notified, Slurm node set DOWN and jobs cancelled, process gets SIGTERM with up to 2 minutes to checkpoint or flush logs, job requeued, K8s node cordoned and drained (unless a pod label opts out), node replaced from spare pool, event logged, job restarts and loads checkpoint.
- **Timing:** about 5 minutes infra-side; the rest of the ~15 minutes is application restart (model load, checkpoint load).
- **Elasticity:** GPU nodes are Kubernetes nodes first, so idle training capacity can absorb inference bursts and vice versa.
- **No workflow change:** researchers still `sbatch` and SSH; platform teams keep K8s telemetry.

## Architecture & Optimization Mechanics
The useful idea is making node health a single source of truth: a Kubernetes cordon propagates directly to the Slurm operator, so the scheduler and infrastructure cannot disagree about a bad node. That closes the classic gap where Slurm keeps scheduling onto hardware the infra layer already knows is dead.

What the talk underplays is that this is still checkpoint-restart, the coarsest form of fault tolerance. At large scale the expensive parts are (a) lost work since the last checkpoint, (b) checkpoint write time, which a 2-minute SIGTERM window will not cover synchronously for a multi-hundred-billion-parameter model with optimizer state, and (c) restart overhead: NCCL re-init, data loader warmup, sharded checkpoint reads across the whole job. Goodput depends far more on async/in-memory checkpointing frequency and restart speed than on the 5-minute node swap. Spare-pool capacity is also a hidden cost; someone pays for idle hot spares.

## Grounded Context (Web Enrichment)
The failure premise is well documented. Meta's Llama 3 405B run hit 419 unexpected interruptions in 54 days on up to 16,384 H100s, roughly one every three hours, with GPU issues 58.7% of the total (faulty GPUs 30.1%, HBM3 17.2%). Meta still achieved over 90% effective training time with only three significant manual interventions, which means automated remediation at this level is table stakes for frontier labs, not a novelty. Meta's cluster reliability work also found XID 79 co-occurs with PCIe errors in 43 to 63% of cases, so a node-level swap is the right granularity for that error class.

Crusoe's own docs and blog match the talk: AutoClusters operates at the Kubernetes layer, replaces failed nodes from spare capacity in under 5 minutes, cordons immediately and gives workloads a configurable grace period. Managed Slurm is built on Slinky v1.0 (rc1 November 2025, GA shortly after). A 2026 Lablup report on 504-GPU pretraining reaches the same conclusion the talk skips: detection and node swap are the easy part; recovery time is dominated by checkpoint and restart behavior.

Sources: [Crusoe: Slurm on CMK](https://www.crusoe.ai/resources/blog/slurm-on-crusoe-managed-kubernetes-how-we-built-managed-gpu-training-infrastructure), [Crusoe: self-healing PyTorch with Slurm](https://www.crusoe.ai/resources/blog/self-healing-distributed-pytorch-training-with-slurm-on-crusoe-managed-kubernetes), [Crusoe AutoClusters docs](https://docs.crusoecloud.com/orchestration/cmk/autoclusters/index.html), [Crusoe Managed Slurm docs](https://docs.crusoecloud.com/orchestration/slurm/overview/index.html), [AutoClusters blog](https://www.crusoe.ai/resources/blog/autoclusters-minimizing-hardware-failures-in-large-gpu-clusters), [Llama 3 Herd of Models](https://arxiv.org/pdf/2407.21783), [Tom's Hardware: Llama 3 failures](https://www.tomshardware.com/tech-industry/artificial-intelligence/faulty-nvidia-h100-gpus-and-hbm3-memory-caused-half-of-the-failures-during-llama-3-training-one-failure-every-three-hours-for-metas-16384-gpu-training-cluster), [CUDO: what breaks in long training runs](https://www.cudocompute.com/blog/what-breaks-in-long-training-runs-and-how-recovery-actually-works), [Lablup: detection to recovery on 504 GPUs](https://arxiv.org/html/2605.09370v1)

## Real-World Application / Actionable Step
- In any multi-node distillation or QAT job, install a SIGTERM handler that writes a checkpoint (or at least flushes an async one) within 2 minutes, and make resume-from-latest the default path. That is the only part of this pipeline you own.
- Use async or in-memory sharded checkpointing (e.g. PyTorch DCP async save) so checkpoint interval can shrink without stalling training; that moves goodput more than node-swap speed.
- When evaluating a GPU cloud, ask for measured end-to-end recovery time at your job size, spare-pool size, and whether spares are billed. A 2-node demo number does not transfer.
- The shared train/inference pool is relevant to routing work: idle training GPUs serving overflow inference is a cheap way to host candidate models for routing experiments.
