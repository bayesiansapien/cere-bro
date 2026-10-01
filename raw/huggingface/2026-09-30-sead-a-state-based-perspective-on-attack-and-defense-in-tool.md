---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.34518
url: https://huggingface.co/papers/2609.34518
arxiv_url: https://arxiv.org/abs/2609.34518
date: 2026-09-30
---

# SEAD: A State-Based Perspective on Attack and Defense in Tool-Using Agents

Language-model agents increasingly use tools to act on external systems. Earlier actions can alter files, permissions, database records, or other state, making a later routine-looking action harmful. Yet the visible interaction may not reveal the underlying state needed to assess that action. We formulate attack and defense as partially observed state control in SEAD, deriving their design requirements from this shared execution process. Because attackers supply instructions while the target chooses concrete actions, DART decomposes harmful goals into locally plausible steps and uses feedback from actual tool execution to guide trajectory search. The defender must decide before execution with incomplete state evidence. SAGE can therefore investigate relevant state through read-only queries before allowing or blocking each action, including those proposed after a block. We construct an environment-verifiable dataset integrating controlled initial states, replayable tool environments, and task-specific executable checks. Across four target models, DART improves semantic attack success by 18.8--35.9 percentage points over the competing baseline, with consistent gains under executable verification. On recorded trajectories, SAGE preserves 95.79% of benign trajectories while intercepting 92.73% of harmful paths by the harm-enabling boundary. In online attack-defense evaluation, it reduces DART's executable attack success from 48.0% to 4.0%. SAGE remains effective across four attack methods and generalizes to out-of-domain environments. Our code and data is available at https://github.com/EverywhereSafety/SEAD.
