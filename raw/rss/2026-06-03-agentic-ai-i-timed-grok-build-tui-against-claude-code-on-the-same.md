---
source: farmer/rss
feed: agentic-ai
farmed: 2026-06-04T06:39:45.916762+00:00
title: I timed Grok Build TUI against Claude Code on the same task. One was 6x faster.
url: https://kenhuangus.substack.com/p/i-timed-grok-build-tui-against-claude
published: 2026-06-03
author: Ken Huang
---

# I timed Grok Build TUI against Claude Code on the same task. One was 6x faster.

<p><em>A small benchmark I ran in WSL on June 3, 2026. Both tools, one prompt, three runs each.</em></p><p>I keep two coding CLIs on this machine: Grok Build TUI and Claude Code. Both take a prompt and write code. I wanted a number, not a vibe, so I gave them the same task, timed each the same way, and ran what they produced. The headline: Claude returned finished, correct code about six times faster. The interesting part is why, and it is not what the headline suggests.</p><h2>The setup</h2><p>Both tools live in WSL Ubuntu and were already authenticated. Grok is the <code>grok</code> binary (Grok Build TUI, version 0.2.20). Claude is the <code>claude</code> Code CLI. I drove both in headless mode so no human sat in the loop, and I measured the full process from launch to exit.</p><h2>The program I asked for</h2><p>I picked a task that is small enough to finish fast and specific enough to check: an LRU cache with tests. Here is the kind of solution both tools were asked to write. First the cache itself, built on an ordered dictionary so reordering is cheap.</p><pre><code>from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = OrderedDict()

    def get(self, key):
        if key not in self.store:
            return None
        self.store.move_to_end(key)   # mark as most-recently used
        return self.store[key]</code></pre><p>The <code>store</code> is an <code>OrderedDict</code>, which remembers insertion order and lets you shove a key to the end in O(1). On a <code>get</code>, <code>move_to_end</code> is the whole trick: a read counts as recent use, so the key you just touched is now the safest from eviction. Drop that one line and your cache evicts the wrong thing under read-heavy load, which is the bug that makes an LRU cache fail with no warning.</p><pre><code>    def put(self, key, value):
        if key in self.store:
            self.store.move_to_end(key)
        self.store[key] = value
        if len(self.store) &gt; self.capacity:
            self.store.popitem(last=False)   # drop least-recently used</code></pre><p><code>put</code> writes the value, then checks size. <code>popitem(last=False)</code> pops from the front, which is the least-recently used end. The order matters: you insert first and evict second, so a fresh write never evicts itself when the cache is full.</p><p>The task also asked for asserts that exercise the real behavior, not just a happy path.</p><pre><code>if __name__ == "__main__":
    c = LRUCache(2)
    c.put("a", 1); c.put("b", 2)
    assert c.get("a") == 1     # touching "a" makes "b" the oldest
    c.put("c", 3)              # so "b" gets evicted, not "a"
    assert c.get("b") is None
    assert c.get("a") == 1 and c.get("c") == 3
    print("ALL PASS")</code></pre><p>The test that matters is the third line. Reading <code>a</code> before inserting <code>c</code> flips which key is oldest, so a correct cache evicts <code>b</code> and a broken one evicts <code>a</code>. If a tool skips that ordering case, its code looks right and fails in production. Both tools got it.</p><h2>How I timed it</h2><p>I wrapped each process launch in a timer and took the median of three runs, so one slow network blip could not decide the result.</p><pre><code>import subprocess, time, statistics

def bench(cmd, runs=3):
    times = []
    for _ in range(runs):
        t0 = time.perf_counter()
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        times.append(time.perf_counter() - t0)
    return statistics.median(times), out.stdout</code></pre><p><code>time.perf_counter()</code> brackets the whole subprocess, so both tools are judged on the same clock: launch to exit, network and all. The median of three runs is the return value. I used wall-clock for both rather than trusting each tool's self-reported timing, because a fair race needs one stopwatch, not two.</p><pre><code>grok_cmd   = ["grok", "-p", PROMPT, "--disable-web-search", "--always-approve"]
claude_cmd = ["claude", "-p", PROMPT, "--output-format", "json"]

grok_median,   grok_code   = bench(grok_cmd)
claude_median, claude_code = bench(claude_cmd)</code></pre><p>Same <code>PROMPT</code> string into both. I disabled web search on grok so it could not wander off to read the internet, and auto-approved its tool calls so it never blocked waiting for me. Claude ran in plain print mode with JSON output, which hands back token counts and a self-reported duration I could cross-check against my stopwatch.</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!AOlJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1b1ca8a-0bc7-4d84-ac6f-ad1018f418ec_2904x744.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Benchmark method: one prompt into both headless CLIs, time each over three runs, run the output, take the median" class="sizing-normal" height="744" src="https://substackcdn.com/image/fetch/$s_!AOlJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1b1ca8a-0bc7-4d84-ac6f-ad1018f418ec_2904x744.png" title="Benchmark method: one prompt into both headless CLIs, time each over three runs, run the output, take the median" width="2904" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>The numbers</h2><p></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/i-timed-grok-build-tui-against-claude">
              Read more
          </a>
      </p>
