<p align="center">
  <img src="social-card.png" alt="A civic repair blueprint tracing defects through root cause, correction, prevention, and effectiveness checks" width="100%">
</p>

<h1 align="center">The American Repair Manual — CAPA Edition</h1>

<p align="center"><strong>Find the failure. Trace the cause. Repair the system. Prove the fix held.</strong></p>

<p align="center">
  <a href="index.html">Open the manual</a> ·
  <a href="downloads/THE_AMERICAN_REPAIR_MANUAL_CURRENT.html">Download standalone HTML</a> ·
  <a href="CURRENT_RELEASE.md">Release status</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

A civic quality-assurance framework for repairing American democracy through corrective and preventive action.

The existing self-contained HTML application is the canonical content artifact:

- `index.html`
- `the-american-repair-manual.html`

The application describes 13 major sections and more than 50 policy areas, with PBHP harm reviews, Maybe/Therefore counterarguments, supporting data, and proposed corrective actions. This repository overlay adds the missing repository-level documentation, validation workflow, and a direct downloadable copy of the current manual without rewriting the policy content.

## Related projects

- [Pause Before Harm Protocol](https://github.com/PauseBeforeHarmProtocol/pbhp) — the harm-review protocol used throughout the Manual.
- [The Record](https://github.com/PauseBeforeHarmProtocol/the-record) — the national accountability archive and current reporting layer.
- [The Record — IN-6](https://github.com/PauseBeforeHarmProtocol/the-record-in6) — the Indiana Sixth District accountability archive.
- [Project Shadow](https://github.com/PauseBeforeHarmProtocol/project-shadow) — the companion runtime and evaluation system; repository access is restricted.

## Prepare and validate a release

```bash
python scripts/prepare_release.py
python scripts/validate.py
```

`prepare_release.py` copies the canonical `index.html` into `downloads/THE_AMERICAN_REPAIR_MANUAL_CURRENT.html`, writes a SHA-256 record, and generates `release/CURRENT_RELEASE.json`.

## Evidence boundary

The Manual is a policy and civic-governance project. Its factual claims and proposals must be source-audited and date-bound. A passing HTML or checksum test demonstrates file integrity and application structure, not that every policy claim has been independently validated.

Maintainer: Phillip Linstrum. AI assistance must remain disclosed where used and does not count as independent review.
