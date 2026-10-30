# Design — public CI for community-edition

## Stack and boundary

data only (YAML and JSON).

Fast checks:

- parse every YAML and JSON document (`.github/scripts/check-yaml.py`)
- `gitleaks` with the committed `.gitleaks.toml`
- DCO trailer check
- outbound-host allowlist

Container-backed checks: There are no container-backed tests.

There are no third-party dependencies, so no licence allowlist or notices file is generated. The parse check is the fast gate until the repository gains a schema validator.

## Decisions

### Self-contained, fork-safe workflows

The workflows live in this repository. A cross-repository reusable workflow
would need either a public `.github` repository before the launch gate or
private access that a fork does not receive. Every PR-triggered workflow is
therefore self-contained, declares `permissions: contents: read`, pins
third-party actions by SHA and references no secret.

### One aggregator

`fast` depends on every fast job and fails when any of them fails or is
cancelled. Marking only `fast` as a required check at the visibility flip keeps
the branch-protection configuration stable as checks are added.

### No release-only lane

The repository is data only; every check is container-free and runs on every
pull request. There is no `integration.yml` and no check is deferred to a
release tag.

### Dependencies and licences

The repository has no third-party dependencies, so it has no licence
allowlist and no notices file. The document parse check is the integrity gate.

### Outbound hosts

Non-test source may reference only hosts on `.github/outbound-allowlist.txt`.
A new host fails the job and must be added deliberately in review. This is a
review gate, not a network sandbox.

## Risks

| Risk | Mitigation |
|---|---|
| A workflow needs a secret when run from a fork | it belongs in the integration lane or is dropped |
| Action supply chain | every action is pinned to a full commit SHA |
| Dependency advisories | Dependabot opens weekly PRs; the only pinned toolchain is `PyYAML`, installed at a fixed version |
