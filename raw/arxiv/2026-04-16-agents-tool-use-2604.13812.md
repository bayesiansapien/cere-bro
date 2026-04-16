---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13812
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13812
published: 2026-04-16
authors: Jacopo Cossio, Daniele Lizzio Bosco, Riccardo Romanello
---

# AlphaCNOT: Learning CNOT Minimization with Model-Based Planning

**arXiv:** https://arxiv.org/abs/2604.13812
**Authors:** Jacopo Cossio, Daniele Lizzio Bosco, Riccardo Romanello

## Abstract

arXiv:2604.13812v1 Announce Type: new  Abstract: Quantum circuit optimization is a central task in Quantum Computing, as current Noisy Intermediate Scale Quantum devices suffer from error propagation that often scales with the number of operations. Among quantum operations, the CNOT gate is of fundamental importance, being the only 2-qubit gate in the universal Clifford+T set. The problem of CNOT gates minimization has been addressed by heuristic algorithms such as the well-known Patel-Markov-Hayes (PMH) for linear reversible synthesis (i.e., CNOT minimization with no topological constraints), and more recently by Reinforcement Learning (RL) based strategies in the more complex case of topology-aware synthesis, where each CNOT can act on a subset of all qubits pairs. In this work we introduce AlphaCNOT, a RL framework based on Monte Carlo Tree Search (MCTS) that address effectively the CNOT minimization problem by modeling it as a planning problem. In contrast to other RL- based solution, our method is model-based, i.e. it can leverage lookahead search to evaluate future trajectories, thus finding more efficient sequences of CNOTs. Our method achieves a reduction of up to 32% in CNOT gate count compared to PMH baseline on linear reversible synthesis, while in the constraint version we report a consistent gate count reduction on a variety of topologies with up to 8 qubits, with respect to state-of-the-art RL-based solutions. Our results suggest the combination of RL with search-based strategies can be applied to different circuit optimization tasks, such as Clifford minimization, thus fostering the transition toward the "quantum utility" era.
