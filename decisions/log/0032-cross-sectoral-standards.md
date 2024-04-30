# 32. Extend Cross Sectoral Standards list to be more comprehensive and extensible

Date: 2024-04-17

## Status

Proposed
* Feedback originally raised by industry initiatives (CX, TfS) in summer 2023
* PACT is now working witih industry initiatives to align on the "complete set" of permitted cross sectoral standards
* Per discussions with TfS and CX, they are aligned to the proposals listed and have a (slight) preference for Proposal 1 (i.e. extensible list and exclusion of "other" option)
* Goal is to reach alignment with initiatives on proposal and raise to Tech WG May 15

## Context

### Business Context
The attribute crossSectoralStandardsUsed in the PACT 2.0.0 specification is intended to communicate the set of Cross Sectoral Standard(s) applied for calculating or allocating GHG emissions for the calculation of the PCF. Per v2.0.0 of the PACT specification, this field is mandatory and must be populated with an array, populated with a set of one or more valid strings. The following strings are valid: `GHG Protocol Product standard, ISO Standard 14067, ISO Standard 14044`.

Three main concerns have been raised with the current specification of this field:
* The provided list is hypothesized to be incomplete and may not include all potential cross-sectoral standards internationally
* Given the current design of the field, when a new cross sectoral standard is identified and it is determined it should be added to the set, this would result in a backwards breaking change and therefore not be available until a major release of the tech specs
* There may be cross sectoral standards we are not aware of (potentially regional cross sectoral standards) and therefore because the user has no option to add an additional standard they used, beyond those listed, this limits the standards the user is disclosing to the data recipient

[For full details see here](https://flat-dollar-c04.notion.site/Extend-the-Cross-Sectoral-Standards-List-to-be-more-comprehensive-and-extensible-ddf602f360e14168b2a300d71a38f672)

## Proposal
To address the above challenges, we propose two options for evaluation by the community and especially with our strategic initiatives

Proposal 1:
* A new attribute which includes a set of options. These options would include (exact list pending final alignment with community): `ISO 14067; ISO14083; PACT Framework v1; PACT Framework v2; PACT Framework v2.1; GHG Protocol Product; PAS 2050; ISO 14040-44; PEF`
* The set of recommended options may be extended without requiring a new version of the specifications (neither minor nor major)

Proposal 2:
* All aspects of Proposal 1, and in addition:
* Additional cross sectoral standards may also be disclosed by the user which are not listed within the recommended options


Proposal 1 may be more advantageous if the community wishes to enforce higher degrees of standardization and not permit the use and/or sharing of additional cross sectoral standards not listed; Proposal 2 is more advantageous to support flexibility of exchange and disclosure of all standards used

## Detailed Technical Proposal

To be updated

## Decision

Pending alignment with initiatives


## Consequences
* Technical Specifications must be updated accordingly

Based on current assumptions:
* The existing attribute `CrossSectoralStandard` will be deprecated in v2.3 and removed from the spec in v3
* A new attribute, meeting the business needs of this ADR will be introduced in v2.3
