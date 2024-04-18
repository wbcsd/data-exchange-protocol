# 33. Introducing piece as declared unit

Date: 2024-04-18

## Status

Proposed

## Context

Framework v.2 and associated tech specs allow only physical metrics as declared units, including: liter, kilogram, cubic meter, kilowatt hour, megajoule, ton kilometer, or square meter

Feedback has been raised to consider adding piece as a declared unit, but also requiring the mass to always be provided. The following considerations motivate this recommendation:

Feedback motivating the addition of `piece` as declaredUnit:

- For some industries (especially automotive and electronics), PCFs are calculated and compared by unit of product (aka “piece”), not by physical unit
- Our current standard requires PCFs to be entered and stored by physical units. Although one could argue that the current standard can also accommodate PCFs calculated by unit to be stored as PCFs calculated by physical unit, we received feedback from users this conversion causes confusion and results in a likely misinterpretation of the PCF data being entered and shared
- In some industries, the physical unit of the product (i.e. mass) is either not known, not systematically maintained in ERP systems, or not identical among products (specifically in the electronics sector, mass may vary slightly among products), and therefore is not the best unit of measure to calculate a comparable PCF

If `piece` is added as a declaredUnit, feedback motivating the need to also ensure the physical unit of the product is shared:

- To enable comparability of products by physical units, a physical unit of measure is necessary (i.e. the mass of one piece); this approach aligns with industry standards such as PEF as well as sector PCF standards (GBA, TfS, Catena-X)
- The physical metric of a product is not always included in the bill of materials, buyers typically do not always know and/or receive from their supplier the mass of a product. If PCFs are exchanged by unit, and arguably the mass of the product is irrelevant for comparability in some contexts, it still remains relevant for other reasons and contexts: for example, to enable a plausibility check (aka mass balance) which is generally beneficial from a supply chain procurement perspective. Therefore, product mass is a highly relevant attribute to propagate through the value chain.

## Proposal
Based on discussions with initiatives (GBA, TfS, Catena-X) and PACT Working Groups to-date, we present the following proposal for consultation and revision.

**Proposal 1**

- Extend the `declaredUnit` attribute to include `piece`
- Add a new attribute `productMassPerDeclaredUnit`
    - Attribute must be populated for which mass is a relevant unit to represent the product (i.e. mass is not relevant for PCFs calculated for energy products or service carbon footprints; mass is relevant for all physical products with mass)
    - Attribute Description: “Mass (in kg) of the product per the provided declared unit, excluding packaging. This attribute supports mass conversion, and is only relevant when the PCF is neither an energy nor service carbon footprint. For example, if declared unit is `piece`, this attribute must be populated with the mass of one piece (aka unit) of product. If the declared unit is `liter` , this attribute must be populated with the mass of 1 `liter` of product)”
    - To be determined under which circumstances this attribute is mandatory (i.e. mandatory if declaredUnit = piece, not mandatory if PCF does not represent a physical product, such as an energy PCF or service PCF)
 
## Technical Specification
To be populated - once we have final alignment on the Proposal

## Consequences

- The proposal would require backwards breaking changes, so would only be releasable in v3 of the technical specifications
- The proposal would resolve one interoperability blocker with Catena-X, which mandates piece as a declaredUnit
