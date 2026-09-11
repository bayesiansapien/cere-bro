---
source: farmer/rss
feed: agentic-ai
farmed: 2026-09-11T11:30:54.548621+00:00
title: AI Targeting and Weapons Software: What Anthropic's New Evals Actually Measure
url: https://kenhuangus.substack.com/p/ai-targeting-and-weapons-software
published: 2026-09-11
author: Ken Huang
---

# AI Targeting and Weapons Software: What Anthropic's New Evals Actually Measure

<p>Anthropic's Frontier Red Team just published capability evaluations for tactical intelligence targeting and conventional weapons software. The headline is blunt: models already substitute for scarce human expertise on parts of the kill chain that used to stay expensive by design.  </p><p>I read the full research note as an engineering and security brief, not as a press release. Below the paywall I unpack the eval designs, the numbers that matter, where the simulations understate and overstate risk, and a practical defender checklist you can use when you review product misuse classifiers or open-weights release decisions. </p><p>Source: <a href="https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities">Anthropic research post (Sep 10, 2026)</a>. </p><h2>Outline: what the paid section covers</h2><ol><li><p>Kill-chain map: which steps Anthropic measured (find, fix, engage-adjacent GNC) and which steps remain out of scope. </p></li><li><p>Targeting evals: identity correlation on synthetic multi-platform social data, photo geolocation versus human GeoGuessr baselines, and text geolocation with a sandboxed search tool. </p></li><li><p>Weapons evals: terminal guidance to a vehicle, payload drop within a grenade-like radius, and GPS-denied / spoofed navigation in simulation. </p></li><li><p>Model ordering: where Opus 5, Mythos-class, Sonnet 5, and open-weights (Kimi K3, GLM 5.2) separate, and why Opus wins terminal guidance on process, not just score. </p></li><li><p>Limitations you should keep in the brief: synthetic social data, simulation graphics, no direct uplift measurement, material bottlenecks still bind many actors. </p></li><li><p>Defender and policy stack: classifiers for closed models, open-weights urgency, law-enforcement resilience, compute advantage, and defender-side use of frontier models. </p></li><li><p>Takeaways and references.<br /></p><p> </p></li></ol><p>Reading order for paid subscribers: start with the kill-chain figure, then the two score tables (photo geolocation and terminal guidance), then the Opus process figure if you brief engineers, then the defense-stack figure if you brief leadership. Skip the middle prose only if you already know the Anthropic post.<br /> </p><p>You can unlock the deep dive - and every paid Agentic AI / AI Security post - at 50% off a yearly subscription here: <a href="https://kenhuangus.substack.com/subscribe?coupon=302342d9">50% off annual subscription</a>. </p>
      <p>
          <a href="https://kenhuangus.substack.com/p/ai-targeting-and-weapons-software">
              Read more
          </a>
      </p>
