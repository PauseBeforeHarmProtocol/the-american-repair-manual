#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, shutil
from pathlib import Path
root=Path(__file__).resolve().parents[1]
source=root/'index.html'
assert source.exists(), source
out=root/'downloads'/'THE_AMERICAN_REPAIR_MANUAL_CURRENT.html'
out.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(source,out)
h=hashlib.sha256(out.read_bytes()).hexdigest()
(out.with_suffix(out.suffix+'.sha256')).write_text(f'{h}  {out.name}\n',encoding='utf-8')
release=root/'release'; release.mkdir(exist_ok=True)
meta={'schema':'american-repair-manual-release-v1','prepared':'2026-07-18','source':'index.html','download':str(out.relative_to(root)),'bytes':out.stat().st_size,'sha256':h,'claim_boundary':'file integrity and structure only; policy content not independently validated'}
(release/'CURRENT_RELEASE.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
print(json.dumps(meta,indent=2))
