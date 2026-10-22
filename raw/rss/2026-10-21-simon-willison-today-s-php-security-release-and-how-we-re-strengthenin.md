---
source: farmer/rss
feed: simon-willison
farmed: 2026-10-22T07:28:59.709838+00:00
title: "Today's PHP Security Release, and How We're Strengthening PHP Security"
url: https://simonwillison.net/2026/Oct/21/php-security-release/
published: 2026-10-21
author: 
---

# Today's PHP Security Release, and How We're Strengthening PHP Security

<p><strong><a href="https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/">Today&#x27;s PHP Security Release, and How We&#x27;re Strengthening PHP Security</a></strong></p>
If you're running anything on PHP it's vital you upgrade - today's updates (across the entire PHP 8.x line) address two remote code execution holes, and there have been exploits circulating since last night, thanks to a leak in the coordinated disclosure process.</p>
<p>This post from the PHP Foundation explain what went so wrong:</p>
<blockquote>
<p>On Tuesday, October 20th, at around 15:00 UTC, the two CVE IDs began circulating on online forums and social media. They came with a wrong release time and a wrong CVSS score of 10.0 (the actual score is 9.2). No technical details leaked. In response, the PHP project brought its pre-announcement forward and <a href="https://www.php.net/archive/2026.php#2026-10-20-1">published it at 19:30 UTC</a>. It also moved the release from October 22nd, 14:00 UTC, to October 21st, 14:00 UTC [...]</p>
<p>As a result of the leak and pre-announcement around 20:00 UTC, Calif, one of the security firms that had reported the issues mistakenly published a video. It showed their proof of concept working against a number of targets and revealed a few additional, though limited, details about the vulnerabilities. Copies of the deleted video started circulating on social media soon after. The video contributed to accelerated development of various PoCs (exploitation proof of concepts), which then increased circulation on October 21st.</p>
</blockquote>
<p><a href="https://www.wiz.io/blog/php2shell-php-rce">This article</a> from the team that discovered the original vulnerability includes a more detailed timeline of the original intended responsible disclosure:</p>
<blockquote>
<ul>
<li><strong>August 19, 2026:</strong> Wiz Research discovers the first PHP vulnerability using Wiz Atlas, Gemini 4 Argon, and GPT-5.6 Sol.</li>
<li><strong>August 20, 2026:</strong> Unauthenticated RCE is confirmed against Drupal.</li>
<li><strong>August 21, 2026:</strong> Unauthenticated RCE is confirmed against WordPress.</li>
<li><strong>August 24, 2026:</strong> Wiz Research reports the vulnerabilities to the PHP security team.</li>
<li><strong>September 21, 2026:</strong> PHP acknowledges the reports and begins developing a coordinated fix.</li>
<li><strong>October 21, 2026:</strong> Patched PHP releases become available.</li>
<li><strong>October 21, 2026:</strong> Public disclosure.</li>
</ul>
</blockquote>

    <p><small></small>Via <a href="https://news.ycombinator.com/item?id=50182987">Hacker News</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/open-source">open-source</a>, <a href="https://simonwillison.net/tags/php">php</a>, <a href="https://simonwillison.net/tags/security">security</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/ai-security-research">ai-security-research</a></p>
