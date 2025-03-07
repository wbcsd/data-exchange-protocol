# 39. Consistent typing of real numbers

Date: 2024-09-23

## Context

As the PACT data model evolved, numerous properties have been added, some of them denoting real numbers, like percentages and ratings (in contrast to integers which are always whole numbers). 

As there
is a certain amount of ambiguity in the JSON format regarding real numbers, this has 
resulted in several properties having different ways of representing numbers. This
can lead to confusion for implementors and users of the data. 

This proposal aims to remedy that by uniformly typing these numbers and adding 
guidelines for future expansion of the specs.

## Background

The JSON data format does not specify any precision for numbers. The representation of 
these have been delegated to implementors. As a result, JSON parsers in different programming languages
thus have several ways of interpreting and storing real numbers. Although rare, in worst case, this could result in (some) data loss.

In order not to be dependent on technical implementations, PACT has choosen to represent 
numeric emission data (carbon footprint emissions) as decimal numbers formatted as strings. 

Example:

    { 
        "fossilGhgEmissions": "12345.6789"
    }
  
This way no precision is lost, although the burden of interpreting these numbers is 
now relegated to the implementors of the PACT API. This is, however, in most cases 
trivial and most programming languages have support for Decimal type numbers
specially purposed for scientific and financial calculations.

## Proposal

Based on discussion both with the community (Takuro Okada of NRI) and internally, we propose the following for consultation and revision.

- Change the type of the following attributes (properties) from Number to "Decimal" (string):
  - `pcf.exemptedEmissionsPercent`
  - `pcf.primaryDataShare`    
  - `pcf.dqi.coveragePercent`     
  - `pcf.dqi.technologicalDQR`    
  - `pcf.dqi.temporalDQR`         
  - `pcf.dqi.geographicalDQR`     
  - `pcf.dqi.completenessDQR`    
  - `pcf.dqi.reliabilityDQR`      

- Note: property `version` will stay a Number as it will always be an integer.

- Add a guideline to the Tech Specs, aiding the addition of future properties, as well
as guiding the types in data extensions:
    - For integers (*and only* for integers) use the JSON **Number** type and include the `integer` format specifier in the OpenAPI schema.

            { counter: 1 }

    - For real numbers *ALWAYS* use the **Decimal** type: an arbitrary sized number, formatted as a string, with a '.' (dot) as decimal point, *without* any thousands separators. 

            { temperature: "12.3" }

## Consequences

As this would break backwards compatibility with version 2.x these changes should - if accepted - be included from version 3 upwards.

## Status

Presented in the Tech Working Group meeting of Sept 25, 2024. 
Feedback collected.
Call for consensus Oct 9, 2024. Consensus reached.
