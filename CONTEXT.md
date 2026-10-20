# Session close — 2026-10-20

## What changed

- Consolidated `beta` into `main` (licence and community files lived only on
  `beta`; `main` now carries them) and deleted `beta`.
- Sanitised the model source: `harbor.example.com` replaced with a documented
  `registry.example.com` placeholder; added `models/README.md` and
  `models/sources.example.yaml` with the model-weights licensing note.
- Updated the stale `ftest` tags to the existing `20220715-*` tags; verified
  the referenced `qnib-pub-containers` images are public.
- Added Apache-2.0, NOTICE, OWNERSHIP, TRADEMARK and the community health
  files.

## Gotchas

- The session branch `30-hostname-profile-resolution` is based on the old
  `beta`; it was merged with `main` and is current.
- Model and `ftest` content exists only on this branch, not on `main` before
  the session merge.
