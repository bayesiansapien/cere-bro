# AutoTTS: Agentic Discovery for Test-Time Scaling

**arXiv:** [2605.08083](https://arxiv.org/abs/2605.08083) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.08083) · **Date:** 2026-05-11
**Tier:** 2 — Test-time scaling / agentic search over reasoning strategies
**Raw:** [farmer file](../../raw/huggingface/2026-05-11-llms-improving-llms-agentic-discovery-for-test-time-sc.md)

## TL;DR

Test-time scaling strategies have been hand-crafted: humans design width-depth heuristics (when to branch, when to continue, when to prune), then tune them by intuition. AutoTTS reformulates the question. Instead of designing the strategies, design the environment in which strategies can be discovered automatically. Width-depth TTS becomes controller synthesis over pre-collected reasoning trajectories and probe signals. Controllers decide branch / continue / probe / prune / stop. They are evaluated cheaply without repeated LLM calls. A beta-parameterization keeps the search tractable, fine-grained execution-trace feedback helps the agent diagnose why a TTS program fails. On math reasoning benchmarks, the discovered strategies improve the accuracy-cost tradeoff over strong manually designed baselines, generalize to held-out benchmarks and model scales, and the entire discovery run costs 39.90 dollars and 160 minutes.

## What is new

The environment-driven framing. Most TTS work treats the search space as a fixed set of heuristics (best-of-N, parallel branch-and-merge, tree-of-thoughts) and tunes them. AutoTTS treats the search space as a controller-synthesis problem: an agent edits a small program (the controller) that decides what to do at each step of reasoning. The environment provides cheap feedback (no LLM calls in the inner loop) and structured failure-mode traces. The agent improves the controller over time.

The 39.90 dollar discovery budget is the headline number. Manually designed TTS heuristics took grad-student months. AutoTTS discovers them in under 3 hours for the price of a casual dinner.

## Why the environment design matters more than the search

Two design moves carry the weight.

**Pre-collected trajectories and probe signals.** The inner loop never calls an LLM. The agent edits a controller, runs it against cached trajectories, and gets evaluated. This is what makes the 39.90 dollar number plausible. Without this, every controller edit would cost an LLM rollout, and the search would balloon to thousands of dollars.

**Beta parameterization.** Instead of letting the agent edit arbitrary code for the controller, the search space is parameterized as a continuous space (beta) with cheap structure. The discovery agent moves in this space rather than in raw program space. This is similar in spirit to the way function-space neural architecture search trades expressiveness for tractability.

**Trace feedback.** When a controller fails, the agent does not just see the failure metric. It sees an execution trace that tells it where the controller diverged from a desirable trajectory. This is the same diagnostic-feedback pattern that makes code-edit agents (Codex, Cursor) effective on real-world code: failures are observable structurally, not just numerically.

## Relation to prior wiki coverage

This belongs to the same family as Stop-Path Pruning (04-20) and the LongAct / Stream-T1 thread on selective compute allocation. All of these papers identify some axis (which tokens, which RL gradients, which video KV slots) where the cost is heterogeneous and pay attention to the structure. AutoTTS does the same one level up: which TTS strategies are worth running for which queries.

The composition with the Jiayi Weng "Learning Beyond Gradients" post (05-10) is direct. Weng argued that code-edit agents can replace gradient-trained neural policies for structured tasks. AutoTTS instantiates this exact pattern for TTS controller synthesis: the policy is code, the agent edits the code, the environment gives structural feedback. AutoTTS is the first concrete frontier-lab demonstration of Weng's framing at meaningful scale.

The Conductor paper (Sakana, same day) is the model-level analogue: an RL-trained orchestrator decides which model to call. AutoTTS is the strategy-level analogue: a discovery agent decides which TTS controller to use. Both are routing problems, both are learned, both target the compute-allocation surface.

## Research angle

**Cross-domain generalization beyond math.** The paper evaluates on math reasoning benchmarks. The next test is whether the discovered controllers transfer to non-math reasoning (long-form QA, code generation, agentic web tasks). If they do, the controller-synthesis frame becomes a general TTS substrate. If they do not, the math-specific structure (verifiable rewards, discrete answer space) is doing more of the work than the framing suggests.

**Composing with model-level routing.** The natural stack is AutoTTS on top of a Conductor-style orchestrator. The Conductor picks which worker model to call, AutoTTS picks how much TTS budget to spend on the call. The compound efficiency win is multiplicative.

**Beta parameterization expressiveness.** The cheap-search property of AutoTTS rides on the beta parameterization. If a stronger parameterization (e.g. a typed program-synthesis substrate) costs more per evaluation but unlocks richer controllers, the discovery cost might rise from 39.90 dollars to several thousand and still be a winning trade if the resulting controllers are substantially better. Worth measuring.

## Links

- [arXiv 2605.08083](https://arxiv.org/abs/2605.08083)
- [HuggingFace](https://huggingface.co/papers/2605.08083)
- [Conductor (same-day model-level orchestrator)](../ai-routing/2026-05-11-conductor-sakana-orchestrating-frontier-models.md)
- [Jiayi Weng — Learning Beyond Gradients (05-10)](2026-05-10-jiayi-weng-learning-beyond-gradients.md)
