# Copilot SDK — original finger reference

## 2026-11-27 09:28 UTC
- Action: Inspected repository state and required project context, fetched and fast-forwarded remote `main`, and located the owner-supplied 3MF.
- Result: `main` fast-forwarded from `be4be22` to `491ee0e653da0dc68fc7fac9271a255680783704`; worktree was clean before this record. The supplied 3MF exists (192,851,495 bytes); a same-named original is tracked in `originals/`. Their content has not yet been compared.
- Owner instruction: This is the original model used as a reference guide; only the fingers remain correct for this project, and the model should be used only as a reference for the fingers. Preserve the distinction between owner guidance and independently tested compatibility.
- Next: Compare source and tracked original hashes and verify remote LFS availability before documenting or uploading anything.
- Sync: LOCAL.

## 2026-11-27 09:30 UTC — cleanup
- Action: Removed the explicitly named isolated original-model LFS readback cache after verifying the remote object.
- Result: Temporary cache removed; no project or source CAD file deleted.
- Next: Validate and push the documentation and handoff updates.
- Sync: LOCAL.

## 2026-11-27 09:30 UTC — documentation verification
- `git diff --check` passed; the original 3MF link target exists. Status listed only the five intended modified documents and this new session note.
- The original file and release gates have no changes; `git lfs ls-files` reported 190 entries.
- Next: Fetch, commit, push and verify. Sync: LOCAL.

## 2026-11-27 09:30 UTC — remote refresh
- `git fetch origin` succeeded; both local HEAD and fetched `origin/main` are `491ee0e653da0dc68fc7fac9271a255680783704`.
- Next: Commit and push the verified documentation, then verify the remote ref. Sync: LOCAL.

## 2026-11-27 09:30 UTC — commit
- Staged the six intended documentation/session paths; `git diff --cached --check` passed.
- Created commit `1d62bcf6c0915c8c5f19d5d933e34ce9937e992b`. Next: push and verify. Sync pending push.

## 2026-11-27 — documentation
- Action: Added the owner's fingers-only reference restriction to the root README, asset map, project hub, decision log and handoff, with a link to the already-tracked original.
- Result: The original remains unchanged and is not described as the current full gauntlet design. Existing physical-test and release-gate requirements remain in force. The pending Mechanics inbox note remains for its explicitly assigned Print queue owner.
- Next: Clean up the isolated readback cache, validate the doc changes, and push.
- Sync: LOCAL.

## 2026-11-27 09:29 UTC — remote readback
- Action: Fetched the original 3MF from remote `main` at `491ee0e653da0dc68fc7fac9271a255680783704` into a newly created isolated LFS cache and verified its SHA-256 and size.
- Result: Remote LFS object readback PASS: 192,851,495 bytes and SHA-256 `07f60e694fd7db847d10357d4fffd24a59badcdc783af3107d92cf3618aed288`. This matches both the supplied file and committed pointer. No duplicate upload is required.
- Next: Update the asset map, project hub, handoff and decision record with the owner's fingers-only reference restriction.
- Sync: LOCAL.

## 2026-11-27 09:28 UTC — original comparison
- Action: Computed SHA-256 and sizes for the supplied OneDrive file and tracked original, and inspected the committed LFS pointer.
- Result: Both files are 192,851,495 bytes, SHA-256 `07f60e694fd7db847d10357d4fffd24a59badcdc783af3107d92cf3618aed288`. The committed LFS pointer has the same object ID and size. No source file or tracked CAD was modified.
- Next: Independently read back the remote LFS object and update project/vault reference guidance without changing release-gate results.
- Sync: LOCAL.
