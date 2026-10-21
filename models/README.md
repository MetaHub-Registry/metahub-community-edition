# Model definitions

The community edition ships model **definitions**, not weights.

## How a model is composed

- `name` — served as `models/<org>/<name>:<quant>`.
- `runtime` — an in-MetaHub collection that provides the runtime image for the
  requesting profile.
- `quants` — tag → OCI source image containing the model layer.
- `latest` / `config` — selection rules and per-profile configuration
  overrides.

## Supply your own source

The example points at `registry.example.com/...`, which is a placeholder.
Replace it with an OCI reference you control. The referenced image must contain
the model layer the repackaging pipeline expects.

See [`docs/model-sources.example.yaml`](../docs/model-sources.example.yaml) for a template.

Note: keep example/template YAML **out of `models/`** — the ingest walks that
tree and aborts on a filename that is not `<repo>/<tag>.yaml`.

## Licensing

Model weights are **not** covered by this repository's Apache-2.0 licence.
Each model carries its own licence, often a custom or non-commercial one.
Check the model card and your redistribution rights before pushing weights to
a registry or serving them to others.
