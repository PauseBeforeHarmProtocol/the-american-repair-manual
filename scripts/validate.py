#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
files=[root/'index.html',root/'the-american-repair-manual.html']
for p in files: assert p.exists(), p
text=(root/'index.html').read_text(encoding='utf-8',errors='replace')
for marker in ['THE AMERICAN REPAIR MANUAL','CAPA','Pause Before Harm','<meta name="viewport"']:
    assert marker.lower() in text.lower(), marker
assert '<script' in text.lower(), 'interactive application script missing'
assert len(re.findall(r'class="panel',text,re.I)) >= 10, 'expected multi-section application'
assert files[0].read_bytes()==files[1].read_bytes(), 'canonical HTML copies differ'
release=json.loads((root/'release/CURRENT_RELEASE.json').read_text())
download=root/release['download']
assert download.exists()
assert hashlib.sha256(download.read_bytes()).hexdigest()==release['sha256']
secret_patterns=[r'github_pat_[A-Za-z0-9_]+',r'ghp_[A-Za-z0-9]+',r'sk-[A-Za-z0-9]{20,}']
for p in root.rglob('*'):
    if p.is_file() and p.stat().st_size < 20_000_000:
        s=p.read_text(encoding='utf-8',errors='ignore')
        for pat in secret_patterns: assert not re.search(pat,s), f'credential-like string in {p}'
print(json.dumps({'status':'PASS','html_bytes':files[0].stat().st_size,'release_sha256':release['sha256']},indent=2))
