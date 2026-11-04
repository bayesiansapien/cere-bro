---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.41216
url: https://huggingface.co/papers/2610.41216
arxiv_url: https://arxiv.org/abs/2610.41216
date: 2026-11-03
---

# TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents

Robot agents built on vision-language models depend on both the planner and its harness: the tools, feedback, memory, and recovery logic around it. Can improvements to a large teacher's harness be carried into a compact agent with lower inference compute cost? We present TinyAstral, a two-stage approach. We first freeze an open-weight teacher and improve its harness through recursive self-improvement (RSI): frontier LLM agents read the teacher's trajectories and propose harness edits, and each edit is accepted only if it passes a paired statistical test. We then freeze the final harness, collect teacher trajectories with reasoning and failure recovery, and distill a small student that replaces the teacher in the same harness. On RoboTwin, harness evolution raises the teacher's success from 33.4% to 63.6%; the final 4B student reaches 62.8%. Across four harness versions, distilled 4B students score close to their corresponding teachers, and later versions yield stronger students, showing that harness evolution gains carry into compact models. The harness gains also transfer to other frozen planners without retraining. On identical episodes, the final 4B student outperforms open 4B agents, the open 27B harness-RSI model SenseNova-RoboRSI, and our own teacher model placed in three competitors' harnesses. It stays close to its teacher on all three training benchmarks, and on three benchmarks never used for RSI or training it scores close to a 552B planner running the same harness. On the measured deployment episodes, it uses about one fifth of its teacher's accelerator time.
