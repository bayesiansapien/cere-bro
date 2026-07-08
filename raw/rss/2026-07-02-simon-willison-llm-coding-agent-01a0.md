---
source: farmer/rss
feed: simon-willison
farmed: 2026-07-08T05:20:41Z
title: llm-coding-agent 0.1a0
url: https://simonwillison.net/2026/Jul/2/llm-coding-agent/#atom-everything
published: 2026-07-02
author: 
---

# llm-coding-agent 0.1a0

<p><strong>Release:</strong> <a href="https://github.com/simonw/llm-coding-agent/releases/tag/0.1a0">llm-coding-agent 0.1a0</a></p>
        <p>Another Fable 5 experiment. Now that my <a href="https://llm.datasette.io/">LLM library</a> has evolved into more of an agent framework it's time to see what a simple coding agent would look like built on it.</p>
<p>I started a <a href="https://github.com/simonw/llm-coding-agent/tree/2466fa03ba8e5122c3bfa93d52167d33bce40ac6">new Python library</a> using my <a href="https://github.com/simonw/python-lib-template-repository">python-lib-template-repository</a> GitHub template repository, then ran these two prompts (here's the <a href="https://claude.ai/code/session_01TEUBvBbMipbFSoqjMiJ7ha">Claude Code for web transcript</a>):</p>
<blockquote>
<p><code>Write a spec.md for this project - it will depend on the latest “llm” alpha from PyPI and implement a Claude code style coding agent complete with tools for reading and editing files and executing commands</code></p>
</blockquote>
<p>Then:</p>
<blockquote>
<p><code>Commit the spec, then build it using red/green TDD in a series of sensible commits (each with passing tests and updated docs) - occasionally manually test it using the OpenAI API key in your environment</code></p>
</blockquote>
<p>Here's <a href="https://github.com/simonw/llm-coding-agent/blob/0.1a0/spec.md">the spec</a>, the <a href="https://github.com/simonw/llm-coding-agent/blob/0.1a0/README.md">resulting README file</a>, and the <a href="https://github.com/simonw/llm-coding-agent/commits/0.1a0">sequence of commits</a>.</p>
<p>I've shipped a slop-alpha to PyPI, so you can run the new agent like this:</p>
<pre><code>uvx --prerelease=allow --with llm-coding-agent llm code
</code></pre>
<p>It's pretty good for a first attempt! Here's the (Fable-authored) <a href="https://github.com/simonw/llm-coding-agent/blob/0.1a0/README.md">README</a>, which lists recipes like <code>llm code --yolo</code> and <code>llm code --allow "pytest*" --allow "git diff*"</code>.</p>
<p>It also presents <a href="https://github.com/simonw/llm-coding-agent/blob/0.1a0/README.md#codingagent">a Python API</a> based around a <code>CodingAgent(model="gpt-5.5", root="/path", approve=True).run("Fix the failing test in tests/test_parser.py")</code> class which I didn't ask for but I'm delighted to see implemented.</p>
<p>Here's the suite of tools <a href="https://github.com/simonw/llm-coding-agent/blob/0.1a0/llm_coding_agent/tools.py#L22">it implemented</a>, listed using <code>uvx ... llm tools</code>:</p>
<blockquote>
<p><code>CodingTools_edit_file(path: str, old_string: str, new_string: str, replace_all: bool = False) -&gt; str</code></p>
<p>Replace an exact string in a file.</p>
<p>old_string must match the file contents exactly (including
whitespace) and must identify a unique location unless replace_all
is true. Returns a diff of the change so it can be verified.</p>
<p><code>CodingTools_execute_command(command: str, timeout: int = 120) -&gt; str</code></p>
<p>Run a shell command in the session root directory.</p>
<p>Returns combined stdout and stderr followed by an Exit code line.
timeout is in seconds (maximum 600); on timeout the whole process
tree is killed.</p>
<p><code>CodingTools_list_files(pattern: str = '**/*', path: str = '.') -&gt; str</code></p>
<p>List files matching a glob pattern, newest first.</p>
<p>Skips hidden directories, node_modules, __pycache__ and (in a git
repository) anything covered by .gitignore. Returns at most 200
paths relative to the searched directory.</p>
<p><code>CodingTools_read_file(path: str, offset: int = 0, limit: int = 2000) -&gt; str</code></p>
<p>Read a text file, returning numbered lines like cat -n.</p>
<p>Paths are relative to the session root. Use offset (0-based first
line) and limit (max lines) to page through files too large to read
in one call.</p>
<p><code>CodingTools_search_files(pattern: str, path: str = '.', glob: str = None, max_results: int = 100) -&gt; str</code></p>
<p>Search file contents for a regular expression.</p>
<p>Returns matches as path:line_number:line, capped at max_results.
Use glob (e.g. "*.py") to restrict which files are searched.</p>
<p><code>CodingTools_write_file(path: str, content: str) -&gt; str</code></p>
<p>Create or overwrite a file with the given content.</p>
<p>Parent directories are created as needed. Prefer edit_file for
modifying existing files.</p>
</blockquote>
<p>I tried it out by running <code>llm code --yolo</code> and then prompting:</p>
<blockquote>
<p><code>mkdir /tmp/demo and then in that folder create a simple swiftui CLI app for telling the time in ascii art</code></p>
</blockquote>
<p>Here's <a href="https://gist.github.com/simonw/750009007050124cd1b390cfe8488e41">the transcript</a>, in which GPT-5.5 reasoning notes that "SwiftUI isn't suitable for a true CLI" and then builds an app that outputs this on <code>swift run AsciiTime</code>:</p>
<pre style="font-size: 9px;">
      █    █████         ████     █             █     ███   
     ██    █        █        █   ██      █     ██    █   █  
      █    ████           ███     █             █       █   
      █        █    █        █    █      █      █      █    
     ███   ████          ████    ███           ███   █████
</pre>
    
    
        <p>Tags: <a href="https://simonwillison.net/tags/projects">projects</a>, <a href="https://simonwillison.net/tags/ai">ai</a>, <a href="https://simonwillison.net/tags/generative-ai">generative-ai</a>, <a href="https://simonwillison.net/tags/llm">llm</a>, <a href="https://simonwillison.net/tags/llm-tool-use">llm-tool-use</a>, <a href="https://simonwillison.net/tags/coding-agents">coding-agents</a>, <a href="https://simonwillison.net/tags/claude-code">claude-code</a>, <a href="https://simonwillison.net/tags/claude-mythos-fable">claude-mythos-fable</a></p>
