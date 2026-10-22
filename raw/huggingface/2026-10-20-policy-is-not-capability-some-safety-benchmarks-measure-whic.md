---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.25060
url: https://huggingface.co/papers/2610.25060
arxiv_url: https://arxiv.org/abs/2610.25060
date: 2026-10-20
---

# Policy Is Not Capability: Some Safety Benchmarks Measure Which Definition of "Unsafe" You Trained On

A guardrail classifier is reported as if unsafe were a property of text. It is not: it is a property of a policy, and the policy enters the model through its labels. We exploit an accident of an industrial deployment in which the same ~53k prompts were labelled twice, under two operational definitions ("is this a request for harmful content?" and "would a moderator block this?"), and used to train ten guardrail arms sharing architecture, codebase and optimiser family, at two model scales. First, the guardrail's own training corpus already contained the benchmarks: JailbreakBench-benign is 88% and OR-Bench-hard 82% present in the training pools, two over-refusal benchmarks, the kind a guardrail reports to argue it does not over-block. Everything below is decontaminated. Second, safety benchmarks stratify sharply by how much of their score is decided by the label definition rather than by the model: with architecture and optimiser fixed, the range across the ten arms is 0.99 on HarmBench-copyright and 0.043 on WildGuard-benign, a 23x spread. Third, a benchmark score can be moved across its entire range by 0.03% of the parameters. Across these arms HarmBench-copyright spans 0-100 and OR-Bench-hard over-refusal 3.4-56.4%, and the four arms whose last supervision signal carries a given policy occupy one extreme of both (exact rank p=0.005, or 0.04-0.14 at worst), at unchanged detection capability. For a distilled student the teacher's soft labels do this even when every hard label carries the other policy, so teacher provenance is an unrecorded confound in any released checkpoint. Fourth, validation accuracy on the one split that grades all twenty arms tracks agreement with the annotator's policy (rho=+0.74), not detection capability (rho=+0.34). We argue that guardrail evaluations should report contamination, a seed floor and the definition they were graded against as first-class variables.
