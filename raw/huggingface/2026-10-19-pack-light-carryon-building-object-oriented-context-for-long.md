---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.18784
url: https://huggingface.co/papers/2610.18784
arxiv_url: https://arxiv.org/abs/2610.18784
date: 2026-10-19
---

# Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents

Long-horizon agents accumulate progress in persistent task state, yet repeatedly process interaction histories describing how that progress was achieved. This raises a natural question: can long-horizon context instead be organized around reusable progress rather than the history that produced it? In this paper, we introduce CarryOn, an object-oriented context runtime that organizes continuation around reusable task objects. Rather than treating compressed histories or reconstructed accounts of progress as the primary basis for continuation, CarryOn builds a context view from continuation carriers, complementary execution context, and a live tail of recent interactions. A core challenge is keeping this reusable basis valid after its surrounding history is retired: how can CarryOn update the basis without reconstructing the full representation at every fold? CarryOn maintains carrier records across folds, revising affected records against bound evidence and applicable environment checks while carrying forward unaffected records and jointly updating execution context. Experiments on OSWorld 2.0 and BrowseComp-Plus show improved gains of 5.8% and 7.0% while reducing total token usage by 51.9% and 22.9%, respectively. Project page: https://ethannju.github.io/carryon
