# How to Test Your Agents on Real Tasks With Harbor (Xander Song, Arize AI)

**Channel:** AI Engineer
**Published:** 2026-10-26
**Source:** https://www.youtube.com/watch?v=kRJjSOYqW0I

## TL;DR
Harbor is the open-source harness from the Terminal-Bench team that turns "ship on vibes" into "ship on evidence" for agents. A task is three things: a natural-language instruction, a Docker environment seeded with real data, and verifier scripts that check side effects and emit a reward. Hold tasks and verifiers fixed, swap the agent (model, prompt, tools, skills, MCP server), run k independent trials in parallel sandboxes, and read pass@k plus cost and tool-call deltas. Arize uses it to evaluate the hybrid unit "Claude Code + our CLI/MCP/skills", not the coding agent alone, and pipes trajectories into Phoenix for per-task diffing between jobs.

## Key Takeaways
- **Primitives:** task (`instruction.md` + Dockerfile + `tests/`), optional oracle (a scripted reference solution), dataset (many tasks), trial (one isolated container run), job (dataset x agents x k trials). Verifiers write to a reward file; binary pass/fail is the default.
- **Contract is file layout, not an API.** Harbor is a host-side CLI that orchestrates containers and expects scripts in fixed locations. No linter validates this; Harbor's published agent skills are the closest thing to scaffolding help.
- **Anti-cheating by mounting order:** tests and solutions mount into the container only after the agent finishes, so the agent never sees them.
- **Oracle-first workflow:** run the oracle before any agent to debug data, environment, and verifiers at zero token cost.
- **Black-box verifiers are the canonical form.** They grade side effects only, like good integration tests, so you can refactor tools and prompts "under green." Arize hit the opposite failure: implementation-coupled tests broke on every tool rename even when behavior was intact.
- **Trajectory-peeking verifiers are a deliberate trade.** Fine for optimization targets (e.g. "did it use SQL?"), fragile for regression suites. Skill-firing tests are cheap but break on renames.
- **Scale:** each trial is independent, so it is horizontally scalable on Daytona, Modal, or E2B. Arize runs about 200 concurrent workers on Daytona.
- **Case study:** agents were paginating REST/GraphQL to answer aggregate questions ("top 3 models by cost"). Arize added a read-only SQL MCP tool, then a one-line prompt nudge ("use SQL for counts/group-bys"). Harbor showed reward flat, SQL calls up, GraphQL calls down, tool calls and turns down. That is an efficiency win with no correctness regression.
- **Synthetic task generation:** Claude brainstormed aggregate and non-aggregate queries across product domains and wrote oracle solutions (SQL or REST). The human only spot-checked questions.
- **Hard part is data.** Realistic seeded data is the bottleneck. Distributed systems (S3, multi-service) are much harder to containerize; mocking pulls you back into the world Harbor tries to escape. Multi-container environments are a partial escape hatch.

## Architecture & Optimization Mechanics
- **Evaluation unit = model + harness + tools + skills + prompt.** This is the correct framing for any routing or compression decision. A quantized or cheaper model's regression often shows up as more turns, wrong tool choice, or pagination loops before it shows up as a failed final answer.
- **Track more than reward.** Reward stayed constant in Arize's experiment. All the signal was in secondary metrics (tool-call count, turns, SQL vs GraphQL usage, cost, latency). An eval that only reports pass/fail would have shown "no change."
- **pass@k over k independent containers** is the right stochasticity control. With k=3 it is still noisy, so report per-task variance before calling a delta real.
- **ATIF (Agent Trajectory Interchange Format)** is Harbor's JSON trace spec: per-step LLM calls, tool calls, observations, tokens, cost. Phoenix converts it to OpenInference/OTel spans so you can diff the same task across two jobs at the trace level.
- **Weak spot the talk glosses over:** an oracle passing only proves the verifier accepts a correct solution. It does not prove the verifier rejects wrong ones. Some of Arize's verifiers were LLM-as-judge, which reintroduces exactly the nondeterminism the oracle was supposed to remove. The honest claim is "verifiers have no false negatives on the reference," not "verifiers are trustworthy."
- **The measured gains are understated by design.** The seeded SQLite file was small, so pagination cost was small. Real gains scale with data volume, but they also showed no numbers at production scale. Treat this as a qualitative demo.

## Grounded Context (Web Enrichment)
Harbor comes from the Terminal-Bench creators and is the official harness for Terminal-Bench 2.0. Adapters cover SWE-bench, LiveCodeBench, and others, with Docker locally and Daytona, Modal, and E2B as cloud backends. ATIF is documented as Harbor's standard trajectory format, and Claude Code and OpenHands are listed as ATIF-emitting agents. The ecosystem has moved quickly. Phoenix shipped a Harbor plugin in September 2026 that turns each trial's trajectory into a trace plus session. Comet's Opik has a similar integration, and Harbor's own docs now include an RL-optimization guide that positions it as a rollout generator for training, not just an eval harness. That last point matters more than the talk suggests: the same tasks and verifiers double as RL reward environments.

On OpenInference, the speaker's claim of donation "to cloud native and the OTel working group" is partly right. Community and vendor sources show Arize proposing the OpenInference donation to OpenTelemetry around May 2026 and completing it around June 2026. No source confirms a separate CNCF-level donation beyond OTel being a CNCF project. Also note that OTel's own GenAI semantic conventions (`gen_ai.*`) compete with OpenInference, and Arize normalizes `gen_ai.*` to OpenInference on ingest. Expect convergence, so do not hard-code against either schema.

## Real-World Application / Actionable Step
- **Use Harbor as the acceptance gate for routing and compression changes.** Build 30 to 50 tasks from real agent workloads. Hold verifiers fixed and sweep {FP16, GPTQ-4bit, AWQ, pruned, distilled} and router policies as "agents." Report pass@k, tokens, turns, tool calls, and $/task per arm. A router that keeps pass@k flat while turns go up is not saving money.
- **Add a negative oracle.** For each task, also run a no-op or deliberately broken solution and require reward 0. This closes the false-positive hole that oracle-only validation leaves open.
- **Keep two verifier tiers.** Pure side-effect verifiers for regression and CI. Trajectory-aware metrics (tool choice, turn count) logged separately as optimization targets, not as pass/fail gates, so model swaps do not flake the suite.
- **Bump k for small deltas.** Use k of at least 5 to 10 when comparing quantized vs full precision. Gaps of 1 to 3 points are inside k=3 noise.
- **Reuse the tasks as RL environments.** If you distill a cheaper agent model, the same Harbor verifiers give you verifiable rewards for rollouts at no extra cost.
