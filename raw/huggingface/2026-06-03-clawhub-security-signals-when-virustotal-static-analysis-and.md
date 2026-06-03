---
source: farmer/huggingface
farmed: 2026-06-03T06:14:02Z
arxiv_id: 2606.01494
url: https://huggingface.co/papers/2606.01494
arxiv_url: https://arxiv.org/abs/2606.01494
date: 2026-06-03
---

# ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree

Agent skills extend AI agents with reusable instructions, tools, scripts, references, and workflows, establishing a security boundary distinct from both model safety and traditional package-malware detection. ClawHub Security Signals is a sanitized dataset of 67,453 latest public OpenClaw skill versions. Each row pairs redacted SKILL.md content and sanitized bundled files where present with a final ClawScan registry verdict and evidence from three scanner families: VirusTotal, static heuristic analysis, and NVIDIA SkillSpector.
  Rather than estimating malicious-skill prevalence, we study scanner disagreement. The three scanners rarely flag the same skills: any pair overlaps on at most 10.4% of their combined positives, only 0.69% of skills are flagged by all three, and 81.9% of flagged skills are identified by a single scanner. The disagreement is structured by attack surface. SkillSpector, which raises semantic agentic-risk advisories rather than malware-reputation signals, is positive for 19,209 of 25,504 suspicious rows (75.3%) but only 14 of 206 malicious rows (6.8%). The malicious-verdict region shows the inverse profile: 150 of 206 malicious rows (72.8%) are VirusTotal-positive, consistent with bundled-code malware evidence.
  These results show that agent-skill security requires layered governance, not single-scanner allow/block decisions. The corpus is released as a sanitized silver-standard dataset: labels are the registry's automated verdicts, not human-annotated ground truth, and the release represents an early, versioned snapshot intended to support the community while a human-annotated subset is developed. Further research is encouraged, including models tailored for skill-security triage.
