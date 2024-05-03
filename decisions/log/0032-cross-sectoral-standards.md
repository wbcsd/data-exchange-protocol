# 32. Extend Cross Sectoral Standards list to be more comprehensive and extensible

Date: 2024-04-17

## Status

Proposed
* Feedback originally raised by industry initiatives (CX, TfS) in Summer 2023
* PACT is now working witih industry initiatives to align on the "complete set" of permitted cross sectoral standards
* Per discussions with TfS and CX, initiatives are aligned to the proposal listed and have a (slight) preference for Proposal 1 (i.e. extensible list and exclusion of "other" option)
* Per discussions with SINE, addition of "other" as an option significantly increases complexity of specification with doubtable value, therefore we are proceeding with proposal of extensible list without the option of "other"
* Goal is to reach alignment with initiatives on proposal and raise to Tech WG May 15
* May 3, 2024: Updated proposal to remove PAS 2050 (Publicly Available Specification (PAS) 2050), which per initiative alignment PAS is outdated and and not maintained, apparently it is mostly in the UK (with Carbon Trust). So in principal it could be added but not recommended

## Context

### Business Context
The attribute crossSectoralStandardsUsed in the PACT 2.0.0 specification is intended to communicate the set of Cross Sectoral Standard(s) applied for calculating or allocating GHG emissions for the calculation of the PCF. Per v2.0.0 of the PACT specification, this field is mandatory and must be populated with an array, populated with a set of one or more valid strings. The following strings are valid: `GHG Protocol Product standard, ISO Standard 14067, ISO Standard 14044`.

Three main concerns have been raised with the current specification of this field:
* The provided list is hypothesized to be incomplete and may not include all potential cross-sectoral standards internationally
* Given the current design of the field, when a new cross sectoral standard is identified and it is determined it should be added to the set, this would result in a backwards breaking change and therefore not be available until a major release of the tech specs
* There may be cross sectoral standards we are not aware of (potentially regional cross sectoral standards) and therefore because the user has no option to add an additional standard they used, beyond those listed, this limits the standards the user is disclosing to the data recipient

[For full details see here](https://flat-dollar-c04.notion.site/Extend-the-Cross-Sectoral-Standards-List-to-be-more-comprehensive-and-extensible-ddf602f360e14168b2a300d71a38f672)

## Proposal
To address the above challenges, we propose the following for evaluation by the community and especially with our strategic initiatives:

* A new attribute which includes a set of options. These options would include (exact list pending final alignment with community): `ISO 14067; ISO14083; PACT Framework v1; PACT Framework v2; PACT Framework v2.1; GHGP Product; ISO14040-44; PEF`
* The set of options may be evolved without breaking backwards compatibility

We have also considered the possibility of disclosing a cross sectoral standard not contained in the set of options explicitly covered by the Technical Specifications. We concluded that this possibility was suboptimal, for the following reasons:
* It would afford more complexity to the Technical Specifications, requiring a structured data type similar to [`ProductOrSectorSpecificRule`](https://wbcsd.github.io/data-exchange-protocol/v2/#dt-productorsectorspecificrule)
* There would be no clear guidance for data recipients who received a `ProductFootprint` with an unexpected cross sectoral standard
* There are no straightforward advantages in this possibility that supersede the disadvantages of accommodating it


## Detailed Technical Proposal

1. Addition of deprecation warnings to the attribute `crossSectoralStandardsUsed`, as well as to the data types `CrossSectoralStandard` and `CrossSectoralStandardSet`.
2. Addition of new property `crossSectoralStandards` defined as follows:

    ```
    <tr>
        <td><dfn>crossSectoralStandards</dfn>
        <td>Array of Strings
        <td>M
        <td>The cross-sectoral standards applied for calculating or allocating [=GHG=] emissions.

        It MUST be a non-empty array and MUST contain only the following values without duplicates:

        : ISO14067
        :: for the ISO 14067 Standard
        : ISO14083
        :: for the ISO 14083 Standard
        : PACT Framework v1
        :: for version 1 of the PACT Framework
        : PACT Framework v2
        :: for version 2 of the PACT Framework
        : PACT Framework v2.1
        :: for version 2.1 of the PACT Framework
        : GHGP Product
        :: for the Greehouse Gas Protocol (GHGP) Product Standard
        : ISO14040-44
        :: for the ISO 14044-44 Standard
        : PEF
        :: for the EU [Product Environmental Footprint Guide](https://ec.europa.eu/environment/archives/eussd/pdf/footprint/PEF%20methodology%20final%20draft.pdf)

        Advisement: 
            The enumeration of standards above CAN evolve in future revisions. A host system MUST accept ProductFootprints from later revisions with `crossSectoralStandards` containing values that are not defined in this specification.
    ```

## Decision

Pending alignment with initiatives


## Consequences
* Technical Specifications must be updated accordingly

Based on current assumptions:
* The existing attribute `crossSectoralStandardsUsed` will be deprecated in v2.3 and removed from the spec in v3
* A new attribute, meeting the business needs of this ADR will be introduced in v2.3
