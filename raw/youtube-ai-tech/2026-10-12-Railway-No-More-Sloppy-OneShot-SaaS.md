# Please... Enough with the Sloppy, One-Shot SaaS Replacements (Mahmoud Abdelwahab, Railway)

**Channel:** AI Engineer
**Published:** 2026-10-12
**Source:** https://www.youtube.com/watch?v=oixzVKMAXG0

## TL;DR
"SaaS is dead" ignores the gap between one-shotted working software and software you actually want to use daily. Abdelwahab replaced Railway's marketing SaaS stack (CMS for site, blog and changelog, email, multi-platform social posting, media library, mini CRM, task tracking, launch planning, calendar, comments, real-time editing) with one agent-built internal tool on Railway. His thesis: agents can build polish, but only if you give them solid abstractions, explicitly ask for product-quality patterns they skip by default, package opinions as skills, and force end-to-end verification. Practical and correct. The one hard number ("700 million tokens" for real-time collaboration) quietly undercuts the "just ask" framing.

## Key Takeaways
- **Stack matters after all.** Not which framework, but that the codebase has solid abstractions so the agent follows existing patterns instead of inventing new ones. His picks: TanStack for web, Payload for content. He chose not to build a CMS from scratch.
- **Patterns agents skip unless asked:**
  - Non-blocking autosave, plus blocking tab close on unsaved changes.
  - Real-time collaboration (built, at ~700M tokens).
  - Optimistic updates with rollback on failure, applied selectively.
  - Undo instead of confirmation dialogs (delayed delete).
  - Archive/unarchive instead of forcing delete.
  - URL state for filters and sorts, so views are shareable.
  - Infinite scroll over "load more."
- **Reference pages:** tell the agent "use page X as the reference" for UI, data fetching and structure. Defines "good" once, yields consistency. Sometimes ignored.
- **Opinions as skills:** two design-engineering skills (UI, typography, layout, error messages; animations) plus Railway's deploy skills.
- **Verification is the most important step.** "Build passed, tests pass" often hides a broken UX. Computer-use-driven end-to-end testing on real infra made it "night and day."

## Architecture & Optimization Mechanics
- **Codebase as prompt.** Consistent abstractions reduce the agent's search space per feature: fewer novel patterns, less drift. This is in-context few-shot via the repo itself.
- **Explicit pattern checklists** compensate for a model prior biased toward minimal working CRUD. The agent can implement optimistic updates trivially; it does not propose them.
- **Verification loop = closed-loop control.** Build, run, observe, fix until the e2e check passes. Tests catch logic; computer use catches UX breakage.
- **Cost reality:** 700M tokens for one feature is not cheap. At frontier pricing that is likely hundreds to low thousands of dollars, which matters when arguing internal tools beat SaaS seats.

## Grounded Context (Web Enrichment)
The tooling claims check out: Payload 3 runs on Railway via official templates, and the in-progress Payload 4.0 previews experimental TanStack Start support plus "Payload Skills" for coding agents and better MCP setup, so his stack is converging with the vendors' own direction. Agent Skills as a portable format is now supported across Claude, Codex CLI, Gemini CLI and Cursor.

His timing checks out: he says the breakthrough came "when GPT-6 came out," and GPT-6 (Astra, then the cheaper Sol/Luna tiers) shipped in September 2026 (see [[2026-09-07-OpenAI-GPT6-Astra-With-Tom-Krcha]] and [[2026-09-23-WorldofAI-GPT-6-Sol-Luna-Opus-5-5-Qwen-4-Trump-SI]]). The broader point (agentic coding plus reliable computer use crossed a usability threshold in 2026) is consistent with the rest of this AIE batch. Also note the speaker is a Railway employee, so "everything runs on Railway" is partly a product demo.

## Real-World Application / Actionable Step
- **For internal research tools (experiment dashboards, eval viewers):** keep a reference page and point the agent at it for every new view. Put URL state on every filter so you can share exact eval slices with collaborators.
- **Keep a "polish checklist" skill** (autosave, optimistic updates, undo, archive, URL state, pagination) and attach it to every UI task.
- **Mandate e2e verification** in the agent's definition of done: run the stack, exercise the feature, fix, repeat.
- **Track tokens per feature.** If a feature costs hundreds of millions of tokens, that is a signal to route boilerplate subtasks to a cheaper model and reserve the frontier model for planning and debugging.
