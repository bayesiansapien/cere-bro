---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.05903
url: https://huggingface.co/papers/2609.05903
arxiv_url: https://arxiv.org/abs/2609.05903
date: 2026-09-11
---

# EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing Agents

Large Language Model (LLM) agents are turning language into real-world effects, making safety necessary against both indirect prompt injections and direct harmful requests. System-level safety harnesses add an enforcement layer beyond model-level defenses, but existing harnesses are usually designed once by experts and applied across heterogeneous models and domains. Effective protection is deployment-dependent: models differ in how much enforcement they need before utility declines, while domains differ in the effects, state, and action sequences that must be governed. A harness that is strict enough for one model may over-block another, and a policy that transfers across domains may miss application-specific safety relations.
  We present EvoSafeHarness, a safety-specific optimization framework that synthesizes a deployable harness for a frozen model in a target domain. It jointly searches a natural-language policy and executable code logic, guided by model behavior, domain specifications, and fresh-context adversarial review to reject benchmark-specific rules. Across four agent benchmark families, EvoSafeHarness achieves a stronger safety-utility frontier than fixed expert-designed defenses. On DecodingTrust-Agent, it reduces average attack success rate from 45.6% to 10.0% at a 3.3-point utility cost and achieves the best score in 14 of 15 cells. On AgentDojo, it reaches 82.8% utility at 0.0% ASR, twice CaMeL's utility at the same operating point, and transfers unchanged to unseen AgentDyn suites. It also achieves the best score on Agent-SafetyBench for every victim and keeps mean ASR below 20% under adaptive PAIR attacks with a refinement budget of 16. Analysis shows that domain semantics determine which safety relations and trajectory state are needed, while model and runtime behavior determine how and where those relations should be enforced.
