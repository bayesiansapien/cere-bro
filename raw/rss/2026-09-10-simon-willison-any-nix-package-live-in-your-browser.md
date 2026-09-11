---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-11T11:30:57.177861+00:00
title: Any Nix package, live in your browser
url: https://simonwillison.net/2026/Sep/10/trynix/
published: 2026-09-10
---

# Any Nix package, live in your browser

<p><strong><a href="https://fzakaria.com/2026/09/04/any-nix-package-live-in-your-browser">Any Nix package, live in your browser</a></strong></p>
Farid Zakaria calls this his "<em>magnum opus</em> of Nix work", and I can see why.</p>
<p><a href="https://trynix.dev">trynix.dev</a> provides a <a href="https://github.com/ktock/qemu-wasm">qemu-wasm</a> powered x86_64 Linux virtual machine running entirely in your browser through WebAssembly. That VM can then be booted with <em>any Nix package</em> from the past 13 years. They are URL addressable, so you can navigate to this page:</p>
<p><a href="https://trynix.dev/?pkg=python3%403.6.2">https://trynix.dev/?pkg=python3%403.6.2</a></p>
<p>Then click "Load" and get an interactive shell against a virtual machine running Python 3.6.2 from 2017.</p>
<p>Farid is building all sorts of neat things on top of this. One recent example: <a href="https://fzakaria.com/2026/09/09/review-a-pull-request-by-booting-it">Review a pull request by booting it</a> introduces <a href="https://github.com/marketplace/actions/trynix-preview">trynix-preview</a>, described like this:</p>
<blockquote>
<p>GitHub action that comments a link on a pull request which lets you boot the PR’s build in the browser using <a href="https://trynix.dev/">https://trynix.dev</a>. No servers, just browsers.</p>
</blockquote>

    <p><small></small>Via <a href="https://lobste.rs/s/7lii0g/review_pull_request_by_booting_it">Lobste.rs</a></small></p>


    <p>Tags: <a href="https://simonwillison.net/tags/code-review">code-review</a>, <a href="https://simonwillison.net/tags/linux">linux</a>, <a href="https://simonwillison.net/tags/webassembly">webassembly</a>, <a href="https://simonwillison.net/tags/github-actions">github-actions</a></p>
