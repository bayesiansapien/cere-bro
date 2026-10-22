---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.04902
url: https://huggingface.co/papers/2610.04902
arxiv_url: https://arxiv.org/abs/2610.04902
date: 2026-10-20
---

# Self-Evaluating Recursive Agents

Recursive language-model agents decompose tasks and delegate subtasks to child instances of the same policy, forming a tree of work. Training them, however, is hard: the final outcome is verifiable, but the self-invented intermediate subtasks are numerous and carry no ground truth. Existing methods score each node with a verifier or judge, which is costly at scale and blind to decomposition quality. We argue that a recursive agent must learn three coupled capabilities within one set of weights: decomposing problems into subtasks, solving them, and evaluating the outcomes, each requiring its own training signal. SERA (Self-Evaluating Recursive Agents) turns evaluation into a learned capability of the policy itself. Before delegating, the parent writes a rubric of weighted success criteria for each child subtask; a ranking objective against verified outcomes then trains rubric generation so that the criteria track genuine subtask success. In addition, a complementary leaf-coverage signal provides direct credit for task decomposition. Our central finding is that training the policy to generate aligned rubrics is what drives the gains: because the same weights both evaluate and execute, learning to judge subtasks sharpens the agent's ability to solve them. Notably, external supervision is also reduced: the judge is consulted only to train the rubric generator, while solving is trained against the agent's own rubric scores, which outperform direct use of the judge. Beyond training, the learned rubric doubles as an inference-time selector for tree search. On TextCraft-Synth and TextWorld-Sync, SERA improves over strong recursive-agent baselines by 5.38 and 13.14 points on average, and rubric-guided tree search at inference adds a further 2.43 points on TextWorld-Sync.
