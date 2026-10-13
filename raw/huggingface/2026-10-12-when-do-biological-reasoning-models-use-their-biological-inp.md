---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.222620+05:30
arxiv_id: 2610.00898
url: https://huggingface.co/papers/2610.00898
arxiv_url: https://arxiv.org/abs/2610.00898
date: 2026-10-12
---

# When Do Biological Reasoning Models Use Their Biological Inputs?

Biological reasoning models use post-training to connect LLMs to biological foundation model representations and biological text. Their benchmark accuracy is taken as evidence that LLMs reason over these inputs. We test this assumption in six biological reasoning models across DNA, protein, and single-cell tasks. We perturb one biological input while holding the query and other inputs fixed, construct evidence conflicts that pair the foundation model representation of one genome, protein, or cell with the text of another, fit linear probes to the representations the language model receives, and analyze reasoning traces against the biological inputs. Evo2 and ESM3 contribute little to BioReason and BioReason-Pro performance on the evaluated tasks. Shuffling the DNA sequence barely changes BioReason disease prediction accuracy, and in evidence conflicts the two models follow the text in 97.9% and 99.7% of cases. Linear probes trained on the Evo2 and ESM3 representations predict the task targets, so these foundation models encode information relevant to the task, but provide limited overall performance improvement to BioReason and BioReason-Pro. In contrast, foundation model inputs contribute to ChatNT, Prot2Text-V2, and CellWhisperer performance, and differentially expressed genes in the gene sentence contribute to Cell2Sentence-Scale performance. Across SFT and RL checkpoints of BioReason-Pro and 42 BioReason checkpoints, increases in accuracy do not imply greater performance contributions from biological inputs. BioReason traces misstate nucleotide changes, while BioReason-Pro traces describe functions omitted from final predictions under evidence conflicts. We find that current post-training strategies do not ensure that foundation model representations contribute to task performance.
