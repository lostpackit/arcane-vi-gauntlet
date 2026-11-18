# Copilot SDK — back up local folders

## 2026-11-18T21:59Z
- Action: User requested the three untracked folders be synced and backed up; inspected status, fetched origin, and read required project instructions.
- Result: `HEAD` and `origin/main` both `e177f0f9b42970ae029fc93077f2847ed54c6cff`; no tracked changes at start. The three folders remain untracked and untouched.
- Evidence: `git status --short --branch --ignored`, `git fetch origin`, `git rev-parse HEAD`, `git rev-parse origin/main`.
- Open items: Verify all requested contents, Git ignore rules, file integrity and LFS handling before staging. Preserve release status and other agents' findings.
- Next: Inventory all three directories and their manifests, inspect local and remote risks, then stage safely.
- Sync: LOCAL.

## 2026-11-18T22:02Z — staged backup
- Action: Staged the three requested folders and compared every staged CAD LFS pointer to its local SHA-256 and byte size.
- Result: 118 staged files; 91/91 CAD pointers valid and 27 non-CAD files all below 100 MiB. No existing canonical release files were changed. Git warned that some text files may be checked out with CRLF on Windows.
- Next: Update the inventory to distinguish backed-up source copies from current canonical release files, then commit and push.
- Sync: LOCAL.

## 2026-11-18T22:01Z — V5.2 comparison
- Action: Compared the four committed V5.2 manifest hashes to uniquely named files in the print pack; checked LFS attributes and remote main.
- Result: 4/4 SHA-256 PASS. Sample STL and 3MF paths have the `lfs` filter; remote main remains `e177f0f9b42970ae029fc93077f2847ed54c6cff`. These are backed up in their requested print-pack locations, not relocated into canonical release paths.
- Next: Stage all 118 requested files and validate every CAD pointer.
- Sync: LOCAL.

## 2026-11-18T22:00Z — integrity
- Action: Verified all package manifest entries and scanned file names/text for obvious credential patterns and files above 100 MiB.
- Result: Print pack 42/42, V5 draft 33/33, V5.1 draft 16/16 SHA-256 PASS. Zero obvious sensitive-name or secret-pattern matches and no files over 100 MiB. Canonical V5.2 manifest lists two revised shells and two concept models also named in the print pack; canonical release placement was not performed.
- Next: Compare four V5.2 hashes and stage requested directories through LFS.
- Sync: LOCAL.

## 2026-11-18T21:59Z — inventory
- Action: Listed every file, size, extension, ignore status and available manifest across the three requested folders; inspected LFS rules.
- Result: Audit kit 13 files / 908,371 bytes, print pack 44 / 85,238,280 bytes, draft package 61 / 125,952,729 bytes; total 118 files / 212,099,380 bytes. No ignored files were listed. The print pack contains V5.2-named models and concept mounts; no CAD was moved or altered.
- Next: Validate manifest checksums, content safety, and LFS staging.
- Sync: LOCAL.
