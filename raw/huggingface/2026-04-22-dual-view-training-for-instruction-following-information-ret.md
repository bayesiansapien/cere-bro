---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.18845
url: https://huggingface.co/papers/2604.18845
arxiv_url: https://arxiv.org/abs/2604.18845
date: 2026-04-22
---

# Dual-View Training for Instruction-Following Information Retrieval

Instruction-following information retrieval (IF-IR) studies retrieval systems that must not only find documents relevant to a query, but also obey explicit user constraints such as required attributes, exclusions, or output preferences. However, most retrievers are trained primarily for semantic relevance and often fail to distinguish documents that match the topic from those that satisfy the instruction. We propose a dual-view data synthesis strategy based on polarity reversal: given a query, a document that is relevant under the instruction, and a hard negative that matches the query but violates the instruction, we prompt an LLM to generate a complementary instruction under which the two documents swap relevance labels. By presenting the same document pair under complementary instructions that invert their relevance labels, the training signal forces the retriever to reconsider the same candidate set through the instruction, rather than relying on fixed topical cues. On a 305M-parameter encoder, our method improves performance on the FollowIR benchmark by 45%, surpassing general-purpose embedding models of comparable or larger scale.
