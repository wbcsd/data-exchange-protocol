# 27. Provide Clarity on Characterization Factors (AR5 and AR6)

Date: [YYYY-MM-DD]

## Status

Proposed

## Context

`characterizationFactors` is a mandatory property of the `CarbonFootprint` data type.
It's data type is `String` and the value MUST be one of the following (see [4.2.2 Properties #characterizationFactors](https://wbcsd.github.io/tr/data-exchange-protocol/#element-attrdef-carbonfootprint-characterizationfactors)):
- AR6
  - for the Sixth Assessment Report of the Intergovernmental Panel on Climate Change (IPCC)
- AR5
  - for the Fifth Assessment Report of the IPCC

However, some PCFs might be calculated with inputs that use both AR5 and AR6 as these can come from
different sources (i.e., different actors in the supply chain). Since the IPCC will keep publishing
reports, this problem tends to get worse in the future.

In the context of the Methodology Working Group, PACT members have expressed a very strong
preference for having the possibility of including more than one characterization factor per PCF.

## Decision

1. Change the definition of the `characterizationFactors` from:
    > The IPCC version of the GWP characterization factors used in the calculation of the PCF (see [=Pathfinder Framework=]   Section 3.2.2). The value MUST be one of the following: [...]

    to (roughly):
    > **Deprecated**
    >
    > The IPCC version of the GWP characterization factors used **in the calculation of the largest relative share of the PCF** (see [=Pathfinder Framework=]   Section 3.2.2). The value MUST be one of the following: [...]
    >
    > [...]
    >
    > **Advisement: This property is deprecated and only kept to ensure backwards-compatibility. It does not replace the (also mandatory) property `characterizationFactorsSources`.**

    (Please refer to the proposed changes to the technical specification for a more detailed and complete diff.)

2. Add the new mandatory property `characterizationFactorsSources` with the new data type `CharacterizationFactorsSources`, defined as a non-empty `Array` of `CharacterizationFactorsSource`. The new data type `CharacterizationFactorsSource` is defined as an `Object` with the mandatory fields `"name"` and `"version"`, both of which are non-empty `Strings`. The value of the `"name"` field SHOULD be `"IPCC Assessment Report"` and the version SHOULD be either `"5"` or `"6"`.

### Rationale

This proposal aims at providing a forward-looking change on characterization factors while preserving backwards-compatibility.

Backwards-compatibility is preserved by keeping the `characterizationFactors` property (despite its becoming deprecated).

It is forward-looking as future adaptations will hardly break backwards-compatibility. If a more fine-grained account of characterization factors use is ever desired, it can be included through optional properties of `CharacterizationFactorsSource`. If ever other sources become relevant (e.g., for specific industries) this too can be acommodated without the need for a breaking change.

## Consequences

1. This ADR introduces a minor change: since the `characterizationFactors` property is maintained, it is backwards compatible.
2. Accordingly, the Technical Specifications version number must be updated from 2.1.x to 2.2.0.
