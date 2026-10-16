---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.227163+05:30
arxiv_id: 2610.19100
url: https://huggingface.co/papers/2610.19100
arxiv_url: https://arxiv.org/abs/2610.19100
date: 2026-10-15
---

# GroundGUI: GUI Grounding by High-Quality Data and Distillation-to-Reinforcement Learning

Constructing robust GUI agents relies on multimodal visual grounding: the ability to precisely map natural language intents to actionable on-screen components. Despite abundant desktop, web, and mobile benchmarks, high-fidelity resources tailored for diverse environments are surprisingly scarce. To bridge this gap, we introduce the Screen Referring Grounding Dataset (ScreenRef), a comprehensive GUI grounding dataset consisting of GUI screenshots paired with natural language referring expressions and box or point annotations. Spanning desktop, web, and mobile domains, ScreenRef comprises 586K screenshots and over 633K referring expression instances, covering tasks such as text recognition, visual matching, spatial understanding, and refusal scenarios. To boost the model's grounding performance, we propose the Distillation-to-Reinforcement Learning (D2RL) method to address the limited generalization of supervised fine-tuning and the sparse reward problem in reinforcement learning. Utilizing ScreenRef, we train Qwen3-VL-8B-Instruct via sequential SFT and D2RL training, yielding GroundGUI-8B. GroundGUI-8B achieves 95.2% on ScreenSpot-V2, 63.9% on ScreenSpot-Pro, 65.4% on OSWorld-G, 86.8% on MMBench-GUI L2, and 38.3% on UI-Vision. Among 8B-scale models, it produces substantial gains over models trained on open-source datasets, with performance comparable or even superior to models trained on closed-source data. Code, models, and datasets are available at https://github.com/PrentisAI/GroundGUI.
