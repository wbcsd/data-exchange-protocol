# 17. Life Cycle status property and additional Life Cycle rules

Date: 2022-12-19

## Status

Accepted

## Context

Context of this ADR Is the technical specification V1.0.0[^1]. It is lacking detailed specifications in the following areas:

1. Acceptable changes to an existing ProductFootprint that constitute a new version of the ProductFootprint
2. Changes that require a new ProductFootprint to be created while the previous is being deprecated.
3. Communication of the status of an existing ProductFootprint if it is invalid / redacted or superseded by other ProductFootprint(s)

## Decision

The following changes to the tech spec Bikeshed file[^2] shall be made
1. addition of fields `status` (with values of either `active` or `deprecated`),  `statusMessage` and `precedingPfIds` to `ProductFootprint`
2. additions to section 5 (lifecycle) of the spec, such that
   1. changes to an existing ProductFootprint are classified into `minor change` and `major change`
   2. where `minor changes` are allowed for new versions, whereas `major changes` require a new ProductFootprint to be created
   3. specification for how to represent a `deprecated` ; i.e. a Product Footprint for which new versions are available; a deprecated product footprint must no longer be used    
   4. addition of a new property `precedingPfIds` which is is a Product Footprint Id and is used to link a new ProductFootprint to the deprecated Product Footprint

## Consequences

1. the changes are backwards-compatible
2. the new property `status` is only relevant to communicate to a data recipient that a ProductFootprint shall ***no longer*** be used ; i.e. there is no status `created` or `updated`


[^1]: https://www.carbon-transparency.com/media/1qcdbdyn/pathfinder-network_technical-specifications-for-use-case-001.pdf
[^2]: [spec/index.bs](../../spec/index.bs)
