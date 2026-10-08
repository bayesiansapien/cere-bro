---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.08430
url: https://huggingface.co/papers/2610.08430
arxiv_url: https://arxiv.org/abs/2610.08430
date: 2026-10-07
---

# NeMo-DCR: Bit-Exact Delta-Compressed Refit for Scalable Agentic RL at Trillion-Parameter Scale

Agentic reinforcement learning (RL) disaggregates training from rollout, so each policy update must reach the rollout clusters before the next batch. Transferring a full 1T checkpoint for such weight synchronization (refit) takes 87.5 min between two AWS regions. Measurements of BF16 training show that about 1% of weights change their stored values per step. Recent systems exploit this sparsity but fall short on placement, exactness, or efficiency: they reimplement placement rules, assemble full tensors, rebuild values arithmetically, or use a cross-cluster collective, and none fully recovers from mid-refit failures.
  We present NeMo-DCR (Delta-Compressed Refit), which sends only changes yet is bit-exact: receivers obtain the same parameter and buffer bits as a dense refit. For placement, fixed affine mappings project changes from training shards into the checkpoint's canonical coordinates, residual conversion covers the other changes, and the serving runtime's native loader places all changes in receiver storage. For exactness, compressible XOR masks carry affine changes whose projection and loader preserve stored bits, and overwrites carry the others. Receivers apply both in place, retries overwrite partial writes, and a joint commit binds the policy to the baseline for the next delta. For efficiency, object storage or a relay tree streams payloads during delta construction, without a cross-cluster collective. Even at 3% and 5% change rates, NeMo-DCR refits of 30B-1T models are 12-40times faster than a transport-only full-checkpoint reference. A 1T relay-tree refit at 3% takes 150 s instead of 87.5 min, making refits practical for cross-cluster agentic RL at trillion-parameter scale.
