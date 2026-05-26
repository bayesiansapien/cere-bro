# QUEST: Training Frontier Deep Research Agents with Fully Synthetic Tasks

**Source:** [arXiv:2605.24218](https://arxiv.org/abs/2605.24218), via HuggingFace Daily Papers 2026-05-26.
**Topic:** Open deep-research agents / synthetic data / long-horizon search.

## TL;DR

Frontier deep-research agents (the systems that turn a query into a multi-step search, synthesis, and citation pipeline) remain proprietary. Existing open agents fail to generalize across task types. QUEST is a family of fully open models (2B to 35B) plus a training recipe that combines mid-training, supervised fine-tuning, and reinforcement learning. The data lever is a curated synthesis pipeline driven by unified rubric trees that produces training data with verifiable rewards without human annotation, generalizing across fact-seeking, citation-grounding, and report-synthesis tasks. With only 8K synthesized tasks, QUEST approaches or surpasses frontier closed-source agents across eight deep research benchmarks and achieves the best overall performance among recent open-weight agents. Everything is released: models, data, training scripts.

```
   Closed frontier baseline                  QUEST open recipe
   (OpenAI Deep Research,                                                 
    Anthropic deep research,                                              
    Google Gemini Deep Research):                                         
                                                                          
   ┌───────────────────────┐               ┌─────────────────────────┐    
   │  proprietary RL data   │               │ unified rubric tree     │    
   │  proprietary verifier  │               │       │                 │    
   │  closed model          │               │       ▼ rubric leaves   │    
   └───────────────────────┘               │ 8K synthetic tasks       │    
            │                              │  with verifiable rewards │    
            ▼                              └────────────┬─────────────┘    
   high cost, no transfer                                ▼                  
                                            mid-train ► SFT ► RL           
                                            ┌────────────────────┐         
                                            │ context manager    │         
                                            │ for long-horizon   │         
                                            └────────────────────┘         
                                                       │                    
                                                       ▼                    
                                            2B-35B open models matching     
                                            frontier closed performance     
```

## What it does

- **Synthetic data via rubric trees**: a tree of evaluation rubrics covers fact-seeking, citation-grounding, and report-synthesis tasks. Each rubric leaf defines a verifiable reward function. Tasks are synthesized to match the rubric tree, producing training data where reward signals are automatic and verifiable.
- **Training recipe**: mid-training adapts the base LLM to the search-and-synthesis substrate, SFT instills the agent's behaviour, RL refines with rubric-verifiable rewards.
- **Context management**: a built-in mechanism for managing long-horizon contexts as the agent does multi-step retrieval and synthesis (the practical bottleneck for any deep-research agent in 2026).
- **Open release**: 2B / 7B / 35B models, training scripts, synthesized data. everything published.

## Key results

- 8K total synthesized training tasks (a small number relative to the gains).
- Eight deep research benchmarks across diverse task types.
- Approaches or surpasses frontier closed-source agents across the benchmark set.
- Best overall performance among recent open-weight deep-research agents.

## How this relates to prior wiki pages

QUEST is the open-weights answer to a problem the wiki has been tracking since DR3-Eval (2026-04-17, the deep research evaluation benchmark covering realistic and reproducible workflows). DR3-Eval said: there is no standard way to measure deep-research agents; QUEST says: here is an open model family good enough to be the baseline everyone else measures against.

On the synthetic-data side, QUEST is the deep-research equivalent of:

- **C2 (2026-04-18)**: scalable rubric-augmented reward modeling from binary preferences, the paper that established the rubric-tree pattern as the right substrate for verifiable rewards.
- **Themis (2026-05-04)**: multilingual code reward models with rubric-based decomposition.
- **Rubric-Based RL (2026-05-13)**: the convergence of rubric trees with RLVR for reward-hacking-resistant post-training.

QUEST is the natural next step in this thread: once you have rubric trees that produce verifiable rewards, you can synthesize the entire training task distribution and skip human annotation. The implication is that the proprietary moat around deep-research agents (which has been "we have the data") is much weaker than expected.

## Research angle

The 8K-task efficiency is the load-bearing result. It says: rubric-tree synthesis is high enough quality that the training-data scaling assumption (more data, more performance) does not hold once you have a coherent rubric structure. This is consistent with the 2026-05-25 Shannon Scaling Law's prediction that scaling past channel capacity injects noise faster than signal: if the rubric tree saturates the relevant signal capacity at 8K tasks, more synthetic data adds noise without adding signal. Direct empirical validation of the Shannon framework on synthetic-data scaling would be a natural next study.

## Industrial implication

This is the strongest open-weights deep-research model published to date. For any organization building an internal research agent that does not need to call out to OpenAI Deep Research or Anthropic, QUEST is the new baseline. The training-scripts release also means a frontier lab cannot defend its position with proprietary data; the synthesis recipe is the moat, and QUEST opens it.
