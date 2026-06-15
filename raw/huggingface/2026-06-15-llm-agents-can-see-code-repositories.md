---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.14061
url: https://huggingface.co/papers/2606.14061
arxiv_url: https://arxiv.org/abs/2606.14061
date: 2026-06-15
---

# LLM Agents Can See Code Repositories

Coding agents powered by large language models have demonstrated strong performance on software engineering tasks. Yet most agents consume repositories almost entirely as text, which differs from how human developers use visual structure such as folder hierarchies and dependency relationships to orient themselves in large codebases. With multimodal large language models (MLLMs), it is an open question whether agents can effectively benefit from visual representations of repositories. This paper presents the first systematic empirical study of visual repository representations for LLM-based agents on repository-level issue resolution. We evaluate four recent multimodal models. Our results show that a strictly vision-only setup degrades accuracy and increases token cost, because agents lack sufficient symbolic detail and compensate with repeated visual queries. In contrast, integrating visual graphs of repository structure as a supplementary modality alongside standard text interfaces helps agents understand structure more efficiently: input token consumption decreases by up to 26% while issue-resolution accuracy is maintained or improved. Visualization is most useful during fault localization and when the agent autonomously controls exploration depth. These findings point to a practical hybrid text-and-vision design for next-generation coding agents.
