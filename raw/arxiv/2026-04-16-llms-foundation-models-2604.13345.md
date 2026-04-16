---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13345
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13345
published: 2026-04-16
authors: Vladimir Kalu\v{s}ev, Branko Brklja\v{c}, Milan Brklja\v{c}
---

# Multi-Agent Object Detection Framework Based on Raspberry Pi YOLO Detector and Slack-Ollama Natural Language Interface

**arXiv:** https://arxiv.org/abs/2604.13345
**Authors:** Vladimir Kalu\v{s}ev, Branko Brklja\v{c}, Milan Brklja\v{c}

## Abstract

arXiv:2604.13345v1 Announce Type: new  Abstract: The paper presents design and prototype implementation of an edge based object detection system within the new paradigm of AI agents orchestration. It goes beyond traditional design approaches by leveraging on LLM based natural language interface for system control and communication and practically demonstrates integration of all system components into a single resource constrained hardware platform. The method is based on the proposed multi-agent object detection framework which tightly integrates different AI agents within the same task of providing object detection and tracking capabilities. The proposed design principles highlight the fast prototyping approach that is characteristic for transformational potential of generative AI systems, which are applied during both development and implementation stages. Instead of specialized communication and control interface, the system is made by using Slack channel chatbot agent and accompanying Ollama LLM reporting agent, which are both run locally on the same Raspberry Pi platform, alongside the dedicated YOLO based computer vision agent performing real time object detection and tracking. Agent orchestration is implemented through a specially designed event based message exchange subsystem, which represents an alternative to completely autonomous agent orchestration and control characteristic for contemporary LLM based frameworks like the recently proposed OpenClaw. Conducted experimental investigation provides valuable insights into limitations of the low cost testbed platforms in the design of completely centralized multi-agent AI systems. The paper also discusses comparative differences between presented approach and the solution that would require additional cloud based external resources.
