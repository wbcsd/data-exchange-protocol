# 0043 - Standardise Restricted Value Casing

Date: [2024-12-15]

## Status

Proposed

## Context

When working with what are commonly defined as enum values, there is consistent inconsistently in the values and how they are presented, this currently manifests as implementation complexity and will only increase complexity in future iterations of the standard.

This can be seen clearly in the following example, but the problem exists in a variety of locations:

https://wbcsd.github.io/tr/2024/data-exchange-protocol-20240410/#dt-assurance

The Assurance datatype has 3 properties that can be easily represented using standard Enum types when implementing the spec in software, these are:

1. coverage
2. level
3. boundary

And these 3 "enum-able" data types give the following options for valid selection:

1. coverage
- "corporate level"
- "product line"
- "PCF system"
- "product level"

2. level
- "limited"
- "reasonable"

3. boundary
- "Gate-to-Gate"
- "Cradle-to-Gate"

As you can see here, the applicable values provide a wide range of acceptable format, using spaces for some, mixed capitalisation, CamelCasing, and the use of hyphens also.

This presents an implementation nightmare when attempting to cover for acceptable values, and it is not clear why free form text in these situations is of much value.

NOTE: This has not covered all situations where this would be useful, I have provided an example using the Assurance datatype, but there are many places where this change can and should be implemented.

## Decision

I recommend using standard ALL_CAPS styling for any fields/attributes and data types where a restricted list of potential values is presented. This will vastly simplify the process of checking for such values, whilst also provide a standard for future changes to the spec.

## Consequences

This change will be a breaking change.
