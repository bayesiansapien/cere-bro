---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.994856+05:30
arxiv_id: 2610.34491
url: https://huggingface.co/papers/2610.34491
arxiv_url: https://arxiv.org/abs/2610.34491
date: 2026-10-28
---

# What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents

Generative models increasingly expose a reasoning effort setting that lets users scale inference-time compute, trading higher cost for potentially improved performance. Users must choose an effort level before knowing whether extra reasoning will help, and even a successful run does not reveal whether the effort purchased was necessary. Reasoning effort is therefore a credence good: buyers observe the outcome but cannot assess the marginal value of the computation they paid for. In this work, we measure the counterfactual effect of effort levels on both proprietary and open-weight models on four benchmarks, spanning single-call reasoning and long-horizon agentic tasks. Effort, it turns out, does not consistently preserve tasks that lower effort solves, can overspend, and can change trajectory behavior. First, we find that although higher effort can raise accuracy in aggregate, it frequently fails on tasks that lower effort solved. Second, on the subset of easy tasks that every effort level solves, higher effort is generally more costly, with the highest effort level costing up to 42x as much as the lowest. Lastly, effort changes not only how many tokens are used, but also how agents solve tasks: at higher effort, agents verify their own work more heavily and more often search for solutions than work through problems directly, both of which lengthen trajectories without necessarily altering the outcome. These findings show that naively choosing the highest level is not only cost-inefficient but also offers no guarantee of the best instance-level performance. A simple alternative, starting at the lowest effort and escalating only after a verified failure, matches or improves on fixed top effort across all models and benchmarks at lower cost for most proprietary models.
