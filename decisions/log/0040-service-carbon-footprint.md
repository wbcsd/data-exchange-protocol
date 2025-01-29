Date: 2024-10-29

## Status

Proposal shared and discussed in Dec 18, 2024 WG. 

Feedback collected from Methodology WG: proposal adapted and clarified

Call for consensus on Jan 29, 2025

## Context
Services are part of companies Scope 3 category 1 (Purchased goods and services). Therefore, accuracy on service carbon footprint is important. 

While the range of services that companies may purchase can vary widely, and with them the variety of calculation approaches and declared units, two main group of services have been identified as being prominent across all sectors and business models: *Desk-based services* (such as consulting, legal, and marketing services) and *IT-related services* (such as software services).

See for more information https://backlog.carbon-transparency.org/Explore-the-possibility-of-including-service-carbon-footprints-methodology-3a9e509d97114e058cbacac03a859b9f


## Proposal
Proposal to include 2 additional units of measurement into the data model for accounting for service-releated emissions.

- **hour**: time in hours for Desk-based services
- **Mbps**: amount of data used, transferred or stored, per time unit, for IT-related services.

## Examples

### Desk-based services

Suppose a desk-based service product is "In-house Software Development". A supplier of this service can issue a PCF stating 1 hour of "In-House software development" would emit 0.5 kgCO2e. The recipient of this service can then multiply this with the amount of hours of software development bought.

In PCF format:

```json
"unitOfMeasurement": "hour"
"productDescription": "In-house software development"
"productAmount": "1.0"
"pcfExcludingBiogenic": "0.5"
```

### IT-related services.

A supplier of a data streaming service can issue a PCF stating that, using its product, the transfer of 1GB per hour will result in 0.2 kgCO2e. 

The purchaser of this service can multiply with the **amount of data** actually streamed per unit of time *and* the **amount of time** to calculate the resulting emissions. 

The Methodology WG confirms the use of **Mbps** for this metric. See also 
https://ghgprotocol.org/sites/default/files/ghgp/GHGP-ICTSG%20-%20ALL%20Chapters.pdf


In PCF format:
```json
"unitOfMeasurement": "Mbps"
"productDescription": "Streaming Service"
"productAmount": "1"
"pcfExcludingBiogenic": "0.0000055"
```

## Rationale

- Definition:
    - Most comprehensible
- Methodology:
    - Balance between the effort and impact, i.e. SCFs are still quite lower than “good” PCFs, and therefore, it is not needed at this stage to create a full methodology

## Consequences

Forward-compatible, not backwards compatible, hence the inclusion in version 3.0.


