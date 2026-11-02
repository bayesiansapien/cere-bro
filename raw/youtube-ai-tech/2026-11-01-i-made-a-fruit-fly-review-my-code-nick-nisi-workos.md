# I Made a Fruit Fly Review My Code (Nick Nisi, WorkOS)

**Channel:** AI Engineer
**Published:** 2026-11-01
**Source:** https://www.youtube.com/watch?v=geMAe-PLJF4

## TL;DR
Human code review is now the main constraint on shipping, not code generation. Nisi makes the point with a stunt: a simulated fruit fly connectome, fed LLM-generated "code smells" and trained with dopamine-style reward and punishment, approves or rejects PRs with about 88% accuracy on his test set. The real proposal is a tiered review pipeline. Team-owned review skills, a lightweight risk classifier, and commercial AI reviewers run first, and only PRs that fail one of them go to a human. Humans stop checking code and start checking intent: why the change exists and whether it is proven to work.

## Key Takeaways
- **Bottleneck shift:** Agents (Claude Code, Codex) plus CI and AI reviewers (Graphite, CodeRabbit, Greptile) produce and pre-check PRs faster than humans can read them. The human approval click is the slowest stage left.
- **Fly setup:** A connectome of a male fruit fly (he cites about 176k neurons, 6.3M connections, 125M+ synapses) is left unchanged except for a small subset of neurons used as memory. A small "System 1" LLM asks 30 unbiased questions about a diff. The answers are encoded as odors on the fly's sensilla.
- **Learning rule:** During training on the codebase, tests act as the teacher. A buggy result gives a bitter taste and punishment dopamine. A clean result gives sugar and reward dopamine. At inference, proboscis extension means approve and retraction means request changes. He describes the memory as a hash table where keys collide on purpose.
- **Ablation check:** Removing the fly's memories breaks behavior, so the fly is doing real work and is not just passing the LLM's verdict through. Reported numbers: 88% overall, 96% and 98% catch rates on two harder bug classes. The live demo went 2 for 3.
- **What it catches:** Changed conditionals and removed logic. It gives no explanation and has no idea why the change was made. That gap in intent is the part humans keep.
- **Proposed pipeline:** team review skill (owned through CODEOWNERS) → lightweight classifier (complexity, does the change match its description, risk) → automated reviewer → auto-merge if all pass, escalate to a human if any fail. After an incident, audit which gate missed it and patch that skill.
- **Proof of work:** Agents should attach screenshots, videos, test output, smoke tests, and repro steps. Human manual verification should decline as trust in these artifacts builds.

## Architecture & Optimization Mechanics
- This is effectively **an LLM feature extractor feeding a tiny fixed recurrent network with neuromodulated plasticity in a small set of neurons.** The LLM turns the diff into a 30-dimensional feature vector. The connectome works as a fixed reservoir, and only a few "memory" neurons are trained with a three-factor rule (pre, post, dopamine). Under the theatrics, this is reservoir computing with a reward-modulated readout.
- The interesting optimization point: **a frozen, biologically wired graph plus a tiny trainable memory reaches 88% on binary PR triage.** That suggests most of the signal is already in the LLM's 30 features, and the readout can be extremely cheap. It is the same lesson as routing work, where a small classifier over good features beats a large judge.
- The review pipeline is a **cascade router for human attention.** Each gate is a cheap model that can escalate. The cost being minimized is senior-engineer minutes, not GPU tokens.
- Weakness: no comparison against a trivial baseline (logistic regression on the same 30 LLM features). Without that, the fly's marginal contribution beyond "not zero, per the ablation" is unproven.

## Grounded Context (Web Enrichment)
Connectome-driven embodied flies are real and recent. In March 2026, Eon Systems connected a FlyWire-derived spiking model of the whole fly brain (about 139k neurons, simulated in Brian2) to the NeuroMechFly v2 body in MuJoCo, producing walking, grooming, and feeding. Eon calls it a work in progress, and there is no peer-reviewed paper on the embodied model yet ([Eon Systems](https://eon.systems/updates/embodied-brain-emulation), [The Register](https://www.theregister.com/2026/03/16/digital_fruit_fly_brain_model/)). The "Doom-playing fly" demos Nisi mentions build on this stack. His neuron count (about 176k, male) appears to refer to the male central nervous system connectome rather than the FlyWire female brain. Treat the exact numbers as approximate.

The bottleneck claim is well supported. Faros AI data on more than 10k developers links high AI adoption to 98% more PRs and 91% longer review time. LinearB reports that AI-generated PRs wait 4.6x longer and are accepted 32.7% of the time, versus 84.4% for human-written ones. One 2026 study of agent PRs reportedly found 61% receive no review at all ([dev.to summary](https://dev.to/code-board/the-review-bottleneck-why-faster-code-generation-isnt-faster-delivery-4273), [alexcloudstar](https://www.alexcloudstar.com/blog/ai-code-review-bottleneck-2026/)). That last figure undercuts the "humans are the gate" framing. Many teams already skip review without the safety cascade Nisi proposes. Atlassian's ICSE 2026 paper shows AI-assisted review cut median PR cycle time by 30.8% across more than 1,900 repos, which is the strongest evidence that a cascade works.

## Real-World Application / Actionable Step
- **For your research repos:** write a `REVIEW.md` skill for your team listing the things you would actually block a PR for, such as silent dtype or quant config changes, eval harness edits, changed seeds, and kernel launch params. Run it as a CI agent gate and escalate only on failure.
- **Require evidence in PRs:** any change to a pruning, quant, or routing path must attach before and after numbers (perplexity, task accuracy, latency at p50 and p99). The agent produces them, and you only read the delta.
- **Reuse the research idea:** "LLM-extracted features plus a tiny trained readout" is a cheap router design. Try it for query difficulty routing. Have a small model answer about 30 fixed yes/no questions about the prompt, then train a logistic or MLP head to choose the model tier. Benchmark it against a learned embedding router.
