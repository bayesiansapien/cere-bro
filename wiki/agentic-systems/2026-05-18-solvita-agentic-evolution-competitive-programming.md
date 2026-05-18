# Solvita: Agentic Evolution for Competitive Programming

**Date ingested:** 2026-05-18
**Source:** HuggingFace Daily Papers 2026-05-18
**arXiv:** [2605.15301](https://arxiv.org/abs/2605.15301)
**Tier:** 2 (agentic systems, self-evolution, code)
**Raw:** [raw/huggingface/2026-05-18-solvita-...md](../../raw/huggingface/2026-05-18-solvita-enhancing-large-language-models-for-competitive-prog.md)

## TL;DR

Solvita is a four-agent code-generation framework (Planner, Solver, Oracle, Hacker) that accumulates problem-solving experience without retraining the underlying LLM. Each agent is paired with a trainable graph-structured knowledge network. Outcome signals (pass/fail verdicts, test certification quality, adversarial vulnerabilities found by the Hacker) update the network weights via reinforcement learning. The result is a closed-loop system where future queries are routed based on past successes and failures. Evaluated on CodeContests, APPS, AetherCode, and live Codeforces rounds, Solvita establishes a new state-of-the-art among code-generation agents, nearly doubling the accuracy of single-pass baselines.

## Why it matters

Two structural claims set Solvita apart from prior multi-agent code-generation work. First, the experience is **partitioned by agent role**. Each agent has its own knowledge network, and the network's edges are weighted by RL updates conditioned on what that agent was responsible for. Second, the experience is **encoded in graph weights, not retrieved as text**. Prior multi-agent code systems with memory (MapCoder, AlphaCodium) used retrieval-augmented generation on a static text corpus. Solvita instead trains the routing weights between problem features and agent strategies. The result is dynamic, learned routing without LLM weight updates.

The Hacker agent is the structural innovation. Most multi-agent code systems have a critic or verifier that grades a proposed solution. The Hacker actively constructs adversarial test cases that exploit weaknesses in the Solver's code, and the resulting attack patterns are stored as RL signal on the Hacker's network. This is the first wiki entry where adversarial test construction is the closed-loop signal source for agent self-evolution.

## Method

Four agents, each paired with a graph-structured knowledge network:

1. **Planner.** Chooses problem-solving strategies based on problem features. Its network learns which strategies have worked for which problem structures.
2. **Solver.** Synthesises code given the strategy. Its network learns which code patterns have worked under which strategies.
3. **Oracle.** Certifies test cases for completeness. Its network learns which test patterns reveal which bug classes.
4. **Hacker.** Constructs adversarial tests targeting the Solver's likely failure modes. Its network learns which attack patterns succeed against which code patterns.

Outcome signals as RL updates:

- Pass/fail verdicts from the verifier update the Solver and Planner networks.
- Test certification quality (does the test suite catch a known buggy implementation) updates the Oracle.
- Adversarial vulnerabilities found by the Hacker update the Hacker and the Solver.

The base LLM is frozen. All learning happens in the graph-structured knowledge networks. At inference time, each agent consults its network to route future queries based on accumulated experience.

## Connection to prior wiki context

**LIFE survey (2026-05-17, the 200+ paper multi-agent survey organising work along four causally linked stages: Lay capability foundation, Integrate via collaboration, Find faults via attribution, Evolve via self-improvement).** Solvita is a textbook Stage 4 system in the LIFE taxonomy: it integrates four specialised agents (Stage 2), uses the Hacker to attribute failures (Stage 3), and evolves the routing graphs from those failures (Stage 4). The LIFE framing predicted that Stage 4 systems would proliferate; Solvita is the most concrete Stage 4 system in the wiki to date that closes the loop through adversarial-test construction.

**EvolveMem (2026-05-15, the paper on self-evolving retrieval configuration via AutoResearch on the agent's own architecture).** Solvita's per-agent knowledge networks are structurally similar to EvolveMem's retrieval-configuration optimisation. Both encode the agent's history as a parameter set that an outer optimisation refines. The difference: EvolveMem optimises retrieval geometry; Solvita optimises routing between agent strategies and problem features.

**Orchard (2026-05-15, the credit-assignment SFT paper learning from productive segments of unresolved trajectories).** Orchard reuses partial-credit information from failed multi-step trajectories. Solvita reuses the failure mode itself as adversarial-test signal. Both treat failed trajectories as supervision substrate; they extract different signals from them.

**FrontierSmith (2026-05-16, the open-ended coding-problem generator with idea-divergence filter).** FrontierSmith generates new problems for an agent to attempt. Solvita evolves the agent given the problems. The pair composes into a closed-loop self-improvement system: generate problems with FrontierSmith, attempt them with Solvita, retrain Solvita's graphs on the resulting verdicts.

**Sylph AI (2026-05-16 social-stream, the Worker-Evaluator-Evolution loop that automates harness construction).** Sylph AI evolves the harness. Solvita evolves the routing inside a fixed harness. Both are agentic-evolution systems; they evolve different substrates.

## Research angle

1. **Hacker generalisation.** The adversarial-test construction is the load-bearing structural claim. Whether the Hacker's learned attack patterns generalise to unseen problem distributions or simply memorise per-benchmark exploits is the deployment-relevant test. Falsifiable: train Solvita on CodeContests and APPS, then evaluate on a held-out distribution like Codeforces Div 1.
2. **Cost of the four-agent overhead.** The accuracy gain (nearly 2x over single-pass baselines) trades against four times the LLM call cost. A productive comparison is Solvita against Conductor (2026-05-11, the Sakana paper that trained a 7B RL orchestrator to invoke frontier models at ~3 calls per question and beat every individual model on GPQA-D / LiveCodeBench / AIME25). Same per-question budget, different routing substrate.
3. **Graph-network ablation.** What fraction of Solvita's gain is from the four-agent structure versus the trainable graph networks? Falsifiable: run Solvita with frozen-uniform routing (no graph learning) and measure the gap.

## Links

- arXiv: <https://arxiv.org/abs/2605.15301>
- Related summaries: [LIFE survey 2026-05-17](2026-05-17-life-survey-multi-agent-collaboration-failure-self-evolution.md), [Conductor 2026-05-11](../ai-routing/2026-05-11-conductor-sakana-orchestrating-frontier-models.md)
