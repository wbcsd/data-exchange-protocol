# 39. Consistent typing of real numbers

Date: 2025-01-18

## Context

In order to report on biogenic emissions, removals and withdrawals, a number of attributes need to be added to the PACT data model.

After reaching consensus on the Methodology WG and sub-working groups, this proposal now describes the changes to be implemented in version 3.0 of the PACT data model. 

## Background

The following guidelines and categorizations have been leading in naming the new attributes, and considering removal or change of definition of existing attributes. These will also be used in future expansion of the specs:

 - Backwards compatible if possible
 - Origins: Biogenic/Fossil
 - Activity: Land-mgmt, land-use, transport
 - Type: CO2 / NonCO2 / GHG. (GHG = CO2+NonCO2)
 - Direction: Emissions / Withdrawal / Removals


## Proposal

### New attributes

DRAFT can be found here https://wbcsd.sharepoint.com/:x:/s/ClimateEnergy/EcdADK69ET9FrsPbusdtEysBjMeFddYBhxTrntisOYLbBw?e=V4Mhfd

Upon finalization these will included in this ADR.

## Consequences

As this would break backwards compatibility with version 2.x these changes should - if accepted - be included from version 3 upwards.

## Status

Presented in the Tech Working Group meeting of January 15, 2025. 
Feedback collected.
