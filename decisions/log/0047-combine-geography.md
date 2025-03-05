# 47 Combine geography attributes into one.  

## Context
The current CarbonFootprint type in the OpenAPI specification includes three separate properties to denote geographic information: `geographicRegion`, `geographyCountry`, and `geographyCountrySubdivision`. This separation can lead to redundancy and complexity in the data model. To simplify the model and improve clarity, we propose combining these properties into a single geography property.

## Proposal
For object type `CarbonFootprint`, combine the properties `geographicRegion`, `geographyCountry`, and `geographyCountrySubdivision` on into a single `geography` property:

This new property will be a string that can denote a region, country, or country subdivision and MUST be in one of the following formats:
 - Country: ISO 3166-1 alpha-2. Two-letter country codes (e.g., `"US"` for the United States, `"DE"` for Germany).
 - ISO 3166-2: Codes for the principal subdivisions (e.g., states or provinces) of all countries coded in ISO 3166-1 (e.g., `"US-CA"` for California, United States).
 - UN M49: Standard for area codes used by the United Nations for statistical purposes (e.g., `"150"` for Europe, `"001"` for the World).

As a consequency, the existing `geographyRegion`, `geographyCountry`, and `geographyCountrySubdivision` properties will be removed.

### Broadening M49 Regions and mapping to M49 Codes

Version 2.x limits the values for `geographyRegion` to the second and third-level regions defined in the UN M49 standard and used their full names (`"Latin America and the Carribean"`, `"Sub-Saharan Africa"`).

This means that, BOTH larger regions (e.g. `"Europe"`) AND more specific regions (`"Western Africa"`) can not be specified.

To be able to make full use of the granularity provided by the UN M49 standard AND to simplify processing of the `geography` values, we propose to allow the use of **all** M49 **codes** 
in the standard and deprecate the use of the full names.

The current allowed values for `geographyRegion` must be mapped to the following codes:

```
Africa: 002
Americas: 019
Asia: 142
Europe: 150
Oceania: 009
Australia and New Zealand: 053
Central Asia: 143
Eastern Asia: 030
Eastern Europe: 151
Latin America and the Caribbean: 419
Melanesia: 054
Micronesia: 057
Northern Africa: 015
Northern America: 021
Northern Europe: 154
Polynesia: 061
South-eastern Asia: 035
Southern Asia: 034
Southern Europe: 039
Sub-Saharan Africa: 202
Western Asia: 145
Western Europe: 155
```

## Examples

``` 
geography: "FR"    // France
geography: "035"   // South-eastern Asia
geography: "DE-BA" // Germany - Bayern
geography: "001"   // World
geography: "484"   // Mexico
```

## Consequences

This change will break backward compatibility with version 2.x. Therefore, it should be included in version 3.0 onwards.

For transforming an existing PCF from 2.x to 3.0 the following logic can be used (pseudo-code)

```
new.pcf.geography = 
  old.pcf.geographyCountrySubdivision ??
  old.pcf.geographyCountry ?? 
  GetM49Code(old.pcf.geographyRegion)
```

The simplified model will make it easier to filter and query geographic information.

## Status

To be presented in the Tech Working Group meeting of March 12, 2025. Feedback to be collected. 