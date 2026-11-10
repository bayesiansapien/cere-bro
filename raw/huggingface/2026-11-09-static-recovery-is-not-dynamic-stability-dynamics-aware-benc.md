---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.208429+00:00
arxiv_id: 2611.07723
url: https://huggingface.co/papers/2611.07723
arxiv_url: https://arxiv.org/abs/2611.07723
date: 2026-11-09
---

# Static Recovery Is Not Dynamic Stability: Dynamics-Aware Benchmarking of Protein Motif Scaffolding

Protein motif scaffolding benchmarks assess whether generative models can build scaffolds around functionally important residues. Their conclusions depend on which motifs are tested and which criteria define success. Existing benchmarks typically use small hand-curated motif sets and static refolding criteria, but protein function often depends on conformational ensembles and transitions. Here, we address both benchmark scope and success criteria. We introduce BILBY-PRO, a systematically derived benchmark of structurally conserved functional motifs from PROSITE-linked experimental structures, comprising 220 cases from 174 PROSITE motif-pattern entries. Evaluating six recent scaffold-generation models reveals distinct patterns in target coverage and unique-solution yield: RFDiffusion and Proteina solve more targets, whereas ESM3 produces more unique successful scaffolds on the targets it solves. We further introduce BILBY-MD, a reference-based all-atom molecular dynamics evaluation framework. Applied to statically solved designs from the original MotifBench benchmark, it compares motif drift, scaffold drift, motif-contact preservation, and motif-dihedral free-energy landscapes against reference simulations. Of 55 statically solved model-problem pairs, 31 satisfy our MD-supported criterion and only 8 pass all checks. Compact, self-contained motifs are often MD-supported, whereas interface-like or context-dependent motifs fail more frequently. Static refolding success therefore provides useful evidence of local motif recovery but does not establish dynamical fidelity of the full scaffold. BILBY highlights three complementary axes of motif-scaffolding evaluation: target coverage, unique-solution yield, and MD-supported dynamical fidelity.
