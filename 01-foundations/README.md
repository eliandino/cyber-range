# Module 1 · Foundations: Git, Linux, Python

**Time:** ~2 weeks · **Cost:** free

## Objectives
- Use Git and GitHub daily: commit, push, branch, pull request.
- Move around a Linux shell comfortably.
- Write small Python scripts that read input, handle errors, and talk to the network.

## Labs
1. **Git setup.** Push this repo (see `SETUP.md`). Make a branch, edit this file, open a pull request, merge it.
2. **Linux.** Install WSL (Windows) or use a terminal (Mac/Linux). Practice: `ls -la`, `chmod`, `chown`, `ps`, `top`, `grep`, `find`, `ip a`, `ss -tulpn`, `curl`. Free practice: OverTheWire *Bandit* levels 0–10.
3. **Python.** Write three scripts: a word counter for a text file, a password strength checker, and a script that resolves a hostname with `socket.gethostbyname`.

## Portfolio project: TCP port scanner
Starter code is in `projects/port-scanner/`. Your job is to extend it:
- [ ] Add a `--timeout` flag
- [ ] Scan ports concurrently with `concurrent.futures.ThreadPoolExecutor`
- [ ] Show the common service name for each open port
- [ ] Save results to JSON with `--output`
- [ ] Write the project README using the template

Only scan `127.0.0.1`, your own home machine, or your own lab VMs.

## Resources
- *Automate the Boring Stuff with Python* (free online)
- OverTheWire Bandit
- GitHub Skills: "Introduction to GitHub"
