# 19. Increment the version of PCF HTTP Endpoints from /0 to /2

Date: 2023-01-04

## Status
In Progress

## Context

In order to accommodate the changes to Use Case 001 Tech Spec v1 to v2, there is a need to increment the prefix of the PCF HTTP Endpoints to /2 (from /0)


## Decision

1. The Technical Specification version V2 will comprise of updates that requires the increment of the PCF HTTP Endpoints version from /0 to /2. These changes are Major changes hence the Major version number update is required.

The changes are as below
1. Inclusion of additional data attributes in alignment with Pathfinder Framework Version V2
2. Inclusion of SSI technology for network identities, digital signatures (and related digital verification & assurance statements)
3. To incorporate the data model extensions and their representation within a ProductFootprint document in accordance with the Guidance and Criteria for Pathfinder Data Model Extensions



## Consequences
1. the incremental version prefix (/2) is backwards-compatible with V1 and V1.1 endpoints
