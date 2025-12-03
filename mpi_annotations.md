# Annotations

This document describes the annotations that are used within the *HPC Container Conformance* project.
The goal of the annotations is to provide a common way to describe the features of a container image. The annotations are used to generate the conformance reports.

## Hardware Annotation

**Key**: `org.supercontainers.mpi.`

### General

A mandatory annotation defines how fine grained the compilation was done.

| Key              | Mandatory | Example                                  | Description                                                                                           |
| ---------------- | --------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| implementation   | &check;   | (openmpi/mpich/threadmpi)                | Mandatory annotation to define how the mpi implementation used                                        |
| framework        |           | (ucx/libfabrics)                         | Mandatory for all non-threadmpi implementation to specify which framework they use                    |
| portability.mode |           | mpi_replace,ucx_replace,libfabric_inject | How is the container expected to be tweaked? replace the complete MPI, inject new libfabrics provider |
