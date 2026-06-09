---
source: farmer/rss
feed: simon-willison
farmed: 2026-06-09T10:56:08.914605+00:00
title: Siri AI at WWDC 2026
url: https://simonwillison.net/2026/Jun/8/wwdc/#atom-everything
published: 2026-06-08
author: Simon Willison
---

# Siri AI at WWDC 2026

<p>Given how badly burned anyone who took Apple's <a href="https://simonwillison.net/2024/Jun/10/apple-intelligence/">2024 WWDC Apple Intelligence announcements</a> at face value was, I'm holding to a strict "I'll believe it when I see it" policy for everything <a href="https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/">they announced today</a>. </p>
<p>The new Siri AI features do at least look feasible with today's technology, especially since Apple are licensing a custom Gemini-derived model that they can run on their own <a href="https://simonwillison.net/2024/Jun/11/private-cloud-compute/">Private Cloud Compute</a>.</p>
<p>It sounds like they'll be taking advantage of vision LLMs to extract information from the user's screen, which neatly sidesteps the need for every existing application to ship custom code in order to integrate with Apple Intelligence. Vision LLMs were a much less mature category in June 2024.</p>
<p>The new Core AI library looks like a good step in enabling developers to finally take full advantage of Apple's hardware for running their own models. It integrates with Meta's open source PyTorch ecosystem, using these <a href="https://apple.github.io/coreai-torch/main/">Core AI PyTorch extensions</a>:</p>
<blockquote>
<p>Core AI PyTorch Extensions (<code>coreai-torch</code>) is a Python package that bridges PyTorch and Core AI. You can use it to bring up an existing PyTorch model — exported as a <code>torch.export.ExportedProgram</code> — into a Core AI <code>AIProgram</code> ready to run on Apple hardware, traversing the FX graph node-by-node and mapping ATen operators to Core AI operations.</p>
</blockquote>
<p>You can install an iOS 27 Developer Beta today, which supposedly has the new features - but you then have to make it through a waiting list for access to the new Siri AI. Aaron Perris from MacRumors reports having <a href="https://twitter.com/aaronp613/status/2064078063814471977">made it off the waitlist</a> so we may start seeing credible reports on how well Siri AI works in the very near future.</p>
<p><strong>Update</strong>: These Private Cloud Compute Gemini models are running in Google Cloud, and using NVIDIA hardware. According to <a href="https://security.apple.com/blog/expanding-pcc/?linkId=100000425571569">Expanding Private Cloud Compute</a> on Apple's Security Research blog:</p>
<blockquote>
<p>For the most demanding tasks, including agentic tool-use and complex reasoning, we worked with Google and NVIDIA to extend our PCC infrastructure to Google Cloud systems using NVIDIA GPUs, while maintaining Apple's powerful security and privacy protections. [...]</p>
<p>PCC on Google Cloud leverages many of the same architectural security patterns as PCC on Apple silicon to implement these layered protections: initial network data parsing for each request happens in a dedicated process within its own namespace, shared inference software is recycled with a short time-to-live duration, and attested keys are held in a separate, dedicated confidential VM isolated from external inputs. [...]</p>
<p>As with PCC on Apple silicon, all binaries will be published for public inspection.</p>
</blockquote>

    <p>Tags: <a href="https://simonwillison.net/tags/vision-llms">vision-llms</a>, <a href="https://simonwillison.net/tags/apple">apple</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/llms">llms</a>, <a href="https://simonwillison.net/tags/gemini">gemini</a>, <a href="https://simonwillison.net/tags/nvidia">nvidia</a>, <a href="https://simonwillison.net/tags/google">google</a></p>
