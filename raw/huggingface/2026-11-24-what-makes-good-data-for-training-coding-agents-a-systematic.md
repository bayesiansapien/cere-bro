---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.921541+00:00
arxiv_id: 2611.30207
url: https://huggingface.co/papers/2611.30207
arxiv_url: https://arxiv.org/abs/2611.30207
date: 2026-11-24
---

# What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym

Reinforcement learning (RL) trains coding agents on software tasks whose hidden tests decide the reward, yet task collections check these tests only against the reference fix. We ask what makes a task good training data, focusing on the correctness of its reward labels. We audit SWE-Gym with two LLM families, and a suspected error counts only if execution reproduces it. We find that unsolved often means mislabelled: 74% of the tasks that a 9B base model never solves have a test that rejects correct fixes (a false negative), versus 20% of those it sometimes solves. We repair or remove such tasks, and the audited tasks that remain train better policies. At equal size and matched difficulty, models trained on them score 2.4 and 2.7 points higher on held-out tasks from SWE-bench Verified and SWE-bench Pro than models trained on the original tasks, whereas simply dropping the never-solved tasks shows no such gain. We further find that wrong patches that pass (false positives) make up about a quarter of all passing patches, and that new tests that catch a quarter of them do not change held-out scores detectably. A pass rate shows whether a task yields reward, not whether that reward is right, so the reward labels themselves must be checked. To this end, we release SWE-Gym-Verified with its 1,087 audited tasks, every verdict with its executed evidence, our training sets, and the full audit pipeline.
