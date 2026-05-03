# cere-bro starter

This is a cere-bro starter kit. The wiki has not been configured yet.

**First step: run `/bootstrap`.**

Bootstrap will ask for your research focus, topics, and GitHub details, then generate your customized `CLAUDE.md` to replace this file. Every subsequent session will use that customized file as its operating instructions.

---

## Skills available

- `/bootstrap` — one-time setup; run this first
- `/ingest` — process raw source files into wiki pages
- `/digest` — write the daily digest from available sources
- `/publish` — deploy the Astro site to GitHub Pages
- `/lint` — health-check the wiki

---

## Until bootstrap runs

Do not attempt to ingest, write digests, or deploy. The wiki structure, topic hierarchy, and site configuration all depend on the bootstrap output.

If you see this file after running bootstrap, it was not replaced correctly — re-run `/bootstrap`.
