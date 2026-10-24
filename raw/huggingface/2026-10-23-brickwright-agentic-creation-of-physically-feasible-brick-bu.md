---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.886473+00:00
arxiv_id: 2610.31651
url: https://huggingface.co/papers/2610.31651
arxiv_url: https://arxiv.org/abs/2610.31651
date: 2026-10-23
---

# BrickWright: Agentic Creation of Physically Feasible Brick Builds

Frontier coding agents are becoming increasingly adept at 3D modeling. Yet, they still face challenges when building objects meant to be assembled in the physical world, often creating invalid assemblies with floating, colliding, or disconnected parts. We argue that providing agents with tools for assembling builds and verifying their physical feasibility is sufficient for them to produce physically valid assemblies that still adhere to input prompts. Focusing on the domain of LEGO brick builds, we present BrickWright, a framework for generating physically feasible brick builds from text or image prompts using pre-trained agents, where a build is physically feasible if it uses only real parts, has no colliding or floating parts, and forms a connected structure if possible. BrickWright guides agents to create builds by writing code with BrickLayer, a Python toolkit with two main components: an ergonomic brick assembly API that halves inference cost compared to working in raw LDraw, and a validator that provides feedback on physical feasibility. Whereas baseline agents achieve physical validity rates ranging from only 9% (GPT-6 Luna) to 69% (GPT-6 Astra), BrickWright-guided agents achieve 100% validity on a sample of 512 prompts, while improving prompt adherence for lightweight agents and maintaining it for stronger agents. Additionally, they outperform specialized models on the text-to-brick task. Code is available on our project page: https://avalovelace1.github.io/brickwright/
