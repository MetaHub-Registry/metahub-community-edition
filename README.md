## MetaHub Registry

![MetaHub Logo](/img/metahub-logo.png)

MetaHub is a registry that takes the context of a user into account to deliver the best suited container image.

## Community Edition **BETA**

GitOps driven set of manifest collections and profiles to drive the **BETA** version of *MetaHub Community Edition*. The goal is to define collection of commonly used and public container images, for everyone to use.

## BETA Version

The current version used is a **BETA** version to refine the definitions and structures used within the *MetaHub Community Edition*.

**Be aware** that the current version is not stable and may change at any time.

## Content and sources

The repository contains YAML definitions only. It does not bundle container
images or model weights.

- **Runtime images** referenced by collections and manipulations are public
  images under `registry.gitlab.com/qnib-pub-containers/...` and can be pulled
  anonymously.
- **Model weights are not included.** The example model definition uses
  `registry.example.com/models/...` as a placeholder. Point it at a registry
  you control; model weights carry their own licence, independent of this
  repository's Apache-2.0. See [`models/README.md`](models/README.md) and
  [`models/sources.example.yaml`](models/sources.example.yaml).

## Licence

The YAML definitions are licensed under Apache-2.0. Images and model weights
referenced by those definitions remain under their own licences.

