# 32. Extend Cross Sectoral Standards list to be more comprehensive and extensible

Date: 2024-04-17

## Status

Proposed
* Feedback originally raised by industry initiatives (CX, TfS) in Summer 2023
* Per discussions with TfS, CX, and Green x Digital, initiatives are aligned to the proposal
* Per discussions with SINE, addition of "other" as an option significantly increases complexity of specification with doubtable value, therefore we are proceeding with proposal of extensible list without the option of "other"
* Update May 15: Per discussions with initiatives, a few of the proposed cross sectoral standards are considered out-dated and/or discouraged by the PACT community (specifically PACT Framework v1 and PAS 2050), however it was considered these should still remain permissable options (technically) although discouraged. Therefore these have been added but indicated as "not recommended".

## Context

### Business Context
The attribute crossSectoralStandardsUsed in the PACT 2.0.0 specification is intended to communicate the set of Cross Sectoral Standard(s) applied for calculating or allocating GHG emissions for the calculation of the PCF. Per v2.0.0 of the PACT specification, this field is mandatory and must be populated with an array, populated with a set of one or more valid strings. The following strings are valid: `GHG Protocol Product standard, ISO Standard 14067, ISO Standard 14044`.

Three main concerns have been raised with the current specification of this field:
* The provided list is hypothesized to be incomplete and may not include all relevant cross-sectoral standards internationally
* Given the current design of the field, when a new cross sectoral standard is identified and it is determined it should be added to the set, this would result in a backwards breaking change and therefore not be available until a major release of the tech specs, causing a long delay before the new standard could be used for data exchange

[For full details see here](https://flat-dollar-c04.notion.site/Extend-the-Cross-Sectoral-Standards-List-to-be-more-comprehensive-and-extensible-ddf602f360e14168b2a300d71a38f672)

## Proposal
To address the above challenges, we (jointly with Catena-X, TfS, and Green x Digital) propose the following for evaluation by the PACT community:

* A new attribute which includes a set of options. These options would include those listed in technical proposal below (exact list pending final alignment with community)
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

        Recommended:
        : ISO14067
        :: for the ISO 14067 Standard, "Greenhouse gases — Carbon footprint of products — Requirements and guidelines for quantification"
        : ISO14083
        :: for the ISO 14083 Standard, "Greenhouse gases — Quantification and reporting of greenhouse gas emissions arising from transport chain operations"
        : ISO14040-44
        :: for the ISO 14040-44 Standard, "Environmental management — Life cycle assessment — Principles and framework"
        : GHGP Product
        :: for the Greehouse Gas Protocol (GHGP) Product Standard
        : PEF
        :: for the EU Product Environmental Footprint Guide
        : PACT Framework v2
        :: for version 2 of the PACT Framework
        : PACT Framework v2.1
        :: for version 2.1 of the PACT Framework
        Not recommended but permitted*:
        : PACT Framework v1
        :: for version 1 of the PACT Framework
        : PAS2050
        : for the Publicly Available Specification (PAS) 2050, "Specification for the assessment of the life cycle greenhouse gas emissions of goods and services"

        Advisement:
            The enumeration of standards above CAN evolve in future revisions. A host system MUST accept ProductFootprints from later revisions with `crossSectoralStandards` containing values that are not defined in this specification.
            The set of standards listed include some standards which PACT does not recommend given they have become deprecated and/or outdated. However, with the goal of enabling transparency, PACT Technical Specifications nevertheless includes these as options.
    ```

## Decision

Pending review by PACT Tech Working Group; all feedback and fundamental objections to be raised by May 29; consensus decision planned June 5


## Consequences
* Technical Specifications must be updated accordingly

Based on current assumptions:
* The existing attribute `crossSectoralStandardsUsed` will be deprecated in v2.3 and removed from the spec in v3
* A new attribute, meeting the business needs of this ADR will be introduced in v2.3
