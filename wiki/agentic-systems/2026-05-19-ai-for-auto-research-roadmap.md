# AI for Auto-Research: Roadmap & User Guide

**arXiv:** [2605.18661](https://arxiv.org/abs/2605.18661) · **HF:** [paper page](https://huggingface.co/papers/2605.18661) · **Tier:** 2 (agentic systems, automated science, deployment)

## TL;DR

A roadmap and user-guide for AI across the complete research lifecycle, organised into four epistemological phases: Creation (idea generation, literature review, coding and experiments, tables and figures), Writing, Validation (peer review, rebuttal, revision), Dissemination. Studying developments through April 2026, the paper identifies a sharp, stage-dependent boundary between reliable assistance and unreliable autonomy: AI excels at structured, retrieval-grounded, tool-mediated tasks, but remains fragile for novel ideas, research-level experiments, and scientific judgement. Generated ideas often degrade after implementation. Research code lags far behind pattern-matching benchmarks. End-to-end autonomous systems have not consistently reached major-venue acceptance standards. Greater automation can obscure rather than eliminate failure modes, making human-governed collaboration the most credible deployment paradigm. The paper provides a structured taxonomy, benchmark suite, tool inventory, cross-stage design principles, and a practitioner playbook.

## Key findings

- Fully automated systems can now generate research papers for as little as $15. Long-horizon agents can execute experiments, draft manuscripts, and simulate critique with minimal human input. The productivity frontier is real.
- The integrity frontier is not. Under scientific pressure, frontier LLMs still fabricate results, miss hidden errors, and fail to judge novelty reliably.
- The reliable / unreliable boundary is stage-dependent:
  - Reliable: structured, retrieval-grounded, tool-mediated tasks (literature search, table generation, code formatting, dissemination assets).
  - Unreliable: genuinely novel idea generation, research-level experiments, scientific judgement (peer review, novelty assessment, rebuttal authority).
- Three specific empirical findings the wiki should track:
  - Generated ideas often degrade after implementation. An idea that scored well in an LLM evaluator regresses when the same agent runs the experiment.
  - Research code lags far behind pattern-matching benchmarks. An agent that beats HumanEval struggles to write a reproducible research experiment.
  - End-to-end autonomous systems have not consistently reached major-venue acceptance standards. The AAAI-26 AI Review Pilot (Kurate cs.AI #10, ai_rating 7.8/10, recurring on the leaderboard) is one of the few concrete data points.
- Greater automation can obscure failure modes, not eliminate them. This is the wiki's running deployment-calibration thread (WildClawBench, CurveBench, PAGER, DiagnosticIQ, AgentKernelArena's PyTorch-to-HIP unseen-shape failures) at the research-process level.

## Relationship to prior wiki entries

This is the wiki's first survey-roadmap entry on AI-for-research. Prior wiki entries treated specific components:

- AIRA-Compose / AIRA-Design (2026-05-18) is the wiki's first concrete example of LLM agents discovering neural architectures that scale faster than hand-designed baselines. AIRA is a Creation-phase success.
- Solvita (2026-05-18) showed adversarial-test construction as a Stage-4 self-evolution mechanism for code agents. This is a Creation-phase success in the narrow code domain.
- The LIFE multi-agent survey (2026-05-17, the 200+ paper survey organising multi-agent work along Lay-Integrate-Find-Evolve stages) is the closest prior structured taxonomy. AI-for-Auto-Research is the research-lifecycle counterpart.
- The Kurate cs.AI #5 paper ("AI scientists produce results without reasoning scientifically", Ríos-García et al., ai_rating 8.5/10, recurring) is the most direct empirical complement: AI scientists produce output without scientific reasoning, which is the failure mode this survey catalogs at the lifecycle level.

The survey aligns with the wiki's standing claim that the deployment-calibration gap (named on 2026-05-18 as the four-benchmark structural decoupling between headline accuracy and deployment capability) is the central diagnostic for any deployed agentic system. AI-for-Auto-Research extends that diagnostic to the research-process layer.

## Why it matters

The "$15 paper" framing forces the field to specify what AI-for-research actually delivers and where it breaks. The structured taxonomy and benchmark suite give labs a measurement layer they were missing. The practitioner playbook recommends human-governed collaboration as the deployment paradigm, which is the operationally honest framing: the gain is in retrieval and structured-task automation, not in scientific autonomy.

This matters for the wiki's research-engineer reader because it reframes the question from "can AI do research" to "which stages of research does AI safely accelerate." The answer (literature review, code formatting, dissemination assets) is the safe deployment surface; the answer (novel ideation, experiment design, peer-review judgement) is where caution applies.

## Research angle

- **Track the AI-for-Research benchmark suite uptake.** Whether the proposed taxonomy and benchmark suite become standard reference points in the next 30-60 days is the load-bearing community signal.
- **The "ideas degrade after implementation" finding deserves a dedicated study.** What is the gap between LLM-evaluator-scored idea quality and post-experiment outcome? Is the gap reducible by giving the evaluator implementation tooling, or is it structural?
- **AAAI-26 AI Review Pilot as a natural experiment.** The pilot is a real-world test of AI review at scale. The 60-90 day Worth Watching question: do AI-pilot reviews correlate with human-reviewer accept/reject decisions enough to merit continuation, or do they diverge?

## Source

`raw/huggingface/2026-05-19-ai-for-auto-research-roadmap-user-guide.md`
