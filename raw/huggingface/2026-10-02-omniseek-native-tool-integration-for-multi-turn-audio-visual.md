---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820833+00:00
arxiv_id: 2610.02181
url: https://huggingface.co/papers/2610.02181
arxiv_url: https://arxiv.org/abs/2610.02181
date: 2026-10-02
---

# OmniSeek: Native Tool Integration for Multi-turn Audio-Visual Reasoning

We present OmniSeek, an agentic framework that transforms an Omni Large Language Model (Omni-LLM) into an active, multi-turn reasoning agent with native tool use. Rather than passively processing an entire audio-visual sequence in a single forward pass, OmniSeek makes evidence acquisition part of the reasoning process: it dynamically decides whether to look or listen, and over which temporal window, to retrieve sparse but critical evidence across different modalities within long contexts. Through an iterative multi-turn protocol, the retrieved raw audio or visual segments are appended back into the context to support subsequent reasoning. To cold-start this capability, we build a data engine that synthesizes OmniTraj-170K, a corpus of multi-hop Chain-of-Thought trajectories with interleaved audio and visual evidence. We first supervise the model on these trajectories to instill multi-turn tool-use behavior, and then further optimize the policy via a two-stage reinforcement learning with verifiable rewards. Moreover, we introduce an Audio-Visual Necessity objective that explicitly rewards successful trajectories whose reasoning depends on both modalities, discouraging single-modality shortcuts. Extensive experiments across a wide range of benchmarks demonstrate that OmniSeek learns adaptive cross-modal evidence seeking and consistently improves audio-visual reasoning performance.
