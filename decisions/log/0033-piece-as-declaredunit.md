# 33. Introducing piece as declared unit

Date: 2024-04-18

## Status

Proposed

* PACT Methodology Working group is aligned to the proposal, per discussions November 2023
* Three sector initiatives (Catena-X, TfS, and Green x Digital) raised feedback requesting the addition of `piece` as declaredUnit. Through discussions with these initiatives, we have arrived at this proposal; we are now working with these initaitives to receive final review and approval before taking the proposal to the PACT Tech Working group May 15.

## Context

Framework v2.0 and associated tech specs allow only physical metrics as declared units, including: liter, kilogram, cubic meter, kilowatt hour, megajoule, ton kilometer, or square meter

Feedback has been raised to consider adding piece as a declared unit, but also requiring the mass to always be provided. The following considerations motivate this recommendation:

Feedback motivating the addition of `piece` as declaredUnit:

- For some industries (especially automotive and electronics), PCFs are calculated and compared by unit of product (aka “piece”), not by physical unit
- Our current standard requires PCFs to be entered and stored by physical units. Although one could argue that the current standard can also accommodate PCFs calculated by unit to be stored as PCFs calculated by physical unit, we received feedback from users that this conversion causes confusion and results in a likely misinterpretation of the PCF data being entered and shared. Further, as PCF exchange is going through a transition period from "spreadsheets" to "solutions", the PACT data model is increasingly exposed to end-users, potentially in the form of questionnaires, hence the need and value of such data attributes to be displayed in an understandable and easy-to-enter and understand way to end-users. In short, humans and not just machines must understand and use the data model.
- In some industries, the physical unit of the product (i.e. mass) is either not known, not systematically maintained in ERP systems, or not identical among products (specifically in the electronics sector, mass may vary slightly among products), and therefore is not the best unit of measure to calculate a comparable PCF

If `piece` is added as a declaredUnit, however, there is still a need to know the physical unit of the product. This was understood based on feedback from the PACT Methodology Working Group which discussed this topic in detail in Fall 2023:

- To enable comparability of products by physical units, a physical unit of measure is necessary (i.e. the mass of one piece); this approach aligns with industry standards such as PEF as well as sector PCF standards (GBA, TfS, Catena-X)
- The physical metric of a product is not always included in the bill of materials, buyers typically do not always know and/or receive from their supplier the mass of a product. If PCFs are exchanged by unit, and arguably the mass of the product is irrelevant for comparability in some contexts, it still remains relevant for other reasons and contexts: for example, to enable a plausibility check (aka mass balance) which is generally beneficial from a supply chain procurement perspective. Therefore, product mass is a highly relevant attribute to propagate through the value chain.

## Proposal
Based on discussions with initiatives (GBA, TfS, Catena-X) and PACT Working Groups to-date, we present the following proposal for consultation and revision.

- Extend the `declaredUnit` attribute to include `piece`
- Add a new attribute `productMassPerDeclaredUnit`
    - Attribute must be populated for which mass is a relevant unit to represent the product (i.e. mass is not relevant for PCFs calculated for energy products or service carbon footprints; mass is relevant for all physical products with mass)
    - Attribute Description: “Mass (in kg) of the product per the provided declared unit, excluding packaging. For example, if declared unit is piece, this attribute must be populated with the mass of one piece (aka unit) of product. If the declared unit is liter, this attribute must be populated with the mass of 1 liter of product (i.e. the density of the product). If the declared unit is kilogram, productMassPerDeclaredUnit must by definition be 1. If the product mass is not relevant (i.e. PCF is for an energy (kWh, MJ), logistics (ton.km) or service product), attribute must be 0."

Several examples using the above proposal can be seen here: https://wbcsd.sharepoint.com/:x:/s/ClimateEnergy/EfT4Uj_q1JxJgWTdh71lW5YBnKFvL5-Gyrqdg_N11P8eRA?e=lNAuWq

## Technical Specification

Addition to the possible values of `DeclaredUnit`:
```
: <dfn>piece</dfn>
:: For a piece, a unit of product
```

Addition of new property `productMassPerDeclaredUnit` to `CarbonFootprint`:
```
<tr>
    <td><dfn>productMassPerDeclaredUnit</dfn> : [=Decimal=]
    <td>string
    <td>M
    <td>The mass (in kg) of the product per the provided <{CarbonFootprint/declaredUnit|declared unit}>, excluding packaging.
    For example, if the declared unit is `piece`, this attribute MUST be populated with the mass of one piece (aka unit) of product.
    If the declared unit is `liter`, this attribute MUST be populated with the mass of 1 liter of product (i.e. the density of the product).
    If the declared unit is `kilogram`, this attribute MUST by definition be populated with `1`.
    If the product mass is not relevant (i.e. PCF is for an energy (kWh, MJ), logistics (ton.km) or service product), this attribute MUST be populated with `0`.
```


## Consequences

- The proposal would require backwards breaking changes, so would only be releasable in v3 of the technical specifications
- As of May 2024, TfS, Catena-X, and Green x Digital all endorse this proposal; further, the proposal would resolve one interoperability blocker with Catena-X, which mandates piece as a declaredUnit
