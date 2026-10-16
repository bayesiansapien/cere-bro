# The Cost of Accessibility in AI (Jemima Abu, CAIS)

**Channel:** AI Engineer
**Published:** 2026-10-14
**Source:** https://www.youtube.com/watch?v=ZccJsdOE54M

## TL;DR
Abu argues that inaccessible products are wasted tokens: if people cannot use what an agent builds, the spend was pointless. In a single uncontrolled run on her work codebase, the same "implement this Figma design" prompt finished in a third of the time and 58% cheaper when the agent had an accessibility skill loaded. Her mechanism is plausible and the most useful idea in the talk: without constraints, agents reinvent native semantic elements (modals, accordions) in verbose custom JavaScript, which costs more tokens and more testing. She admits the experiment is n=1 and not evidence, which is correct. Treat it as an anecdote that supports a sensible hypothesis, not as a measured result.

## Key Takeaways
- **Headline number:** a skill-guided run was 58% cheaper and ~3x faster than the unguided run. That is one run per arm with no variance estimate.
- **Agents inherit codebase bias.** An inaccessible codebase teaches the agent that accessibility is not a constraint, and every generated feature compounds it.
- **Agents over-generate.** Without guidance they rebuild native widgets from scratch instead of using semantic HTML (`<dialog>`, `<details>`). More code means more tokens, more tests, more bugs.
- **Bake it in, do not retrofit.** The "blueberry muffin" analogy: ARIA labels sprinkled on at the end is not accessibility, and late fixes mean regression testing and refactors.
- **"Our users don't use assistive tech" is survivorship bias.** They do not show up because they cannot use the product.
- **Recipe:** define platform requirements, audit and fix the existing codebase before adding agents (so they do not copy bad patterns), centralize fixes in a component library, enforce a mandatory accessibility skill.
- **Minimal skill:** semantic HTML first, ARIA only when HTML cannot express the behavior, every mouse interaction also keyboard-operable, everything labeled for screen readers, and a self-audit before running. She recommends Chrome's Modern Web Guidance skill.

## Architecture & Optimization Mechanics
- **Constraints shrink the agent's search space.** A skill that says "use the native element" prunes an entire branch of exploration (write custom widget, test it, debug focus handling). This is the same reason a good system prompt lowers token cost: fewer trajectories, shorter outputs.
- **Codebase as few-shot prior.** Existing code is the strongest in-context example. Auditing before agent adoption is data cleaning for the in-context distribution.
- **Primitive reuse beats generation.** Native platform primitives are pre-tested, pre-optimized building blocks. Analogous to calling a fused library kernel instead of having an agent hand-write a custom one.
- **Self-audit step** is a cheap verifier at the end of the trajectory, the same closed-loop pattern as e2e verification elsewhere in this batch.

## Grounded Context (Web Enrichment)
Her 96% figure is accurate and slightly understated in direction. The 2026 WebAIM Million report found detectable WCAG 2 failures on 95.9% of the top million homepages, up from 94.8% in 2025, with average errors per page rising 10.1% to 56.1 and average page complexity up 22.5% in a year. Several commentators link the regression to growing AI-generated, element-heavy pages, which supports her thesis. Six error types (low contrast, missing alt text, missing labels, empty links, empty buttons, missing document language) still make up about 96% of detected failures, so a lightweight skill targeting those would catch most automated findings.

Chrome's Modern Web Guidance is real and open source (installed via `npx modern-web-guidance@latest install`), covering about 100 modern web features with Baseline-aware fallbacks; its listing claims agent accuracy rising from roughly 50 to 57% to 78 to 88% with guidance, which I could not verify against Google's own materials. Her legal framing is loose: the ADA does not explicitly list website requirements for private businesses, though courts and lawsuits treat it that way. For public entities, DOJ's Title II rule mandates WCAG 2.1 AA, and an April 2026 interim final rule pushed the first compliance deadline from April 2026 to April 2027 (2028 for small entities). The 58% saving should not be repeated as a stat.

## Real-World Application / Actionable Step
- **Run the experiment properly for your own agent workflows:** pick 10 UI tasks, run each 3 to 5 times with and without a constraint skill, and record tokens, wall-clock and pass rate. This tests the general hypothesis that "constraint skills reduce token cost" and is directly relevant to routing and cost work.
- **Install Modern Web Guidance** for any internal dashboards or demo frontends you have agents build.
- **Add a 6-item accessibility checklist** (the six WebAIM error types) to your UI skill, alongside the polish checklist from [[2026-10-12-Railway-No-More-Sloppy-OneShot-SaaS]].
- **Audit before agent adoption** in any repo: clean the patterns you do not want copied, since the codebase is the agent's strongest prior.
