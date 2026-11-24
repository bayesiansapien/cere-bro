---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.250938+00:00
arxiv_id: 2611.25252
url: https://huggingface.co/papers/2611.25252
arxiv_url: https://arxiv.org/abs/2611.25252
date: 2026-11-23
---

# Moving Generality from Model to Modeler: LLM Agents for PHM on a Deployment-Style Benchmark

Coding agents built on large language models (LLMs) now help develop many models published as general solutions. Should generality instead reside in the agent that builds a model for each new task? We examine this question in prognostics and health management (PHM), where every model must work on unseen equipment. Our deployment-style benchmark, NextUnit-Bench, covers 24 public datasets split into 58 folds that hold out units or operating conditions; each agent has two hours to deliver an executable predictor, then run on the hidden units. First, frontier agents outperform AutoML, which reaches less than half the best agent's score, and faithful implementations of published methods on four datasets, of which only 6 of 30 beat the strongest agent's own design; published accuracies, where reproducible, rest on the papers' own conventions, and a single convention, capping the remaining life of test engines, can halve the reported error. Second, the agents' advantage is a design made on each machine's data; once made, a plain-text plan of a few hundred words carries most of the gap between two frontier agents, and given a weaker agent's plan, the strongest agent falls to that agent's level, often to identical predictions. Before touching the data, however, it matters little whose plan an agent carries out, and domain toolkits appear to help neither: what sets the strongest apart is how much it learns from the data. Third, such designs reach only implementers that can execute them: given the strongest agent's designs, a locally deployable open-weight model delivers half as often, even when they are lightened, and scores no higher than without them. Generality, we argue, is not disappearing but moving, from the model to the modeler.
