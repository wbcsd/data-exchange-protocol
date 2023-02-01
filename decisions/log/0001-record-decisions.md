# 1. Record decisions

Date: 2022-05-26

## Status

Accepted

## Context

We need to record the decisions made on this project.

## Decision

We will use a variant of Architecture Decision Records.

## Consequences

We will use [adr-tools](https://github.com/npryce/adr-tools) for creating ADR files and
for managing the TOC at [README.md](README.md).

Whenever we create and before we submit a PR, we run [scripts/adr-generate-toc.sh](../../scripts//adr-generate-toc.sh) to update the README.md's toc.

A starting point on ADRs and their rational can be found in [this cognitect blog post](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
