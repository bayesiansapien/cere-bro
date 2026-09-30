---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.934967+00:00
arxiv_id: 2609.34065
url: https://huggingface.co/papers/2609.34065
arxiv_url: https://arxiv.org/abs/2609.34065
date: 2026-09-29
---

# Who Gets a Token, and What Does It Carry? Unequal Name Support and Concept Access in Large Language Models

Names are personal identifiers, but they also carry social meaning and are widely used to evaluate how language models treat different people. Such evaluations typically assume that matched names are comparable model inputs. We show that this assumption often fails at the lexical interface: matched names are not necessarily matched inputs. Some names receive direct single-token access, while others are assembled from multiple subwords, creating unequal name-surface support. Across nearly half a million first names and 12 LLM-associated tokenizers, direct lexical access is highly selective, model dependent, and uneven across race- and gender-associated name metadata. We introduce NameTrace, a model-native, fine-grained, pre-behavioral framework for measuring whether unequal name-surface support remains a vocabulary property or becomes visible in task-relevant internal representations. NameTrace measures concept accessibility from the model's own probabilities over task-specific adjective axes with continuous task-aligned weights. On matched atomic and short-fragmented names within the same race/ethnicity--gender-associated strata, support predicts systematic differences in concept accessibility across fellowship, hiring, clinical assessment, and lending. These differences persist across all eight matched strata, extend across model families, and transfer to unseen names. Hidden-state interventions further show that the measured task directions have downstream leverage, shifting later constrained choices. Unequal lexical support is therefore demographically structured at the input and remains visible in task-relevant model computation. NameTrace makes lexical comparability measurable, supporting a broader principle: behavioral comparability begins with lexical comparability.
