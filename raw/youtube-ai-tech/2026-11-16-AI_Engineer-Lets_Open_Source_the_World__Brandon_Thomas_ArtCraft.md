# Let's Open Source the World: Brandon Thomas, ArtCraft

**Channel:** AI Engineer
**Published:** 2026-11-16
**Source:** https://www.youtube.com/watch?v=UCL4K36SHp0

## TL;DR
Brandon Thomas (ex-Square infra, ArtCraft founder) used coding agents to build open-source, Rust-native "clean-room" clones of Adobe's Creative Suite: Photoshop, Premiere, InDesign, Animate. He then went on to Office, Figma, Acrobat and CAD. The suite went viral. His thesis is that agentic coding collapses the cost of rebuilding entrenched rent-seeking software, so users can own and reshape their apps again, as on the pre-Web-2.0 internet. His stated parity (60% of Photoshop) and adoption numbers are self-reported. The legal status of AI-generated "clean room" clones is unresolved.

## Key Takeaways
- **Origin insight:** ArtCraft's filmmaker users (micro-drama studios doing $30-50K/month of fulfillment) were vibe-coding their own workflows on top of its open APIs. Non-engineers will customize software if it is open and agent-addressable.
- **Build method:** one large spec prompt per app covering:
  - UI/UX separated from the core
  - every tool MCP- and CLI-addressable
  - per-tool plans, data structures and file-format importers
  A usable Photoshop approximation appeared within 24 hours. Feature parity is now about 60% and climbing.
- **Claimed scale:**
  - 300K GitHub stars and 4,000 contributors
  - 1.7M downloads/day
  - 25% of users on Linux
  - 300 community apps
  - A community member is rebuilding Unreal Engine in Rust on 40 machines.
- **Why Rust:** native performance for creative apps (Electron is too slow), low defect rate, cross-platform including NetBSD and tablets, and WASM for the web. Agents drive Rust fine without the team knowing it. The pain point is compile times and CI capacity, so they run their own colocated runners.
- **Agent vs human review rule:**
  - Humans own schema migrations, API design and backend state.
  - Agents run fully autonomously on "immutable" artifacts like desktop apps and games.
- **Autocraft:** a soon-to-be-open-source autonomous software factory that ingests issues, triages, develops agentically, and logs every decision as eval and post-training data.
- **Side benefits:** they added locales Adobe never supported (Arabic InDesign) and revived end-of-life apps (Adobe Animate) for studios that depend on them.

## Architecture & Optimization Mechanics
- **MCP/CLI-first app design** turns every GUI app into an agent tool surface. The app becomes an environment for agents, not just a product for humans.
- **Decision logs as training data:** Autocraft records triage and implementation decisions to post-train on its own decision trees. This is a self-distillation flywheel: cheap agent runs produce labeled trajectories for smaller specialized models.
- **Risk partitioning by mutability** (autonomous on stateless client code, human-gated on schemas and APIs) is a practical way to decide where to spend expensive human or large-model verification.

## Grounded Context (Web Enrichment)
Coverage from Phoronix, TweakTown, Latent Space and others confirms the launch in early October 2026. The suite (PhotoCraft, FilmCraft and others) is written in Rust and was built with Claude Opus 5.5. Independent star counts are far lower than the talk's "300K." Reports cite about 21.5K to 43K stars for PhotoCraft in the first weeks, so treat his aggregate numbers as unverified or suite-wide at best. Reviewers call the builds early alpha: Content-Aware Fill is missing, and the "10x faster startup than Photoshop" claim is his own. Phoronix flags real legal exposure. Whether an LLM trained on Adobe tutorials and docs can produce a genuine clean-room implementation is untested in court.

## Real-World Application / Actionable Step
- **Build your research tooling MCP/CLI-first.** For your compression and routing experiment harness, expose quantize, prune, eval and route-sweep as MCP tools. Agents can then run overnight sweeps without a human, which is the "immutable artifact" category.
- **Copy the decision-log flywheel.** Log every routing decision with its outcome (accepted or escalated) as labeled data, and periodically distill a smaller router from those logs.
- **Use the mutability rule for agent autonomy:** fully autonomous for eval scripts and plots; human-gated for anything touching shared datasets, model registries or serving configs.
