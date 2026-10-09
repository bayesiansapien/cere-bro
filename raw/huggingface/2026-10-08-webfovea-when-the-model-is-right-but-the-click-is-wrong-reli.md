---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.307121+05:30
arxiv_id: 2610.03036
url: https://huggingface.co/papers/2610.03036
arxiv_url: https://arxiv.org/abs/2610.03036
date: 2026-10-08
---

# WebFovea: When the Model Is Right but the Click Is Wrong -- Reliable Round Trips for Vision-Based Web Agents on Live Websites

We present WebFovea, a vision-based web agent that placed 2nd in the WebRetriever Challenge 2026 with a final score of 57.0 out of 100. The challenge evaluates agents end to end on Protocol III of the WebRetriever benchmark (arXiv:2607.06118): starting from an entry URL on a live website, the agent must operate the site's own interface and return a verifiable answer. A capable multimodal large language model (LLM) is necessary for this, but not sufficient. The model's decisions reach the browser through the harness, the code between the model and the page. At every step, four things must go right: the model's reply must be parsed into the intended action, the action must take effect on the page, the result must be reported back accurately, and the model must be shown the information it needs. On real websites, many of the failures we observed occurred at one of these four stages rather than in the model's reasoning. A coordinate-space mismatch placed every click at 3/4 of its intended coordinates; actions on native dropdowns, inside iframes, and in text boxes failed silently; and self-generated chat-template tokens contaminated 4.9% of task episodes. WebFovea hardens each stage and surrounds the loop with guardrails that keep the agent within the rules and its budget. The four-stage view does not depend on the model, although some individual fixes do. Because we used the same model in all four submissions, the rise of our official hidden-set score from 31.0 to 57.0 reflects changes to the harness, up to run-to-run variance on live sites. We describe the design, the evidence for each component (including negative results), a failure analysis, the limitations, and a roadmap that includes routing different steps to different models. Code is available at https://github.com/jianganghan/WebFovea.
