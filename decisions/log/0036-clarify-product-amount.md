# 36. Clarify product amount

Date: 2024-08-29

## Status

Proposed

* PACT Methodology Working group is aligned to the proposal, per discussions July and August 2024.
* Reviewed with TfS and SAP, now working to present proposal for v3 to the PACT Tech Working group September 11.


## Context 

To share a given PCF, Framework V2 and Tech Specs require the PCF to be shared with units kgCO2e / `declaredUnit` 
 
`declaredUnit` may be specified with the physical unit (liter, kilogram, cubic meter, etc.), or piece (to be released in v3) 
 
To share the actual AMOUNT of declared units the product contains, the attribute `unitaryProductAmount` must be populated. 
 
For example, a 12L bottle of bio-Ethanol: 
```
declaredUnit: liter 
unitaryProductAmount: 12 
pCfExcludingBiogenic: 1.5 
```
 
This data should be interpreted as the bio-ethanol has a carbon intensity of 1.5 kgCO2e / liter. The total carbon intensity of the 12L bottle (i.e. the product) has a TOTAL carbon intensity therefore of 1.5 kgCO2e x 12 = 18 kgCO2e (assuming packaging emissions are excluded). 
 

## Problem Statement 
 
We received feedback from the PACT community (specifically from suppliers requested to provide PCF data) that from a data-entry perspective, these attributes are not very clear and easily confused, which is risky given the fundamental nature of these three attributes. 

For example, some suppliers entered their entire supply amount in the `unitaryProductAmount` attribute, and others entered the PCF of the ENTIRE product as `pCfExcludingBiogenic`, rather than for 1 unit of the given declared unit. 
 
## Proposal 
 
Introducing `“piece”` as a `declaredUnit` (see feedback item here) helps to address this problem, however it doesn’t fully address the confusion of the attributes and their interpretation especially when a physical declared unit is being used. Additionally, examples in the   PACT v2.2.0 Simplified Tech Specs Data Model_vSHARED.xlsx were created and provided to support further bringing clarity in the data exchange. 
 
However, besides the above additions, the PACT Methodology working group members raised feedback to consider the naming of the attributes, which are not intuitive enough to users. 
 
The specific feedback received was that part of the confusion might come from the term '*declared unit*'. ISO14067 (6.3.3 Functional or declared unit), states *“CFP study shall clearly specify the functional or declared unit of the system under study. The functional or declared unit shall be consistent with the goal and scope of the CFP study. The primary purpose of a functional or declared unit is to provide a reference to which the inputs and outputs are related. Therefore, the functional or declared unit shall be clearly defined and measurable.”*                                     
 
Therefore, per ISO the '*declared unit*' is already an amount. It is not a unit of measure. PACT Tech Specs currently do not reflect this, in that declaredUnit is only a unit of measure in the specs. 

### Data Model Proposal 
 
Therefore, we propose the following changes to the data model: 
 
- Rename `declaredUnit` to `declaredUnitOfMeasurement` 
- Rename `unitaryProductAmount` to `declaredUnitAmount` 
- Specify the `pCfExcludingBiogenic` and `pCfIncludingBiogenic` should be calculated with units (kgCO2e / declared unit), with an explanation of the definition of declared unit 
- Declared Unit (per the ISO concept) is therefore defined as the `declaredUnitAmount` of  `declaredUnitOfMeasurement` (i.e. 12L for a 12L bottle) 
- The mass of packaging is to be excluded from the `declaredUnitAmount` (similar to `productMassPerDeclaredUnit`, where the mass of packaging is likewise excluded) 
 
### Considerations regarding packaging

This proposal sparked a debate among initiatives regarding how the emissions due to packaging should be accounted for and disclosed. PACT maintains the opinion that emissions due to packaging must be calculated and disclosed, to drive comparability and transparency given the footprint of a product is considered holistically - including its packaging.

We exclude the mass of product packaging from the declaredUnitAmount  and productMassPerDeclaredUnit  attributes for the following reasons: 
- Excluding mass of packaging is common practice when assessing the functional unit in LCA 
- Data recipients who wish to conduct mass balance (validation of procured products by mass) will do so using the unpackaged product, hence the need for the mass of the unpackaged product 

Excluding the mass of packaging does not however imply that the emissions due to packaging will be excluded from disclosure – packaging emissions transparency are being addressed in separate backlog item: https://flat-dollar-c04.notion.site/Provide-clarity-on-packaging-accounting-i-e-primary-secondary-and-tertiary-packaging-inclusion-ed6a3c17c99845c788e45b9d9fbfb5fa  

## Examples 
The below examples indicates how a PCF will be encoded in the data model in V2 vs. V3 (this proposal). 

### 12l bottle of Bio-Ethanol

| Current version 2                             | 12L Bottle of bio-Ethanol (with packaging) |
|-----------------------------------------------|--------------------------------------------|
| declaredUnit	                                | liter                                      |
| unitaryProductAmount	                        | 12                                         |
| pCfExcludingBiogenic (kgCO2e/declared unit)   | 1.5                                 |
| productMassPerDeclaredUnit (kg/declared unit) | 0.789                               |


| Proposed version 3                            | 12L Bottle of bio-Ethanol (with packaging) | 12L Bottle of bio-Ethanol (with packaging) |
|-----------------------------------------------|---------|-------|
| declaredUnitOfMeasurement                     | liter	  | piece |
| declaredUnitAmount                            | 12      | 1     |
| pCfExcludingBiogenic (kgCO2e/declared unit)	| 18      | 18    |  
| productMassPerDeclaredUnit (kg/declared unit) | 9.468	  | 9.468 |


### 2000kg car, 600,000 kgCO2e/car

| Current version 2                             | PCF of a car |
|-----------------------------------------------|--------------|
| declaredUnit                                  | kilogram     |
| unitaryProductAmount                          | 2000         |
| pCfExcludingBiogenic (kgCO2e/declared unit)   | 300          |
| productMassPerDeclaredUnit (kg/declared unit) | 1            |

| Proposed version 3                            |              | Alternative |
|-----------------------------------------------|--------------|-------------|
| declaredUnitofMeasurement                     | kilogram     | piece       |
| declaredUnitAmount                            | 2000         | 1           |
| pCfExcludingBiogenic (kgCO2e/declared unit)   | 600000       | 600000      |
| productMassPerDeclaredUnit (kg/declared unit) | 2000         | 2000        |
