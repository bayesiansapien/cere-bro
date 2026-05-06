# T^2PO: Token- and Turn-Level Policy Optimization for Stable Multi-Turn Agentic RL

**Source:** HuggingFace Daily Papers, 2026-05-05
**Paper:** [arXiv:2605.02178](https://arxiv.org/abs/2605.02178) · [HF page](https://huggingface.co/papers/2605.02178)
**Raw:** [`raw/huggingface/2026-05-05-t2po-uncertainty-guided-exploration-control-stable-multi-turn-agentic-rl.md`](../../raw/huggingface/2026-05-05-t2po-uncertainty-guided-exploration-control-stable-multi-turn-agentic-rl.md)
**Tier:** 2 (Tier 1 intersection: agentic RL stability, exploration control)

## TL;DR

Multi-turn RL on agent tasks (WebShop, ALFWorld, Search QA) collapses frequently. The authors argue the root cause is *inefficient exploration*: the policy keeps emitting low-information actions that neither reduce uncertainty nor advance the task. T^2PO controls exploration at two levels. At the token level, it monitors uncertainty dynamics and triggers a "thinking intervention" once marginal uncertainty change drops below a threshold. At the turn level, it identifies turns with negligible exploration progress and resamples them dynamically rather than wasting rollouts. Result: substantial gains in training stability and performance across the three environments.

## Why it matters

Two of the wiki's recent threads converge here. AgenticQwen (Gmail, 05-04) used a self-failure-mining flywheel to harden a 30B-A3B MoE on its own errors, but the flywheel itself depends on stable training that does not collapse mid-rollout. Step-Level Optimization (05-02) used Stuck and Milestone monitors at *inference* to escalate to a frontier model when trajectory information stalls. T^2PO is the *training-time* version of the same idea: the same "trajectory information stalls" signal, used to trigger a thinking step and a resample, instead of escalating to a more expensive model. The shared abstraction is *uncertainty change as a state signal for an external policy intervention*, applied to RL training rather than inference.

## Connections

- **Step-Level Optimization (2026-05-02)** — Stuck Monitor and Milestone Monitor at inference. T^2PO mirrors the structure at training: token-level uncertainty derivative (analog of Stuck Monitor) + turn-level exploration progress (analog of Milestone Monitor). The two papers identify the same control surface.
- **AgenticQwen (2026-05-04)** — adversarial flywheel + self-failure mining. AgenticQwen's stability came from data design; T^2PO comes from training-loop control. Composing them, AgenticQwen's flywheel for distribution hardening + T^2PO's per-turn resampling for stability — is the natural next experiment. Neither has been measured against the other.
- **AHE (2026-05-04)** — agentic harness engineering with experience compression and decision-as-contract. T^2PO's per-turn resampling is a primitive that AHE's outer loop could call: the harness layer decides whether a turn yielded enough information; if not, T^2PO resamples within the same turn.
- **Compliance vs Sensibility (2026-05-02)** — reasoning modes are linear directions. T^2PO's thinking intervention is structurally what an activation-steering intervention would induce: forcing a representation shift when uncertainty stagnates. The compositional question is whether thinking interventions selected by uncertainty dynamics are equivalent to direct steering of the reasoning-mode direction.

## Research angle (Tier 1 intersection)

1. **T^2PO + Step-Level Optimization composition.** Use the same uncertainty signal at training (T^2PO) and inference (Step-Level Optimization). A model trained under T^2PO should be more sensitive to exploration-stagnation signals at deployment, making step-level escalation cheaper. Falsifiable: compare escalation rate of T^2PO-trained vs vanilla-trained agents under identical Step-Level Optimization escalation thresholds.
2. **Token-level uncertainty as KV-cache eviction signal.** The same marginal uncertainty change that T^2PO uses to trigger thinking is computable from KV-cache attention weights. A KV eviction policy that biases retention toward high-uncertainty-derivative tokens has not been built.
3. **Resample budget formalization.** Per-turn resampling adds a budget variable composing with Ch 15's structured-output retry budget, Ch 14's fallback chain, and the trajectory-routing escalation budget. Joint budget allocation is unsolved (flagged in the 05-04 digest already; T^2PO adds a fifth dimension).

## Open questions

- The threshold for "marginal uncertainty change falls below" is presumably tuned per environment. How transferable is the threshold across WebShop, ALFWorld, and Search QA — and to harder environments like Claw-Eval-Live or InteractWeb-Bench?
- Does T^2PO improve final policy quality, or only training stability? The abstract claims both, but the gain decomposition (stability vs capability) is the load-bearing question.
- The thinking intervention is an explicit token-level injection. Whether it is robust to adversarial environments where uncertainty signals are intentionally suppressed is not addressed.
