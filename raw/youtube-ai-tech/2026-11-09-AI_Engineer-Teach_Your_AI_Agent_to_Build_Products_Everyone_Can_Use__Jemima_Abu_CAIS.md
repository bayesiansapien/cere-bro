# Teach Your AI Agent to Build Products Everyone Can Use (Jemima Abu, CAIS)

**Channel:** AI Engineer
**Published:** 2026-11-09
**Source:** https://www.youtube.com/watch?v=YV1x6gCdgQA

## TL;DR
Coding agents reproduce the accessibility debt baked into their training data (96% of the top 1M sites have WCAG failures), so they default to popular-but-wrong patterns like div buttons and custom JS accordions. Abu's fix is procedural: encode accessibility requirements as a mandatory agent skill, audit the codebase first so the agent does not imitate bad local code, and centralize fixes in a design system. Her headline number (accessibility skill made a Figma-to-code run 3x faster and 58% cheaper) is a single uncontrolled run, which she herself concedes.

## Key Takeaways
- **Human bias becomes model bias.** Models learn "good code" from a corpus where 96% of sites fail accessibility. Without explicit constraints, agents perpetuate it and lock out roughly 16% of the population with disabilities.
- **Popular is not best.** Agents pick the most common implementation (custom JS accordion) over the native one (`<details>`, `popover`), which is shorter, accessible by default and browser-tested. Skills should steer toward platform primitives.
- **Codebase priors dominate.** An agent dropped into an inaccessible codebase treats it as the house style. Audit and fix first (an agent can do the audit).
- **Bake in, do not bolt on.** Retrofitting ARIA labels onto a finished site does not work; accessibility overlays are the same anti-pattern.
- **Skill contents (web):** semantic HTML first, ARIA only when no native element exists, every interactive element keyboard-operable. Pair with Google/Chrome's "modern web guidance" skill that tells agents which newer native features to use.
- **Experiment claim:** without skill, 15 min runtime; with skill, 5 min and 58% lower cost. n=1, no controls.

## Architecture & Optimization Mechanics
- The cost result has a plausible mechanism even if the number is anecdotal: a tight skill prunes the agent's search space. Fewer exploratory edits, fewer tool calls, fewer output tokens. Native elements also mean literally fewer generated lines than bespoke JS.
- This is the same lever as a good system prompt for routing: constraining the output distribution toward short canonical solutions reduces tokens per task, which is where agent cost actually lives.
- Persistent instructions (skills, CLAUDE.md rules) act as a prior that overrides both pretraining frequency and in-repo examples. Order of influence in practice: explicit mandatory rule > local codebase pattern > pretraining popularity.

## Grounded Context (Web Enrichment)
Independent 2026 evidence backs the core diagnosis. A CHI '26 paper (Calò, Gurita, De Russis) measured a "semantic accessibility gap" in HTML from Claude, Gemini and GPT models against WCAG 2.1. An AudioEye study (Sept 2026, vendor-funded, so discount accordingly) had five AI tools build 15 sites targeting WCAG 2.2 AA; all 15 failed Level A, averaging 55 issues per page, and simply asking for "accessible" made little difference. That last finding is the strongest support for Abu's real point: a vague instruction does nothing, a concrete enforceable skill is what changes output.

Earlier academic work found LLMs handle easy items (contrast, alt text) reasonably but fail on ARIA and complex widgets, which matches her "semantic HTML, minimal ARIA" rule. Her 58% cost reduction remains unverified anecdote. Treat it as a hypothesis, not a result.

## Real-World Application / Actionable Step
- If you ship any web UI (demos, internal dashboards, eval viewers), add a short accessibility skill to your agent config: semantic HTML, native `<details>`/`<dialog>`/`popover` over custom JS, keyboard operability, ARIA only as fallback. Add an axe-core or Lighthouse check to CI so the skill is verified, not trusted.
- Broader lesson for your agent tooling: measure tokens and wall-clock with vs. without a constraining skill on your own recurring tasks. If constraints cut tokens consistently, that is a cheap, model-agnostic cost optimization worth stacking with routing.
