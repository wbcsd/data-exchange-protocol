# 30. Extending the syntactic allowance of exempt emissions

Date: 2024-03-12

## Status

Proposed

## Context

Pathfinder Framework 2.0 limits exempted emissions to 5%.

This is reflected in the Tech Specs accordingly, so the property
[`exemptedEmissionsPercent`](https://wbcsd.github.io/tr/2023/data-exchange-protocol-20231207/#element-attrdef-carbonfootprint-exemptedemissionspercent) is defined as a percentage between `0` and `5`.

However, feedback has been provided to the Methodology Working Group stating that
this limit is too restrictive:

1. PCFs cannot be shared if the exempt emissions exceed 5% - e.g. if they are 5.1% and all other requirements are met.
2. Companies may be incentivized to report an untrue value in order to meet the synthetic requirements of being 5% or less.

Therefore, the Methodology Working Group proposes the following changes to the tech specs:

1. to remove the upper limit at the **syntactical level**.
2. while clearly stating that the **methodological** requirement for exempt emissions as is - i.e. at 5% or less.


## Decision

The definition of `exemptedEmissionsPercent` is updated from

> The Percentage of emissions excluded from PCF, expressed as a decimal number between `0.0` and `5` including. See [=Pathfinder Framework=].

to

> The percentage of emissions EXCLUDED from the cradle-to-gate PCF in total. The percentage MUST be expressed as a decimal number, and SHOULD comply with the Pathfinder Framework (a maximum of 5% of the cradle to gate PCF emissions may be excluded) as well as any relevant sector-specific guidelines referring to exemption rules/cut-off criteria.

The necessary update to the tech specs will be reflected in the **next major release** (see below).


## Consequences

This change breaks backwards compatibility.