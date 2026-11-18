---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.108525+00:00
arxiv_id: 2611.07222
url: https://huggingface.co/papers/2611.07222
arxiv_url: https://arxiv.org/abs/2611.07222
date: 2026-11-17
---

# SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection

Tool-using agents act on email, files, and payments, so an instruction hidden in a web page or a shared document can make an agent send data or money to an attacker. Many runtime defenses put a language model on the decision that lets an action through, so the decision depends on a model that may read the attacker's text and adds model calls to every step. Provenance defenses keep the model off the final check but need a model to plan or route each task first. Where an action goes can instead be read from the tools' typed returns: an email's sender or a payment's account arrives in a typed field, while injected instructions arrive as free text. SPILLWAY turns this observation into a deterministic floor with no per-task plan. The check admits a call when each target value that appears in tool output but not in the user's task was returned by a read-only tool in a typed field or is covered by a fixed delegation rule. A deterministic sanitizer removes instruction-like regions its fixed rules match before the model reads them and retains the removed spans as evidence, and a local judge may restore a refused call, never one whose target lies in the removed text. Across three backbones, and seven task suites on one of them, no standard templated injection redirects an action to an attacker's target under SPILLWAY, at the highest observed mean utility and composite scores (NRP, ERS) of the defenses we run under that attack. A forged chat template also produces a raw zero, and mean in-scope attack success under a released reinforcement-learning attacker is .007. SPILLWAY reaches this floor with no defense-triggered backbone re-run and almost no added model call. As personal AI agents act on users' email, files, and payments, SPILLWAY gives them an auditable refusal floor on where their actions go that keeps them useful and holds across backbones.
