## Why

The repository is canonical on private GitHub and is about to become public.
Branch protection and required status checks are unavailable on private
repositories under the current plan, so the fast checks must exist, be green
and work from a fork **before** the visibility flip. Today all building happens
in GoCD, which contributors cannot see or run.

## What Changes

Add a public, fork-safe fast lane to `community-edition`. The repository is
data only (YAML and JSON), so there are no container-backed checks and no
integration workflow.

- parse every YAML and JSON document (`.github/scripts/check-yaml.py`)
- `gitleaks` with the committed `.gitleaks.toml`
- DCO trailer check
- outbound-host allowlist

An aggregator job named `fast` depends on every fast job and is the single
check to mark required at the visibility flip. Every workflow declares
`contents: read`, pins third-party actions by full commit SHA, uses no secrets
and avoids `pull_request_target`.

## Capabilities

### New Capabilities

- `public-ci`: the fast checks, fork-safety rules and aggregator for `community-edition`.

### Modified Capabilities

None.

## Impact

- New `.github/workflows/` and `.github/scripts/`; `.github/dependabot.yml` for
  dependency updates. No licence allowlist or notices file: the repository has
  no third-party dependencies.
- No runtime behaviour, API, image or GoCD pipeline change.
- Part of the session lane `oss-public-ci`; the visibility flip is gated on this
  lane being green.
