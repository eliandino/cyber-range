# Cyber Range: White-Hat Security on Azure

A self-paced, project-based course in ethical hacking, Azure, and Python.
Every module ends with a real project that lives in this repo, so finishing the course means finishing a portfolio.

**Student:** Eliezer
**Started:** YYYY-MM-DD
**Status:** Module 1 in progress

Open the [progress tracker](tracker/index.html) to check off labs and, at the end, issue your certificate of completion.

---

## How this course works

1. Work through the modules in order. Each one has a README with objectives, labs, and a portfolio project.
2. Document every project using [`templates/PROJECT_TEMPLATE.md`](templates/PROJECT_TEMPLATE.md) and commit it to that module's `projects/` folder.
3. Check off labs here **and** in the tracker. Commit after every lab so your GitHub activity graph tells the story too.
4. When all eight modules are done, open the tracker and issue your certificate.

## Rules of engagement

- **Only attack systems you own or have written permission to test.** Your Azure lab counts; nothing else does. Follow the [Microsoft Cloud Penetration Testing Rules of Engagement](https://www.microsoft.com/en-us/msrc/pentest-rules-of-engagement).
- **Never commit secrets.** No passwords, keys, `.env` files, or public IPs of live lab machines. The `.gitignore` helps, but check before every push.
- **Control costs.** Set an Azure budget alert on day one. Deallocate VMs when you're done for the day. Delete resource groups when a module is finished.
- **Never expose RDP (3389) or SSH (22) to `0.0.0.0/0`** unless it's a deliberate, short-lived honeypot in Module 4.

---

## Curriculum

### Module 1 · Foundations: Git, Linux, Python
- [ ] Install Git, VS Code, Python 3.12+, and set up this repo on GitHub
- [ ] Linux command line: files, permissions, processes, networking commands
- [ ] Python basics: variables, functions, files, `argparse`, `socket`
- [ ] **Project:** Python TCP port scanner (run only against your own machines)

### Module 2 · Azure Basics
- [ ] Create an Azure free account and a budget alert
- [ ] Deploy a Linux VM in the portal, connect via SSH key
- [ ] Deploy a Windows VM, connect via RDP locked to your IP
- [ ] Network Security Groups, resource groups, Azure CLI
- [ ] **Project:** Hardened Linux VM deployed entirely with Azure CLI, documented

### Module 3 · Networking & Recon
- [ ] TCP/IP, ports, DNS, HTTP fundamentals
- [ ] Nmap scans against your own lab VMs
- [ ] Packet capture and analysis with Wireshark / tcpdump
- [ ] **Project:** Recon report on your own two-VM lab

### Module 4 · SOC Home Lab
- [ ] Log Analytics workspace and Microsoft Sentinel
- [ ] Deploy an intentionally exposed honeypot VM
- [ ] Ingest failed-login logs, write KQL queries
- [ ] Build a workbook / attack map by geolocation
- [ ] **Project:** Azure honeypot + Sentinel SOC lab, with before/after hardening metrics

### Module 5 · Python Security Tools
- [ ] Parse auth logs and flag brute-force patterns
- [ ] File integrity checker with SHA-256 hashes
- [ ] Query a threat-intel API (e.g., AbuseIPDB) for suspicious IPs
- [ ] **Project:** Packaged CLI security toolkit with tests and a README

### Module 6 · Web Application Security
- [ ] Deploy OWASP Juice Shop on your own Azure VM
- [ ] Burp Suite Community basics: proxy, repeater, intruder
- [ ] Work through OWASP Top 10 categories in Juice Shop
- [ ] **Project:** Web app findings report with severity ratings and fixes

### Module 7 · Automation & DevSecOps
- [ ] Infrastructure as code with Bicep (or Terraform)
- [ ] GitHub Actions: deploy your lab from a workflow using OIDC (no stored secrets)
- [ ] Enable secret scanning, Dependabot, and CodeQL on your repos
- [ ] **Project:** One-command lab deployment pipeline

### Module 8 · Capstone
- [ ] Design a small vulnerable environment in Azure
- [ ] Attack it: recon, exploitation, privilege escalation (your lab only)
- [ ] Detect it: Sentinel analytics rules that catch your own attack
- [ ] **Project:** Professional penetration test report + detection write-up
- [ ] 🎓 Issue your certificate of completion

---

## Optional real-world certifications

| When | Cert | Why |
|---|---|---|
| After Module 2 | Microsoft AZ-900 | Proves Azure fundamentals |
| After Module 4 | Microsoft SC-900 | Security, compliance, identity basics |
| After Module 6 | CompTIA Security+ | The standard entry-level security cert |
| After Capstone | SC-200 or eJPT | Blue-team (SOC) or red-team (pentest) path |

## Portfolio index

Update this table as you finish projects. It's what recruiters will read first.

| # | Project | Skills | Link |
|---|---|---|---|
| 1 | Python port scanner | Python, sockets, networking | _pending_ |
| 2 | Hardened Azure VM | Azure CLI, NSGs, SSH | _pending_ |
| 3 | Lab recon report | Nmap, Wireshark | _pending_ |
| 4 | Honeypot SOC lab | Sentinel, KQL, Log Analytics | _pending_ |
| 5 | Security CLI toolkit | Python, testing, threat intel | _pending_ |
| 6 | Web app pentest | OWASP Top 10, Burp Suite | _pending_ |
| 7 | Lab deployment pipeline | Bicep, GitHub Actions, OIDC | _pending_ |
| 8 | Capstone pentest + detection | Red + blue team | _pending_ |
