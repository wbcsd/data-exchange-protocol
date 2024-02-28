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

Further refinements notwithstanding, with this ADR we propose to clarify what the error response returned by Action Events should be when PF data is unavailable and to explicitly recommend that `ProductIds` are included in the PF Request Event request body.

## Decision

### Technical Specification (V2)

1. In section 6.8.2. Response Syntax, replace
    ```
    The host system upon not accepting the event SHOULD respond with an [=error response=] (see [[#api-error-responses]]).
    ```
    with
    ```
    If the host system accepts the event but cannot process it due to unavailability of the PF data for the     [=ProductFootprintFragment=]
    in the request, it SHOULD return an [=error response=] (see [[#api-error-responses]]) with the [=error response code=]:     404 and appropriate [=error message=] indicating the unavailability of the PF data for the requested    [=ProductFootprintFragment=] value.
    ```

2. In the definition of `ProductFootprintFragment`, add
    ```
    It is RECOMMENDED to include at least the [=ProductIds=] in the PF Request Event request body.:
    ```
    followed by an example


## Consequences

1. As this ADR creates a non-breaking change, the Tech Specs Version number must be updated from 2.1.x to 2.2.y.
