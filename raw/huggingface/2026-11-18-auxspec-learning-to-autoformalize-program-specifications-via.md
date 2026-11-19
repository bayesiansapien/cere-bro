---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.21421
url: https://huggingface.co/papers/2611.21421
arxiv_url: https://arxiv.org/abs/2611.21421
date: 2026-11-18
---

# AuXSpec: Learning to Autoformalize Program Specifications via Executable Postconditions

Formal specifications define intended program behavior and underpin verification, but writing them in theorem provers such as Lean is slow and expertise-intensive, making specification a major bottleneck to scaling formally correct code. Autoformalization from natural-language problems is promising, yet training specification models requires scalable feedback on whether generated specifications capture intended behavior. Prior approaches obtain this feedback through explicit proofs or separately implemented code with formal correspondence proofs, both expensive. We introduce AuXSpec, a Lean framework that pairs declarative postconditions with executable counterparts, obtained through type class resolution when possible and otherwise defined separately with an equivalence proof. Test cases can then evaluate declarative specifications by execution, letting us use agreement as a reinforcement-learning reward. Using AuXSpec, we synthesize 3,037 LeetCode problems and expand training to 19.5K samples through expert iteration on Codeforces. Experiments show that training Qwen3.5-9B and Qwen3.8-27B with the execution-based reward improves SpecGen pass@4 on AuXSpec-Test 0.7% to 82.7% and 14.3% to 84.3%, and the 27B model outperforms all frontier models. On the out-of-domain Verina benchmark with its original prompts, both models improve 7.0% to 90.5% and 21.9% to 90.5% and surpass VeriSpecGen-30B-A3B, the prior state of the art among open-source specification models, on pass@1 (theirs 47.6% vs. ours 73.7% and 84.5%) and pass@4 (theirs 63.9% at pass@10 vs. ours 90.5%). We release the weights of the trained 9B and 27B models and the 3,037 problems with test cases, including the 300-problem AuXSpec-Test benchmark with expert review and correctness proofs for future evaluation. Models and data: https://huggingface.co/collections/eth-algopt/auxspec. Website: https://auxspec.org
