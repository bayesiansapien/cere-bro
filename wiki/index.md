# Wiki Index

Catalog of all pages. Updated on every ingest.

---

## agentic-systems

| Page | Summary |
|------|---------|
| [gui-agents.md](agentic-systems/gui-agents.md) | Concept: MLLM-based GUI agents, long-horizon challenges, key papers |
| [agent-benchmarks.md](agentic-systems/agent-benchmarks.md) | Concept: benchmarks for agentic AI — OccuBench, GameWorld, MERRIN, explore/exploit |
| [2026-04-16-ui-copilot.md](agentic-systems/2026-04-16-ui-copilot.md) | UI-Copilot: memory decoupling + TIPO for long-horizon GUI tasks |
| [2026-04-16-trex-llm-finetuning-automation.md](agentic-systems/2026-04-16-trex-llm-finetuning-automation.md) | TREX: multi-agent LLM fine-tuning automation via search tree |
| [2026-04-16-exploration-exploitation-lm-agents.md](agentic-systems/2026-04-16-exploration-exploitation-lm-agents.md) | Measurable explore/exploit errors in LM agents |
| [2026-04-16-occubench.md](agentic-systems/2026-04-16-occubench.md) | OccuBench: 100 professional task scenarios via Language World Models |
| [2026-04-16-do-ai-coding-agents-log-like-humans.md](agentic-systems/2026-04-16-do-ai-coding-agents-log-like-humans.md) | AI coding agents fail logging instructions 67% of the time |
| [2026-04-16-defenseclaw-maestro-agentic-security.md](agentic-systems/2026-04-16-defenseclaw-maestro-agentic-security.md) | DefenseClaw: security control plane for OpenClaw + MAESTRO threat model |
| [2026-04-16-vakra-agent-reasoning-failure-modes.md](agentic-systems/2026-04-16-vakra-agent-reasoning-failure-modes.md) | VAKRA: tool-use failure modes in agents |
| [2026-04-17-claude-code-architecture.md](agentic-systems/2026-04-17-claude-code-architecture.md) | Claude Code v2.1.88 architecture: while-loop core + 5 surrounding systems |
| [2026-04-17-superlocalmemory-agent-memory.md](agentic-systems/2026-04-17-superlocalmemory-agent-memory.md) | SuperLocalMemory V3.3: biologically-inspired local agent memory with forgetting curves |
| [2026-04-25-claude-code-memory-systems-chapter8.md](agentic-systems/2026-04-25-claude-code-memory-systems-chapter8.md) | Claude Code memory systems (Chapter 8): QueryEngine eager flush + LRU cache + path-set dedup; Apr 23 postmortem caching bug analysis |

## llms-foundation-models

| Page | Summary |
|------|---------|
| [rl-for-llms.md](llms-foundation-models/rl-for-llms.md) | Concept: RL for LLMs — RLHF, RLVR, PreRL, and reasoning model training |
| [2026-04-16-prerl-rl-in-pretrain-space.md](llms-foundation-models/2026-04-16-prerl-rl-in-pretrain-space.md) | PreRL/DSRL: RL in pre-train space bypasses base model ceiling |
| [2026-04-16-open-vs-closed-models-mid-2026.md](llms-foundation-models/2026-04-16-open-vs-closed-models-mid-2026.md) | Nathan Lambert's 13 bets on open vs. closed models mid-2026 |
| [2026-04-16-infinitesciencegym-benchmark.md](llms-foundation-models/2026-04-16-infinitesciencegym-benchmark.md) | InfiniteScienceGym: procedurally generated scientific analysis benchmark |
| [2026-04-24-gpt-55-launch-system-card.md](llms-foundation-models/2026-04-24-gpt-55-launch-system-card.md) | GPT-5.5: first OpenAI pre-train since GPT-4.5; $5/$30 per M tokens; perfect reversion 0.18→0.52; SemiAnalysis switched daily driver |
| [2026-04-24-deepseek-v4-architecture.md](llms-foundation-models/2026-04-24-deepseek-v4-architecture.md) | DeepSeek V4: 1.6T/49B MoE on Huawei Ascend 950PR; CSA/HCA -73% FLOPs; Engram O(1) factual retrieval; cache costs -90% |
| [2026-04-28-hope-nested-learning-architecture.md](llms-foundation-models/2026-04-28-hope-nested-learning-architecture.md) | Hope/Nested Learning: Self-Modifying Titans replace attention; Continuum Memory replaces FFN; multi-timescale in-context adaptation |
| [2026-05-02-compliance-vs-sensibility-reasoning-controllability.md](llms-foundation-models/2026-05-02-compliance-vs-sensibility-reasoning-controllability.md) | Reasoning types (induction/deduction/abduction) resist instruction override; linearly encoded layers 16-24; mechanistic intervention +29% compliance |
| [2026-05-02-safety-drift-fine-tuning-high-stakes.md](llms-foundation-models/2026-05-02-safety-drift-fine-tuning-high-stakes.md) | Benign fine-tuning causes heterogeneous, contradictory safety changes across 100 deployed models; base-model evals predict nothing about fine-tuned variants |

## multimodal

| Page | Summary |
|------|---------|
| [2026-04-16-seedance-2-video-generation.md](multimodal/2026-04-16-seedance-2-video-generation.md) | Seedance 2.0: unified audio-video generation with 4 input modalities |
| [2026-04-16-rationalrewards-visual-generation.md](multimodal/2026-04-16-rationalrewards-visual-generation.md) | RationalRewards: critique-before-score reward models for visual generation |
| [2026-04-16-gameworld-multimodal-game-agents.md](multimodal/2026-04-16-gameworld-multimodal-game-agents.md) | GameWorld: 34-game benchmark for MLLM game agents |
| [2026-04-16-merrin-multimodal-retrieval.md](multimodal/2026-04-16-merrin-multimodal-retrieval.md) | MERRIN: multimodal web retrieval benchmark; avg accuracy 22.3% |
| [2026-05-02-vipo-visual-preference-optimization.md](multimodal/2026-05-02-vipo-visual-preference-optimization.md) | ViPO: 1M image + 300K video preference pairs; Poly-DPO collapses to DPO on clean data |
| [2026-05-02-semi-dpo-noisy-preferences.md](multimodal/2026-05-02-semi-dpo-noisy-preferences.md) | Semi-DPO: treats conflicting DPO preference labels as noisy unlabeled data; iterative pseudo-labeling |

## inference-efficiency

| Page | Summary |
|------|---------|
| [knowledge-distillation.md](inference-efficiency/knowledge-distillation.md) | Concept: knowledge distillation, on-policy distillation, cross-tokenizer BLD |
| [kv-cache.md](inference-efficiency/kv-cache.md) | Concept: KV cache — context dependency, reuse, compression, eviction |
| [2026-05-02-nemotron-3-nano-omni-multimodal.md](inference-efficiency/2026-05-02-nemotron-3-nano-omni-multimodal.md) | Nemotron 3 Nano Omni: 30B multimodal with native audio; token-reduction for lower latency; FP4/FP8/BF16 released |
| [2026-05-02-flashrt-efficient-red-teaming.md](inference-efficiency/2026-05-02-flashrt-efficient-red-teaming.md) | FlashRT: 264GB → 65GB, 1hr → 10min for optimization-based red-teaming at 32K context |
| [2026-04-16-tip-token-importance-on-policy-distillation.md](inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md) | TIP: two-axis token importance taxonomy; 47% memory reduction |
| [2026-04-17-kv-packet-recomputation-free-kv-cache.md](inference-efficiency/2026-04-17-kv-packet-recomputation-free-kv-cache.md) | KV Packet: soft-token adapters for zero-recomputation KV cache reuse |
| [2026-04-17-cross-tokenizer-distillation-byte-level.md](inference-efficiency/2026-04-17-cross-tokenizer-distillation-byte-level.md) | Byte-Level Distillation: bytes as universal cross-tokenizer interface |
| [2026-04-17-model-capability-dominates-inference-time.md](inference-efficiency/2026-04-17-model-capability-dominates-inference-time.md) | AIMO 3: model capability 4x > prompt-level optimization; gap is selection not prompting |

## ai-routing

| Page | Summary |
|------|---------|
| [llm-routing.md](ai-routing/llm-routing.md) | Concept: LLM routing — surrogate models, parity gates, open problems |
| [2026-04-17-tracer-llm-routing.md](ai-routing/2026-04-17-tracer-llm-routing.md) | TRACER: trace-driven surrogate routing; 100% coverage on 150-class benchmark |
| [2026-05-01-ken-huang-ch14-routing-provider-abstraction.md](ai-routing/2026-05-01-ken-huang-ch14-routing-provider-abstraction.md) | Ch 14: Claude Code compile-time static routing vs Hermes runtime dynamic routing; fallback chains; stripSignatureBlocks; per-turn cheap routing |
| [2026-05-02-step-level-optimization-computer-use-agents.md](ai-routing/2026-05-02-step-level-optimization-computer-use-agents.md) | Step-level cascade: Stuck + Milestone monitors escalate to frontier model only at high-risk junctures; modular, no retraining |

## hardware

| Page | Summary |
|------|---------|
| [gpu-kernels.md](hardware/gpu-kernels.md) | Concept: GPU kernel optimization, accelerator-specific tuning, NKI, memory hierarchy, AccelOpt, Nemotron, goodput |
| [2026-04-21-semianalysis-gpu-cluster-goodput.md](hardware/2026-04-21-semianalysis-gpu-cluster-goodput.md) | SemiAnalysis: gold vs silver tier neoclouds differ 6–21% in goodput; fault-tolerance tooling is fragmented and immature |
| [2026-04-27-semiconductor-week17.md](hardware/2026-04-27-semiconductor-week17.md) | Semiconductor Week 17: AI memory supercycle, agentic RISC-V CPU design, TSMC A13, AI-driven EDA N-of-3 pattern |

## ai-industry

| Page | Summary |
|------|---------|
| [2026-04-17-claude-market-share-surge.md](ai-industry/2026-04-17-claude-market-share-surge.md) | Claude doubles market share in a month; Gemini reaches 25% AI traffic share |
| [2026-04-17-anthropic-mythos-policy.md](ai-industry/2026-04-17-anthropic-mythos-policy.md) | Anthropic's Mythos: withheld from public, pitched to Pentagon; trust debate |
| [2026-04-22-amazon-anthropic-capital-concentration.md](ai-industry/2026-04-22-amazon-anthropic-capital-concentration.md) | Amazon $33B → Anthropic; Anthropic $100B → AWS over 10 years; circular capital deal locks infrastructure; Bezos Project Prometheus nears $10B |
| [2026-04-18-openai-exec-departures-restructuring.md](ai-industry/2026-04-18-openai-exec-departures-restructuring.md) | OpenAI loses three execs, restructures around coding/enterprise; IPO doubts |
| [2026-04-29-ucp-agentic-commerce-protocol.md](ai-industry/2026-04-29-ucp-agentic-commerce-protocol.md) | UCP vs. ACP: Google's Universal Commerce Protocol wins governance layer; Stripe defects from OpenAI's ACP; full purchase journey vs. checkout-only |
| [2026-04-29-claude-creative-work-connectors.md](ai-industry/2026-04-29-claude-creative-work-connectors.md) | Claude creative tool MCP connectors (Blender/Adobe/Autodesk/Ableton); /model flag; Remote Control push notifications; Opus opt-in |

## inference-efficiency (new 2026-04-21)

| Page | Summary |
|------|---------|
| [2026-04-21-nemotron3-super-hybrid-moe.md](inference-efficiency/2026-04-21-nemotron3-super-hybrid-moe.md) | Nemotron 3 Super: 120B/12B-active Mamba-MoE, NVFP4 pretraining, 2.2x throughput over GPT-OSS-120B, native speculative decoding via MTP |

## inference-efficiency (new 2026-04-20)

| Page | Summary |
|------|---------|
| [2026-04-20-accelopt-gpu-kernel-optimization.md](inference-efficiency/2026-04-20-accelopt-gpu-kernel-optimization.md) | AccelOpt: LLM agent self-improves Trainium kernel optimization via slow-fast memory; 49%→61% throughput at 26x lower cost |
| [2026-04-20-maximal-brain-damage-sign-bit-flips.md](inference-efficiency/2026-04-20-maximal-brain-damage-sign-bit-flips.md) | Maximal Brain Damage: 2 sign-bit flips collapse ResNet-50 by 99.8% and zero Qwen3-30B reasoning; same insight as compression = attack surface |
| [2026-04-20-stop-path-pruning-parallel-reasoning.md](inference-efficiency/2026-04-20-stop-path-pruning-parallel-reasoning.md) | STOP: learnable super-token prunes futile parallel reasoning paths at prefix; AIME25 84%→90% at fixed compute |
| [2026-04-20-1d-ordered-tokens-test-time-search.md](inference-efficiency/2026-04-20-1d-ordered-tokens-test-time-search.md) | 1D coarse-to-fine tokens enable test-time search; 2D grid tokens don't — intermediate states need semantic meaning for verifiers to steer |
| [2026-04-20-avr-adaptive-visual-reasoning.md](inference-efficiency/2026-04-20-avr-adaptive-visual-reasoning.md) | AVR: GRPO-trained format selection cuts VRM token usage 50-90%; perceive-only or direct-answer for simple visual queries |
| [2026-04-20-w-rac-retrieval-aware-chunking.md](inference-efficiency/2026-04-20-w-rac-retrieval-aware-chunking.md) | W-RAC: decouple text extraction from chunk planning; LLM decides ID groupings not text; 51.7% chunking cost reduction |

## agentic-systems (new 2026-04-20)

| Page | Summary |
|------|---------|
| [2026-04-20-gta-2-tool-agent-benchmark.md](agentic-systems/2026-04-20-gta-2-tool-agent-benchmark.md) | GTA-2: frontier models at 14.39% on open-ended workflows; execution harness matters more than model |
| [2026-04-20-prl-bench-physics-benchmark.md](agentic-systems/2026-04-20-prl-bench-physics-benchmark.md) | PRL-Bench: all frontier models below 50% on real physics research tasks from PRL (Aug 2025+) |
| [2026-04-20-query-agent-loop-claude-vs-hermes.md](agentic-systems/2026-04-20-query-agent-loop-claude-vs-hermes.md) | Claude Code 7-site state machine loop vs. Hermes IterationBudget — recovery architecture is what separates functional agents |

## multimodal (new 2026-04-20)

| Page | Summary |
|------|---------|
| [2026-04-20-qwen35-omni.md](multimodal/2026-04-20-qwen35-omni.md) | Qwen3.5-Omni: MoE + 256k context omnimodal; ARIA streaming speech alignment; SOTA 215 audio-visual benchmarks |

## inference-efficiency (new 2026-04-22)

| Page | Summary |
|------|---------|
| [2026-04-22-turbo-quant-kv-cache-quantization.md](inference-efficiency/2026-04-22-turbo-quant-kv-cache-quantization.md) | TurboQuant: random rotation → Beta distribution → optimal scalar quantization + 1-bit QJL; 6x KV cache compression at 2.5 bits/channel, near-zero quality loss, no calibration |
| [2026-04-22-prfaas-cross-datacenter-prefill.md](inference-efficiency/2026-04-22-prfaas-cross-datacenter-prefill.md) | PrfaaS: hybrid-attention models (13x smaller KV cache) enable cross-datacenter prefill disaggregation; 54% throughput, 50% lower TTFT |
| [2026-04-22-sdvg-speculative-decoding-video.md](inference-efficiency/2026-04-22-sdvg-speculative-decoding-video.md) | SDVG: speculative decoding for video via ImageReward quality router; 1.3B drafter + 14B target; 2.09x speedup at 95.7% quality |
| [2026-04-22-shadowpeft-centralized-layer-space.md](inference-efficiency/2026-04-22-shadowpeft-centralized-layer-space.md) | ShadowPEFT: single depth-shared shadow module replaces per-layer LoRA; independently pretrainable, detachable at edge; matches/outperforms LoRA |
| [2026-04-18-longact-saliency-sparse-rl.md](inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md) | LongAct: high-magnitude KV activations guide sparse RL updates; +8% LongBench v2 |
| [2026-04-18-tessy-teacher-student-sft.md](inference-efficiency/2026-04-18-tessy-teacher-student-sft.md) | TESSY: interleave teacher/student tokens to fix stylistic divergence in distillation |
| [2026-04-18-switch-kd-vision-language-distillation.md](inference-efficiency/2026-04-18-switch-kd-vision-language-distillation.md) | Switch-KD: VLM distillation through shared text-probability space; +3.6pt avg |

## agentic-systems (new 2026-04-18)

| Page | Summary |
|------|---------|
| [2026-04-18-corpus2skill-knowledge-navigation.md](agentic-systems/2026-04-18-corpus2skill-knowledge-navigation.md) | Corpus2Skill: compile corpus into skill tree, navigate not retrieve; beats RAPTOR |
| [2026-04-18-dr3-eval-deep-research-benchmark.md](agentic-systems/2026-04-18-dr3-eval-deep-research-benchmark.md) | DR3-Eval: reproducible deep research benchmark with static corpus sandboxes |
| [2026-04-19-unidoc-rl-visual-rag.md](agentic-systems/2026-04-19-unidoc-rl-visual-rag.md) | UniDoc-RL: RL agent for hierarchical visual RAG (doc→image→region); +17.7% over prior RL methods |
| [2026-04-19-claude-code-architecture.md](agentic-systems/2026-04-19-claude-code-architecture.md) | Claude Code architecture reverse-engineered: trivial while-loop + ML permission classifier + 5-layer compaction |
| [2026-04-23-persistent-agent-infrastructure.md](agentic-systems/2026-04-23-persistent-agent-infrastructure.md) | Kimi K2.6 (5 days, 300 sub-agents), OpenAI Agent Studio (Slack + screen memory), Anthropic Conway (containerized): three independent convergences on always-on agents |
| [2026-04-23-claude-code-vs-hermes-permissions.md](agentic-systems/2026-04-23-claude-code-vs-hermes-permissions.md) | Claude Code (ML classifier + layered rules) vs. Hermes (regex + container bypass): different safety bets, both untested at multi-day agent scale |
| [2026-04-22-ml-intern-agentic-posttraining.md](agentic-systems/2026-04-22-ml-intern-agentic-posttraining.md) | ml-intern: open-source agentic post-training loop; reads papers, generates data, trains via GRPO, evaluates, iterates; Qwen3-1.7B 10%→32% GPQA in 10 hours |
| [2026-04-22-evaluation-driven-scaling-scientific.md](agentic-systems/2026-04-22-evaluation-driven-scaling-scientific.md) | SimpleTES: parallel exploration + feedback refinement + local selection; 2x LASSO speedup, 24.5% quantum circuit gate reduction, new Erdős constructions |
| [2026-04-22-agentspex-workflow-language.md](agentic-systems/2026-04-22-agentspex-workflow-language.md) | AgentSPEX: declarative YAML workflow language for agents; typed steps, branching, state management, sandboxed harness with checkpointing |
| [2026-04-21-reward-free-self-evolution-agents.md](agentic-systems/2026-04-21-reward-free-self-evolution-agents.md) | Reward-free self-evolution: agents trained to explore accumulate world knowledge; 14B beats Gemini-2.5-Flash on web tasks |
| [2026-04-21-precise-debugging-benchmark.md](agentic-systems/2026-04-21-precise-debugging-benchmark.md) | PDB: frontier models pass unit tests 76% but edit precision below 45%; models regenerate not debug |

## llms-foundation-models (new 2026-04-18)

| Page | Summary |
|------|---------|
| [2026-04-18-c2-rubric-reward-modeling.md](llms-foundation-models/2026-04-18-c2-rubric-reward-modeling.md) | C2: cooperative-critical rubric generator avoids misleading reward model with bad rubrics |
| [2026-04-19-vgf-value-gradient-flow-rl.md](llms-foundation-models/2026-04-19-vgf-value-gradient-flow-rl.md) | VGF: behavior-regularized RL as optimal transport; no policy parameterization; SOTA offline RL + LLM tasks |
| [2026-04-19-asguard-activation-jailbreak-defense.md](llms-foundation-models/2026-04-19-asguard-activation-jailbreak-defense.md) | ASGuard: circuit analysis finds refusal-head vulnerability; activation scaling hardens against tense-changing jailbreaks |
| [2026-04-22-tempo-test-time-training.md](llms-foundation-models/2026-04-22-tempo-test-time-training.md) | TEMPO: EM-guided critic recalibration prevents reward drift in test-time training; OLMO3-7B 33%→51.1% AIME, Qwen3-14B 42.3%→65.8% |
| [2026-04-22-chain-of-thought-degrades-spatial.md](llms-foundation-models/2026-04-22-chain-of-thought-degrades-spatial.md) | CoT consistently degrades visual-spatial reasoning across 17 models and 13 benchmarks; No-Image++ ablation exposes language shortcut learning |
| [2026-04-22-target-pretraining-nag.md](llms-foundation-models/2026-04-22-target-pretraining-nag.md) | NAG-based pretraining data selection: sparse high-impact neurons characterize target inputs; +4.9% over random on HellaSwag, training-free |
| [2026-04-22-weight-disentanglement-task-arithmetic.md](llms-foundation-models/2026-04-22-weight-disentanglement-task-arithmetic.md) | OrthoReg: Task-Feature Specialization causes weight orthogonality; enforcing it during fine-tuning consistently improves task arithmetic |
| [2026-04-21-gft-sft-as-degenerate-rl.md](llms-foundation-models/2026-04-21-gft-sft-as-degenerate-rl.md) | GFT: SFT is degenerate policy gradient; group contrastive supervision fixes sparse reward + gradient instability |
| [2026-04-21-rlvr-weak-supervision-reasoning-faithfulness.md](llms-foundation-models/2026-04-21-rlvr-weak-supervision-reasoning-faithfulness.md) | When RLVR generalizes: reward saturation dynamics predict it; reasoning faithfulness (not diversity) is the pre-RL predictor |
| [2026-04-21-geometric-canary.md](llms-foundation-models/2026-04-21-geometric-canary.md) | Geometric Canary: supervised stability predicts steerability (ρ=0.89–0.97); unsupervised detects drift 2x better than CKA |

## daily-digest

| Page | Summary |
|------|---------|
| [2026-04-16.md](daily-digest/2026-04/2026-04-16.md) | Daily digest: TIP distillation, PreRL/DSRL, GUI agents, industry news |
| [2026-04-17.md](daily-digest/2026-04/2026-04-17.md) | Daily digest: TRACER routing, KV Packet, BLD cross-tokenizer, Claude Opus 4.7 |
| [2026-04-18.md](daily-digest/2026-04/2026-04-18.md) | Daily digest: LongAct, TESSY, Switch-KD distillation cluster; Mythos/Pentagon; OpenAI turbulence |
| [2026-04-19.md](daily-digest/2026-04/2026-04-19.md) | Daily digest: VGF (RL as optimal transport), TRACER full deep dive, UniDoc-RL visual RAG, ASGuard mechanistic alignment |
| [2026-04-20.md](daily-digest/2026-04/2026-04-20.md) | Daily digest: STOP path pruning, AccelOpt GPU kernels, Maximal Brain Damage vulnerability, GTA-2 agent benchmark, selective-compute convergence |
| [2026-04-21.md](daily-digest/2026-04/2026-04-21.md) | Daily digest: Nemotron 3 Super (Tier 1), SemiAnalysis goodput (Tier 1), GFT (SFT is broken RL), RLVR faithfulness, speculative execution cross-domain pattern |
| [2026-04-22.md](daily-digest/2026-04/2026-04-22.md) | Daily digest: TurboQuant (KV 6x compression), PrfaaS (cross-DC disaggregation), ml-intern (agentic post-training), TEMPO (EM-guided TTT), CoT degrades spatial reasoning |
| [2026-04-23.md](daily-digest/2026-04/2026-04-23.md) | Daily digest: persistent agent convergence (Kimi K2.6, OpenAI, Anthropic Conway), permission systems analysis, medical LLM reliability crisis, Mythos breach, Trainium2 |
| [2026-04-24.md](daily-digest/2026-04/2026-04-24.md) | Daily digest: GPT-5.5 launch, Expert Upcycling (MoE +32% GPU efficiency), NPO (near-future teacher RLVR), LLaDA2.0-Uni, Hybrid Policy Distillation |
| [2026-04-25.md](daily-digest/2026-04/2026-04-25.md) | Daily digest: GPT-5.5 system card agentic safety numbers, DeepSeek V4 architecture, Claude Code memory systems Chapter 8, Hybrid Policy Distillation deep dive |
| [2026-04-26.md](daily-digest/2026-04/2026-04-26.md) | Daily digest: weekend light day; Codex folds into GPT-5.5; old prompts hurt performance; 500 investment bankers zero client-ready outputs |
| [2026-04-27.md](daily-digest/2026-04/2026-04-27.md) | Daily digest: Agentic World Modeling L1/L2/L3 taxonomy (211▲), Stochastic KV Routing (depth axis), Semiconductor Week 17, Google $40B Anthropic |
| [2026-04-28.md](daily-digest/2026-04/2026-04-28.md) | Daily digest: Hope/Nested Learning architecture, From Skills to Talent multi-agent org, Why Fine-Tuning Hallucinations, Ubuntu AI launch, Google Pentagon deal |
| [2026-04-29.md](daily-digest/2026-04/2026-04-29.md) | Daily digest: RecursiveMAS cross-agent credit assignment, UCP governance win, Claude creative MCP connectors, Building Pi neural chip, OpenAI on AWS |
| [2026-04-30.md](daily-digest/2026-04/2026-04-30.md) | Daily digest: Speculative decoding into RL training (NVIDIA, 2.5x at 235B), Tide cross-arch dLLM distillation, GLM-5V-Turbo native multimodal agent, ClawGym, Zig anti-LLM policy |

## inference-efficiency (new 2026-04-30)

| Page | Summary |
|------|---------|
| [speculative-decoding.md](inference-efficiency/speculative-decoding.md) | Concept: speculative decoding — lossless target-preserving acceleration; now spans inference, video, and RL training |
| [2026-04-30-speculative-decoding-rl-rollouts.md](inference-efficiency/2026-04-30-speculative-decoding-rl-rollouts.md) | NVIDIA NeMo-RL: speculative decoding inside RL post-training; lossless under policy drift; k=3 sweet spot; 1.77x at 8B, 2.5x projection at 235B on 2048 GB200s |
| [2026-04-30-tide-cross-arch-diffusion-distillation.md](inference-efficiency/2026-04-30-tide-cross-arch-diffusion-distillation.md) | Tide: first cross-architecture distillation for diffusion LLMs; Tidal/CompDemo/Reverse Calm; 16B MoE → 0.6B; HumanEval 32.3 → 48.78; 22x memory, 5x speedup |

## agentic-systems (new 2026-04-30)

| Page | Summary |
|------|---------|
| [2026-04-30-clawgym-agent-framework.md](agentic-systems/2026-04-30-clawgym-agent-framework.md) | ClawGym: full-lifecycle Claw-agent framework; 13.5K dual-route synthesized tasks + sandbox-parallel RL + 200-instance bench; Qwen3-8B +43.46% on ClawGym-Bench |

## multimodal (new 2026-04-30)

| Page | Summary |
|------|---------|
| [2026-04-30-glm-5v-turbo-multimodal-agent.md](multimodal/2026-04-30-glm-5v-turbo-multimodal-agent.md) | GLM-5V-Turbo (Z.ai): native multimodal agent foundation; CogViT + Multimodal MTP + joint RL over 30+ tasks; 94.8 Design2Code beats Opus 4.6 |
| [2026-04-30-diffusion-templates-plugin-framework.md](multimodal/2026-04-30-diffusion-templates-plugin-framework.md) | Diffusion Templates (Alibaba): unified plugin framework — KV-Cache and LoRA under one capability-injection abstraction |
| [2026-04-30-fash-icnn-fashion-identity.md](multimodal/2026-04-30-fash-icnn-fashion-identity.md) | FASH-iCNN (Adobe): texture/luminance > color as carriers of editorial fashion identity; CNN probing methodology generalizes |
| [2026-04-30-x-wam-4d-world-model-robotics.md](multimodal/2026-04-30-x-wam-4d-world-model-robotics.md) | X-WAM: unified 4D world+action with Asynchronous Noise Sampling; fewer steps for action, full steps for video; 90.7% RoboTwin 2.0 |

## llms-foundation-models (new 2026-04-30)

| Page | Summary |
|------|---------|
| [2026-04-30-llm-user-simulation-survey.md](llms-foundation-models/2026-04-30-llm-user-simulation-survey.md) | Survey of LLM-based conversational user simulation; granularity × objective taxonomy; flags evaluation-vs-training simulator conflation |

## ai-industry (new 2026-04-30)

| Page | Summary |
|------|---------|
| [2026-04-30-zig-anti-ai-policy.md](ai-industry/2026-04-30-zig-anti-ai-policy.md) | Zig's "Contributor Poker" rationale: PR review = contributor investment; LLM-authored PRs short-circuit it; Bun (Anthropic-acquired) refuses to upstream

## inference-efficiency (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01-roundpipe-pipeline-parallelism-consumer-gpus.md](inference-efficiency/2026-05-01-roundpipe-pipeline-parallelism-consumer-gpus.md) | RoundPipe: stateless GPU worker pool breaks weight-binding bottleneck on consumer servers; 1.48–2.16x speedup; LoRA fine-tuning Qwen3-235B at 31K context on 8x RTX 4090 |
| [2026-05-01-lenvm-token-level-length-value-model.md](inference-efficiency/2026-05-01-lenvm-token-level-length-value-model.md) | LenVM: token-level RL value model for length control; constant negative reward → bounded monotone return; LIFEBench 30.9→64.8; GSM8K @200 tokens 63% vs 6% baseline |

## llms-foundation-models (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01-copd-co-evolving-policy-distillation.md](llms-foundation-models/2026-05-01-copd-co-evolving-policy-distillation.md) | CoPD: parallel RLVR experts + bidirectional OPD during training; 5th paper in cross-distillation-channel pattern; surpasses domain-specific experts on text/image/video reasoning |

## agentic-systems (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01-claw-eval-live-agent-benchmark.md](agentic-systems/2026-05-01-claw-eval-live-agent-benchmark.md) | Claw-Eval-Live: refreshable signal layer + reproducible release snapshot; 105 tasks, 13 frontier models; best 66.7%, none reach 70%; trajectory-aware grading; middle-band discrimination → routing opportunity |
| [2026-05-01-interactweb-bench-blind-execution.md](agentic-systems/2026-05-01-interactweb-bench-blind-execution.md) | InteractWeb-Bench: first benchmark grading clarifying behavior; four-action space (Clarify/Implement/Verify/Submit); frontier MLLM agents trapped in "blind execution" |
| [2026-05-01-synthetic-computers-at-scale.md](agentic-systems/2026-05-01-synthetic-computers-at-scale.md) | Synthetic Computers at Scale: 1K populated computers × 8h × 2K-turn agent simulations as long-horizon training data; in-domain + out-of-domain gains validate signal |
| [2026-05-01-ara-agent-native-research-artifacts.md](agentic-systems/2026-05-01-ara-agent-native-research-artifacts.md) | Ara: agent-executable 4-layer research artifact replacing the narrative paper; PaperBench 72.4→93.7%; failure traces help weaker agents but constrain stronger ones |
| [2026-05-01-intern-atlas-method-evolution-graph.md](agentic-systems/2026-05-01-intern-atlas-method-evolution-graph.md) | Intern-Atlas: 9.4M-edge methodological evolution graph from 1.03M papers; bottleneck-typed transitions as causal links; routing data structure for ideas |
| [2026-05-01-eywa-heterogeneous-foundation-collab.md](agentic-systems/2026-05-01-eywa-heterogeneous-foundation-collab.md) | Eywa: language-mediated wrappers for heterogeneous scientific FMs (chemistry/protein/materials/climate); language as universal control plane over heterogeneous foundation models |
| [2026-05-01-mcp-claude-vs-hermes-chapter13.md](agentic-systems/2026-05-01-mcp-claude-vs-hermes-chapter13.md) | Ken Huang Ch 13: MCP integration; Claude Code TS-async session-bound vs Hermes long-lived MCPServerTask + sampling + credential stripping |

## multimodal (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01-edit-r1-verifier-rl-image-editing.md](multimodal/2026-05-01-edit-r1-verifier-rl-image-editing.md) | Edit-R1: CoT reasoning verifier reward for image editing; SFT cold-start + GCPO; scorer-to-reasoning-verifier shift generalizes beyond editing |
| [2026-05-01-fd-loss-frechet-visual-generation.md](multimodal/2026-05-01-fd-loss-frechet-visual-generation.md) | FD-loss: decouple population (50K) from batch (1024) to make Fréchet Distance trainable; 0.72 FID one-step ImageNet; multi-representation FDrk metric |
| [2026-05-01-visual-generation-taxonomy-survey.md](multimodal/2026-05-01-visual-generation-taxonomy-survey.md) | Visual Generation taxonomy: Atomic / Conditional / In-Context / Agentic / World-Modeling Generation; locates current frontier and the open levels |
| [2026-05-01-phyco-controllable-physics-priors.md](multimodal/2026-05-01-phyco-controllable-physics-priors.md) | PhyCo: 100K physics simulation videos + ControlNet on physical-property maps + VLM-guided reward for physically consistent video generation |

## ai-industry (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01-semianalysis-ai-value-capture-model-labs.md](ai-industry/2026-05-01-semianalysis-ai-value-capture-model-labs.md) | SemiAnalysis: structural shift to model labs capturing value; Anthropic ARR $9B→$44B+, margin 38%→70%; Nvidia/TSMC restraint; "One Chart to Rule Them All" pricing framework |
| [2026-05-01-marcus-capital-misallocation.md](ai-industry/2026-05-01-marcus-capital-misallocation.md) | Marcus: "greatest capital misallocation in history" — direct counterpoint to SemiAnalysis the same day; mainstream AI-bubble framing |
| [2026-05-01-pragmatic-engineer-github-anthropic-trust.md](ai-industry/2026-05-01-pragmatic-engineer-github-anthropic-trust.md) | Pragmatic Engineer: GitHub at zero nines under 3.5x AI load; Anthropic in "extraction era" (silent Claude Code nerfing, $100/mo gate, OpenClaw block) |

## daily-digest (new 2026-05-01)

| Page | Summary |
|------|---------|
| [2026-05-01.md](daily-digest/2026-05/2026-05-01.md) | Daily digest: SemiAnalysis vs Marcus on AI value capture; RoundPipe 235B-on-consumer-GPU; LenVM token-level length VM; CoPD as 5th cross-distillation paper; 6-benchmark agent eval crisis; Ara+Intern-Atlas AI-native research stack

## ai-industry (new 2026-05-01 late-landed)

| Page | Summary |
|------|---------|
| [2026-05-01-pentagon-eight-tech-giants-ai-fighting-force.md](ai-industry/2026-05-01-pentagon-eight-tech-giants-ai-fighting-force.md) | Pentagon "AI-first fighting force" contracts to eight tech firms; Anthropic excluded for rejecting usage clause; capability rank decoupled from procurement |
| [2026-05-01-anthropic-claude-security-launch.md](ai-industry/2026-05-01-anthropic-claude-security-launch.md) | Anthropic Claude Security: defender-side product drawing on capability withheld in Mythos; commercial response to GPT-5.5 = Mythos parity |
| [2026-05-01-gpt-55-uk-aisi-cyber-eval.md](ai-industry/2026-05-01-gpt-55-uk-aisi-cyber-eval.md) | UK AISI: GPT-5.5 second model to autonomously solve full network attack simulation, parity with Mythos; Mythos restriction logic empirically broken |
| [2026-05-01-china-ai-startups-onshoring.md](ai-industry/2026-05-01-china-ai-startups-onshoring.md) | Moonshot AI, StepFun considering dissolving offshore structures for domestic IPO path; bilateral AI sovereignty after Manus block |
| [2026-05-01-aisn-72-ai-wellbeing-public-sentiment.md](ai-industry/2026-05-01-aisn-72-ai-wellbeing-public-sentiment.md) | CAIS AI Wellbeing study (56 LLMs, Grok highest, Gemini lowest); anti-AI violence (Altman home Molotov); 26% positive / 46% negative US sentiment; Mythos exfiltration; Apple Cook→Ternus |

## ai-routing (new 2026-05-01 late-landed)

| Page | Summary |
|------|---------|
| [2026-05-01-ken-huang-ch14-routing-provider-abstraction.md](ai-routing/2026-05-01-ken-huang-ch14-routing-provider-abstraction.md) | Ch 14 cross-harness routing: Claude Code compile-time abstraction with signature-stripping fallback vs Hermes runtime API-mode detection + ordered fallback chains + switch_model + conservative cheap-model heuristic |

## multimodal (new 2026-05-02)

| Page | Summary |
|------|---------|
| [2026-05-02-nemotron-3-nano-omni.md](multimodal/2026-05-02-nemotron-3-nano-omni.md) | Nemotron 3 Nano Omni (multimodal angle): 30B native-audio omni model; multimodal token reduction as routing primitive; fourth open-frontier release in 72h |

## daily-digest (new 2026-05-02)

| Page | Summary |
|------|---------|
| [2026-05-02.md](daily-digest/2026-05/2026-05-02.md) | Daily digest: Routing legible on 3 axes (Step-level, Ken Huang Ch 14, Surrogate); Compliance-vs-Sensibility + Safety Drift converge on "operational properties are vector-valued"; cyber arms race in 3 vectors (GPT-5.5=Mythos, Claude Security, FlashRT); Pentagon excludes Anthropic; bilateral AI sovereignty

## llms-foundation-models (new 2026-05-02 / 05-03 RSS)

| Page | Summary |
|------|---------|
| [2026-05-02-defense-trilemma-np-hardness-reward-hacking.md](llms-foundation-models/2026-05-02-defense-trilemma-np-hardness-reward-hacking.md) | Ken Huang on the Defense Trilemma (Lean-4-verified topology proof: no continuous, utility-preserving wrapper is complete) + three converging complexity results (NP-complete semantic self-verification, no-free-lunch on alignment, reward hacking grows structurally with tools) |
| [2026-05-02-arc-agi-3-three-systematic-reasoning-errors.md](llms-foundation-models/2026-05-02-arc-agi-3-three-systematic-reasoning-errors.md) | ARC Prize Foundation analyzed 160 game runs: GPT-5.5 and Opus 4.7 stay below 1% on ARC-AGI-3; three systematic error patterns named |
| [2026-05-03-ken-huang-world-models-architectures.md](llms-foundation-models/2026-05-03-ken-huang-world-models-architectures.md) | World Models survey: LeCun JEPA vs Xing PAN/GLP debate; transformers/diffusion/SSM/RNN substrates; Mamba/SSM quietly excellent for world models; hybrids are the empirical default |
| [2026-05-03-mit-superposition-scaling-laws.md](llms-foundation-models/2026-05-03-mit-superposition-scaling-laws.md) | MIT: superposition (features in approximately non-interfering directions) explains why scaling works so reliably; mechanistic substrate for the operational-targets-are-sparse thread |
| [2026-05-03-philosophy-bench-ethical-divergence.md](llms-foundation-models/2026-05-03-philosophy-bench-ethical-divergence.md) | Philosophy-Bench: 100 everyday ethical scenarios; frontier LMs diverge systematically; ethics is a vector, not a scalar |
| [2026-05-03-marcus-llm-patient-outcomes.md](llms-foundation-models/2026-05-03-marcus-llm-patient-outcomes.md) | Marcus quoting Topol/Nature Medicine: very little evidence LLMs benefit patient outcomes outside admin work |

## agentic-systems (new 2026-05-02 RSS)

| Page | Summary |
|------|---------|
| [2026-05-02-ken-huang-ch15-structured-output.md](agentic-systems/2026-05-02-ken-huang-ch15-structured-output.md) | Ch 15: Structured output via tool-use forcing in both Claude Code (SyntheticOutputTool + Ajv schema-id cache) and Hermes (extract_structured + JSONL trajectory schema); ModelCapabilities.structured_output as routing sub-axis |

## ai-industry (new 2026-05-02 / 05-03)

| Page | Summary |
|------|---------|
| [2026-05-02-chatgpt-ads-tracking-default.md](ai-industry/2026-05-02-chatgpt-ads-tracking-default.md) | OpenAI turned on marketing cookies by default for free ChatGPT users; revenue diversification; pairs with Anthropic Opus metering |
| [2026-05-03-microsoft-copilot-coauthor-vscode.md](ai-industry/2026-05-03-microsoft-copilot-coauthor-vscode.md) | Microsoft injecting "Co-Authored-by Copilot" into VS Code commits even with AI off; commit-attribution and code-provenance integrity |
| [2026-05-03-xiaomi-mimo-25-pro-open-weight-coding.md](ai-industry/2026-05-03-xiaomi-mimo-25-pro-open-weight-coding.md) | Xiaomi MiMo-V2.5-Pro: open-weight near-parity with Claude Opus 4.6 at 40-60% fewer tokens per task; pricing axis shift from capability ceiling to per-task cost |

## llms-foundation-models (new 2026-05-04)

| Page | Summary |
|------|---------|
| [2026-05-04-themis-multilingual-code-reward-models.md](llms-foundation-models/2026-05-04-themis-multilingual-code-reward-models.md) | Themis: first multi-criteria multilingual code reward model benchmark (5 dim × 8 lang) + 350K preference pairs + 600M-32B RM suite; code-domain version of ViPO/Semi-DPO dimension-collapse diagnosis |

## agentic-systems (new 2026-05-04)

| Page | Summary |
|------|---------|
| [2026-05-04-lwd-fleet-rl-vla-policies.md](agentic-systems/2026-05-04-lwd-fleet-rl-vla-policies.md) | LWD: fleet-scale offline-to-online RL for VLA policies; Distributional Implicit Value Learning + Q-learning via Adjoint Matching; primitives transfer to language-domain trajectory routing |

## multimodal (new 2026-05-04)

| Page | Summary |
|------|---------|
| [2026-05-04-genlip-generative-language-image-pretraining.md](multimodal/2026-05-04-genlip-generative-language-image-pretraining.md) | GenLIP: minimalist ViT pretraining via direct image→text token prediction with LM loss; no contrastive batches, no text decoder |
| [2026-05-04-end-to-end-autoregressive-image-generation-1d-tokenizer.md](multimodal/2026-05-04-end-to-end-autoregressive-image-generation-1d-tokenizer.md) | End-to-end joint training of 1D semantic tokenizer + AR generator; FID 1.48 without classifier-free guidance on ImageNet 256x256 |
| [2026-05-04-unividx-unified-video-generation.md](multimodal/2026-05-04-unividx-unified-video-generation.md) | UniVidX: VDM priors for omni-directional cross-modal generation; Stochastic Condition Masking + Decoupled Gated LoRA + Cross-Modal Self-Attention |
| [2026-05-04-map2world-3d-world-generation.md](multimodal/2026-05-04-map2world-3d-world-generation.md) | Map2World: segment-map-conditioned 3D world generation with arbitrary shapes; Tier 4 |
| [2026-05-04-analogretriever-circuit-retrieval.md](multimodal/2026-05-04-analogretriever-circuit-retrieval.md) | AnalogRetriever: tri-modal retrieval (SPICE netlists, schematics, descriptions) for analog circuit IP; data-quality pipeline 22% to 100% compile rate |

## daily-digest (new 2026-05-04)

| Page | Summary |
|------|---------|
| [2026-05-04.md](daily-digest/2026-05/2026-05-04.md) | Daily digest: Defense Trilemma + NP-hard reward hacking detection (the "computational wall"); MIT superposition as substrate for the operational-targets-are-sparse thread; Xiaomi MiMo-V2.5-Pro shifts pricing axis to tokens-per-task; Themis multi-criteria code RM continues the dimension-collapse pattern; Ken Huang World Models survey; routing surface now five axes

## new pages (2026-05-05)

| Page | Summary |
|------|---------|
| [inference-efficiency/2026-05-05-motion-aware-caching-video.md](inference-efficiency/2026-05-05-motion-aware-caching-video.md) | MotionCache: inter-frame motion deltas decide which pixels need full denoising; 6.28x on SkyReels-V2 at 1% VBench drop; video-AR analogue of selective KV reuse |
| [agentic-systems/2026-05-05-t2po-uncertainty-multi-turn-rl.md](agentic-systems/2026-05-05-t2po-uncertainty-multi-turn-rl.md) | T^2PO: token + turn level uncertainty controls exploration in multi-turn agent RL; training-time twin of Step-Level Optimization (05-02) |
| [agentic-systems/2026-05-05-ctx2skill-self-evolving-skills.md](agentic-systems/2026-05-05-ctx2skill-self-evolving-skills.md) | Ctx2Skill: Challenger/Reasoner/Judge self-play extracts pluggable natural-language skills from context; Cross-time Replay prevents adversarial collapse |
| [agentic-systems/2026-05-05-physicianbench-ehr-agents.md](agentic-systems/2026-05-05-physicianbench-ehr-agents.md) | PhysicianBench: 100 EHR clinical workflows, ~27 tool calls per task; best closed-source 46%, open-source 19%; eighth benchmark in the agent-cluster |
| [agentic-systems/2026-05-05-academiclaw-student-tasks.md](agentic-systems/2026-05-05-academiclaw-student-tasks.md) | AcademiClaw: 80 academic-level tasks across 25+ domains; best 55%; compute consumption does not predict output quality |
| [inference-efficiency/2026-05-04-distillation-panic-lambert.md](inference-efficiency/2026-05-04-distillation-panic-lambert.md) | The Distillation Panic (Lambert): policy critique of conflating "distillation attacks" with the entire distillation toolbox every lab depends on |
| [llms-foundation-models/2026-05-04-import-ai-455-automated-ai-rd.md](llms-foundation-models/2026-05-04-import-ai-455-automated-ai-rd.md) | Import AI 455 (Clark): 60% probability of fully autonomous AI R&D by end of 2028, built from public benchmark trajectories (SWE-Bench, METR, CORE-Bench, MLE-Bench) |
| [agentic-systems/2026-05-04-agentic-pentester-architecture.md](agentic-systems/2026-05-04-agentic-pentester-architecture.md) | Ken Huang on RidgeGen vs Shannon vs Strix: same Gemini 3 Flash, three architectures, 0% vs 63% hallucination, >5x finding gap; belief state, evidence-as-invariant, semantic reasoning are the three primitives |
| [ai-industry/2026-05-04-anthropic-openai-services-companies.md](ai-industry/2026-05-04-anthropic-openai-services-companies.md) | Anthropic JV $1.5B (Blackstone/Goldman/H&F) + OpenAI $4B Deployment Company: both labs build services arms because "selling AI requires more than the AI" |
| [hardware/2026-05-04-cerebras-40b-ipo.md](hardware/2026-05-04-cerebras-40b-ipo.md) | Cerebras targets $40B Nasdaq IPO (CBRS); first public-market validation of inference-specialty silicon since Groq |

## daily-digest (new 2026-05-05)

| Page | Summary |
|------|---------|
| [2026-05-05.md](daily-digest/2026-05/2026-05-05.md) | Daily digest: MotionCache extends KV-cache iteration-as-optimization to video; T^2PO is the training-time twin of Step-Level Optimization; Distillation Panic (Lambert) names the policy threat; Import AI 455 (Clark) puts automated AI R&D at 60% by 2028; Ken Huang pentester benchmark instantiates harness > weights at constant model; PhysicianBench + AcademiClaw take the agent-benchmark cluster to eight; Anthropic JV + OpenAI Deployment Co move the lab business above the API

## new pages (2026-05-06)

| Page | Summary |
|------|---------|
| [agentic-systems/2026-05-06-agent-security-study.md](agentic-systems/2026-05-06-agent-security-study.md) | 847 production agents: 91% tool-chaining vulnerable, 89.4% goal drift at step 30, 94% memory-aug poisonable; OpenClaw/Moltbook: 770K agents simultaneously compromised |
| [agentic-systems/2026-05-06-ctx2skill-context-learning.md](agentic-systems/2026-05-06-ctx2skill-context-learning.md) | Ctx2Skill: self-evolving Challenger/Reasoner/Judge loop extracts reusable skills from context; Cross-time Replay prevents adversarial collapse |
| [llms-foundation-models/2026-05-06-deepseek-v4.md](llms-foundation-models/2026-05-06-deepseek-v4.md) | DeepSeek V4 Pro: 1.6T/49B active MoE, 1M context, open-sourced; V4 Flash 284B/13B active; claims to close gap with frontier |
| [ai-industry/2026-05-06-musk-altman-trial-week2.md](ai-industry/2026-05-06-musk-altman-trial-week2.md) | Musk v. Altman week 2: xAI distillation admission, Brockman $30B stake, OpenAI IPO floated; Lambert's Distillation Panic confirmed by sworn testimony |

## daily-digest (new 2026-05-06)

| Page | Summary |
|------|---------|
| [2026-05-06.md](daily-digest/2026-05/2026-05-06.md) | Daily digest: agent security audit (91% tool-chaining vulnerable, 770K incident); ProgramBench 0%; Musk admits xAI distillation; DeepSeek V4 open-sourced; OpenAI/MS renegotiation closes; Ctx2Skill self-evolving skill loop; TobyPhln xAI retrospective via Twitter

## new pages (2026-05-07)

| Page | Summary |
|------|---------|
| [inference-efficiency/2026-05-07-stream-r1-reliability-perplexity-distillation.md](inference-efficiency/2026-05-07-stream-r1-reliability-perplexity-distillation.md) | Stream-R1: DMD distillation reweighted at rollout (reward-rescaled) and pixel (saliency-weighted) levels by a single shared video reward model; video-streaming analogue of TIP |
| [inference-efficiency/2026-05-07-stream-t1-test-time-scaling-streaming-video.md](inference-efficiency/2026-05-07-stream-t1-test-time-scaling-streaming-video.md) | Stream-T1: test-time scaling with Stream-Scaled Memory Sinking, the first content-aware KV eviction policy in the wiki (route by reward feedback, not recency) |
| [inference-efficiency/2026-05-07-liveditor-in-context-sparse-attention.md](inference-efficiency/2026-05-07-liveditor-in-context-sparse-attention.md) | LIVEditor / ISA: in-context sparse attention for ICL video editing; route high-error queries to full attention, low-error to 0-th order Taylor sparse path; ~60% latency reduction |
| [inference-efficiency/2026-05-07-d-opsd-self-distillation-step-distilled-diffusion.md](inference-efficiency/2026-05-07-d-opsd-self-distillation-step-distilled-diffusion.md) | D-OPSD: same model is teacher and student under different conditioning; on-policy self-distillation for step-distilled diffusion fine-tuning; 7th paper in neutral-channel pattern |
| [agentic-systems/2026-05-07-bright-pro-rtriever-reasoning-retrieval.md](agentic-systems/2026-05-07-bright-pro-rtriever-reasoning-retrieval.md) | BRIGHT-Pro / RTriever-4B: first benchmark for evidence-portfolio retrieval rather than top-1 relevance; aspect-decomposed synthetic corpus; Qwen3-Embedding-4B LoRA |
| [agentic-systems/2026-05-07-opensearch-vl-multimodal-search-agents.md](agentic-systems/2026-05-07-opensearch-vl-multimodal-search-agents.md) | OpenSearch-VL: open recipe for frontier multimodal search agents; multi-turn fatal-aware GRPO with one-sided advantage clamping (mask post-failure tokens, preserve pre-failure reasoning) |
| [agentic-systems/2026-05-07-medskillaudit-domain-specific-agent-skill-audit.md](agentic-systems/2026-05-07-medskillaudit-domain-specific-agent-skill-audit.md) | MedSkillAudit: pre-deployment audit of medical research agent skills; 57.3% below Limited Release; negative ICC on Academic Writing reveals rubric-expert mismatch |
| [vision-audio-video/2026-05-07-joyai-image-spatial-intelligence-unified.md](vision-audio-video/2026-05-07-joyai-image-spatial-intelligence-unified.md) | JoyAI-Image: unified MLLM + MMDiT with spatial-intelligence training recipe; bidirectional perception+generation loop |
| [vision-audio-video/2026-05-07-rldx-1-vla-humanoid-manipulation.md](vision-audio-video/2026-05-07-rldx-1-vla-humanoid-manipulation.md) | RLDX-1: Multi-Stream Action Transformer VLA for dexterous humanoid manipulation; 86.8% on ALLEX vs ~40% for pi0.5 / GR00T N1.6 |
| [vision-audio-video/2026-05-07-hermes-plus-plus-driving-world-model.md](vision-audio-video/2026-05-07-hermes-plus-plus-driving-world-model.md) | HERMES++: unified driving world model for 3D scene understanding + future geometry; BEV + LLM-enhanced world queries + Joint Geometric Optimisation |
| [vision-audio-video/2026-05-07-physforge-physics-grounded-3d-assets.md](vision-audio-video/2026-05-07-physforge-physics-grounded-3d-assets.md) | PhysForge: VLM-architects-then-diffusion-realises pipeline; PhysDB 150k assets with four-tier physical annotations; KineVoxel Injection |
| [vision-audio-video/2026-05-07-multi-view-proficiency-estimation.md](vision-audio-video/2026-05-07-multi-view-proficiency-estimation.md) | Multi-view proficiency on Ego-Exo4D: SkillFormer / PATS / ProfVLM; 20x fewer parameters and 3x fewer epochs than video-transformer baselines |
| [vision-audio-video/2026-05-07-apex-ai-music-popularity-prediction.md](vision-audio-video/2026-05-07-apex-ai-music-popularity-prediction.md) | APEX: 211k songs / 10k hours from Suno + Udio; joint popularity + aesthetic quality prediction; AI-music as language-scale training corpus |

## daily-digest (new 2026-05-07)

| Page | Summary |
|------|---------|
| [2026-05-07.md](daily-digest/2026-05/2026-05-07.md) | Daily digest: four papers in one day attack uniform-supervision waste in compressed video diffusion (Stream-R1, Stream-T1, LIVEditor, D-OPSD); Stream-T1 ships the first content-aware KV eviction; OpenSearch-VL adds fatal-aware GRPO; BRIGHT-Pro and OpenSearch-VL together argue evidence-portfolio retrieval; MedSkillAudit shifts evaluation to skill release readiness

## 2026-05-08 ingest

| Topic | Page | Summary |
|-------|------|---------|
| llms-foundation-models | [ResRL: Negative Sample Projection Residual RL](llms-foundation-models/2026-05-08-resrl-negative-sample-projection-rl.md) | Fixes RLVR diversity-collapse via SVD-projection of negative-token hidden states onto positive subspace. +9.4% Avg@16 on math. From Meituan + Chinese Academy of Sciences. Tier 2. |
| responsible-ai | [First Token Knows: Hallucination Detection](responsible-ai/2026-05-08-first-token-knows-hallucination-detection.md) | Single-decode first-token entropy matches semantic self-consistency at 1/11 cost. AUROC 0.820 vs 0.793 across 3 7-8B models. Tier 2. |
| llms-foundation-models | [SxS: Disclosure Policies for LLM Reasoning](llms-foundation-models/2026-05-08-sxs-disclosure-policies-llm-reasoning.md) | Disclosure-as-learnable-action for streaming LLM reasoning. Decouples state-update from public commitment in single-stream autoregressive generation. Tier 2. |
| ai-industry | [Lambert: Notes from inside China's AI labs](ai-industry/2026-05-08-lambert-china-ai-labs.md) | Six labs, 36 hours. Build-not-buy, Claude-pilled-despite-ban, students-as-peers, Nvidia-chip desperation. Direct connection to today's ResRL paper from Meituan. Tier 2 industry essay. |
| ai-industry | [Anthropic ↔ Colossus 1 Deal: Capacity Crunch](ai-industry/2026-05-08-anthropic-colossus-deal-capacity.md) | Triple-source: Pragmatic Engineer (cause), Simon Willison (environmental brand-risk), Lambert (oblique demand evidence). Tier 1 industry. |

| ai-industry | [GitHub Reliability Crisis Under AI Agent-Load](ai-industry/2026-05-08-github-reliability-crisis-ai-load.md) | 86% uptime over 90 days, data-integrity incidents (2,092 PRs lost), Mitchell Hashimoto leaves after 18 years. CTO blames AI agents. Pairs with Anthropic-Colossus as the AI-infrastructure-stress cluster. Tier 1 industry. |
| ai-routing | [Netflix Tech Blog: State of Routing in Model Serving (STUB)](ai-routing/2026-05-08-netflix-state-of-routing-model-serving.md) | Title-level signal only via Gmail Medium digest. Tier 1 stub awaiting body read. |

## 2026-05-09 ingest

| Topic | Page | Summary |
|-------|------|---------|
| inference-efficiency | [UniPool: globally shared MoE expert pool](inference-efficiency/2026-05-09-unipool-shared-expert-pool-moe.md) | Replaces per-layer expert ownership with one global pool accessed by per-layer routers. Pool-level balance loss + NormRouter. Wins across five LLaMA scales 182M to 978M. **Tier 1.** |
| inference-efficiency | [EMO: pretraining MoE for emergent modularity](inference-efficiency/2026-05-09-emo-pretraining-moe-emergent-modularity.md) | Per-document expert pool. 1B active / 14B total, 1T tokens. Retains 25% of experts at 1% drop. Allen AI + Berkeley. **Tier 1.** |
| llms-foundation-models | [TIDE: every layer knows the token (Apple)](llms-foundation-models/2026-05-09-tide-every-layer-knows-token.md) | EmbeddingMemory injects K small token-specific blocks at every layer. Fixes Rare Token Problem and Contextual Collapse Problem. **Tier 1 architecture.** |
| hardware | [KernelBench-X: LLM-generated GPU kernel benchmark](hardware/2026-05-09-kernelbench-x-llm-gpu-kernel-benchmark.md) | 176 tasks, 15 categories. Quantization 0/30. Fusion 28%. Iteration improves correctness not performance. Category dominates method 3x. **Tier 1.** |
| inference-efficiency | [MiA-Signature: long-context activation compression](inference-efficiency/2026-05-09-mia-signature-long-context-activation.md) | Submodular concept signature approximates global activation pattern. Drops into RAG and agentic systems. **Tier 1 long-context.** |
| agentic-systems | [DCI: Direct Corpus Interaction (no retriever)](agentic-systems/2026-05-09-dci-direct-corpus-interaction.md) | Replaces RAG with grep on raw corpus. Sonnet 4.6 jumps 69→80 on BrowseComp-Plus, $424 cheaper. Repost-amplified. **Tier 2.** |
| agentic-systems | [Skill curation cluster: StraTA + Skill1 + SkillOS](agentic-systems/2026-05-09-skill-curation-cluster-strata-skill1-skillos.md) | Three papers same day at three layers of the persistent-skill-memory stack. Six papers in three weeks total. Pattern settled. **Tier 2.** |
| llms-foundation-models | [Prescriptive Scaling Laws for Data Constrained Training](llms-foundation-models/2026-05-09-prescriptive-scaling-laws-data-constrained.md) | Extends Chinchilla with additive overfitting penalty. Past saturation, scale capacity not data. Strong weight decay (lambda=1.0) cuts overfitting 70%. **Tier 2.** |
| llms-foundation-models | [Balanced Aggregation: GRPO aggregation-bias fix](llms-foundation-models/2026-05-09-balanced-aggregation-grpo.md) | Drop-in replacement for sequence/token aggregation in GRPO. Composes with ResRL. **Tier 2.** |
| agentic-systems | [AI Co-Mathematician: 48% on FrontierMath Tier 4](agentic-systems/2026-05-09-ai-co-mathematician.md) | Asynchronous stateful workspace, tracked failed hypotheses, native math artifacts. Same architecture as Anthropic Dreaming. **Tier 2.** |
| agentic-systems | [Auto Research with Specialist Agents](agentic-systems/2026-05-09-auto-research-specialist-agents.md) | Closed-loop empirical training-recipe search, no human in loop. +38.7% NanoChat-D12 CORE. **Tier 2.** |
| responsible-ai | [Anthropic Natural Language Autoencoders](responsible-ai/2026-05-09-anthropic-natural-language-autoencoders.md) | Translates Claude's activations to readable text. Models recognize evaluations and deceive without showing it in CoT. Activation-level audit. **Tier 2.** |
| daily-digest | [2026-05-09](daily-digest/2026-05/2026-05-09.md) | MoE convergence (UniPool + EMO same day, opposite directions on per-layer ownership). Apple TIDE rejects single-injection assumption. KernelBench-X 0/30 quantization. Skill cluster six-of-six. NLAs reveal CoT-fake-reasoning. |
| social-stream | [2026-05-09 morning](social-stream/2026-05/2026-05-09-morning.md) | Claude Code workflow cluster (4 posts). DCI repost-amplified. NLAs cluster. ASI-Arch autonomous architecture discovery. NVIDIA + Unsloth fine-tuning optimizations. |

## 2026-05-10 ingest

| Topic | Page | Summary |
|-------|------|---------|
| llms-foundation-models | [Gowers + ChatGPT 5.5 Pro: PhD-level math research](llms-foundation-models/2026-05-10-gowers-gpt55-pro-math.md) | Fields Medalist Timothy Gowers gave ChatGPT 5.5 Pro an open number-theory problem; in under an hour the model improved an exponential bound to a polynomial one. MIT collaborator called the central idea "completely original." **Tier 2.** |
| agentic-systems | [Jiayi Weng — Learning Beyond Gradients](agentic-systems/2026-05-10-jiayi-weng-learning-beyond-gradients.md) | Codex iterates a NumPy + cv2 heuristic VizDoom policy with no neural net training. Frames iterated heuristic learning as a candidate next paradigm after pretraining and RL. Amplified as "bearish on RL." **Tier 2.** |
| ai-industry | [Broadcom won't build OpenAI's chip without Microsoft 40%](ai-industry/2026-05-10-broadcom-openai-microsoft-chip.md) | $18B phase 1 stalled until Microsoft anchors 40% of orders. Capacity-binding-constraint thread now includes silicon-vendor financing. |
| responsible-ai | [Pseudoscientific emotion AI in the workplace (Atlantic)](responsible-ai/2026-05-10-emotion-ai-workplace-atlantic.md) | Ellen Cushing's Atlantic feature surfaces workplace emotion-detection AI deploying ahead of validation. EU AI Act restricts it; US has no equivalent. **Tier 2.** |
| agentic-systems | [OncoAgent: dual-tier multi-agent oncology framework](agentic-systems/2026-05-10-oncoagent-multi-agent-oncology.md) | Hackathon-origin privacy-preserving oncology system. Dual-tier (sensitive data isolated from agent reasoning) matches the DeepMind co-clinician Talker+Planner pattern. Tier 3 quick hit. |
| daily-digest | [2026-05-10](daily-digest/2026-05/2026-05-10.md) | Consolidation day: HF re-listed yesterday's 38 papers. Two non-paper items push back on the RL substrate from different angles (Gowers single-shot research math, Weng iterated heuristic learning). Capacity-binding industry thread continues with Broadcom-OpenAI-Microsoft. |
| social-stream | [2026-05-10 morning slot](social-stream/2026-05/2026-05-10-morning.md) | Near-empty slot. 2 tweets total, 0 retweets. Single substantive item: @MillionInt amplifying Jiayi Weng's "Learning Beyond Gradients" blog. |

## 2026-05-11 ingest

| Topic | Page | Summary |
|-------|------|---------|
| inference-efficiency | [MISA: Mixture of Indexer Sparse Attention](inference-efficiency/2026-05-11-misa-mixture-of-indexer-sparse-attention.md) | Treats DSA's 64 indexer heads as an MoE pool, routes h=8 active heads per query via block-level statistics. 3.82x kernel speedup over DSA on H200, 92 percent of selected tokens recovered. First head-axis routing in sparse attention. **Tier 1.** |
| inference-efficiency | [UniPrefill: universal prefill acceleration](inference-efficiency/2026-05-11-uniprefill-universal-prefill-acceleration.md) | Architecture-agnostic block-wise dynamic sparsification, ships as vLLM continuous-batching operator with prefill-decode co-processing and tensor parallel. 2.1x TTFT, speedup grows with concurrency. Works on hybrids where prior sparse prefill degrades. **Tier 1.** |
| inference-efficiency | [MDN: Momentum DeltaNet](inference-efficiency/2026-05-11-mdn-momentum-deltanet-linear-attention.md) | Parallelizes stepwise momentum for linear attention via geometric reordering of update coefficients. Spectral analysis constrains gating for stability. Beats Transformer / Mamba2 / GDN at 400M and 1.3B. First substrate-level update to linear attention recurrent rule the wiki has tracked. **Tier 1.** |
| ai-routing | [Conductor (Sakana ICLR 2026)](ai-routing/2026-05-11-conductor-sakana-orchestrating-frontier-models.md) | 7B RL policy orchestrates GPT-5 / Claude Sonnet 4 / Gemini 2.5 Pro at ~3 calls per question, beats every individual frontier model on GPQA-D, LiveCodeBench, AIME25. Recursive topologies emerge on self-call. **Cross-source confirmed (DAIR.AI + Twitter retweet)**. **Tier 1.** |
| ai-routing | [CaRE: Bi-Level Routing MoE](ai-routing/2026-05-11-care-bi-level-routing-moe-continual-learning.md) | Continual learning to 300+ tasks. Task-router selection stage above expert-routing stage, outputs injected at every intermediate layer. Introduces OmniBenchmark-1K. **Tier 1 task-axis routing.** |
| agentic-systems | [AutoTTS: agentic discovery for test-time scaling](agentic-systems/2026-05-11-autotts-agentic-discovery-test-time-scaling.md) | Controller-synthesis framing for width-depth TTS. Beta parameterization, trajectory cache, trace feedback. Discovers strategies beating hand-tuned baselines in 160 minutes for 39.90 dollars. **Tier 2.** Direct demonstration of Jiayi Weng (05-10) "code-as-policy" framing at frontier-lab scale. |
| daily-digest | [2026-05-11](daily-digest/2026-05/2026-05-11.md) | Routing moved inside the model: MISA (head axis), CaRE (task axis), Sakana Conductor (worker model axis), HeavySkill (skill axis). Four independent observations in 24 hours that the orchestrator should be the model, not the wrapper. The wiki's [LLM Routing](ai-routing/llm-routing.md) concept page goes from 3 axes to 5. |
| social-stream | [2026-05-11 morning slot](social-stream/2026-05/2026-05-11-morning.md) | Sakana Conductor cross-source confirmed (DAIR.AI Gmail + @burkov retweet). Jensen Huang at CMU commencement cluster of 4. @MillionInt clarity-of-writing regression. Six opaque article reposts unresolvable from x.com/i/article/ IDs. |

## 2026-05-12 ingest

| Topic | Page | Summary |
|-------|------|---------|
| inference-efficiency | [Make Each Token Count: learned KV eviction that beats the full cache](inference-efficiency/2026-05-12-make-each-token-count-kv-eviction.md) | Globally calibrated retention gates per cached entry, shared final scoring projection across layers/heads, single unified memory budget across modalities. Surpasses full-cache inference on long-context language, vision-language reasoning, and multi-turn dialogue. First eviction paper to claim eviction *improves* quality rather than approximating the full cache. **Tier 1.** |
| llms-foundation-models | [RLRT (Rebellious Student): reverse-read self-distillation signal](llms-foundation-models/2026-05-12-rebellious-student-rlrt.md) | Reinforces tokens the student discovered without teacher guidance on correct rollouts. Information asymmetry becomes a new RLVR exploration axis. Beats self-distillation and exploration baselines on Qwen3 checkpoints. **Tier 2.** |
| llms-foundation-models | [G-Zero: verifier-free self-play via Hint-delta](llms-foundation-models/2026-05-12-g-zero-verifier-free-self-play.md) | Intrinsic reward = predictive shift between unhinted and hinted responses. Proposer (GRPO) finds blind spots, Generator (DPO) internalizes hint-guided improvements. Best-iterate suboptimality bound for verifier-free open-ended generation. **Tier 2.** |
| llms-foundation-models | [Geometry Conflict: explaining and controlling forgetting](llms-foundation-models/2026-05-12-geometry-conflict-continual-post-training.md) | Forgetting = state-relative update-integration failure when new task's covariance geometry misaligns with model state. GCWM (Geometry-Conflict Wasserstein Merging) is data-free, beats baselines on Qwen3 0.6B-14B. Microscopic mechanism behind the macroscopic 1/k merging law. **Tier 2.** |
| llms-foundation-models | [Model Merging Scaling Laws](llms-foundation-models/2026-05-12-model-merging-scaling-laws.md) | Compact power law: size-dependent floor decreases with model capacity, merging tail decays as ~1/k in number of experts. Holds across Average / TA / TIES / DARE. Makes merging a predictable, budget-aware alternative to multitask fine-tuning. **Tier 2.** |
| llms-foundation-models | [Soohak: mathematician-curated research-math benchmark](llms-foundation-models/2026-05-12-soohak-research-math-benchmark.md) | 439 problems by 64 mathematicians. Frontier ceiling ~30% on Challenge subset (Gemini-3-Pro 30.4%, GPT-5 26.4%, Claude-Opus-4.5 10.4%). Refusal subset caps every model under 50%, identifying calibrated abstention as a new training target. **Tier 2.** |
| vision-audio-video | [Auto-Rubric as Reward (ARR)](vision-audio-video/2026-05-12-auto-rubric-as-reward-arr.md) | Externalizes VLM preferences as prompt-specific rubrics upstream of policy training; Rubric Policy Optimization (RPO) distills to binary reward. Beats pairwise RMs and VLM judges on text-to-image and image editing. **Tier 2.** |
| vision-audio-video | [DeltaRubric: plan-and-execute multimodal reward modeling](vision-audio-video/2026-05-12-delta-rubric.md) | Single MLLM acts as Disagreement Planner then Checklist Verifier. Multi-role RL training. +22.6 / +18.8 points on VL-RewardBench (Qwen3-VL 4B/8B). **Tier 2.** |
| vision-audio-video | [ROMA: reinforcing multimodal reasoning against visual degradation](vision-audio-video/2026-05-12-roma-visual-degradation.md) | Dual-forward-pass strategy plus correctness-conditioned regularization to avoid reward poisoning from corrupted views. +2.4% on seen and +2.3% on unseen corruptions over GRPO on Qwen3-VL. **Tier 2.** |
| agentic-systems | [X-OmniClaw: Android-native unified mobile agent](agentic-systems/2026-05-12-x-omniclaw-mobile-agent.md) | Hybrid XML-plus-visual grounding, working + long-term personal memory, behavior-cloned skill traces. Mobile-agent architectural blueprint. **Tier 2.** |
| daily-digest | [2026-05-12](daily-digest/2026-05/2026-05-12.md) | "Concentrate the budget where the signal lives" extends from training (TIP, LongAct, RLRT, G-Zero) to inference (Make Each Token Count) to merging (Geometry Conflict + Scaling Laws). Multimodal RM rubric pattern hits four papers in three weeks. Soohak operationalizes the over-confidence critique. Baidu Ernie 5.1 at 6% pre-training cost is the Chinese training-economics signal. |
| social-stream | [2026-05-12 morning slot](social-stream/2026-05/2026-05-12-morning.md) | Quiet slot. No @bayesiansapien retweets. @bcherny on Cowork + Opus 4.7 one-shotting flight booking (cluster of 2). Claude Code agent view research preview. AWS announces Claude Platform GA. NVIDIA-Dell Las Vegas keynote cluster. |

## 2026-05-13 ingest (backfill)

| Topic | Page | Summary |
|-------|------|---------|
| inference-efficiency | [Sparse-to-Dense Reward Principle](inference-efficiency/2026-05-13-sparse-to-dense-reward-principle.md) | GRPO and OPD are two reward-density regimes, not separate recipes. Allocation rule: spend scarce labels on the strongest teacher via sparse RL first, bridge to the student via forward-KL + OPD, then student-side GRPO. 1.7B Qwen3 bridged from RL-improved 8B teacher beats direct GRPO on same student. **Tier 1.** |
| inference-efficiency | [The Many Faces of On-Policy Distillation](inference-efficiency/2026-05-13-many-faces-on-policy-distillation.md) | Three named OPD failure modes: prefix-induced distribution mismatch, biased TopK reverse-KL gradients, OPSD aggregation collapse when privileged information is instance-specific. OPSD works only when privileged information is a shared latent rule. **Tier 1.** |
| inference-efficiency | [Token Superposition Training (TST)](inference-efficiency/2026-05-13-token-superposition-training.md) | Pre-train with bag-of-tokens MCE objective in superposition phase, recover to standard NTP. 2.5x training-time reduction at 10B-A1B MoE. Deployed model identical to standard NTP baseline. No changes to parallelism/optimizer/tokenizer/data/architecture. **Tier 1.** |
| inference-efficiency | [δ-mem: compact online associative state](inference-efficiency/2026-05-13-delta-mem-online-memory.md) | 8x8 online state, delta-rule updated, produces low-rank corrections to frozen full-attention backbone. 1.10x average gain, 1.31x on MemoryAgentBench, 1.20x on LoCoMo. No fine-tuning, no context extension. **Tier 1.** |
| inference-efficiency | [FocuSFT: dilution-aware long-context fine-tuning](inference-efficiency/2026-05-13-focusft-dilution-aware-long-context.md) | Attention sinks are a training-side phenomenon. Bilevel optimization with bidirectional context and causal response masking. +14 pts on BABILong, 529x attention-sink-mass reduction, 3x context engagement. Training-side complement to Make Each Token Count. **Tier 1.** |
| llms-foundation-models | [Reward Hacking in Rubric-Based RL](llms-foundation-models/2026-05-13-reward-hacking-rubric-based-rl.md) | Resolves the 12-May 60-day rubric-overfitting prediction in 24 hours. Three failure modes: compound-criterion partial satisfaction, implicit-as-explicit, imprecise topical matching. Self-internalization-gap diagnostic. **Tier 2.** |
| responsible-ai | [Massive Activations ME Layer](responsible-ai/2026-05-13-massive-activations-me-layer.md) | Identifies a single layer in each model family where attention-sink-producing massive activations are born by joint RMSNorm + FFN action. Training-free intervention reduces sink influence and improves instruction-following and math reasoning. **Tier 2.** |
| agentic-systems | [Probe&Prefill: LLM agents already know when to call tools](agentic-systems/2026-05-13-llm-agents-already-know-when-to-call-tools.md) | Linear probe on pre-generation hidden state predicts tool necessity at AUROC 0.89-0.96, exceeds verbalized reasoning. 48% reduction in tool calls at 1.7% accuracy loss via probe-driven response prefilling. **Tier 2.** |
| agentic-systems | [Useful Memories Become Faulty](agentic-systems/2026-05-13-useful-memories-become-faulty.md) | LLM-rewritten agent memory degrades over consecutive consolidations. GPT-5.4 fails on 54% of ARC-AGI problems it had previously solved without memory. Episodic-only retention beats forced consolidation. **Tier 2.** |
| agentic-systems | [LongMemEval-V2: environment-specific agent memory](agentic-systems/2026-05-13-longmemeval-v2.md) | 451 questions, 5 memory abilities, up to 500 trajectories per question. AgentRunbook-C (file-per-trajectory + coding-agent retrieval in sandbox) reaches 72.5% vs 48.5% best RAG baseline. Coding-agent retrieval is the new Pareto front. **Tier 2.** |
| agentic-systems | [Agent-BRACE: decoupling belief from action](agentic-systems/2026-05-13-agent-brace.md) | Belief-state model + policy model trained jointly via RL. Belief is structured set of atomic NL claims with verbalized ordinal certainty labels. +14.5 pp on Qwen2.5-3B at near-constant context length. **Tier 2.** |
| hardware | [SemiAnalysis: Cerebras — Faster Tokens Please](hardware/2026-05-13-semianalysis-cerebras-ipo.md) | Four-article IPO-eve deep dive. Thesis: past a capability threshold developers prefer faster tokens to smarter tokens; SRAM-based machines win on interactivity-per-watt where HBM GPUs cannot. Opus 4.6 Fast (6x price, 2.5x interactivity) is the revealed preference. **Tier 1.** |
| ai-industry | [Recursive emerges from stealth with $650M](ai-industry/2026-05-13-recursive-650m-stealth.md) | Second high-profile RSI lab in two weeks. RSI is a venture-funded category now. Foundational risk per same-day Many Faces paper: OPSD-style self-improvement works only when privileged information is a shared latent rule. **Tier 2.** |
| ai-industry | [Anthropic overtakes OpenAI in B2B](ai-industry/2026-05-13-anthropic-overtakes-openai-b2b.md) | 34.4% vs 32.3% Ramp AI Index. Anthropic quadrupled in one year. Same-day Claude for Small Business launch with 15 agentic workflows. Deployment-services week across Anthropic, OpenAI, Google. **Tier 2.** |
| daily-digest | [2026-05-13](daily-digest/2026-05/2026-05-13.md) | On-policy distillation gets a theory (Sparse-to-Dense allocation + Many Faces failure taxonomy) on the same day SemiAnalysis prices the fast-tokens economy. FocuSFT + Massive Activations ME Layer + Make Each Token Count = top-to-bottom attention-sink story. Reward Hacking in Rubric RL resolves the 12-May rubric prediction in 24 hours. Anthropic leads OpenAI in B2B for the first time. |

## 2026-05-14 ingest

| Topic | Page | Summary |
|-------|------|---------|
| inference-efficiency | [MinT: million-scale LoRA serving over 1T-class base](inference-efficiency/2026-05-14-mint-million-scale-lora-serving.md) | Managed infrastructure for LoRA RL post-training and serving. 18.3x step reduction via adapter-only handoff on 4B dense, 2.85x on 30B MoE. 1.77x wall-time via concurrent multi-policy GRPO. 10^6-scale addressable adapter catalog. The catalog axis is now its own routing surface. **Tier 1.** |
| inference-efficiency | [Orthrus: dual-view AR+diffusion on shared KV cache](inference-efficiency/2026-05-14-orthrus-dual-view-diffusion-ar.md) | AR head and diffusion head share one KV cache via exact-consensus mechanism. Output bit-identical to AR baseline. 7.8x speedup with O(1) memory cache overhead. First lossless parallel-decoding architecture in the wiki with structurally O(1) verification cost. **Tier 1.** |
| inference-efficiency | [The Extrapolation Cliff in on-policy distillation](inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md) | Closed-form clip-safety threshold λ-star(p, b, c) for OPD with structured outputs. Three pre-registered tests on Amazon Fashion hit locked prediction windows. ListOPD brings 1.7B Qwen3 to in-domain parity with 8B-SFT at one-fifth params. First closed-form λ-bound on OPD. **Tier 1.** |
| inference-efficiency | [MMProLong: long-context VLM training recipe](inference-efficiency/2026-05-14-mmprolong-long-context-vlm.md) | 7B Qwen2.5-VL extended 32K → 128K with 5B tokens; generalizes to 256K and 512K beyond training. Long-document VQA > OCR; balanced length distribution beats target-length; retrieval is the bottleneck. Training-side complement to Make-Each-Token-Count. **Tier 2.** |
| hardware | [Position: LLM inference is energy-to-token production](hardware/2026-05-14-energy-to-token-position-paper.md) | Token Production Function bounded by both compute-per-token and energy-per-token ceilings. First arXiv-side framing in the wiki that formalizes the SemiAnalysis Cerebras / Anthropic Opus 4.6 Fast / Cerebras IPO thesis. Routing-as-energy-allocation is now an open research direction. **Tier 1.** |
| agentic-systems | [DAgger for LLM agents](agentic-systems/2026-05-14-dagger-llm-agents.md) | Re-applies 2011 Ross-Gordon-Bagnell DAgger to multi-turn LM agents. Turn-level interpolation of student and teacher trajectories, supervised teacher labels on on-policy states. +3.9 on SWE-bench Verified at 4B (27.3% beats published 8B SWE-agents). **Tier 2.** |
| agentic-systems | [AgentLens: 10.7% of passing SWE-bench Verified trajectories are Lucky](agentic-systems/2026-05-14-agentlens-lucky-pass-swe-eval.md) | Prefix Tree Acceptor reference space per task + context-sensitive intent-stage labeler (Exploration / Implementation / Verification / Orchestration). Some models drop 5 ranking positions when scored by quality vs pass rate. AgentLens-Bench: 1,815 trajectories from 47 tasks. **Tier 2.** |
| agentic-systems | [MAP (Map-then-Act): cognitive-map paradigm for long-horizon agents](agentic-systems/2026-05-14-map-then-act-paradigm.md) | Build environment prior first (Global Exploration → Task-Specific Mapping → Knowledge-Augmented Execution). Frontier models surpass near-zero ARC-AGI-3 baselines in 22 of 25 game environments. Training on map-then-act trajectories beats expert execution traces. **Tier 2.** |
| agentic-systems | [Context Training with Active Information Seeking](agentic-systems/2026-05-14-context-training-active-info-seeking.md) | Adds Wikipedia + browser tools to context optimizers. Naive integration degrades performance; recovery is a search-based procedure that maintains and prunes multiple candidate contexts. Generated contexts transfer across models. **Tier 2.** |
| llms-foundation-models | [Many-Shot CoT-ICL: long context as structured curriculum](llms-foundation-models/2026-05-14-many-shot-cot-icl.md) | Setting-dependent scaling (helps reasoning models, fails on non-reasoning). Similarity-based retrieval fails on reasoning. Curvilinear Demonstration Selection (CDS) gives up to +5.42 pp on geometry with 64 demos. Long context is a structured curriculum, not a retrieval buffer. **Tier 2.** |
| responsible-ai | [WriteSAE: SAE for the matrix-recurrent cache write](responsible-ai/2026-05-14-writesae-sae-recurrent-state.md) | First SAE that reaches state-space and hybrid models (Mamba-2, Gated DeltaNet, RWKV-7). Atoms in native rank-1 outer-product shape, closed-form per-token logit shift (R² = 0.98). Sustained three-position installs lift mid-rank target-in-continuation from 33.3% to 100%. First behavioral install at the matrix-recurrent write site. **Tier 2.** |
| daily-digest | [2026-05-14](daily-digest/2026-05/2026-05-14.md) | "Where does the routing decision live": MinT at the adapter catalog, Orthrus at the KV cache, Extrapolation Cliff at the distillation loss. Energy-to-Token formalizes the SemiAnalysis Cerebras empirical thesis. Agentic-stack triangle: AgentLens measures, DAgger fixes training, MAP fixes architecture. Benchmark over-aggregation thread: Soohak + AgentLens + AssetOps + Pangram in three days. |
| social-stream | [2026-05-14 morning slot](social-stream/2026-05/2026-05-14-morning.md) | δ-mem cluster of 2 (HuggingPapers + dair_ai). AutoTTS amplification cluster of 2. Bystander Effect process-failure paper. Lighthouse Attention + Token Superposition Training: three papers in a week on "asymmetric training, identical inference." Refusal-neurons MLP-bypass tweet. NVIDIA + SAP OpenShell + Snap GPU pipelines. Anthropic Mythos/Glasswing cyber-eval results. |

## 2026-05-15 ingest

| Topic | Page | Summary |
|-------|------|---------|
| ai-routing | [RouteProfile: design space of LLM profiles for routing](ai-routing/2026-05-15-routeprofile-llm-profile-design-space.md) | 4-dimensional profile design space (organizational form, representation type, aggregation depth, learning config). Structured > flat, query-level > domain-level, structured+trainable wins on new-model generalization. The routing decision was the wrong unit of analysis; the profile is. **Tier 1.** |
| ai-routing | [Dynamic Latent Routing (DLR) for LM post-training](ai-routing/2026-05-15-dlr-dynamic-latent-routing-post-training.md) | Joint learning of discrete latent codes, routing policies, and model parameters in one stage. Motivated by General Dijkstra Search theorem on temporal sub-policy composition. +6.6 pp over SFT in low-data fine-tuning across 4 datasets, 6 models. Learned codes have distinct causal roles. **Tier 1.** |
| inference-efficiency | [Forcing-KV: head-role-conditioned KV compression for AR video diffusion](inference-efficiency/2026-05-15-forcing-kv-video-diffusion-kv-cache-compression.md) | Static heads vs dynamic heads as a stable functional split across samples and denoising steps. Structured pruning for static, segment-similarity pruning for dynamic. 29+ fps on H200 at 30% memory reduction, 1.35x-1.50x speedup at 480P, 2.82x at 1080P. **Tier 1.** |
| inference-efficiency | [Asynchronous continuous batching: CPU-GPU overlap](inference-efficiency/2026-05-15-async-continuous-batching-cpu-gpu-overlap.md) | HF transformers continuous-batching now ships async overlap via 3 CUDA streams + 2 buffer slots + carry-over mask. GPU utilization 76.0% → 99.4%, 22% generation speedup on 8B at batch 32. No new kernels, no model changes. **Tier 1.** |
| agentic-systems | [Agent memory cluster: STALE + Preping + EvolveMem + MemEye + MemLens + BOOKMARKS](agentic-systems/2026-05-15-agent-memory-cluster-stale-preping-evolvemem.md) | Six papers in one day. STALE caps best frontier at 55.2% on implicit-conflict detection. MemLens caps multi-session multimodal below 30%. EvolveMem self-evolves retrieval config (+25.7% on LoCoMo). Preping pre-task memory at 2-3x lower deployment cost. The memory layer is now a programmable substrate. **Tier 2 cluster.** |
| agentic-systems | [agent-memory.md (new concept page)](agentic-systems/agent-memory.md) | First-class concept page for agent memory. Tracks storage substrate, retrieval mechanism, write-time policy, staleness handling, visual fidelity as architectural axes. Open problems: implicit-conflict detection, multi-session multimodal, cold-start cost. |
| agentic-systems | [WildClawBench: native-runtime long-horizon agent benchmark](agentic-systems/2026-05-15-wildclawbench-native-runtime-agent-benchmark.md) | 60 native-runtime tasks, 8 min wall-clock + 20+ tool calls each, hybrid grading (deterministic + state audit + LLM/VLM judge). Claude Opus 4.7 caps at 62.2%. Switching harness alone shifts a single model by 18 points. The harness is the load-bearing layer. **Tier 2.** |
| agentic-systems | [Orchard: open-source agentic modeling framework](agentic-systems/2026-05-15-orchard-open-source-agentic-framework.md) | Kubernetes-native environment service + three recipes (SWE, GUI, Claw). Orchard-SWE on Qwen3-30B-A3B-Thinking: 64.3% SFT → 67.5% SFT+RL on SWE-bench Verified, open-source SOTA at 30B. Credit-assignment SFT learns from productive segments of unresolved trajectories. **Tier 2.** |
| agentic-systems | [SDAR: self-distilled agentic RL](agentic-systems/2026-05-15-sdar-self-distilled-agentic-rl.md) | Gated OPSD as auxiliary; RL primary backbone. Sigmoid gate over detached token-level signals strengthens distillation on teacher-endorsed positive-gap tokens. +9.4% ALFWorld, +7.0% Search-QA, +10.2% WebShop-Acc over GRPO. Avoids naive GRPO+OPSD instability. **Tier 2.** |
| agentic-systems | [EvoEnv: self-evolving RL via verifiable environment synthesis](agentic-systems/2026-05-15-evoenv-self-evolving-rl-via-environment-synthesis.md) | Construct environments, not data. Solve-verify asymmetry as the structural invariant. On already-strong Qwen3-4B-Thinking: fixed-data RLVR reduces score, EvoEnv improves 72.4 → 74.8. Stable self-improvement in the strong regime. **Tier 2.** |
| llms-foundation-models | [SU-01: gold-medal olympiad reasoning at 30B via simple recipe](llms-foundation-models/2026-05-15-su-01-gold-olympiad-reasoning-30b.md) | 30B-A3B + reverse-perplexity SFT + two-stage RL + TTS + only 200 RL steps. Gold IMO 2025 (35 pts), USAMO 2026 (35 pts, 10 above gold), IPhO 2024/2025. 57.6% IMO-ProofBench direct, 70.2% with TTS. Specializable-generalist framing's first frontier-tier datapoint. **Tier 2.** |
| llms-foundation-models | [Darwin Family: training-free evolutionary merging](llms-foundation-models/2026-05-15-darwin-family-evolutionary-merging.md) | 14-D merge genome + MRI-Trust Fusion + Architecture Mapper (cross-arch Transformer + Mamba). Darwin-27B-Opus: 86.9% GPQA Diamond, rank #6 of 1,252 models, no gradient training. Recursive multi-generation evolution supported. **Tier 2.** |
| daily-digest | [2026-05-15](daily-digest/2026-05/2026-05-15.md) | Six papers on agent memory as a programmable substrate (STALE 55.2%, MemLens <30%, EvolveMem +25.7%). RouteProfile + DLR open routing on two new axes (profile design, training-time latent routing). Forcing-KV + async continuous batching: inference stack updates with no model changes. WildClawBench caps Claude Opus 4.7 at 62.2%, 18-point harness sensitivity. SU-01 gold-medal IMO at 30B with 200 RL steps. Darwin training-free GPQA #6. |
| social-stream | [2026-05-15 morning slot](social-stream/2026-05/2026-05-15-morning.md) | xAI Grok Build CLI launch (cluster of 4 — @xai mainline + @JasonBud + @milichab). Early-beta agentic CLI with subagents, plan mode, /imagine, /imagine-video. The fifth-frontier-lab CLI in the harness-as-load-bearing thread that today's WildClawBench formalizes. NVIDIA Jensen CMU commencement, Lex Fridman China travel announcement, marketing noise (Tesla, Intel × McLaren). No @bayesiansapien retweets. |

## 2026-05-16 ingest

| Topic | Page | Summary |
|-------|------|---------|
| inference-efficiency | [Lighthouse Attention: training-only long-context pre-training wrapper](inference-efficiency/2026-05-16-lighthouse-attention-long-context-pretraining.md) | Nous Research's symmetric-pyramid pooling of Q/K/V with gradient-free top-k cascade. Kernel-decoupled: reuses standard FlashAttention. Two-stage training with short recovery phase removes wrapper. 1.4-1.7x at 98K context, ~17x forward+backward at 512K on a single B200. Open-source counterpart to Subquadratic's Appen numbers. **Tier 1.** |
| ai-routing | [BEAM: binary expert activation masking for dynamic MoE routing](ai-routing/2026-05-16-beam-binary-expert-activation-masking-moe.md) | Token-adaptive trainable binary masks over experts learned end-to-end via STE plus auxiliary regularization. Custom vLLM kernel ships with the paper. >98% retention, up to 85% MoE-FLOP reduction, 2.5x decoding, 1.4x throughput. Routing now has seven internal addressable layers. **Tier 1.** |
| inference-efficiency | [ATESD: adaptive teacher exposure for self-distillation](inference-efficiency/2026-05-16-atesd-adaptive-teacher-exposure-self-distillation.md) | Teacher exposure becomes a learnable Beta-policy control variable with discounted learning-progress reward. +0.95 / +2.05 / +2.33 Average@12 over OPSD on Qwen3-{1.7B,4B,8B} across AIME 24/25 and HMMT 25. Third axis of teacher-signal control after Extrapolation Cliff (branch) and SDAR (student-gating). **Tier 1.** |
| responsible-ai | [LiSA: lifelong safety adaptation via conservative policy induction](responsible-ai/2026-05-16-lisa-lifelong-safety-adaptation.md) | Memory-augmented guardrail adaptation with posterior-lower-bound gating to prevent overgeneralization. Conflict-aware local rules. Robust at 20% label-flip noise. Pushes latency-performance frontier beyond backbone scaling on PrivacyLens+, ConFaide+, AgentHarm. Safety-side analogue of EvolveMem. **Tier 2.** |
| agentic-systems | [FrontierSmith: synthesizing open-ended coding problems at scale](agentic-systems/2026-05-16-frontiersmith-synthetic-open-ended-coding.md) | Mutate competitive-programming seeds into open-ended variants; idea-divergence metric prunes mode-collapse cases; agents generate tests and verifiers. Qwen3.5-9B: +8.82 FrontierCS, +306.36 ALE-bench Elo. Third self-substrate-synthesis paper this week after EvoEnv and EvolveMem. **Tier 2.** |
| agentic-systems | [SPIN: structural LLM planning via DAG validation and prefix-stop](agentic-systems/2026-05-16-spin-dag-planning-wrapper.md) | DAG contract + repair prompting before execution; incremental prefix evaluation stops when answer is sufficient. AssetOpsBench: 1061 → 623 executed tasks, Accomplished 0.638 → 0.706, tool calls 11.81 → 6.82 per run. First wrapper to improve the benchmark that surfaced the -0.13 measurement crisis. **Tier 2.** |
| daily-digest | [2026-05-16](daily-digest/2026-05/2026-05-16.md) | Three Tier 1 papers reform uniform defaults: Lighthouse (pre-training attention), BEAM (MoE expert masks), ATESD (teacher exposure). The uniform-default-reform thread now spans eight axes in two months. Subquadratic-train + dense-deploy cross-source confirmed (Subquadratic + Lighthouse). Self-substrate-synthesis is a three-paper cluster (FrontierSmith + EvoEnv + EvolveMem). Industry: Anthropic at $900B above OpenAI, Microsoft pulls Claude Code licenses, OpenAI Codex mobile, Anthropic-Gates $200M. |
| social-stream | [2026-05-16 morning slot](social-stream/2026-05/2026-05-16-morning.md) | Strongest retweet batch in a week (14 retweets). Mech-interpretability cluster of 2 (circuit non-uniqueness). Direct Lighthouse Attention amplification from @NousResearch. Is Grep All You Need? (harness > embeddings). Stanford-OpenAI-DeepMind-Anthropic automating-AI-R&D paper. Anthropic 2028 policy + Bill Gurley on open-source-as-strategy. Sylph AI harness evolution loop. LIFE multi-agent survey. |

## 2026-05-17 ingest

| Topic | Page | Summary |
|-------|------|---------|
| ai-routing | [MoE-muP: maximally scale-stable parameterization for Mixture-of-Experts](ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md) | Vankadara et al. (Gatsby UCL, Amazon, Tübingen). First principled scaling theory for MoE. Closed-form MSSP across M (experts), Ne (expert width), K (sparsity), N (width), L (depth). Covers SGD, Adam, Adafactor. Identifies muP failure modes inside MoE and the non-commutative co-scaling space. Kurate cs.LG #13 with ai_rating 9.0/10. **Tier 1.** |
| inference-efficiency | [Raschka architecture survey: KV sharing, mHC, compressed attention](inference-efficiency/2026-05-17-raschka-llm-architecture-kv-sharing-mhc-compressed-attention.md) | Sebastian Raschka catalog of four moves in May 2026 open-model wave: Gemma 4 cross-layer KV sharing plus per-layer embeddings; Laguna XS.2 layer-wise attention budgeting; ZAYA1-8B compressed convolutional attention; DeepSeek V4 mHC plus compressed attention. All long-context efficiency. **Tier 1.** |
| inference-efficiency | [MTP merges into llama.cpp: Strix Halo benchmarks confirm consumer-hardware envelope](inference-efficiency/2026-05-17-mtp-llama-cpp-merge-strix-halo-benchmarks.md) | Multi-Token Prediction in llama.cpp upstream (PR #22673). Qwen3.6-27B 5-turn chat: -22.46% wall-clock, +136% generation throughput. Qwen3.6-35B: total wall-clock regresses ~11% because prompt-processing drops more than generation gains. Crossover sits near 30B. **Tier 1.** |
| ai-industry | [Open Artifacts #21: May 2026 open-model wave + CAISI gap](ai-industry/2026-05-17-open-artifacts-21-may-open-model-wave-caisi.md) | Six frontier-tier open MoEs in two weeks: Gemma 4, Kimi K2.6, GLM-5.1, Qwen3.6, Laguna XS.2, MiMo-V2.5-Pro, DeepSeek V4. Fireworks training-platform additions at 256K context. CAISI IRT-Elo open-closed gap analysis disputed inside Interconnects as harness artifact. **Tier 2.** |
| agentic-systems | [LIFE survey: collaboration, failure attribution, self-evolution in LLM multi-agent systems](agentic-systems/2026-05-17-life-survey-multi-agent-collaboration-failure-self-evolution.md) | 200+ paper survey along four causally linked stages: Lay capability, Integrate collaboration, Find faults via attribution, Evolve via self-improvement. Names error propagation across agents as the central under-examined Stage 3 risk. Unifies five Stage 4 wiki clusters. **Tier 2.** |
| vision-audio-video | [CurveBench: hierarchical topological reasoning from visual input](vision-audio-video/2026-05-17-curvebench-hierarchical-topological-reasoning.md) | 756 nested-Jordan-curve images, rooted containment tree task. Gemini 3.1 Pro 71.1% Easy, 19.1% Hard. RLVR Qwen3-VL-8B: 2.8% to 33.3% on Easy, beats GPT-5.4 and Claude Opus 4.5. Third VLM benchmark this month confirming the structural-representation gap. **Tier 2.** |
| responsible-ai | [LLM-based detection of manipulative political narratives](responsible-ai/2026-05-17-llm-detection-manipulative-political-narratives.md) | LLM-as-labeler plus UMAP plus HDBSCAN pipeline applied to 1.2M social media posts. 41 distinct manipulative-narrative clusters surfaced. Pipeline shape (LLM filter then unsupervised cluster) is now mainstream-published methodology. **Tier 2.** |
| daily-digest | [2026-05-17](daily-digest/2026-05/2026-05-17.md) | HF feed largely re-surfaced 05-16 batch. Tier 1 signal landed elsewhere: MoE-muP from Kurate, Raschka architecture survey from Gmail, MTP-in-llama.cpp from Reddit. LIFE supplies the Stage 4 taxonomy unifying five wiki clusters. CurveBench is third VLM-ceiling-lowering benchmark this month. Six summary pages and one Media Live slot synthesis. |
| social-stream | [2026-05-17 morning slot](social-stream/2026-05/2026-05-17-morning.md) | Quietest morning slot in two weeks. Zero @bayesiansapien retweets, two sparse AI-handle tweets. Only operational signal: @_sholtodouglas (Anthropic) opens DMs for "when do you reach for other models instead of Claude". Net Tier-1 research content extracted: zero. |

## 2026-05-18 ingest

| Topic | Page | Summary |
|-------|------|---------|
| inference-efficiency | [HodgeCover: harmonic-kernel obstructions in learning-free MoE compression](inference-efficiency/2026-05-18-hodgecover-simplicial-laplacian-moe-compression.md) | Names the structural blind spot of every prior pairwise-scoring MoE compressor: three experts can be pairwise mergeable but form an irreducible cycle when merged. Models obstruction as the harmonic kernel of the simplicial Laplacian on a 2-complex of experts. Greedy harmonic coverage wins on the aggressive-compression frontier. **Tier 1.** |
| inference-efficiency | [FashionChameleon: training-free KV cache rescheduling](inference-efficiency/2026-05-18-fashionchameleon-training-free-kv-cache-rescheduling.md) | Three-mechanism rescheduling (garment refresh, historical withdraw, reference disentangle) for interactive multi-condition video. Adds a fourth axis to the KV cache thread alongside learned eviction, head-role compression, architectural sharing. 720p / 23.8 FPS on H200. **Tier 1.** |
| llms-foundation-models | [AIRA-Compose / AIRA-Design: agentic architecture search](llms-foundation-models/2026-05-18-aira-compose-design-agentic-architecture-search.md) | 11 LLM agents in 24-hour search over Attention/MLP/Mamba primitives. 14 novel architectures. AIRAformer-D +2.4% over Llama 3.2, AIRAhybrid-D +3.8%, compute-optimal scaling slope 54% steeper than Llama 3.2 / 71% steeper than best Composer Transformer at 1B. **Tier 2.** |
| llms-foundation-models | [CIPO: correction-oriented policy optimization with verifiable rewards](llms-foundation-models/2026-05-18-cipo-correction-oriented-rlvr.md) | Mines on-policy failed RLVR trajectories and converts them into correction-oriented supervision via the model's own success rollouts. No PRM, no LLM critic. Pass@K gain exceeds pass@1 gain across 11 benchmarks. Cleanest empirical counter yet to the RLVR Weak Supervision 2026-04-21 critique. **Tier 2.** |
| llms-foundation-models | [NudgeRL: strategy-guided exploration for RLVR](llms-foundation-models/2026-05-18-nudgerl-strategy-guided-rlvr.md) | Conditions rollouts on lightweight strategy-level contexts. Inter- and intra-context reward decomposition plus distillation back to base policy. Matches vanilla GRPO at 8x larger rollout budgets across five math benchmarks. Complementary to CIPO. **Tier 2.** |
| agentic-systems | [Solvita: agentic evolution for competitive programming](agentic-systems/2026-05-18-solvita-agentic-evolution-competitive-programming.md) | Four-agent framework (Planner, Solver, Oracle, Hacker) with trainable graph-structured knowledge networks. Hacker constructs adversarial tests as RL signal source. Nearly doubles single-pass accuracy on CodeContests / APPS / live Codeforces. First wiki Stage 4 system with adversarial-test signal. **Tier 2.** |
| agentic-systems | [Look Before You Leap: autonomous exploration for LLM agents](agentic-systems/2026-05-18-look-before-you-leap-explore-then-act.md) | Introduces Exploration Checkpoint Coverage as a verifiable exploration metric independent of task reward. Training interleaves task and exploration rollouts under their own verifiable rewards. Explore-then-Act paradigm. **Tier 2.** |
| agentic-systems | [MMSkills: multimodal skill packages for visual agents](agentic-systems/2026-05-18-mmskills-multimodal-skill-packages-visual-agents.md) | Each MMSkill bundles a textual procedure with runtime state cards and multi-view keyframes. Branch-loaded inference keeps heavy multimodal evidence off the main path. Improves both frontier and smaller multimodal agents on GUI and game benchmarks. **Tier 2.** |
| agentic-systems | [PAGER: bridging the Semantic-Execution Gap in geometric GUI control](agentic-systems/2026-05-18-pager-precision-geometric-gui.md) | PAGE Bench (4,906 problems, 224K pixel-level actions). General multimodal models: 88% action-type accuracy but under 6% task success. PAGER: dependency-structured planning + precision-aligned RL with state-conditioned geometric feedback. 4.1x higher task success. **Tier 2.** |
| responsible-ai | [DiagnosticIQ: LLM deployment calibration bottleneck in industrial maintenance](responsible-ai/2026-05-18-diagnosticiq-industrial-llm-deployment-calibration.md) | 6,690 questions on rule-to-action recommendation. Top three LLMs within one Macro point. 13-60% accuracy drop under distractor expansion. 49-63% of frontier answers persist under condition inversion. Deployment bottleneck is calibration, not capability. **Tier 2.** |
| daily-digest | [2026-05-18](daily-digest/2026-05/2026-05-18.md) | MoE design surface mapped end-to-end in one week: MoE-muP (theory), BEAM (per-token activation), HodgeCover (compression). CIPO and NudgeRL attack RLVR sparse-reward from opposite ends. PAGER + DiagnosticIQ bring deployment-calibration-gap pattern to four confirmations. AIRA shows agents discover scaling-frontier architectures. FashionChameleon adds rescheduling as fourth KV cache axis. |
| social-stream | [2026-05-18 morning slot](social-stream/2026-05/2026-05-18-morning.md) | Empty for second consecutive Monday. Zero retweets, zero articles, two non-AI aphorisms from @MillionInt. No signal to synthesize. |

## 2026-05-19 ingest

| Topic | Page | Summary |
|-------|------|---------|
| inference-efficiency | [CompactAttention: chunked-prefill speedup via Block-Union KV selection](inference-efficiency/2026-05-19-compactattention-chunked-prefill-block-union-kv-selection.md) | Treats 2D block-sparse masks as KV-selection signals, not direct kernel execution plans. Q-block and intra-group GQA unions produce minimal block tables under paged execution. 2.72x attention speedup at 128K on LLaMA-3.1-8B-Instruct with near-dense RULER accuracy. **Tier 1.** |
| inference-efficiency | [EndPrompt: long-context extension from short training sequences](inference-efficiency/2026-05-19-endprompt-terminal-anchoring-long-context-extension.md) | Two-segment construction (short context plus brief terminal prompt with positional indices near target length) injects long-range relative distances without long physical sequences. Beats LongLoRA, LCEG, full-length FT on RULER (76.03 avg) and LongBench. RoPE smoothness + Bernstein inequality grounding. **Tier 1.** |
| inference-efficiency | [SNLP: layer-parallel inference via structured Newton corrections](inference-efficiency/2026-05-19-snlp-layer-parallel-inference-structured-newton.md) | Treats hidden-state trace across layers as nonlinear residual equation. Identity Newton (residual) gives prefix-sum-like update; HC Newton uses mHC residual mixing matrix. SNLP-aware regularization improves baseline PPL by 4.7%-23.4%. 2.3x wall-clock on 0.5B Nanochat at +6.1% PPL. **Tier 1.** |
| inference-efficiency | [PUMA: semantic-preserving early exit for reasoning models](inference-efficiency/2026-05-19-puma-semantic-preserving-early-exit-reasoning.md) | Reasoning-level semantic redundancy as exit signal (versus answer-level signals that exit before reasoning converges). Redundancy Detector + answer verification. 26.2% token reduction at preserved accuracy across five LRMs and five benchmarks. Generalises to code and zero-shot vision-language. **Tier 1.** |
| inference-efficiency | [ZEDA: post-trained MoE can skip half its experts via self-distillation](inference-efficiency/2026-05-19-zeda-post-trained-moe-skip-half-experts.md) | Parameter-free zero-output experts injected per layer. Two-stage self-distillation from frozen original MoE as teacher with group-level balancing loss. 50%+ expert FLOPs eliminated at marginal loss on Qwen3-30B-A3B and GLM-4.7-Flash. Completes the four-axis MoE map (MoE-muP, BEAM, HodgeCover, ZEDA). **Tier 1.** |
| inference-efficiency | [LongLive-2.0: NVFP4 parallel infrastructure for long video generation](inference-efficiency/2026-05-19-longlive-2-nvfp4-parallel-infrastructure-long-video.md) | First wiki paper to operationalise NVFP4 end-to-end across training and inference for a frontier-grade generative model. Balanced SP training, W4A4 NVFP4 inference with NVFP4-quantized KV cache on Blackwell, SP fallback on non-Blackwell. 2.15x training, 1.84x inference, 45.7 FPS at 5B. **Tier 1.** |
| inference-efficiency | [Measuring maximum activations in open LLMs](inference-efficiency/2026-05-19-max-activations-open-llms.md) | Unified measurement across 27 checkpoints from 8 open families. Global maxima span 4 orders of magnitude at comparable parameter counts. MoE checkpoints 14-23x lower peaks than dense counterparts. Residual stream carries the global maximum in 22 of 24 checkpoints. Recommends activation-maxima reporting as release norm before low-bit deployment. **Tier 2.** |
| hardware | [AgentKernelArena: agentic GPU-kernel optimisation benchmark with generalization](hardware/2026-05-19-agentkernelarena-gpu-kernel-optimization-agents-benchmark.md) | 196 tasks across HIP-to-HIP, Triton-to-Triton, PyTorch-to-HIP. Cursor Agent / Claude Code / Codex Agent reach 6.89x / 6.69x / 2.13x mean speedups. HIP and Triton optimisations transfer to unseen shapes; PyTorch-to-HIP exhibits substantial correctness drops on unseen shapes, confirming shape-hardcoding failure mode. **Tier 1.** |
| llms-foundation-models | [MixSD: mixed contextual self-distillation for knowledge injection](llms-foundation-models/2026-05-19-mixsd-mixed-contextual-self-distillation-knowledge-injection.md) | Constructs supervision dynamically by mixing tokens from two base-model conditionals: expert (sees fact in context) and naive (original prior). Up to 100% held-out capability retention at near-perfect training accuracy; SFT retains 1%. Reduces movement along Fisher-sensitive directions. **Tier 2.** |
| llms-foundation-models | [DiHAL: geometry-guided diffusion-transformer hybrid](llms-foundation-models/2026-05-19-dihal-geometry-guided-diffusion-language-model.md) | First principled selection rule in the wiki for where diffusion should enter a pretrained transformer. Geometry score picks layer; diffusion bridge replaces lower prefix; upper layers and LM head retained. Hidden-state recovery avoids continuous-to-discrete loss. **Tier 2.** |
| llms-foundation-models | [NGM: plug-and-play training-free memory module](llms-foundation-models/2026-05-19-ngm-plug-and-play-training-free-memory.md) | Causal N-Gram Encoder averages pretrained token embeddings; Cosine-Gated Memory Injector uses non-parametric cosine gate with ReLU. Zero training. On Qwen3 0.6B to 14B across 8 benchmarks: +0.5 to +1.2 averages, +3.0 LiveCodeBench, +3.03 GPQA for Qwen3-14B. **Tier 2.** |
| responsible-ai | [Monitoring the Internal Monologue: probe trajectories](responsible-ai/2026-05-19-monitoring-internal-monologue-probe-trajectories.md) | Probe at each generated token; trajectory carries more separation signal than any static prediction. Signal-processing features (volatility, trend, steady-state) significantly improve outcome separability. Max-pooling reaches 95% AUROC; average and last-token pooling collapse to near-random. **Tier 2.** |
| agentic-systems | [AI for Auto-Research: roadmap and user guide](agentic-systems/2026-05-19-ai-for-auto-research-roadmap.md) | Four phases (Creation, Writing, Validation, Dissemination). Reliable / unreliable boundary is stage-dependent. Generated ideas degrade after implementation. Research code lags pattern-matching benchmarks. End-to-end autonomous systems have not reached major-venue acceptance. **Tier 2.** |
| daily-digest | [2026-05-19](daily-digest/2026-05/2026-05-19.md) | MoE design surface gets its fourth principled axis (ZEDA); KV-cache thread gets the chunked-prefill specialisation (CompactAttention); SNLP makes the layer-by-layer assumption negotiable; LongLive-2.0 operationalises NVFP4 end-to-end. Deployment-calibration gap crosses five domains with AgentKernelArena. |
| social-stream | [2026-05-19 morning slot](social-stream/2026-05/2026-05-19-morning.md) | Cursor Composer 2.5 ships on Kimi K2.5 with SpaceXAI 10x-compute follow-on training. NVIDIA Vera CPU hand-delivery blog post. Anthropic Claude Code Fast Mode + cache diagnostics + usage credits. Tesla FSD v14.3.3 testimonials. Open Collider creativity engine via @brivael repost of @cdriclion. |

## 2026-05-20 ingest

| Topic | Page | Summary |
|-------|------|---------|
| llms-foundation-models | [AntiSD: anti-self-distillation via PMI divergence ascent](llms-foundation-models/2026-05-20-antisd-anti-self-distillation-pmi-divergence-ascent.md) | PMI analysis traces conditioned-teacher failure to inflated confidence on already-implied tokens and deflated confidence on deliberation tokens. Ascending the KL between student and teacher reverses the per-token sign with naturally bounded advantage. 2-10x fewer steps to GRPO baseline, +11.5 points final accuracy across 4B-30B math. |
| llms-foundation-models | [CEPO: Contrastive Evidence Policy Optimization](llms-foundation-models/2026-05-20-cepo-contrastive-evidence-policy-optimization.md) | RLVR self-distillation that contrasts a correct-answer teacher against a wrong-answer teacher built from rejected rollouts in the same batch. Provable inheritance of safety guarantees, strict sharpening of credit at decisive tokens. 43.43% / 60.56% versus GRPO 41.17% / 57.43% at 2B / 4B on multimodal math. |
| llms-foundation-models | [CopT: Contrastive On-Policy Thinking with continuous spaces](llms-foundation-models/2026-05-20-copt-contrastive-on-policy-thinking-continuous-spaces.md) | Reverses CoT to answer-first then conditional thinking; continuous-versus-discrete embedding contrast as a sequence-level reverse-KL estimator with MI semantics. Up to 23% accuracy lift and 57% token reduction across math, code, agentic reasoning, no training. |
| inference-efficiency | [PEEK: context map as an orientation cache for long-context agents](inference-efficiency/2026-05-20-peek-context-map-orientation-cache.md) | Constant-sized prompt-resident orientation cache for recurring external contexts. Distiller-Cartographer-Evictor pipeline. 6.3-34.0% improvement and 1.7-5.8x lower cost than ACE on long-context reasoning. Generalises to OpenAI Codex. |
| inference-efficiency | [Context Memorization: attention-state external memory](inference-efficiency/2026-05-20-context-memorization-attention-state-memory.md) | Training-free externalisation of long prefix as precomputed Q-K-V interactions with representative queries. Model never attends to prefix at inference. 1.36x attention latency reduction at 8K. Beats full-attention RAG using 20% of its memory. |
| llms-foundation-models | [Delta Attention Residuals](llms-foundation-models/2026-05-20-delta-attention-residuals.md) | Routing attention residuals over sublayer deltas instead of cumulative states fixes deep-layer routing collapse (max weight 0.6 versus 0.2). 1.7-8.2% PPL gains across 220M-7.6B. Pretrained checkpoints can be converted via fine-tuning. |
| inference-efficiency | [Graft: hybrid draft-tree construction for speculative decoding](inference-efficiency/2026-05-20-graft-draft-less-retrieve-more-speculative-decoding.md) | Couples dynamic pruning with retrieval-grafting. Pruning frees budget that funds retrieval-indexed tokens grafted into the topological gaps. Training-free and lossless. Up to 5.41x short-context speedup; 21.8% over EAGLE-3 on Qwen3-235B. |
| agentic-systems | [EnvFactory: scaling tool-use agents via executable environments synthesis](agentic-systems/2026-05-20-envfactory-tool-use-agents-executable-environments.md) | Two-pipeline framework: autonomous environment exploration / verification plus topology-aware trajectory generation with implicit-intent calibration. 85 environments across 7 domains. +15% BFCLv3, +8.6% MCP-Atlas, +6% conversational benchmarks at 5x fewer environments than prior work. |
| agentic-systems | [OpenComputer: verifiable software worlds for computer-use agents](agentic-systems/2026-05-20-opencomputer-verifiable-software-worlds.md) | 33 desktop apps, 1,000 finalized tasks. Hard-coded verifiers beat LLM-as-judge on fine-grained app state. Sixth deployment-calibration benchmark in six days confirming the in-distribution-versus-out-of-distribution capability gap. |
| agentic-systems | [AutoResearchClaw: self-reinforcing autonomous research](agentic-systems/2026-05-20-autoresearchclaw-self-reinforcing-autonomous-research.md) | Multi-agent pipeline with Pivot/Refine self-healing executor and seven human-in-loop intervention modes. Beats AI Scientist v2 by 54.7% on ARC-Bench. Intervention-mode ablation shows U-shaped collaboration optimum: targeted human-in-loop at high-leverage points beats both full autonomy and full step-by-step oversight. |
| llms-foundation-models | [GoLongRL: capability-oriented long-context RLVR](llms-foundation-models/2026-05-20-golongrl-long-context-rlvr.md) | Fully open-source 23K-sample RLVR dataset across 9 task types plus TMN-Reweight for heterogeneous multitask optimization. Qwen3-30B-A3B trained on this data reaches DeepSeek-R1-0528 / Qwen3-235B-A22B-Thinking-class long-context performance. |
| llms-foundation-models | [BetaPRM: process rewards with learned reliability](llms-foundation-models/2026-05-20-process-rewards-learned-reliability-betaprm.md) | Distributional PRM that predicts step-success probability plus prediction reliability via Beta-Binomial likelihood. ACA uses reliability to allocate compute. Up to 33.57% token reduction at improved accuracy over fixed-budget Best-of-16. |
| responsible-ai | [Language-Switching Triggers Take a Latent Detour Through LMs](responsible-ai/2026-05-20-language-switching-backdoor-circuit.md) | Three-phase circuit decomposition of an 8B language-switching backdoor: distributed attention composition, mid-layer propagation in subspace orthogonal to natural language-identity direction, final-MLP conversion to French logits. Probes searching for language-like signals would miss the trigger entirely. |
| daily-digest | [2026-05-20](daily-digest/2026-05/2026-05-20.md) | Reasoning RL credit-assignment surface reworked from three angles (AntiSD, CEPO, CopT). Long-context efficiency stack adds an orientation-cache tier (PEEK) and a prefix attention-state lookup (Context Memorization). Graft pushes speculative-decoding Pareto. Delta Attention Residuals at architecture level. Google I/O 2026 ships three Nature science-AI artifacts. Karpathy joins Anthropic. |
| social-stream | [2026-05-20 morning slot](social-stream/2026-05/2026-05-20-morning.md) | Google I/O 2026 (Co-Scientist, Gemini for Science, ERA in Nature; Gemini 3.5 Flash, Gemini Omni, Gemini Spark; consumption-based subscription tiers). Andrej Karpathy joins Anthropic's pre-training team under Nick Joseph. Cursor Composer 2.5 + CursorBench 3.1 + Jira-native agent surface. SpaceXAI S-1 rumour at $2T valuation. Anthropic computer-use best-practices guide. |

## 2026-05-21 ingest

| Topic | Page | Summary |
|-------|------|---------|
| inference-efficiency | [OScaR: extreme KV cache quantization](inference-efficiency/2026-05-21-oscar-extreme-kv-cache-quantization.md) | Names Token Norm Imbalance as the per-channel quantization failure at INT2. Two-pass fix: Canalized Rotation plus Omni-Token Scaling. 3.0x decode speedup, 5.3x memory reduction over BF16 FlashDecoding-v2. Near-lossless INT2 across text, multimodal, omni-modal. |
| inference-efficiency | [OCTOPUS: octahedral triplet KV codec](inference-efficiency/2026-05-21-octopus-octahedral-kv-cache-codec.md) | Stability AI. Joint triplet quantization via octahedral parametrization of S^2; non-uniform bit allocation between direction and norm. Matches or beats every prior rotation codec (TurboQuant, PolarQuant, QJL) at every reported bit width. Data-oblivious, fused Triton implementation. |
| inference-efficiency | [Mix-Quant: phase-aware NVFP4 for agentic LLMs](inference-efficiency/2026-05-21-mix-quant-phase-aware-quantization.md) | NVFP4 for compute-intensive prefill, BF16 for error-sensitive decode. 3x prefill speedup at preserved task accuracy. First text-LLM phase-aware NVFP4 deployment in the wiki. Same Blackwell hardware path as LongLive-2.0. |
| inference-efficiency | [TIDE: lossless MoE diffusion LLM inference](inference-efficiency/2026-05-21-tide-moe-diffusion-llm-inference.md) | Temporal-stability-aware expert offload for dLLM-MoE serving. Interval-based refresh strategy formulated as a programming problem. 1.4-1.5x throughput on LLaDA2.0 models on single GPU-CPU. Lossless, training-free. |
| llms-foundation-models | [RELEX: rank-1 RLVR extrapolation](llms-foundation-models/2026-05-21-relex-rank1-rlvr-extrapolation.md) | RLVR weight trajectories are rank-1 and predictable. SVD over 15% of training plus linear-magnitude extrapolation reproduces or exceeds full-training checkpoints, extrapolates 10-20x beyond observation window. Tested across Qwen2.5-Math-1.5B, Qwen3-4B-Base, Qwen3-8B-Base. |
| llms-foundation-models | [The Unlearnability Phenomenon in RLVR](llms-foundation-models/2026-05-21-unlearnability-rlvr.md) | A substantial subset of hard examples remains unlearnable under RLVR despite correct rollouts. Cross-example gradient analysis: unlearnable examples have low gradient similarity, ungeneralizable reasoning patterns. Data augmentation does not improve gradient similarity. RLVR cannot rescue representations the pre-train does not support. |
| llms-foundation-models | [CPO: conditional equivalence of DPO and RLHF](llms-foundation-models/2026-05-21-cpo-dpo-rlhf-conditional-equivalence.md) | Proves DPO and RLHF equivalent only under an implicit assumption frequently violated in practice (the RLHF-optimal policy must prefer the human-preferred response). CPO restores provable alignment with constraint-based RLHF. State-of-the-art on standard alignment benchmarks. |
| llms-foundation-models | [HRM-Text: 1B model on $1,500 budget matches 2-7B open models](llms-foundation-models/2026-05-21-hrm-text-efficient-pretraining.md) | Hierarchical Recurrent Model replaces standard Transformer in pre-training; instruction-response PrefixLM objective replaces raw-text next-token-prediction. MagicNorm stabilizes deep recurrence. 60.7% MMLU, 84.5% GSM8K, 56.2% MATH at 100-900x fewer tokens, 96-432x less compute. |
| llms-foundation-models | [DynMuon: dynamic spectral shaping of Muon](llms-foundation-models/2026-05-21-dynmuon-spectral-shaping.md) | Generalizes Muon by treating singular-value exponent p as a scheduled control variable. Theory: positive p early emphasizes high-curvature directions, mildly negative p late spreads to low-curvature directions. 10.6-26.5% fewer steps to target loss versus Muon across model sizes. |
| agentic-systems | [SpecBench: measuring reward hacking in long-horizon coding agents](agentic-systems/2026-05-21-specbench-reward-hacking-coding-agents.md) | Visible-versus-held-out test gap as reward-hacking diagnostic. 30 systems-level programming tasks from JSON parser to OS kernel. Reward hacking grows 28 percentage points per 10x code size. Documented 2,900-line hash-table compiler that memorized test inputs. |
| agentic-systems | [SaaSBench: enterprise SaaS coding agents](agentic-systems/2026-05-21-saasbench-enterprise-saas-coding-agents.md) | 30 enterprise SaaS tasks across 6 domains, 8 languages, 13 frameworks, 5,370 validation nodes. 95% of long-horizon coding-agent failures occur before deep business logic, in configuration and integration. Eighth deployment-calibration benchmark in seven days. |
| daily-digest | [2026-05-21](daily-digest/2026-05/2026-05-21.md) | KV cache quantization Pareto front reworked from two angles (OScaR, OCTOPUS) plus phase-aware Mix-Quant. RLVR's foundations get reframed (RELEX rank-1 extrapolation, Unlearnability Phenomenon, CPO conditional equivalence). HRM-Text + DynMuon attack pre-training cost. OpenAI Erdos proof, Anthropic profitability + SpaceX S-1 deal, Cohere Apache 2.0, OpenAI IPO. |
| social-stream | [2026-05-21 morning slot](social-stream/2026-05/2026-05-21-morning.md) | SpaceX S-1 filed, $15B/year Anthropic compute deal disclosed, Anthropic also renting xAI Colossus 2. Cursor 3.5 ships unified Automations workspace and multi-repo agents. Scoble's personal-agent S-1 analysis as a consumer-side autonomous-research signal. HUMAIN-McKinsey + HUMAIN-Accenture Saudi consulting partnerships. Tesla Model S/X Signature Delivery (autonomy framing). |

## 2026-05-22 ingest

| Topic | Page | Summary |
|-------|------|---------|
| inference-efficiency | [KVServe: service-aware adaptive KV cache compression](inference-efficiency/2026-05-22-kvserve-adaptive-kv-compression-disaggregated-serving.md) | First framework treating KV compression as a service-level optimization. Modular strategy space, Bayesian Profiling Engine, Service-Aware Online Controller. 9.13x JCT speedup in PD-separated serving, 32.8x TTFT reduction in KV-disaggregated serving, 50x lower offline search overhead. Integrated into vLLM. |
| inference-efficiency | [RTPurbo: Full Attention Strikes Back](inference-efficiency/2026-05-22-rtpurbo-full-attention-sparse-transfer.md) | Full-attention LLMs are intrinsically sparse and can be sparsified with hundreds of training steps. 16-dim retrieval indexer, dynamic top-p selection. 9.36x prefill speedup at 1M context, 2.01x decode speedup, near-lossless accuracy. Composes orthogonally with KVServe. |
| inference-efficiency | [Gated DeltaNet-2: decoupled erase and write](inference-efficiency/2026-05-22-gated-deltanet-2-linear-attention-decoupled-erase-write.md) | NVIDIA. Linear attention with channel-wise erase gate and channel-wise write gate. Strict generalization of KDA and Gated DeltaNet. Beats Mamba-2, Gated DeltaNet, KDA, Mamba-3 at 1.3B / 100B tokens. Strongest gain on long-context RULER multi-key retrieval. |
| inference-efficiency | [WorldKV: training-free world memory via chunk retrieval](inference-efficiency/2026-05-22-worldkv-world-memory-retrieval-compression.md) | World Retrieval stores evicted KV chunks and retrieves by camera/action correspondence; World Compression halves chunk storage by anchor-frame key-key similarity. 2x throughput at full-KV fidelity, no fine-tuning, competitive with memory-trained baselines. |
| inference-efficiency | [Tencent Hy-MT2 with 1.25-bit AngelSlim quantization](inference-efficiency/2026-05-21-tencent-hy-mt2-translation-quantization.md) | 1.8B / 7B / 30B-A3B multilingual translation family across 33 languages. 1.8B compressed to 440 MB at 1.25 bits, 1.5x speedup. 7B/30B-A3B beat DeepSeek-V4-Pro and Kimi K2.6. iPhone-resident MT. |
| inference-efficiency | [Maximally Scale-Stable Parameterization for MoE](inference-efficiency/2026-05-21-moe-mup-scale-stable-parameterization.md) | Kurate cs.LG #14 (ai_rating 9.0/10). Extends muP to Mixture-of-Experts by accounting for activation-pattern-dependent effective width. Learning rates transfer across width and expert-count axes jointly without retuning. |
| inference-efficiency | [ik_llama.cpp + MTP at 110 tok/s on 12GB VRAM](inference-efficiency/2026-05-21-ik-llamacpp-mtp-cpu-offload-qwen36.md) | Practitioner report: Qwen3.6-35B-A3B at 110 tok/s decode on RTX 4070 Super (12 GB) via ik_llama.cpp with multi-token-prediction speculative decoding and CPU offload of expert layers. Companion llama.cpp b9274 fixes MTP VRAM leak on sleep/resume. |
| llms-foundation-models | [OpenAI reasoning model disproves Erdős unit-distance conjecture](llms-foundation-models/2026-05-21-openai-erdos-unit-distance-proof.md) | Unreleased OpenAI reasoning model produced counterexample to 1946 Erdős conjecture, proof extracted from CoT transcript. Tim Gowers calls it a milestone; Marcus/Newport call it narrow but impressive. First top-journal-worthy AI math result that did not require external symbolic scaffolding. |
| llms-foundation-models | [Cohere Command A+ open-sourced under Apache 2.0](llms-foundation-models/2026-05-21-cohere-command-a-plus-open-source.md) | Cohere's strongest model released as Apache 2.0 weights, most permissive of the May 2026 open-weight cohort. Joins Tencent Hy-MT2 and Llama-Heretic recant in the same week's open-weight news. |
| ai-industry | [Anthropic first profitable quarter on SpaceX compute deal](ai-industry/2026-05-21-anthropic-profitability-spacex-deal-ipo.md) | WSJ scoop: $559M operating profit on $10.9B Q2 revenue. SpaceX S-1 discloses $15B/yr Anthropic compute deal, $6.36B xAI 2025 loss, $2T valuation target, Musk 85.1% voting. Marcus/Zitron note one-time discount may exceed projected profit. OpenAI IPO filing within days. |
| responsible-ai | [AISN #73: Beijing summit, Eigenism, Musk loses OpenAI suit](responsible-ai/2026-05-21-aisn-73-beijing-summit-eigenism-musk-verdict.md) | AI safety becomes bipartisan in DC post-Beijing summit. CAIS Eigenism paper: AI cares about humans because shared history is part of AI's information pattern. Musk loses on statute of limitations; testifies xAI "partly" distilled OpenAI. Brockman 2018 diary entries enter evidence. |
| responsible-ai | [AI Snake Oil: resilience beats nonproliferation](responsible-ai/2026-05-21-ai-snake-oil-resilience-vs-nonproliferation.md) | Kapoor and Narayanan: AI lacks the physical chokepoint that nonproliferation needs. Open-weight gap is months not years; nonproliferation would require escalating licensing controls. Cybersecurity-fuzzer precedent shows resilience works when funded. |
| hardware | [SemiAnalysis EDA Market Primer Part 2](hardware/2026-05-21-semianalysis-eda-market-primer.md) | $16B Big-3 EDA industry growing 13% CAGR vs 7% semiconductor R&D. Systems companies are 45% of demand. 60-70% of design time spent on verification, growing 15%/yr. $50-100M cost per chip respin. |
| daily-digest | [2026-05-22](daily-digest/2026-05/2026-05-22.md) | Four HuggingFace papers attack KV cache from four directions in one day (KVServe, RTPurbo, Gated DeltaNet-2, WorldKV). Anthropic projects first profitable quarter on $15B/yr SpaceX deal. OpenAI Erdős proof; Cohere Apache 2.0; Eigenism framework; resilience-versus-nonproliferation debate. |
| social-stream | [2026-05-22 morning slot](social-stream/2026-05/2026-05-22-morning.md) | NVIDIA AI tokenomics cluster + "demand parabolic" Dell keynote + GTC Taipei June 1. Anthropic /usage Claude Code feature. @ns123abc memory shortage to 2030s; Anthropic more accessible compute than OpenAI claim. Cursor doubled Teams plan usage. Cosmo agentic UI startup. Curated reposts empty. |
