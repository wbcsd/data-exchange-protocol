# Proposal to simply versioning of Product Footprints
Date: 2024-10-21

## Status
Work in progress. Feedback gathered during v2.2 and v2.3 specification process. Now being presented to the Tech Working group. 

## Context
The PACT technical specifications version 2.x describe guidelines how to handle changes to poduct footprints over time. See the [Product Footprint Lifecycle](https://wbcsd.github.io/tr/2024/data-exchange-protocol-20241024/#lifecycle). 

These guidelines consider different categories of changes to footprints: some might be caused by the availability of new or updated underlying footprints, others might be corrections of calculation errors, yet others might be fixes of descriptions.

Version 2.x prescribes a separation between *major* and *minor* footprint changes and provides logic to distinguish between the two. 

To distinghuish between these different changes a mechanism of recording major and minor versions has been devised:

1.	major changes will result in a new ProductFootprint to be made available, with a new ProductFootprint ID and version=1. To be able to track back to previous versions the last Footprint ID is added to the PrecedingPfIds list.
([6.4 New ProductFootprint creation from major changes](https://wbcsd.github.io/tr/2024/data-exchange-protocol-20241024/#lifecycle-major-changes))

2.	minor changes result in either version updates ([6.3 ProductFootprint version creation from minor changes](https://wbcsd.github.io/tr/2024/data-exchange-protocol-20241024/#lifecycle-minor-changes)) where only the version number is incremented, and the PfId stays the same. In some cases however a new ProductFootprint needs to be created.

This logic however leaves room for interpretation ("Some cases"). For example: according to the specs, changing a single emission attribute (for example pcfExcludingBiogenic) would constitute a minor change, but what about changing multiple minor attributes? Would that be considered a major change? Or changing a single attribute, but by a very large amount? 

It is to be expected that human decision-making needs to be be applied. For thousands (let alone millions) of footprints this would incur lots of overhead.
Feedback from the community indicates the need to reconsider the benefits of this finegrained versioning method and proposes a way of simplifiying this, while maintaining backwards compatibility.


## Proposal 
In order to simplify versioning and not delegating the burden of determining what constitutes a minor change vs a major change we propose to **regard any change as a major change**.

### Updating PCFs
Starting version 3.0, a change to any part of the footprint MUST result in a *new* footprint with a new id. The old id MUST be added to the PrecedingPfIds list to be able to track back to the previous version.
The version number of this new PCF MUST always be 1 and the updated property always null.
The old PCF MUST have its `status` set to `Deprecated`.

### Deprecating PCFs
If a PCF becomes obsolete without being replaced, the `status` property of the PCF needs to be set to `Deprecated`.

### Properties to be become obsolete
Starting PACT 4.x the properties `version` and `updated` will be made obsolete, anticipating a situation where no 2.x versions will be communicating with 4.x.


## Consequences

### Simplicity
Any 3.x implementation of the PACT API does not need to implement any reasoning to distinguish between major and minor changes. 

### Backwards and forwards compatibility
Changes originating in 3.x will be handled correctly by 2.x API's: any change involve a new ID and a link back to the old ID. So, in terms of 2.x, the change is a *major* one, which will deprecate previous PCF's. 
The one exception of a change originating in 3.x is the deprecation of an old PCF *without* it being replaced by a new one. In this case the ID will not change, but the status does (and be set to `Deprecated`).

Major changes originating in 2.x will be be handled correctly by 3.x API's. 
Any minor update originating from 2.x to 3.x will be handled as a change to an existing PCF.

### Implementation guidelines
1) Version 3.x MAY in its internal data model store the `version` and `updated` properties.
   Any incoming minor change will be accepted if `incoming.version` is higer than `existing.version`.
   The updated PCF will be stored, including `version` and `updated` properties.

2) Version 3.x MAY choose NOT to store `version` and `updated` properties:
   In that case any incoming minor change will be accepted if `incoming.updated` is later than `existing.created`
   The PCF will be stored, making sure the `created` date/time is set to the incoming `updated` data/time.
