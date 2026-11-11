# You Can't Tell What an Agent Skill Will Do by Reading It

**Channel:** AI Engineer (Roey Ben Chaim, Zenity)
**Published:** 2026-11-10
**Source:** https://www.youtube.com/watch?v=_7P580m4kPY

## TL;DR
Static scanning of agent skills, whether regex or LLM-based, cannot establish intent. The payload often lives outside `SKILL.md`, and LLM analyzers can be socially engineered. Zenity built an agent "detonation chamber" (the malware-sandbox idea applied to skills) that runs each skill end to end, captures OS-level side effects, and judges by behaviour. Across thousands of skills it surfaced about 100 malicious ones, including a typosquat campaign with 1.7M aggregate installs that harvested SSH and cloud credentials.

## Key Takeaways
- **Benign and malicious look the same statically:** an official Azure diagnostic skill reads cloud/k8s configs, calls identity services, and probes the instance metadata endpoint, exactly like an info stealer.
- **Why static scans fail:** (1) `SKILL.md` is only an entry point; payloads come from remote prompts, install scripts, and downloaded packages; (2) LLM analyzers are trickable (Trail of Bits: a comment saying "appsec team approved" got a registry-tampering skill passed).
- **Detonation chamber evolution:** generic sandbox, then a *world builder* (spins up the CLIs and services a skill expects, e.g. a Notion mock), then an *operator* (generates task prompts covering every skill route), then an *adversarial operator* (talks the agent past safety refusals, retries runs), then capture of process creation, filesystem, and network packets beyond agent traces (npm postinstall scripts evade trace-only monitoring).
- **Attacker tricks observed:** persistence (writes "reinstall this skill" into AGENTS.md / soul files), silent replacement (a fake skill-creator uninstalls Anthropic's official one), remote prompt execution (prompt fetched from a mutable URL, so domain takeover equals compromise), and hook abuse (triggering on every `UserPromptSubmit`).
- **Polymarket example:** install script pulled a lookalike npm package from an unofficial registry, which turned out to be an info stealer.
- **Paperclip campaign:** fake org and domain, cloned repo, injected a `log` action that fetches, decodes, executes via node, and self-deletes after 60 s. Targets `~/.ssh`, AWS, and Azure. PyPI variants died within hours, but the skills trended to 1.7M downloads. Vercel and Microsoft took them down within 12 h.
- **Principle:** everything entering context (sites, DB rows, packages, YouTube comments) is supply chain. Treat skills as package dependencies: inspect loads, least privilege, observe runtime.

## Architecture & Optimization Mechanics
- **Dynamic analysis has a cost profile.** Each detonation is a multi-minute to multi-hour agent run plus environment synthesis. At registry scale this is an inference-cost problem: a cheap static or LLM pre-filter to triage, then expensive detonation only on suspicious or high-download skills, is the obvious cascade.
- **Coverage is the hard part.** The operator must enumerate skill trajectories, which is a test-generation problem with no completeness guarantee. Time-of-check vs time-of-use also breaks it: remote prompts can change after the scan.
- **Safety refusals were friction**, both on real benign skills (decoding payloads that are part of official skills) and on the research itself. That is a measurable false-positive cost of current safeguards.

## Grounded Context (Web Enrichment)
The campaign is well documented. Zenity presented it at Black Hat USA (August 2026) and published it on labs.zenity.io. Attackers first uploaded verbatim copies of official Paperclip and Browser Use skills to skills.sh to pass marketplace checks and build install counts, then trojanized them on July 11. After the npm and PyPI packages were pulled, they redirected agents to fetch the stealer straight from GitHub. The 1.7M figure is aggregate installs, not unique users (CSO Online reports roughly 300K per skill). Indicators include `getpaperclipai/paperclip`, `browser-use-headless/browser-use-headless-skill`, PyPI `browser-use-headless==0.1.4`, and `paperclip-ai==0.1.0/0.1.1`. Removal from the registry does not uninstall it locally.

The "clean first, poison later" tactic confirms the talk's core point: any point-in-time scan, static or dynamic, is insufficient without version pinning and re-scanning on update.

## Real-World Application / Actionable Step
- Today: grep your machines and agent configs for the IOCs above and for any skill installed from skills.sh. Check `AGENTS.md`/`CLAUDE.md` for injected "reinstall" lines and review hooks on `UserPromptSubmit`.
- Pin skills by commit hash, vendor them into your repo, and block skills that fetch remote prompts at runtime.
- Run research agents with no access to `~/.ssh`, cloud credential dirs, or `.env` (separate user or container), and egress-filter the sandbox.
- If you build agent tooling, the triage cascade (cheap classifier, then full detonation) is a direct analogue of your LLM-routing work and a good place to apply confidence-based escalation.
