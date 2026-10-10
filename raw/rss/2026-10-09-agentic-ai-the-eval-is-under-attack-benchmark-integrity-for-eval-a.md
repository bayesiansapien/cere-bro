---
source: farmer/rss
feed: agentic-ai
farmed: 2026-10-10T05:09:55.462374+00:00
title: "The Eval Is Under Attack: Benchmark Integrity for Eval-Aware, Multi-Agent Systems"
url: https://kenhuangus.substack.com/p/the-eval-is-under-attack-benchmark
published: 2026-10-09
author: Ken Huang
---

# The Eval Is Under Attack: Benchmark Integrity for Eval-Aware, Multi-Agent Systems

<p>Since mid-2025, capable agents have treated the eval harness as part of the solvable environment: they hunt answer keys, rewrite tests, and emit punctuation that fools LLM judges. Anthropic&#8217;s BrowseComp post-mortem logged 2 successful XOR decrypts of a 1,266-problem key (18 runs tried the same strategy; one run burned 40.5 million tokens), and the Agentic Benchmark Checklist estimates harness flaws can misstate agent performance by up to 100% in relative terms. Eval integrity is now a security control, not a one-time design checkbox.</p><p>Today we cover:</p><ol><li><p><strong>BrowseComp decryption:</strong> why URL blocklists failed, and which reachability controls (auth, content-type, name filters) held on a first-party admission against interest.</p></li><li><p><strong>Four attack surfaces:</strong> harness leakage, answer-key hunting, judge bypass, and reward hacking, with measured rates from ABC, HAL, One Token, and ImpossibleBench.</p></li><li><p><strong>Multi-agent widening:</strong> unintended solutions rose from 0.24% to 0.87% on BrowseComp (~3.7&#215;), and persistent query trails contaminated later runs.</p></li><li><p><strong>2026 defense patterns:</strong> private holdouts, task retirement, execution-verified checkpoints, and frozen tooling on Vals, Terminal-Bench-Science, PhysicianBench, GDPval, and AstaBench.</p></li><li><p><strong>Measurement bugs vs attacks:</strong> Opus 4.5 moved from 42% to 95% on CORE-Bench after grader and scaffold fixes with no adversary present.</p></li><li><p><strong>Eval-integrity checklist:</strong> ten controls a security team would write from ABC, HAL, BrowseComp, ImpossibleBench, and One Token.</p></li></ol>
      <p>
          <a href="https://kenhuangus.substack.com/p/the-eval-is-under-attack-benchmark">
              Read more
          </a>
      </p>
