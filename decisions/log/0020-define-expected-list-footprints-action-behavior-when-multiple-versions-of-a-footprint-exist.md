# 20. Define expected ListFootprints action behavior when multiple versions of a footprint exist

Date: 2023-01-25

## Status

Accepted

## Context

Context of this ADR is the technical specification V1.0.0[^1]. It is lacking detailed specifications in the following areas:

1. Expected behavior of the ListFootprints action when multiple versions of a footprint exist

## Decision

The following changes to the tech spec Bikeshed file[^2] shall be made
1. Addition of a paragraph to the `Action ListFootprints` section that makes returning of the latest footprint versions mandatory and returning of previous footprint versions optional.

## Consequences

1. The changes are backwards-compatible
2. When ListFootprints action is called, the host system must return the latest versions and may no longer return previous versions of footprints


[^1]: https://www.carbon-transparency.com/media/1qcdbdyn/pathfinder-network_technical-specifications-for-use-case-001.pdf
[^2]: [spec/index.bs](../../spec/index.bs)
