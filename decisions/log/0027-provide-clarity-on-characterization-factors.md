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

1. Change the definition of the `characterizationFactors` from (roughly):
    > The IPCC version of the GWP characterization factors used in the calculation of the PCF (see [=Pathfinder Framework=]   Section 3.2.2). The value MUST be one of the following: [...]

    to:
    > **Deprecated**
    >
    > The IPCC version of the GWP characterization factors used **for the largest relative share of the PCF** in **ist** calculation (see [=Pathfinder Framework=]   Section 3.2.2). The value MUST be one of the following: [...]
    >
    > [...]
    >
    > **Note: This property is deprecated and only kept to ensure backwards-compatibility. It does not replace the (also mandatory) property `characterizationFactorsList`.**

    (Please refer to the proposed changes to the technical specification for a more detailed and complete diff.)

2. Add the new mandatory property `characterizationFactorsList` with the new data type `CharacterizationFactorsSet`, defined as a non-empty `Object`, such that:
   1. it has two **Optional** properties `ar5` and `ar6`, both of which have `Percent` values;
   2. the sum total of the values cannot exceed 100.
   3. the key of the highest value must match the value of the `characterizationFactors` property (where `ar5` corresponds to `"AR5"` and `ar6` to `"AR6"`). If both values are equal, any of them can be used as the value of `characterizationFactors`.


### Rationale

This proposal aims at providing a forward-looking change that improves clarity on characterization factors while preserving backwards-compatibility.

Backwards-compatibility is preserved by keeping the `characterizationFactors` property (despite its becoming deprecated).

Clarity on characterization factors is improved as the PCF now states clearly whether one or more characterization factors were used, with the possibility of specifying the extend to which each was used. In case the Host System cannot achieve such fine-grained information, they can either provide an approximation or set both to `50`.

It is forward-looking as it preserves the possibility of adding further properties to the `CharacterizationFactorsSet` data type, such as further characterization factors, or more utility driven properties like `uknown`.

## Consequences

1. This ADR introduces a minor change: since the `characterizationFactors` property is maintained, it is backwards compatible.
2. Accordingly, the Technical Specifications version number must be updated from 2.1.x to 2.2.0.
