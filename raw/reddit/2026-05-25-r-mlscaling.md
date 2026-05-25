# r/MLScaling | 2026-05-25 IST | sort=new
> Scraped 2026-05-25 10:32 IST | lookback=24h | tier_default=1
> Gwern-flavored sub on scaling laws + frontier evals. Low volume but extremely high signal. Take everything.

### "MesaNet: Sequence Modeling by Locally Optimal Test-Time Training", Von Oswald et al 2025

**Meta:** score=1 · comments=0 · tier=1 · flair=R, RNN, G, M-L, RL, Emp · posted=2026-05-25 00:58Z
**Author:** u/gwern
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tmts0t/mesanet_sequence_modeling_by_locally_optimal/](https://www.reddit.com/r/mlscaling/comments/1tmts0t/mesanet_sequence_modeling_by_locally_optimal/)
**Link:** [https://arxiv.org/abs/2506.05233#google](https://arxiv.org/abs/2506.05233#google)

---

### "Inside the British Lab Hunting for Dangers Lurking in AI: The government’s AISI , staffed by alumni from OA and Google, is becoming a model for countries grappling with AI’s emerging risks"

**Meta:** score=6 · comments=0 · tier=1 · flair=N, D, Bio, OA, A · posted=2026-05-24 18:13Z
**Author:** u/gwern
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tmjpg6/inside_the_british_lab_hunting_for_dangers/](https://www.reddit.com/r/mlscaling/comments/1tmjpg6/inside_the_british_lab_hunting_for_dangers/)
**Link:** [https://www.nytimes.com/2026/05/24/technology/uk-ai-safety-institute.html](https://www.nytimes.com/2026/05/24/technology/uk-ai-safety-institute.html)

---

### Best strategy for hard negative sampling in large-scale entity resolution training?

**Meta:** score=1 · comments=0 · tier=1 · posted=2026-05-24 17:48Z
**Author:** u/Main_Deer_8600
**Reddit:** [https://www.reddit.com/r/mlscaling/comments/1tmj0xa/best_strategy_for_hard_negative_sampling_in/](https://www.reddit.com/r/mlscaling/comments/1tmj0xa/best_strategy_for_hard_negative_sampling_in/)

I’m working on a record linkage / entity resolution problem and would appreciate suggestions from people who have handled large-scale imbalanced datasets.

Use case:  
I want to fine-tune a cross-encoder reranker model for a binary classification task where the model predicts whether two records belong to the same person (`match` vs `no match`).

Each record pair may contain fields like:

* Name
* Email
* Phone
* Address
* RTC / ID-related info
* Other textual attributes

Dataset challenge:  
The dataset contains crores of real-world record pairs and is heavily imbalanced:

* Only lakhs of positive (`match`) pairs
* Remaining are negative (`no match`) pairs

The main issue is with handling the huge number of negative samples.

I do NOT want to do random downsampling because:

* Data quality is uncertain
* Random sampling may remove important negative patterns
* I want the sampled negatives to represent all difficulty levels

Ideally, I want the negative samples to include:

1. Easy negatives → completely different records
2. Moderate negatives → partially similar records
3. Hard negatives → highly similar records but actually not matches

Another challenge is that all inputs are textual data.

Questions:

* What is the best strategy to create a representative negative sample set for this kind of problem?
* Has anyone used clustering, semantic similarity, BM25, embeddings, or curriculum mining for hard-negative selection in entity resolution tasks?
* How would you balance dive

[…truncated, see permalink]

---
