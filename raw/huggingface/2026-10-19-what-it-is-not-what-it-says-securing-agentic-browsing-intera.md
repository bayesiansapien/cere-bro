---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.22697
url: https://huggingface.co/papers/2610.22697
arxiv_url: https://arxiv.org/abs/2610.22697
date: 2026-10-19
---

# What It Is, Not What It Says: Securing Agentic Browsing Interactions with Web Semantics

AI agents increasingly browse the web on users' behalf, yet they consume webpages as screenshots or text, exposing their LLMs to unvetted third-party content. Browsers enforce semantics under which what an element can do depends on what it is and where it comes from, not on what it says. Agents flatten these semantics, so injected text can persuade the LLM to exercise the user's authority for content that has none. As LLMs remain easy to persuade, the agent's interface to the web must itself ensure the integrity of what the agent reads, interprets, and does. We propose Intact, which runs on an unmodified browser. Intact builds GenTree, a bespoke representation that captures provenance and web semantics. Intact passes the page via GenTree to the LLM one element at a time, so the LLM decides on each element without any other element's text. Its harness executes each step only within the capabilities of the step's element and asks the user before acting on third-party content. On 1,270 real webpages, GenTree attributes 2.3x as many elements to third parties as the browser, which misattributes 58.7% of them to the first party. On 1,091 of these webpages with injected attacks, only 12.8% of attacks get through Intact's planner, each at most as a consent request, against 73.1% for a conventional planner. Isolation disrupts functionality on only 3.7% of tasks, and a parallel schedule could remove most of its added latency.
