# 11. Capitalization of "specVersion" field

Date: 2022-06-07

## Status

Accepted

## Context

Version 1.0.0 introduces the field `specversion`, which contains the version of the Pathfinder standard that was used.
This is in conflict with the standard's naming convention: All other fields use CamelCasing.

## Decision

Rename field `specversion` to `specVersion` to conform with the standard's naming conventions.

## Consequences

Standards draft must be updated.
