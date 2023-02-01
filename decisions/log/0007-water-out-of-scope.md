# 2. Water content removed from spec

Date: 2022-06-06

## Status

Accepted

## Context

The property `waterContent` of complex type `ProductFootprint` is mandatory w/ version 0.8.0, although there is a separate proposal to make optional.  There are further discussions about the structure and content of that value.

The above decisions require methodological input, and are not related to carbon (any more than plastic, timber, palm oil, etc are).  While the spec here could certainly be expanded to include other types of footprints, that is outside the scope of PACT and at this point should be removed.

## Decision

The field `waterContent` of should be removed from PACT