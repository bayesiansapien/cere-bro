---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.23121
url: https://huggingface.co/papers/2610.23121
arxiv_url: https://arxiv.org/abs/2610.23121
date: 2026-10-19
---

# Scene-Designer: Learning Design Intelligence for Agentic 3D Scene Generation

Generating complete, coherent, and usable 3D indoor scenes from natural language requires strong design intelligence: the ability to design high-quality scenes and critique their quality. However, existing approaches either rely on general-purpose models lacking domain-specific design experience or learn from static scenes. In this work, we introduce Scene-Designer, an agentic framework that learns design intelligence through complementary design and critique experiences. We construct two datasets: Scene-OTA-35K, which provides Observation--Thought--Action supervision for learning scene design and efficient error correction, and Scene-OTC-15K, which provides Observation--Thought--Critic supervision for learning scene quality critique across physical validity, functional correctness, and layout coherence. Based on these experiences, we propose Scene-GRPO, a Critic-guided GRPO framework that improves design decisions and reduces unnecessary trial-and-error corrections. Extensive experiments demonstrate that Scene-Designer achieves superior performance in physical validity, functional correctness, and layout coherence, while the learned Scene-Critic significantly outperforms general-purpose models in scene critique. Moreover, test-time Critic guidance further improves scene generation, showing that the Critic can provide useful guidance beyond training. Additional analysis suggests a trend of mutual enhancement between scene design and critique abilities.
