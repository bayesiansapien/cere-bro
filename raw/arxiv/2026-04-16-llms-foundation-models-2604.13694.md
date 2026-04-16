---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13694
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13694
published: 2026-04-16
authors: Chenghao Sun, Chengsheng Zhang, Guanzheng Qin
---

# Weight Patching: Toward Source-Level Mechanistic Localization in LLMs

**arXiv:** https://arxiv.org/abs/2604.13694
**Authors:** Chenghao Sun, Chengsheng Zhang, Guanzheng Qin

## Abstract

arXiv:2604.13694v1 Announce Type: new  Abstract: Mechanistic interpretability seeks to localize model behavior to the internal components that causally realize it. Prior work has advanced activation-space localization and causal tracing, but modules that appear important in activation space may merely aggregate or amplify upstream signals rather than encode the target capability in their own parameters. To address this gap, we propose Weight Patching, a parameter-space intervention method for source-oriented analysis in paired same-architecture models that differ in how strongly they express a target capability under the inputs of interest. Given a base model and a behavior-specialized counterpart, Weight Patching replaces selected module weights from the specialized model into the base model under a fixed input. We instantiate the method on instruction following and introduce a framework centered on a vector-anchor behavioral interface that provides a shared internal criterion for whether a task-relevant control state has been formed or recovered in open-ended generation. Under this framework, the analysis reveals a hierarchy from shallow candidate source-side carriers to aggregation and routing modules, and further to downstream execution circuits. The recovered component scores can also guide mechanism-aware model merging, improving selective fusion across the evaluated expert combinations and providing additional external validation.
