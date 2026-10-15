---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.510197+00:00
arxiv_id: 2610.13416
url: https://huggingface.co/papers/2610.13416
arxiv_url: https://arxiv.org/abs/2610.13416
date: 2026-10-14
---

# Web$hell: A Unified Interface for Agentic Web Access

Large language model (LLM) agents are becoming direct users of the open web. As they take on increasingly complex and information-intensive tasks, effective web access is becoming a core capability for agentic problem solving. Existing approaches have advanced agentic web access through different access models, including search-augmented agents, browser-based agents, and, more recently, filesystem-based agents. Nevertheless, as users expect agents to complete long-horizon, end-to-end tasks, they increasingly need to conduct broad information gathering, perform browser actions, and revisit acquired evidence within a single trajectory. Yet our preliminary analyses reveal that existing access models struggle to meet these demands. They primarily support either information gathering or browser interaction, while combining their capabilities can involve substantial costs or performance trade-offs. To this end, we present Web\hell, an interface that unifies web access under a single access model. Using a common schema defined by WebContract, WebCompiler compiles live webpages into addressable information and action objects. These objects are maintained in WebCache and handled through a shared set of operations, providing agents with consistent, operable, and persistent web access. Through extensive experiments across web search, web navigation, and deep research benchmarks, we show that Webhell achieves strong task performance at lower cost. Our results further indicate the importance of interface design for effective web access, with Web\$hell opening new possibilities for more capable and efficient LLM agents on the web.
