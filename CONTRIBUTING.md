# Contributing to the Shared AI Engineering Brain

We collaborate on the **Physics** of AI Engineering (Concepts & Tools). We keep our **Execution** (Applied & Sources) private.

## How to Contribute Knowledge

### 1. Identify a Gap
If you are reading a paper or watching a video and realize the vault is missing a core `Concept` or `Tool`, that is your opportunity to contribute.

### 2. Create the Note
- Use the Underscore naming convention: `[[Concepts/Example_Note_Name]]`.
- Follow the existing formatting of notes in that folder.
- Ensure the note is technical and objective. Do not include project-specific details.

### 3. Link the Knowledge
A note is only useful if it is connected.
- Link your new Concept to related `Tools`.
- Update the relevant Map of Content (MOC) in the `/Hubs` folder.

### 4. Submit a Pull Request
- Give your PR a descriptive title: `Add Concept: Late Chunking` or `Update Tool: vLLM v0.5.0`.
- Briefly explain why this addition is valuable to the team.

## Note on Privacy
**NEVER** commit files from these folders:
- `/Applied` (Proprietary designs)
- `/Sources` (Raw transcripts/data)
- `/Daily_Notes` (Personal workspace)

Our `.gitignore` is configured to prevent this, but please double-check before pushing. The fastest safe path is the `kg-contribute` skill, which drafts the note from `CONVENTIONS.md` + `Templates/`, runs a privacy scan, and opens the PR for you.

## Governance — how a PR becomes the bundle

- **Members open PRs; nobody pushes to the default branch.** It is protected: every change needs a PR + 1 approving review + green CI.
- **Nobody hand-edits `okf/`.** The OKF bundle is *generated*. You edit only wikilink source notes under `Concepts/`, `Tools/`, `Hubs/`. On merge, CI runs `okf-build`, validates, and publishes the bundle + interactive graph to GitHub Pages — so the bundle always equals the approved public layer.
- **Two privacy layers:** the `kg-contribute` skill scans your draft *before* the PR; CI (`scripts/okf-validate.py`) re-checks that nothing links into the private layer and that every note is OKF-valid. Maintainer review is the final gate.

### One-time maintainer setup
1. **Pages:** Settings → Pages → Source: **GitHub Actions**.
2. **Branch protection** (require PR + review + the `build` check):
   ```bash
   gh api --method PUT repos/OWNER/REPO/branches/master/protection --input - <<'JSON'
   { "required_status_checks": { "strict": true, "contexts": ["build"] },
     "enforce_admins": false,
     "required_pull_request_reviews": { "required_approving_review_count": 1 },
     "restrictions": null }
   JSON
   ```

---
Happy Engineering!
