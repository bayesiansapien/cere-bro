---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.640512
arxiv_id: 2610.27911
url: https://huggingface.co/papers/2610.27911
arxiv_url: https://arxiv.org/abs/2610.27911
date: 2026-10-21
---

# MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal Records

Enterprise agents answer questions over workplace records that evolve through team collaboration. As information is shared, corrected, and revised across documents, chats, and figures, multiple versions of the same information accumulate in the workspace. Reliable question answering therefore requires agents to reason over sufficient evidence, resolve cross-source and temporal conflicts, and recognize when the available evidence is insufficient to establish an answer. To systematically evaluate these capabilities, we introduce MMEnterprise-Bench, a benchmark comprising 1,613 questions grounded in evolving multimodal records from simulated collaboration projects, covering three categories: Evidence Reasoning, Conflict Resolution, and Unanswerability. We evaluate 10 proprietary and open-source multimodal LLMs and find that even the strongest models struggle when evidence contains cross-source or temporal conflicts or spans multiple images. Moreover, increasing the retrieval budget or employing a larger retriever improves evidence recall but does not consistently translate into higher answer accuracy. These findings highlight the persistent challenges of reasoning over evolving workplace records and establish MMEnterprise-Bench as a testbed for developing more reliable enterprise agents. Code and data are available at https://mlvlab.github.io/MMEnterprise-Bench/.
