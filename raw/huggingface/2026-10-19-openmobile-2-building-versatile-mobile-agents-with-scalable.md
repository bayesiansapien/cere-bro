---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.14157
url: https://huggingface.co/papers/2610.14157
arxiv_url: https://arxiv.org/abs/2610.14157
date: 2026-10-19
---

# OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments and App-Native Tools

We introduce OpenMobile-2, a near-frontier mobile agent with fully open training environments and recipes. We make three key advances: (1) Diverse environments with simulated commercial apps: We build MobileGym++, featuring 35 realistic, functionally rich commercial-style apps with cross-app workflows, while preserving full controllability for reset and verification. Together with newly configured apps in Android emulators, this yields a diverse playground spanning over 110 apps. (2) Open training data at scale: Building on this foundation, we curate nearly 12K mobile interaction trajectories for supervised fine-tuning and the largest open collection of verifiable RL training data for mobile agents, comprising over 2K executable tasks with automatic rewards. (3) Hybrid GUI and app-native tool use: We explore an experimental mobile-use setting where apps expose selected functionalities as app-native tools alongside their GUIs, allowing agents to interleave GUI actions and tool calls within a task. We implement this setting in MobileGym++ with over 300 carefully scoped tools across 50+ apps. Additionally, we introduce MobileGym++ Bench for complex, long-horizon commercial mobile scenarios, supporting both GUI-only and hybrid GUI-tool evaluation on a shared task suite. OpenMobile-2 performs competitively across established benchmarks, including AndroidWorld (79.9) and MobileWorld (50.4), while showing promising transfer to real-device mobile use, nearly doubling SPA-Bench performance from 31.9 to 59.6. All resources are available at https://os-copilot.github.io/OpenMobile2-Home/.
