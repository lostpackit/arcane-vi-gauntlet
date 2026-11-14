---
type: risk-register
tags: [risk, blockers]
---

# Risks and blockers

| Risk | Status | Required next evidence |
|---|---|---|
| Remote LFS binary readback | UNVERIFIED | Push acknowledged 45/45 objects; GitHub shows pointer blobs and local fsck passes. Independently fetch/read remote objects when downloading is permitted |
| V3 fit-validation assets missing locally | BLOCKED | Locate/provide V3 files; do not substitute other assets |
| Extracted V4 file hashes unavailable | UNKNOWN | Obtain V4 file manifest or compare against trusted release archive |
| Requested 61-entry asset manifest absent | UNKNOWN | Obtain canonical SHA-256 CSV; current audit-kit CSV covers 9 originals and an absent V4 ZIP |
| V4 printability and support requirements | UNKNOWN | Bambu Studio actual slice |
| Finger mounting and five string paths | UNKNOWN | Assembly geometry and physical travel |
| Circular LED groove width/depth and diffuser clearance | BLOCKED | Measure channel and real LED strip |
| Electronics and battery mounting/access | BLOCKED | Selected parts and dimensions |
| Bonded seam strength and serviceability | UNKNOWN | Test coupons and mechanical review |
| Third-party source license | UNKNOWN | Provenance and terms |

For current priority and ownership, see [[HANDOFF]]. Record any newly discovered risk there **after the action**.
