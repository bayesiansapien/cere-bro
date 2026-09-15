---
source: farmer/huggingface
farmed: 2026-09-15T10:58:02.142912
arxiv_id: 2609.15134
url: https://huggingface.co/papers/2609.15134
arxiv_url: https://arxiv.org/abs/2609.15134
date: 2026-09-15
---

# HazardAuditor: From Executable Threats to Safer Computer-Use Agents

Computer-use agents increasingly interact with browsers, terminals, file systems, and external services, introducing safety risks that emerge through runtime behavior rather than generated content alone. Existing guard models target static prompts and responses and are poorly suited to agent execution; existing executable safety platforms produce evaluation verdicts rather than the normalized supervision a guard model needs to learn across heterogeneous agent frameworks. We introduce HazardAuditor, an execution-grounded framework that closes both gaps. Its infrastructure runs heterogeneous agents (Claude Code, Codex, Hermes, and OpenClaw) in controlled environments and normalizes their interactions into a canonical event representation for cross-framework supervision. We further observe that token-level post-training objectives create a structural mismatch for generative guards, causing longer rationales to dominate gradient updates. Guard Policy Optimization (GuardPO) addresses this by converting deterministic safety outcomes into sequence-level advantages and normalizing rationale and verdict regions, making the safety decision the effective unit of optimization. Across multiple benchmarks and heterogeneous computer-use systems, HazardAuditor improves accuracy by up to 16.5 percentage points over the strongest prior guard. Code, models, and evaluation artifacts will be available at https://yunhao-feng.github.io/HazardAuditor/.
