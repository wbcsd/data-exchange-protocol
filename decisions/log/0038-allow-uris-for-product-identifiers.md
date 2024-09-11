# 38. Allow URI's for Product Identifiers

Date: 2024-09-11

## Status

Proposed

This is an expansion of the common URN format introduced by ADR-0034. The proposal is ready for review, following consultation with GS1, Digital Twin and being presented in the PACT Tech WG September 11.

## Context



The current PACT Technical Specifications mandate the use of Uniform Resource Names (URNs) for product identification and classification, and include a recommended `urn:pact` namespace with a common format for specifying product ids. 

For most point-to-point cases this default, recommended way of using id's will suffice. However, there is a need to accommodate emerging standards like Digital Link and Digital Product Passport, which rely on Uniform Resource Identifiers (URIs), a superset of URNs. 

This ADR proposes expanding from URNs to URIs for product identification within the PACT Technical Specifications.

### Specific problems this proposal addresses 
 The PACT Technical Specification will be revised to use URIs for product identification, replacing the current requirement for URNs. This change will:
 * Expand Compatibility: Allow for the integration of emerging and future product identification standards, such as Digital Link and Digital Product Passport.
 * Enhance Interoperability: Improve compatibility with various identifier schemes and systems used by different organizations and industry networks.
 * Future-Proofing: Ensure the PACT specification remains adaptable to evolving digitalization trends in supply chain sustainability and circular economy.

Scope 
 * The scope of this proposal is for product identifiers `productIDs` *and* product *classification* identifiers as stored in `productClassification` (see ADR-0037). 
 

## Proposal

The proposal consists of three recommendations:
 1. Change the data type of `productIDs` from URN to **URI** (as defined in RFC )
 1. Change the data type of `productClassification` from *array* or URN to *array* of **URI** 
 1. Include additional examples for real-world URI's in the documentation

 ### Examples

 GS1 Digital Link

    https://qr.patagonia.com/01/00889833298392/21/000000001842
    

## Consequences

 * Inclusion of v3 ensures backwards compatibility with v2.x URNs.
