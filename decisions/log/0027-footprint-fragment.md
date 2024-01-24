# 27. Refining the Footprint Fragment

Date: 2023-12-29

## Status

In Progress

## Context

The "Asynchronous request and retrieval of Product Footprints" (section 6.8.4) as described in the Tech. Specs. (2.1.0) consists of two related events. That is:
* **Request** Event (see section 6.8.4.1.)
* **Response** Event (see section 6.8.4.2.)

The 'request' event includes a so called 'ProductFootprintFragment' that is defined as:
* *"A JSON object which references a subset of ProductFootprint properties, including nested properties."*

The 'ProductFootprintFragment' is intended to enable the data recipient (sending the request) to specify what it is looking for (which data) and share that with the data owner (receiving the request). However, the current definition of the 'ProductFootprintFragment' is very open and that might negatively addect the chances on an successful exchange.
* For example, one could - theoretically - make a request for PFs with ["fossilGhgEmission": "1.9"].

It is questionable whether data owners are able and willing to process such a wide variety of scenarios. Hence, the definition needs to be refined to properly support the use case of requesting and retrieving footprints in an asynchronous manner. In short, the 'ProductFootprintFragment' should be refined in such a way that:
* it is clear to data owners (host systems) what a request will look like so that they can ensure proper processing
* it is clear to data recipients how to request data from data owners (to the best chance at getting a response)


## Summary

In general, we propose to refine the definition of the 'ProductFootprintFragment' by (re)defining:
* hich properties MUST, MAY, and MUST NOT be included in the fragment:
  * **mandatory**: explicitly defining properties that MUST be included as a part of the fragment
  * **optional**: explicitly defining properties that MAY be included as a part of the fragment
  * **forbidden**: implicitly excluding properties as a part of the fragment by not including them as a mandatory or optional properties
* which operators are allowed to specify the desired values of these properties:
  * for example, eq, lt, le, gt, ge as supported for filtering in ***Action ListFootprints***

## Decision

### Technical Specification (V2)
The following lists of mandatory and optional properties are proposed:
* **mandatory**: productIds, ...
* **optional**: specVersion, companyIds, extensions, ...


## Consequences

1. ?? As this ADR creates a breaking change, the Tech Specs Version number must be updated from 2.1.x to 2.2.y. 
