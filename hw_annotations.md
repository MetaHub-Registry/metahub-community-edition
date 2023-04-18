# Annotations

This document describes the annotations that are used within the *HPC Container Conformance* project.  
The goal of the annotations is to provide a common way to describe the features of a container image. The annotations are used to generate the conformance reports.

## Hardware Annotation

**Key**: `org.supercontainers.hardware.`

### CPU

A mandatory annotation defines how fine grained the compilation was done.

| Key        | Mandatory | Values                      | Description                                                                                              |
| ---------- | --------- | ---------------------------- | -------------------------------------------------------------------------------------------------------- |
| cpu.target | &check;   | (platform/microarch/generic) | Mandatory annotation to define how the cpu arch is specified                                             |
|            |           | platform                     | Platform hands over the responsibility to the OCI platform object                                        |
|            |           | microarch                    | real micro-arch of the CPU (zen2, skylake_avx512)                                                        |
|            |           | generic                      | non-vendor related arch family (x86_64_v4) which is less specific than `microarch` but a good compromise |

#### Platform Target

Images with the annotation `org.supercontainers.hardware.cpu.target=platform` are expected to be compiled for generic AMD64 or ARM platforms. They will be identified using the `OCI platform object` (e.g. `linux/amd64`, `linux/arm64/v8`).
Such a container will match the [generic platform](filter/cpu/generic.yaml) filter:

```yaml
name: "generic"
rules:
  - name: "platform-generic"
    op: "eq"
    key: "org.supercontainers.hardware.cpu.target"
    value: "platform"
```

#### Drilling Down

For `microarch` and `generic` targets one of the following is mandatory.

| Key                  | Mandatory | Example        | Description                                                               |
| -------------------- | ---- | ----- | --------------------------------------------------------------------------------------- |
| cpu.target.microarch | (&check;) | `zen2`         | The result of `spack arch -t`  (what `archspec` spits out as a microarch) |
| cpu.target.generic   | (&check;) | `x86_64[_v\d]` | Non vendor specific architecture.                                         |

Those annotations are used in conjuction with [archspec]() logic, so that `

### GPU

| Key                  | Mandatory | Example      | Description                                                                                                |
| -------------------- | --------- | ------------ | ---------------------------------------------------------------------------------------------------------- |
| `gpu.vendor`         | &check;   | nvidida, amd | If a accelerator is present, this field describes the vendor and the subsequent path within the annotation |
| `gpu.<vendor>`.model | &check;   | a10,mi250    | The common name for the model                                                                              |

### System Vendor

Some container might be designed to run on specific compute nodes. This is the case for HPC systems, where the compute nodes are often designed for a specific vendor. This annotations can be used to point that out.

| Key                             | Mandatory | Example       | Description                                          |
| ------------------------------- | --------- | ------------- | ---------------------------------------------------- |
| `system.vendor`                 |           | hpe,aws,azure | System vendor                                        |
| `system.<vendor>.instance.type` |           | g5.4xlarge    | The instance type the image is desinged to work with |