# 27. Refining the Footprint Fragment

Date: 2023-12-29

## Status

Accepted

## Context

The "Asynchronous request and retrieval of Product Footprints" (section 6.8.4) as described in the Tech. Specs. (2.1.0) consists of two related events. That is:
* **Request** Event (see section 6.8.4.1.)
* **Response** Event (see section 6.8.4.2.)

The 'request' event includes a so called 'ProductFootprintFragment' that is defined as:
* *"A JSON object which references a subset of ProductFootprint properties, including nested properties."*

The 'ProductFootprintFragment' is intended to enable the data recipient (sending the request) to specify what it is looking for (which data) and share that with the data owner (receiving the request). However, the current definition of the 'ProductFootprintFragment' is very open and that might negatively effect the chances of a successful exchange.
* For example, one could - theoretically - make a request for PFs with ["fossilGhgEmission": "1.9"].

It is questionable whether data owners are able and willing to process such a wide variety of scenarios. Hence, the definition needs to be refined to properly support the use case of requesting and retrieving footprints in an asynchronous manner. In short, the 'ProductFootprintFragment' should be refined in such a way that:
* it is clear to data owners (host systems) what a request will look like so that they can ensure proper processing
* it is clear to data recipients how to request data from data owners (to the best chance at getting a response)


## Summary

This ADR aims to provide additional guidance on processing of PF Request Events. It includes the creation of a new overarching section with end-to-end business cases, as well as one clarification and one recommendation.

## Decision

### Technical Specification (V2)

1. Add a new section to the Technical Specifications titled 'Business Cases', with a subsection dedicated to the processing of PF Request Events. The proposed text for this section can be found in the [Appendix](#appendix) below.

2. In section 6.8.2. Response Syntax, replace
    ```
    The host system upon not accepting the event SHOULD respond with an [=error response=] (see [[#api-error-responses]]).
    ```
    with
    ```
    If the host system accepts the event but cannot process it due to unavailability of the PF data for the     [=ProductFootprintFragment=]
    in the request, it SHOULD return an [=error response=] (see [[#api-error-responses]]) with the [=error response code=]:     404 and appropriate [=error message=] indicating the unavailability of the PF data for the requested    [=ProductFootprintFragment=] value.
    ```

3. In the definition of `ProductFootprintFragment`, add
    ```
    It is RECOMMENDED to include at least the [=ProductIds=] in the PF Request Event request body.:
    ```
    followed by an example


## Consequences

1. As this ADR creates a non-breaking change, the Tech Specs Version number must be updated from 2.1.x to 2.2.y.

## Appendix

This appendix contains the text intended for the new section to be added to the Technical Specifications.

### The General principles of Event processing

1. A host system should strive to accept an event unless for the following reasons
    1. event processing is not support by the host system
    2. the syntax in the event is not supported (e.g. when the event failed “syntax checks” of the request host system)
2. Whenever a host system’s `Event` endpoint returns an error response, no follow up response event (or error event) will be sent back to the original requester
3. The requested host system will attempt to always send a response event to the requesting host system, **but the requesting host system should not rely on this behavior and retry after an appropriate amount of time by sending another new request event.**

### Async Event Processing: Business Case 1 – Requesting Product Footprints

#### Context and Assumptions

- This business case is triggered by a data recipient if they wish to access a Product Footprint **they could not yet access through the `ListFootprints` API.**
- The data recipient and data owner have a mutually agreed upon way to identify products

#### Workflow

1. The data recipient sends a `ProductFootprintFragment`  to the `Events Endpoint` of the data owner. The data recipient should always include 1 or more product ids in property `productIds`. The data recipient should limit each fragment to exactly 1 specific product (e.g. a specific type of apple instead of all apples that somebody is offering)
    1. If the recipient is requesting a specific reporting period, it should include the reporting period accordingly (example …)
    2. if the recipient is requesting a specific geography, it should include …
    3. if the recipient has another need that is not covered above, the data recipient should <…>
        1. Note: it is possible that this request will not be commonly understood by the data owner’s host system

#### Cases

- Case 0: The solution does not support this kind of processing
    - either because the event processing does not exit at all, or the product footprint fragment as it is submitted by the data recipient is not supported by the requested host system
    - The `events` endpoint responds with HTTP error code `400` and with a body with error code `NotImplemented`
- Case 1: A PCF does not exist (yet) or a partially matching PCF exists
    - accept the event (HTTP Code 200 returned by the events endpoint)
    - In case of a partial match, the data owner needs to decide whether to calculate the PCF(s) or not.
        - Note: the decision making and decision making protocol for this case is up to the discretion of each data owner
    - In case the data owner decided or needs to calculate the PCF and the calculation succeeded,
        - the host system makes the newly calculated footprints also available to the data recipient through `ListFootprints`
        - the host system of the data owner sends back the 1 or more product footprints in a single event to the data requester
    - in case the data owner decided to not make additional PCFs available
        - the host system responds listing the (partially) matching PCFs
    - if the product cannot be found or otherwise identified through the product footprint fragment
        - the host system of the data owner responds with a PF Response Error Event with code `NoSuchFootprint`
    - If the PCF calculation failed for other reasons
        - the host system SHOULD send **`PF Response Error Event`** with error code `InternalError`
- Case 2: The PCF(s) exists
    - the host system accepts the event (Code 200)
    - If the data recipient does not have access to the PCF yet
        - the data owner decides on making the PCF available or not
        - if the data owner made the matching PCF(s) available, their host system returns the PCFs to the data recipient
        - otherwise, the host system of the data owner responds with a error event with error code `AccessDenied`
    - if the data recipient has access to the PCF(s)
        - the data owner responds by sending
- Default / Backup Case:
    - the host systems accepts the event (Code 200)
    - the host system sends back a `PF Response Error Event` with code `BadRequest`
