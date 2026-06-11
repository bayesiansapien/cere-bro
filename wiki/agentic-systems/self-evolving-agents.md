# Self-Evolving Agents

**Concept page.** An agent is *self-evolving* when it improves its own behavior after deployment without a human writing the next round of code, prompts, or training data. The agent observes its own runs, extracts what worked and what failed, and feeds that back into one or more of its own parts.

The field has split the "self" into two distinct levers, and most of the confusion in the literature comes from conflating them:

- **Harness updates** (the scaffold around the model). A meta-agent rewrites tools, prompts, retry logic, memory, and the search procedure while the model weights stay frozen. This is the "agent harness" object that [Scaling the Harness](2026-05-27-scaling-the-harness.md) (05-27, the position paper arguing system scaling, not model scaling, is the next bottleneck, with six harness components) named as a first-class design surface. Lineage: Darwin Godel Machine, Meta-Harness, Hyperagents.
- **Weight updates** (the model itself). A test-time training loop updates the model's own parameters on task feedback while the harness stays fixed. Lineage: TTRL, the Discover test-time-training line.

These two were studied in isolation until 2026-06. The current frontier is combining them, and understanding how each scales.

---

## State of knowledge (as of 2026-06-11)

**Four papers in one day push the frontier from "evolve the agent" to "manufacture the substrate the agent learns from" — environments, harnesses, data, and research strategy all become scalable objects.** The day's [Agentic Environment Engineering survey](2026-06-11-agentic-environment-engineering-survey.md) (arxiv 2606.12191) is the map: it organizes the field around an environment lifecycle (modeling, synthesis, evaluation, application) and names Environment-as-a-Service as the endpoint. The three concrete systems each take one substrate:

- **Strategy substrate — [Arbor](2026-06-11-arbor-hypothesis-tree-refinement.md)** (arxiv 2606.11926). A long-lived coordinator runs research strategy over a persistent **Hypothesis Tree** (nodes link hypotheses → artifacts → evidence → distilled insights) while short-lived executors test hypotheses in isolated worktrees. Crucially it admits *only verified improvements* — the architectural answer to the 06-08/06-09 confabulation worry below. Beats Codex and Claude Code on all six Autonomous-Optimization tasks at >2.5x their held-out gain; 86.36% Any-Medal on MLE-Bench Lite. The coordinator/executor split is the [Disentangling](2026-06-08-disentangling-agent-self-evolution.md) routing insight made concrete.
- **Harness substrate — EvoTrainer** (arxiv 2606.03108). Co-evolves the LLM policy *and* the training harness through empirical feedback: diagnose rollouts, revise diagnostics, backtest interventions, accumulate reusable skills. Matches or beats human-engineered RL references, largest gain on long-horizon agentic SWE. This is HarnessForge's harness-policy co-evolution (06-08) moved inside the RL training loop. (Summarized with [RACES](../llms-foundation-models/2026-06-11-races-composable-verifiable-environments.md).)
- **Environment substrate — [RACES](../llms-foundation-models/2026-06-11-races-composable-verifiable-environments.md)** (arxiv 2606.12373). Treats verifiable RL environments as typed LEGO bricks: when one environment's output type matches another's input type, they auto-fuse into a new *still-verifiable* environment, via four operators (SEQUENTIAL, PARALLEL, SORT, SELECT). 50 composed base environments match 300 hand-built ones; +3.1 pts on six unseen benchmarks. This is the safer sibling of [EvoEnv](2026-05-15-evoenv-self-evolving-rl-via-environment-synthesis.md) (05-15) — composition *inherits* verifiability instead of re-establishing it.
- **Data substrate — [DeNovoSWE](2026-06-11-denovoswe-whole-repo-generation.md)** (arxiv 2606.10728). A sandboxed agentic workflow auto-builds 4,818 whole-repo-from-docs instances (divide-and-conquer + critic-repair), no human labels; lifts Qwen3-30B-A3B on BeyondSWE-Doc2Repo 5.8% → 47.2%. Measured by the same day's harness-aware [Claw-SWE-Bench](2026-06-11-claw-swe-bench-harness-evaluation.md), which confirms empirically that harness choice swings Pass@1 by 27.4 pp — as much as the model (29.4 pp).

The common thread: 2026's agent gains are substrate gains, and the new discipline is making each substrate a scalable, verifiable object. The standing risk from the cluster below — self-generated signal entrenches false beliefs unless an external verifier gates it — is precisely what Arbor's verified-improvement gate and RACES's composition-preserves-verifiability are built to contain.

## State of knowledge (as of 2026-06-09)

**Two 06-09 papers hit the skill-memory layer from opposite sides: make stored skills cheap, and stop trusting self-generated memory.** [LatentSkill](2026-06-09-latentskill-in-weight-skills.md) (arxiv 2606.06087) is the efficiency answer to the skill-library wave (Socratic-SWE, OpenSkill, Skill-RM): instead of injecting textual skills into the prompt every step, a pretrained hypernetwork converts each skill into a plug-and-play LoRA adapter, moving skills from context space to weight space. ALFWorld success +21.4 / +13.4 (seen / unseen) at 64.1% fewer prefill tokens, and the skill LoRAs compose by parameter-space arithmetic, the same hypernetwork-to-LoRA engine as [Code2LoRA](../inference-efficiency/2026-06-06-code2lora-hypernetwork-repo-adapters.md) and [Video2LoRA](../inference-efficiency/2026-06-06-video2lora-parametric-video-internalization.md) (06-06), new payload. [Honest Lying](2026-06-09-honest-lying-memory-confabulation.md) (arxiv 2605.29463) is the cold-water counterpart: Reflexion-style agents store confident-but-wrong task interpretations and keep acting on them across resets (16 frozen ALFWorld environments where 0 of 121 reflections name the correct object). It introduces the Reflection Repetition Rate to detect this, and shows programmatic failure extraction beats open-ended self-diagnosis (0% to 86% correct-object mention). This continues the 06-08 [Self-Revising Discovery Systems](2026-06-08-self-revising-discovery-systems.md) worry (is self-improvement real or confident remixing?) and the [ToolMaze](2026-06-08-toolmaze-dynamic-replanning.md) over-trust pathology: self-generated signal, whether a reflection or a mined trace, reinforces false beliefs unless an external verifier gates it.

## State of knowledge (as of 2026-06-08)

### Combining both levers beats either alone
[SIA](2026-06-08-sia-self-improving-harness-weights.md) (06-08, Hexo Labs) is the first system to update both the harness and the weights in one unified loop. A Feedback-Agent rewrites the scaffold *and* runs weight updates on a task-specific agent. Combining both beats scaffold-iteration alone on three contrasting domains: +56.6% on LawBench (Chinese legal charge classification), 91.9% runtime reduction on GPU kernel optimization, and +502% on single-cell RNA denoising. The stated division of labor: harness updates make the model *agentic* (how it searches and acts), weight updates build *domain intuition* no prompt can instil.

[HarnessForge](2026-06-08-harnessforge-harness-policy-coevolution.md) (06-08) reaches the same conclusion from the co-evolution angle: it formalizes an agent system as a harness-policy pair and co-evolves them via fault-guided harness tailoring plus harness-conditioned policy alignment, beating harness-only and policy-only baselines by up to 12.0% on five benchmarks. Its sharpest claim is that *executable compatibility* between harness and reasoning policy is essential, the two cannot be optimized in isolation.

### But a stronger model does NOT make a better self-evolving agent
This is the load-bearing 06-08 finding. [Disentangling Agent Self-Evolution](2026-06-08-disentangling-agent-self-evolution.md) (06-08, via DAIR.AI) separates **harness-updating** (an evolver model writes edits) from **harness-benefit** (a solver model exploits those edits) and shows they scale completely differently:

- **Updating is flat across model tiers.** Edit quality barely depends on model strength. Updates written by Qwen3.5-9B match those from Claude Opus 4.6. Paying for a frontier model on the *evolver* side buys almost nothing.
- **Benefit is non-monotonic.** Weak solvers gain little (they cannot activate or follow the harness component), mid-tier solvers benefit most, and the strongest solvers benefit less (they already solve the task without the scaffold).

The practical lever: **put a cheap model on the evolver, spend your capability budget on the solver.** This is a routing insight in disguise (see [LLM routing](../ai-routing/llm-routing.md)), and it directly tempers SIA's enthusiasm: if updating is flat across tiers, the gains SIA reports come from the *combination* and from the weight-update lever, not from a smarter scaffold-writer.

### Where the training signal comes from
The other 06-08 theme is the *substrate* a self-evolving loop learns from:
- [Socratic-SWE](2026-06-08-socratic-swe-trace-derived-skills.md) (06-08, SJTU + Alibaba) reuses the agent's own historical solving traces, distilling them into structured skills that summarize recurring failures and repair patterns, then generating targeted repair tasks graded by a solver-gradient-alignment reward. 50.40% on SWE-bench Verified after three iterations. The curriculum adapts to the agent's evolving weaknesses, unlike fixed bug-injection synthesis.
- [OpenSkill](2026-06-08-openskill-open-world-self-evolution.md) (06-08) tackles the hardest case: open-world deployment that supplies *neither* curated skills *nor* verifier signals, only a task prompt. The agent builds both its skills and its own verification anchors from documentation, repos, and the web, then practices against self-built virtual tasks. Its self-built verifier aligns with ground truth despite never accessing it, and skills transfer across models.

This builds on the earlier self-evolving cluster: [EvoDS](2026-06-05-evods-self-evolving-data-science-agent.md) and [MLEvolve](2026-06-05-mlevolve-self-evolving-ml-discovery.md) (06-05, self-evolving data-science / ML-discovery agents), [SEPO](2026-06-05-sepo-self-evolving-prompt-agent.md) (06-05, self-evolving prompt agent), [SkillOpt](2026-05-25-skillopt-executive-optimizer-agent-skills.md) (05-25), [Ctx2Skill](2026-05-05-ctx2skill-self-evolving-skills.md) (05-05), and [EvoEnv](2026-05-15-evoenv-self-evolving-rl-via-environment-synthesis.md) (05-15, self-evolving RL via environment synthesis).

---

## Open problems

- **Does the cheap-evolver finding survive harder tasks?** Disentangling tested a finite task set. If frontier evolvers eventually pull ahead on genuinely novel scaffolding, the routing recipe flips.
- **Verifier bootstrapping.** OpenSkill's self-built verifier working without ground truth is the riskiest claim in the cluster, the whole loop's safety rests on it.
- **Compounding vs collapse.** None of the 06-08 papers runs the loop long enough to show whether self-evolution compounds or drifts. This is the same control worry Anthropic raised about Sakana's recursive-self-improvement lab (06-07).
- **Discovery vs remix.** [Self-Revising Discovery Systems](2026-06-08-self-revising-discovery-systems.md) (06-08) formalizes the distinction between retrieval, search, and genuine discovery (inventing a concept not already in the toolkit) and gates accepted revisions by description length (one run: 25 of 388 proposals accepted, 6.4%). Most self-evolving agents only do retrieval and search.

## Industry signal
Sakana AI launched a dedicated recursive-self-improvement lab (06-07), explicitly betting that self-improvement, not raw compute, is the next lever. Anthropic flagged the control risk. The research cluster above is the academic front of the same bet.

## Related pages
- [Scaling the Harness](2026-05-27-scaling-the-harness.md): the harness as a design object
- [Code as Agent Harness](2026-05-23-code-as-agent-harness.md)
- [Agent benchmarks](agent-benchmarks.md) · [Agent memory](agent-memory.md) · [Tool calling](tool-calling.md)
- [LLM routing](../ai-routing/llm-routing.md): the cheap-evolver/expensive-solver split is a routing decision
