---
type: validation-log
tags: [testing, validation]
---

# Validation and print test log

**No independently verified physical build, complete Bambu Studio slice, finger-string test or LED fit test has been recorded in this repository.** Do not convert earlier digital claims into PASS without rerunning checks.

For each test, add a separate note from [[templates/Validation_Template]] or append a row here with date, part, printer/material/profile, method, observed evidence, PASS/FAIL/UNKNOWN/BLOCKED, and the associated commit.

| Date | Test | Status | Evidence |
|---|---|---|---|
| 2026-11-14 | Required asset size/SHA-256 verification | PASS (59/59) | [[docs/ASSET_MAP]]; `docs/ASSET_SHA256_MANIFEST.csv`; 9 originals + 49 V4 + 1 V3 ZIP; V1/V2 excluded |
| 2026-11-14 | V3 archive structure/content | PASS | `tar.exe -tf` listed 21 file entries; every entry opened/decompressed, 1,247,730 bytes total |
| 2026-11-14 | Remote commit and asset visibility | PASS | `origin/main` equals `91f7233aceca2251a1f136ffff24f0524421176c`; GitHub listings show 9 originals and 13 shells per V4 side |
| 2026-11-14 | Git LFS V3 configuration | PASS (attribute only) | `git check-attr` reports `filter=lfs`; 45 existing assets tracked; V3 push/readback pending |
| 2026-11-14 | V4 independent release audit | NOT RUN | [[audits/claude/CLAUDE_MASTER_PROMPT]] |
| 2026-11-14 | Full X1C slicer check | NOT RUN | [[docs/RELEASE_GATES]] |
| 2026-11-14 | LED strip and ring fit | BLOCKED | LED hardware dimensions not selected |
| 2026-11-14 | Original finger mount and tendon travel | NOT RUN | Original fingers/assembly not validated |

Also update [[docs/RELEASE_GATES]] and [[HANDOFF]] after every test.
