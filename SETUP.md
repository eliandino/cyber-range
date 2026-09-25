# Setup: getting this course onto GitHub

## 1. Create the repo on GitHub
1. Go to github.com → **New repository**.
2. Name it `cyber-range` (or anything you like). Public is best for a portfolio.
3. Don't add a README or .gitignore; this folder already has them.

## 2. Push this folder
From inside the unzipped folder:

```bash
git init
git add .
git commit -m "Start course: Cyber Range"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/cyber-range.git
git push -u origin main
```

No terminal handy? On the empty repo page, click **uploading an existing file** and drag the folder contents in.

## 3. Turn on the tracker website (GitHub Pages)
1. Repo → **Settings** → **Pages**.
2. Source: **Deploy from a branch**, branch `main`, folder `/ (root)`.
3. Your tracker will be at `https://YOUR-USERNAME.github.io/cyber-range/tracker/`.

Tracker progress is saved in your browser. Use **Export progress** and commit `progress.json` to keep a backup in the repo.

## 4. Turn on free security features
Repo → **Settings** → **Code security**: enable Dependabot alerts, secret scanning, and push protection.

## 5. Azure account
1. Sign up at azure.microsoft.com/free (students: Azure for Students, no card needed).
2. Immediately: **Cost Management → Budgets → Add**, set a small monthly budget with an email alert at 50% and 90%.
3. Install the Azure CLI and run `az login`.

## Daily workflow
```bash
git pull
# ...do the lab, write notes...
git add .
git commit -m "Module 2: deployed hardened VM with CLI"
git push
```
