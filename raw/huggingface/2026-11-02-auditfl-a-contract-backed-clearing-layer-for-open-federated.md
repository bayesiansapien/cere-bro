---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.503007+05:30
arxiv_id: 2610.41278
url: https://huggingface.co/papers/2610.41278
arxiv_url: https://arxiv.org/abs/2610.41278
date: 2026-11-02
---

# AuditFL: A Contract-Backed Clearing Layer for Open Federated Learning

Federated learning (FL) keeps raw data local, but most deployments still rely on a trusted coordinator for client admission, checkpoint distribution, update collection, aggregation, and rewards. This paper presents AuditFL, a contract-backed clearing layer for auditable FL in open settings. AuditFL keeps training and aggregation off chain, stores model artifacts in an assumed reliable off-chain artifact store, and records only content identifiers and economic state on chain. Clients reserve update tickets with deposits, publish update identifiers, and later claim refunds or rewards; the task coordinator publishes global checkpoints and finalizes rounds through deterministic settlement rules. The design does not remove the aggregator, but makes its on-chain round decisions attributable, replayable, auditable, and economically constrained. We implement AuditFL as both a deterministic state-machine prototype and a Solidity contract on a local Ethereum-compatible Anvil chain. On full MNIST with Dirichlet non-IID splits, 12 rounds, and up to 200 clients, AuditFL preserves the Plain FL learning trajectory while its overhead follows closed-form control-plane models. At 200 clients, the contract run issues 5,026 transactions, stores 2,413 off-chain artifacts (144.9 MiB), and consumes 829.7M EVM gas, dominated by per-client reserve and publish calls. Controlled dropout, invalid-update, and artifact-unavailability stress tests reduce inclusion nearly linearly but still finalize rounds, with final-accuracy changes remaining within a few tenths of an accuracy percentage point even under high injected failure rates.
