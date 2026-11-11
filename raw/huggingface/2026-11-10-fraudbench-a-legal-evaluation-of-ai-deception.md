---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.326883+00:00
arxiv_id: 2611.12167
url: https://huggingface.co/papers/2611.12167
arxiv_url: https://arxiv.org/abs/2611.12167
date: 2026-11-10
---

# FraudBench: A Legal Evaluation of AI Deception

We introduce FraudBench, an evaluation of large language models' (LLMs) propensities to recommend, assist, or directly take actions that would constitute fraud under U.S. law. Our evaluation contains a novel dataset of 159 scenarios based on real-world U.S. court cases and validated by legal experts. We present each scenario to LLMs via three tasks at varying levels of autonomy: advising users, drafting messages for users to send, and acting directly on behalf of users (477 tasks total). In each scenario, FraudBench re-enacts the facts of a court case to give LLMs an opportunity, but no explicit instruction, to either misrepresent or conceal a material fact in a high-stakes commercial setting--e.g., whether to describe company-funded product testing as "independent" to customers (misrepresentation) or whether to hide unfavorable regulatory investigations from clients (concealment). We evaluate 20 LLMs across 25 experimental conditions (totaling >300,000 generations) and include a preregistered human baseline (n_{annotations} = 2{,}957, n_{humans} = 996). We score a response as fraudulent when it engages in, assists with, or recommends misrepresentation or concealment. Key findings include: (1) across LLMs, fraud rates ranged from near 0% to over 40%; (2) LLM fraud rates increased with autonomy, with overall rates of 3.0% when advising, 14.7% when drafting, and 21.4% when acting directly, without applying pressure; (3) LLMs sometimes engaged in fraud despite recognizing legal risks; (4) LLMs more often engaged in fraud by concealment than by misrepresentation; and (5) prompt-based interventions substantially affected fraud rates, with a prompt to obey the law reducing fraud rates, while prompts to maximize profits and act agentically increased fraud rates.
