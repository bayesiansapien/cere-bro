---
source: farmer/huggingface
farmed: 2026-09-19T13:33:45
arxiv_id: 2609.17496
url: https://huggingface.co/papers/2609.17496
arxiv_url: https://arxiv.org/abs/2609.17496
upvotes: 13
date: 2026-09-19
---

# Verifiable Social Reasoning for LLM Assistants

LLM assistants are widely used for daily social advice, yet evaluating their social reasoning in such consultation settings remains challenging since (i) it requires setups where the assistant learns about social situations from subjective user narratives, and (ii) social properties, such as others' intentions, typically lack verifiable ground truth. To address these challenges, we introduce Fuse, a multi-agent simulation framework for studying user-mediated social reasoning. In Fuse, a target agent with a hidden motive interacts with other agents including one representing the user, who then consults the evaluated assistant to infer the target's motive, providing verifiable ground truth by construction. Simulation faithfulness is validated through a human study with 24k annotations. We apply Fuse to 12 LLMs and demonstrate its analytical utility by systematically isolating key factors, showing that (i) user mediation compounds the inherent difficulty of social reasoning; (ii) LLMs exhibit systematic sensitivity to biased user framing; (iii) models can require more details than humans need to reach a correct prediction; and (iv) longer conversations do not always improve performance despite providing opportunities for clarifying questions. We open-source Fuse and a dataset with 21k examples.
