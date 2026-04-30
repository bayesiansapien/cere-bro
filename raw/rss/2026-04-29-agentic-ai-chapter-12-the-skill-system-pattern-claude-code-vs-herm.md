---
source: farmer/rss
feed: agentic-ai
farmed: 2026-04-30T00:00:00+00:00
title: "Chapter 12: The Skill System Pattern (Claude Code vs. Hermes Agent)"
url: https://kenhuangus.substack.com/p/chapter-12-the-skill-system-pattern
published: 2026-04-29
author: Ken Huang
---

# Chapter 12: The Skill System Pattern (Claude Code vs. Hermes Agent)

<h2>1. Pattern Summary</h2><p>The skill system is how agents accumulate and reuse procedural knowledge. A skill is a named, versioned, markdown-formatted procedure that the agent can discover, load, and follow &#8212; turning a one-time solution into a reusable capability. The pattern matters because agents that can only act on in-context instructions are bounded by what the user types; agents with a skill library can draw on accumulated expertise across thousands of past sessions. This chapter covers new ground: the full skill lifecycle as a first-class harness pattern, from SKILL.md frontmatter through progressive disclosure, agent-managed creation, slash command invocation, security scanning, and the Skills Hub marketplace. None of this appeared in chapters 1&#8211;11 except as brief mentions.</p><h2>2. Claude Code Implementation</h2><p>Claude Code's skill primitive is the <code>CLAUDE.md</code> file. Any directory in the project tree can contain a <code>CLAUDE.md</code>, and the harness auto-discovers and injects all of them at session start via <code>startRelevantMemoryPrefetch()</code>.</p><pre><code>// src/QueryEngine.ts &#8212; session-scoped dedup set prevents re-injection
private loadedNestedMemoryPaths = new Set&lt;string&gt;()

// src/Tool.ts &#8212; passed through ToolUseContext to every tool call
/**
 * CLAUDE.md paths already injected as nested_memory attachments this
 * session. Dedup for memoryFilesToAttachments &#8212; readFileState is an LRU
 * that evicts entries in busy sessions, so its .has() check alone can
 * re-inject the same CLAUDE.md dozens of times.
 */
loadedNestedMemoryPaths?: Set&lt;string&gt;</code></pre><p>The <code>discoveredSkillNames</code> set feeds telemetry so Anthropic can track which skills are actually being used:</p><pre><code>// src/QueryEngine.ts &#8212; telemetry only, not used for logic
private discoveredSkillNames = new Set&lt;string&gt;()

// In processUserInputContext:
discoveredSkillNames: this.discoveredSkillNames,</code></pre><p>Slash commands are loaded from the filesystem via <code>getSlashCommandToolSkills()</code>:</p><pre><code>// src/commands.js &#8212; discovers skills for /skill-name invocation
export async function getSlashCommandToolSkills(cwd: string): Promise&lt;Skill[]&gt; {
  // Loads from: built-in skills, .claude/skills/, remote skill directories
  // Returns Skill[] for registration as slash commands
}</code></pre><p>The design is intentionally minimal. CLAUDE.md files are static markdown &#8212; the agent reads them but cannot create or modify them. There is no security scanner, no hub, no trust model, and no version field. The harness treats CLAUDE.md as a memory attachment, not a first-class capability primitive.</p><p><strong>Limitations:</strong> Static files only. No agent creation. No security scanning. No hub or marketplace. No platform filtering. No version pinning. No progressive disclosure &#8212; the full file is always injected.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes treats skills as a first-class harness subsystem with five distinct components. Each is worth examining in detail.</p><h3>a) SKILL.md Format and Progressive Disclosure</h3><p>Every skill is a directory containing a <code>SKILL.md</code> file with YAML frontmatter:</p><pre><code># ~/.hermes/skills/ransomware-response/SKILL.md
---
name: ransomware-response
description: Structured response procedure for active ransomware incidents
version: 1.2.0
platforms: [linux, macos]          # skip on Windows &#8212; different isolation tools
prerequisites:
  commands: [volatility3, yara]    # advisory: warn if missing, don't block
required_environment_variables:
  - name: SIEM_API_KEY
    prompt: "Enter your SIEM API key"
    help: "https://docs.yoursiem.com/api-keys"
  - name: EDR_ENDPOINT
    prompt: "Enter EDR API endpoint URL"
setup:
  collect_secrets:
    - env_var: SIEM_API_KEY
      prompt: "SIEM API key for log ingestion"
      secret: true
      provider_url: "https://docs.yoursiem.com/api-keys"
metadata:
  hermes:
    tags: [incident-response, ransomware, forensics]
    related_skills: [memory-forensics, network-isolation]
---

# Ransomware Response Procedure

## Trigger Conditions
Invoke this skill when: file encryption activity detected, ransom note found,
lateral movement from a compromised host, or EDR alert severity &gt;= CRITICAL.

## Step 1: Contain
...</code></pre><p>The <code>_get_required_environment_variables()</code> function normalizes all three ways a skill can declare secrets &#8212; <code>required_environment_variables</code>, <code>setup.collect_secrets</code>, and legacy <code>prerequisites.env_vars</code> &#8212; into a single canonical list:</p><pre><code># hermes-agent/tools/skills_tool.py
def _get_required_environment_variables(
    frontmatter: Dict[str, Any],
    legacy_env_vars: List[str] | None = None,
) -&gt; List[Dict[str, Any]]:
    # Merges required_environment_variables + setup.collect_secrets + legacy prereqs
    # Deduplicates by env var name, preserves prompt/help/required_for metadata
    # Returns: [{"name": "SIEM_API_KEY", "prompt": "...", "help": "..."}, ...]</code></pre><p>Discovery uses a four-tier progressive disclosure architecture that keeps token costs low:</p><pre><code>Tier 0: skills_categories()  &#8594; category names + skill counts only
Tier 1: skills_list()        &#8594; name + description per skill (no body)
Tier 2: skill_view(name)     &#8594; full SKILL.md content + linked file list
Tier 3: skill_view(name, file_path="references/ioc-formats.md")
                             &#8594; individual supporting file on demand</code></pre><p><code>_find_all_skills()</code> does the heavy lifting for tiers 0 and 1:</p><pre><code># hermes-agent/tools/skills_tool.py
def _find_all_skills(*, skip_disabled: bool = False) -&gt; List[Dict[str, Any]]:
    # rglob("SKILL.md") across ~/.hermes/skills/ + external dirs
    # Skips: .git, .github, .hub directories
    # Filters: skill_matches_platform(frontmatter) &#8212; checks sys.platform
    # Deduplicates: seen_names set (local dir wins over external)
    # Returns: [{"name": ..., "description": ..., "category": ...}]
    # Reads only first 4000 chars of each SKILL.md &#8212; enough for frontmatter</code></pre><p>The platform filter is a first-class feature. A skill with <code>platforms: [macos]</code> is invisible on Linux &#8212; it never appears in <code>skills_list()</code>, never registers as a slash command, and never gets preloaded. This matters for cyber skills that use platform-specific forensic tools.</p><h3>b) Agent-Managed Creation: skill_manage()</h3><p>The agent can create, edit, patch, delete, and add supporting files to skills. This is the self-improvement loop: after solving a novel problem, the agent codifies the approach as a reusable skill.</p><pre><code># hermes-agent/tools/skill_manager_tool.py
def _atomic_write_text(file_path: Path, content: str, encoding: str = "utf-8") -&gt; None:
    """
    Write via tempfile + os.replace() &#8212; never leaves a partial file on disk.
    If the process is killed mid-write, the original file is untouched.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_path = tempfile.mkstemp(
        dir=str(file_path.parent),
        prefix=f".{file_path.name}.tmp.",
    )
    try:
        with os.fdopen(fd, "w", encoding=encoding) as f:
            f.write(content)
        os.replace(temp_path, file_path)   # atomic on POSIX
    except Exception:
        os.unlink(temp_path)               # clean up on failure
        raise</code></pre><p>Every write &#8212; create, edit, patch, write<em>file &#8212; goes through `</em>atomic<em>write</em>text`. After the write, the skill is immediately security-scanned. If the scan blocks it, the write is rolled back:</p><pre><code># hermes-agent/tools/skill_manager_tool.py
def _create_skill(name: str, content: str, category: str = None) -&gt; Dict[str, Any]:
    # 1. Validate name (lowercase, hyphens/dots/underscores, max 64 chars)
    # 2. Validate frontmatter (YAML parses, has name + description, has body)
    # 3. Check for name collision across all skill dirs
    # 4. Write SKILL.md atomically
    skill_dir.mkdir(parents=True, exist_ok=True)
    _atomic_write_text(skill_md, content)

    # 5. Security scan &#8212; roll back the entire directory on block
    scan_error = _security_scan_skill(skill_dir)
    if scan_error:
        shutil.rmtree(skill_dir, ignore_errors=True)   # full rollback
        return {"success": False, "error": scan_error}

    return {"success": True, "message": f"Skill '{name}' created.", ...}</code></pre><p>The same rollback pattern applies to <code>_edit_skill</code> (restores original content) and <code>_write_file</code> (deletes the new file or restores the previous version). The agent cannot leave the skill library in a partially-written state.</p><p>Supporting files live in four allowed subdirectories &#8212; <code>references/</code>, <code>templates/</code>, <code>scripts/</code>, <code>assets/</code> &#8212; and path traversal is explicitly blocked:</p><pre><code># hermes-agent/tools/skill_manager_tool.py
ALLOWED_SUBDIRS = {"references", "templates", "scripts", "assets"}

def _validate_file_path(file_path: str) -&gt; Optional[str]:
    if ".." in Path(file_path).parts:
        return "Path traversal ('..') is not allowed."
    if Path(file_path).parts[0] not in ALLOWED_SUBDIRS:
        return f"File must be under one of: {', '.join(sorted(ALLOWED_SUBDIRS))}"</code></pre><h3>c) Slash Command Invocation</h3><p><code>scan_skill_commands()</code> builds the <code>/command &#8594; skill</code> mapping at session start:</p><pre><code># hermes-agent/agent/skill_commands.py
def scan_skill_commands() -&gt; Dict[str, Dict[str, Any]]:
    """
    Walk ~/.hermes/skills/ + external dirs, parse frontmatter, build mapping.
    Skips: .git/.github/.hub dirs, platform-incompatible skills, disabled skills.
    Normalizes: spaces/underscores &#8594; hyphens, strips non-alnum chars.
    Returns: {"/ransomware-response": {"name": ..., "skill_md_path": ..., ...}}
    """</code></pre><p>When the user types <code>/ransomware-response</code>, <code>build_skill_invocation_message()</code> loads the full skill content and formats it as a system message:</p><pre><code># hermes-agent/agent/skill_commands.py
def build_skill_invocation_message(
    cmd_key: str,
    user_instruction: str = "",
    task_id: str | None = None,
) -&gt; Optional[str]:
    # Loads skill via skill_view() (tier 2 &#8212; full content + linked file list)
    # Injects resolved config values from ~/.hermes/config.yaml
    # Appends setup notes if required env vars are missing
    # Lists supporting files the agent can load on demand (tier 3)
    activation_note = (
        f'[SYSTEM: The user has invoked the "{skill_name}" skill, indicating they want '
        "you to follow its instructions. The full skill content is loaded below.]"
    )
    return _build_skill_message(loaded_skill, skill_dir, activation_note, user_instruction)</code></pre><p>Skills can also be preloaded at session start via <code>--skill ransomware-response</code> on the CLI, which calls <code>build_preloaded_skills_prompt()</code>. The activation note changes to signal session-wide guidance rather than a one-shot invocation.</p><h3>d) Security Scanning: skills_guard.py</h3><p>Every externally-sourced skill &#8212; hub installs, community downloads, and agent-created skills &#8212; passes through <code>scan_skill()</code> before installation. The scanner uses regex-based static analysis across nine threat categories:</p><pre><code># hermes-agent/tools/skills_guard.py
THREAT_PATTERNS = [
    # Exfiltration: curl/wget/requests with secret env vars
    (r'curl\s+[^\n]*\$\{?\w*(KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL|API)',
     "env_exfil_curl", "critical", "exfiltration",
     "curl command interpolating secret environment variable"),

    # Injection: prompt injection patterns
    (r'ignore\s+(?:\w+\s+)*(previous|all|above|prior)\s+instructions',
     "prompt_injection_ignore", "critical", "injection",
     "prompt injection: ignore previous instructions"),

    # Destructive: filesystem damage
    (r'rm\s+-rf\s+/',
     "destructive_root_rm", "critical", "destructive",
     "recursive delete from root"),

    # Persistence: cron, shell rc files, SSH backdoors
    (r'authorized_keys',
     "ssh_backdoor", "critical", "persistence",
     "modifies SSH authorized keys"),

    # Network: reverse shells and tunnels
    (r'/bin/(ba)?sh\s+-i\s+.*&gt;/dev/tcp/',
     "bash_reverse_shell", "critical", "network",
     "bash interactive reverse shell via /dev/tcp"),

    # Obfuscation: eval, base64 decode pipes, chr() building
    (r'base64\s+(-d|--decode)\s*\|',
     "base64_decode_pipe", "high", "obfuscation",
     "base64 decodes and pipes to execution"),

    # Supply chain: curl/wget piped to shell
    (r'curl\s+[^\n]*\|\s*(ba)?sh',
     "curl_pipe_shell", "critical", "supply_chain",
     "curl piped to shell (download-and-execute)"),

    # Privilege escalation: sudo, NOPASSWD, SUID
    (r'NOPASSWD',
     "nopasswd_sudo", "critical", "privilege_escalation",
     "NOPASSWD sudoers entry (passwordless privilege escalation)"),

    # Credential exposure: hardcoded secrets, embedded private keys
    (r'-----BEGIN\s+(RSA\s+)?PRIVATE\s+KEY-----',
     "embedded_private_key", "critical", "credential_exposure",
     "embedded private key"),
    # ... 80+ more patterns across all categories
]</code></pre><p>The install policy maps trust level &#215; verdict to a decision:</p><pre><code># hermes-agent/tools/skills_guard.py
INSTALL_POLICY = {
    #                  safe      caution    dangerous
    "builtin":       ("allow",  "allow",   "allow"),    # ships with Hermes
    "trusted":       ("allow",  "allow",   "block"),    # openai/skills, anthropics/skills
    "community":     ("allow",  "block",   "block"),    # everything else
    "agent-created": ("allow",  "allow",   "ask"),      # agent writes: ask on dangerous
}</code></pre><p><code>should_allow_install()</code> returns a three-way decision: <code>True</code> (allow), <code>False</code> (block), or <code>None</code> (ask user):</p><pre><code># hermes-agent/tools/skills_guard.py
def should_allow_install(result: ScanResult, force: bool = False) -&gt; Tuple[bool, str]:
    policy = INSTALL_POLICY.get(result.trust_level, INSTALL_POLICY["community"])
    vi = VERDICT_INDEX.get(result.verdict, 2)   # safe=0, caution=1, dangerous=2
    decision = policy[vi]

    if decision == "allow":
        return True, f"Allowed ({result.trust_level} source, {result.verdict} verdict)"
    if force:
        return True, f"Force-installed despite {result.verdict} verdict"
    if decision == "ask":
        return None, f"Requires confirmation ({result.trust_level} source + {result.verdict} verdict)"
    return False, f"Blocked ({result.trust_level} source + {result.verdict} verdict). Use --force to override."</code></pre><p>The scanner also detects invisible Unicode characters (zero-width spaces, RTL overrides, etc.) used for text-hiding injection attacks &#8212; a threat vector that regex alone cannot catch.</p><h3>e) Skills Hub: GitHubSource, WellKnownSkillSource, HubLockFile</h3><p>The Skills Hub provides a marketplace for discovering and installing community skills. <code>GitHubSource</code> is the primary adapter:</p><pre><code># hermes-agent/tools/skills_hub.py
class GitHubSource(SkillSource):
    # Default taps &#8212; repos scanned when searching for skills
    DEFAULT_TAPS = [
        {"repo": "openai/skills", "path": "skills/"},
        {"repo": "anthropics/skills", "path": "skills/"},
        {"repo": "VoltAgent/awesome-agent-skills", "path": "skills/"},
        {"repo": "garrytan/gstack", "path": ""},
    ]

    def trust_level_for(self, identifier: str) -&gt; str:
        # identifier: "owner/repo/path/to/skill"
        repo = "/".join(identifier.split("/", 2)[:2])
        return "trusted" if repo in TRUSTED_REPOS else "community"
        # TRUSTED_REPOS = {"openai/skills", "anthropics/skills"}</code></pre><p><code>GitHubAuth</code> tries four authentication methods in order: <code>GITHUB_TOKEN</code> env var &#8594; <code>gh auth token</code> CLI &#8594; GitHub App JWT &#8594; anonymous (60 req/hr). This means the hub works out of the box for most users without any configuration.</p><p><code>WellKnownSkillSource</code> implements the open <code>/.well-known/skills/index.json</code> standard, allowing any domain to publish a skill registry:</p><pre><code># hermes-agent/tools/skills_hub.py
class WellKnownSkillSource(SkillSource):
    """
    Any domain can expose skills at /.well-known/skills/index.json.
    Format: {"skills": [{"name": "...", "description": "...", "files": ["SKILL.md"]}]}
    Skills are fetched from /.well-known/skills/&lt;skill-name&gt;/SKILL.md
    Trust level: always "community" &#8212; scan before install.
    """
    BASE_PATH = "/.well-known/skills"</code></pre><p><code>HubLockFile</code> tracks provenance of every installed hub skill in <code>~/.hermes/skills/.hub/lock.json</code>:</p><pre><code># hermes-agent/tools/skills_hub.py
class HubLockFile:
    """Manages skills/.hub/lock.json &#8212; tracks provenance of installed hub skills."""

    def record_install(self, name, source, identifier, trust_level,
                       scan_verdict, skill_hash, install_path, files, metadata=None):
        # Writes: source, identifier, trust_level, scan_verdict,
        #         content_hash (SHA-256), install_path, files list,
        #         installed_at, updated_at
        # content_hash enables tamper detection on subsequent loads</code></pre><p>The lock file is the audit trail for the skill library. If a skill is modified after installation, the content hash mismatch is detectable. Skills that fail the hash check can be quarantined to <code>~/.hermes/skills/.hub/quarantine/</code> pending re-scan.</p><h2>4. Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!OGHp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76e62e4d-6bb1-489e-9717-30a819beaa1d_1051x717.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="717" src="https://substackcdn.com/image/fetch/$s_!OGHp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76e62e4d-6bb1-489e-9717-30a819beaa1d_1051x717.png" title="Comparison table" width="1051" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p><strong>Use Claude Code's CLAUDE.md approach when:</strong></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-12-the-skill-system-pattern">
              Read more
          </a>
      </p>