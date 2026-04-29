# Wiki Index

Catalog of all pages. Updated on every ingest.

---

## agents-tool-use

| Page | Summary |
|------|---------|
| [gui-agents.md](agents-tool-use/gui-agents.md) | Concept: MLLM-based GUI agents, long-horizon challenges, key papers |
| [agent-benchmarks.md](agents-tool-use/agent-benchmarks.md) | Concept: benchmarks for agentic AI — OccuBench, GameWorld, MERRIN, explore/exploit |
| [2026-04-16-ui-copilot.md](agents-tool-use/2026-04-16-ui-copilot.md) | UI-Copilot: memory decoupling + TIPO for long-horizon GUI tasks |
| [2026-04-16-trex-llm-finetuning-automation.md](agents-tool-use/2026-04-16-trex-llm-finetuning-automation.md) | TREX: multi-agent LLM fine-tuning automation via search tree |
| [2026-04-16-exploration-exploitation-lm-agents.md](agents-tool-use/2026-04-16-exploration-exploitation-lm-agents.md) | Measurable explore/exploit errors in LM agents |
| [2026-04-16-occubench.md](agents-tool-use/2026-04-16-occubench.md) | OccuBench: 100 professional task scenarios via Language World Models |
| [2026-04-16-do-ai-coding-agents-log-like-humans.md](agents-tool-use/2026-04-16-do-ai-coding-agents-log-like-humans.md) | AI coding agents fail logging instructions 67% of the time |
| [2026-04-16-defenseclaw-maestro-agentic-security.md](agents-tool-use/2026-04-16-defenseclaw-maestro-agentic-security.md) | DefenseClaw: security control plane for OpenClaw + MAESTRO threat model |
| [2026-04-16-vakra-agent-reasoning-failure-modes.md](agents-tool-use/2026-04-16-vakra-agent-reasoning-failure-modes.md) | VAKRA: tool-use failure modes in agents |
| [2026-04-17-claude-code-architecture.md](agents-tool-use/2026-04-17-claude-code-architecture.md) | Claude Code v2.1.88 architecture: while-loop core + 5 surrounding systems |
| [2026-04-17-superlocalmemory-agent-memory.md](agents-tool-use/2026-04-17-superlocalmemory-agent-memory.md) | SuperLocalMemory V3.3: biologically-inspired local agent memory with forgetting curves |
| [2026-04-25-claude-code-memory-systems-chapter8.md](agents-tool-use/2026-04-25-claude-code-memory-systems-chapter8.md) | Claude Code memory systems (Chapter 8): QueryEngine eager flush + LRU cache + path-set dedup; Apr 23 postmortem caching bug analysis |

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

## multimodal

| Page | Summary |
|------|---------|
| [2026-04-16-seedance-2-video-generation.md](multimodal/2026-04-16-seedance-2-video-generation.md) | Seedance 2.0: unified audio-video generation with 4 input modalities |
| [2026-04-16-rationalrewards-visual-generation.md](multimodal/2026-04-16-rationalrewards-visual-generation.md) | RationalRewards: critique-before-score reward models for visual generation |
| [2026-04-16-gameworld-multimodal-game-agents.md](multimodal/2026-04-16-gameworld-multimodal-game-agents.md) | GameWorld: 34-game benchmark for MLLM game agents |
| [2026-04-16-merrin-multimodal-retrieval.md](multimodal/2026-04-16-merrin-multimodal-retrieval.md) | MERRIN: multimodal web retrieval benchmark; avg accuracy 22.3% |

## inference-efficiency

| Page | Summary |
|------|---------|
| [knowledge-distillation.md](inference-efficiency/knowledge-distillation.md) | Concept: knowledge distillation, on-policy distillation, cross-tokenizer BLD |
| [kv-cache.md](inference-efficiency/kv-cache.md) | Concept: KV cache — context dependency, reuse, compression, eviction |
| [2026-04-16-tip-token-importance-on-policy-distillation.md](inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md) | TIP: two-axis token importance taxonomy; 47% memory reduction |
| [2026-04-17-kv-packet-recomputation-free-kv-cache.md](inference-efficiency/2026-04-17-kv-packet-recomputation-free-kv-cache.md) | KV Packet: soft-token adapters for zero-recomputation KV cache reuse |
| [2026-04-17-cross-tokenizer-distillation-byte-level.md](inference-efficiency/2026-04-17-cross-tokenizer-distillation-byte-level.md) | Byte-Level Distillation: bytes as universal cross-tokenizer interface |
| [2026-04-17-model-capability-dominates-inference-time.md](inference-efficiency/2026-04-17-model-capability-dominates-inference-time.md) | AIMO 3: model capability 4x > prompt-level optimization; gap is selection not prompting |

## ai-routing

| Page | Summary |
|------|---------|
| [llm-routing.md](ai-routing/llm-routing.md) | Concept: LLM routing — surrogate models, parity gates, open problems |
| [2026-04-17-tracer-llm-routing.md](ai-routing/2026-04-17-tracer-llm-routing.md) | TRACER: trace-driven surrogate routing; 100% coverage on 150-class benchmark |

## hardware

| Page | Summary |
|------|---------|
| [gpu-kernels.md](hardware/gpu-kernels.md) | Concept: GPU kernel optimization, accelerator-specific tuning, NKI, memory hierarchy, AccelOpt, Nemotron, goodput |
| [2026-04-21-semianalysis-gpu-cluster-goodput.md](hardware/2026-04-21-semianalysis-gpu-cluster-goodput.md) | SemiAnalysis: gold vs silver tier neoclouds differ 6–21% in goodput; fault-tolerance tooling is fragmented and immature |

## ai-industry

| Page | Summary |
|------|---------|
| [2026-04-17-claude-market-share-surge.md](ai-industry/2026-04-17-claude-market-share-surge.md) | Claude doubles market share in a month; Gemini reaches 25% AI traffic share |
| [2026-04-17-anthropic-mythos-policy.md](ai-industry/2026-04-17-anthropic-mythos-policy.md) | Anthropic's Mythos: withheld from public, pitched to Pentagon; trust debate |
| [2026-04-22-amazon-anthropic-capital-concentration.md](ai-industry/2026-04-22-amazon-anthropic-capital-concentration.md) | Amazon $33B → Anthropic; Anthropic $100B → AWS over 10 years; circular capital deal locks infrastructure; Bezos Project Prometheus nears $10B |
| [2026-04-18-openai-exec-departures-restructuring.md](ai-industry/2026-04-18-openai-exec-departures-restructuring.md) | OpenAI loses three execs, restructures around coding/enterprise; IPO doubts |

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

## agents-tool-use (new 2026-04-20)

| Page | Summary |
|------|---------|
| [2026-04-20-gta-2-tool-agent-benchmark.md](agents-tool-use/2026-04-20-gta-2-tool-agent-benchmark.md) | GTA-2: frontier models at 14.39% on open-ended workflows; execution harness matters more than model |
| [2026-04-20-prl-bench-physics-benchmark.md](agents-tool-use/2026-04-20-prl-bench-physics-benchmark.md) | PRL-Bench: all frontier models below 50% on real physics research tasks from PRL (Aug 2025+) |
| [2026-04-20-query-agent-loop-claude-vs-hermes.md](agents-tool-use/2026-04-20-query-agent-loop-claude-vs-hermes.md) | Claude Code 7-site state machine loop vs. Hermes IterationBudget — recovery architecture is what separates functional agents |

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

## agents-tool-use (new 2026-04-18)

| Page | Summary |
|------|---------|
| [2026-04-18-corpus2skill-knowledge-navigation.md](agents-tool-use/2026-04-18-corpus2skill-knowledge-navigation.md) | Corpus2Skill: compile corpus into skill tree, navigate not retrieve; beats RAPTOR |
| [2026-04-18-dr3-eval-deep-research-benchmark.md](agents-tool-use/2026-04-18-dr3-eval-deep-research-benchmark.md) | DR3-Eval: reproducible deep research benchmark with static corpus sandboxes |
| [2026-04-19-unidoc-rl-visual-rag.md](agents-tool-use/2026-04-19-unidoc-rl-visual-rag.md) | UniDoc-RL: RL agent for hierarchical visual RAG (doc→image→region); +17.7% over prior RL methods |
| [2026-04-19-claude-code-architecture.md](agents-tool-use/2026-04-19-claude-code-architecture.md) | Claude Code architecture reverse-engineered: trivial while-loop + ML permission classifier + 5-layer compaction |
| [2026-04-23-persistent-agent-infrastructure.md](agents-tool-use/2026-04-23-persistent-agent-infrastructure.md) | Kimi K2.6 (5 days, 300 sub-agents), OpenAI Agent Studio (Slack + screen memory), Anthropic Conway (containerized): three independent convergences on always-on agents |
| [2026-04-23-claude-code-vs-hermes-permissions.md](agents-tool-use/2026-04-23-claude-code-vs-hermes-permissions.md) | Claude Code (ML classifier + layered rules) vs. Hermes (regex + container bypass): different safety bets, both untested at multi-day agent scale |
| [2026-04-22-ml-intern-agentic-posttraining.md](agents-tool-use/2026-04-22-ml-intern-agentic-posttraining.md) | ml-intern: open-source agentic post-training loop; reads papers, generates data, trains via GRPO, evaluates, iterates; Qwen3-1.7B 10%→32% GPQA in 10 hours |
| [2026-04-22-evaluation-driven-scaling-scientific.md](agents-tool-use/2026-04-22-evaluation-driven-scaling-scientific.md) | SimpleTES: parallel exploration + feedback refinement + local selection; 2x LASSO speedup, 24.5% quantum circuit gate reduction, new Erdős constructions |
| [2026-04-22-agentspex-workflow-language.md](agents-tool-use/2026-04-22-agentspex-workflow-language.md) | AgentSPEX: declarative YAML workflow language for agents; typed steps, branching, state management, sandboxed harness with checkpointing |
| [2026-04-21-reward-free-self-evolution-agents.md](agents-tool-use/2026-04-21-reward-free-self-evolution-agents.md) | Reward-free self-evolution: agents trained to explore accumulate world knowledge; 14B beats Gemini-2.5-Flash on web tasks |
| [2026-04-21-precise-debugging-benchmark.md](agents-tool-use/2026-04-21-precise-debugging-benchmark.md) | PDB: frontier models pass unit tests 76% but edit precision below 45%; models regenerate not debug |

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
| [2026-04-23.md](daily-digest/2026-04/2026-04-23.md) | Daily digest: persistent agent convergence (Kimi K2.6, OpenAI, Anthropic Conway), permission systems analysis, medical LLM reliability crisis, Mythos breach, Trainium2 |
| [2026-04-22.md](daily-digest/2026-04/2026-04-22.md) | Daily digest: TurboQuant (KV 6x compression), PrfaaS (cross-DC disaggregation), ml-intern (agentic post-training), TEMPO (EM-guided TTT), CoT degrades spatial reasoning |
| [2026-04-21.md](daily-digest/2026-04/2026-04-21.md) | Daily digest: Nemotron 3 Super (Tier 1), SemiAnalysis goodput (Tier 1), GFT (SFT is broken RL), RLVR faithfulness, speculative execution cross-domain pattern |
| [2026-04-20.md](daily-digest/2026-04/2026-04-20.md) | Daily digest: STOP path pruning, AccelOpt GPU kernels, Maximal Brain Damage vulnerability, GTA-2 agent benchmark, selective-compute convergence |
