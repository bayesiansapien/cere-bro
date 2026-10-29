---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.993703+05:30
arxiv_id: 2610.32046
url: https://huggingface.co/papers/2610.32046
arxiv_url: https://arxiv.org/abs/2610.32046
date: 2026-10-28
---

# Can Test-Time Memory Evolution Outperform Test-Time Training for Scientific Discovery?

Recent test-time training (TTT) frameworks have enabled open-weight large language models (LLMs) to outperform inference-only frameworks powered by frontier models on scientific discovery tasks. However, TTT introduces additional computational cost for online weight updates during the discovery process, making computational efficiency an important consideration when scaling to larger models. This motivates us to explore an efficient test-time adaptation method for scientific discovery. We introduce Test-Time Memory Evolution (TTME), a plug-and-play test-time adaptation method, as an alternative to TTT. TTME continually updates the external memory by distilling the experience to guide subsequent discovery without updating model weights. To have a clean comparison, we evaluate TTME and TTT under the same discovery framework, replacing only the test-time adaptation method. Our evaluation shows that TTME outperforms TTT on all five mathematical tasks, while reducing computational cost by 82.8-84.6% in FLOPs and 47.7-58.4% in runtime. These results establish TTME as an effective and computationally efficient alternative to TTT in the evaluated discovery settings.
