
## Data Type: <dfn element>ProductFootprint</dfn> ## {#dt-pf}

`ProductFootprint` is a data type which represents the carbon footprint
of a product under a specific scope ([[#dt-carbonfootprint-scope]])
and with values calculated in accordance with the [=PACT Methodology=].

The objective of a `ProductFootprint` is to provide interoperability between
the creator (the [=data owner=]) and the consumer (the [=data recipient=]) of
ProductFootprints. The details on the exchange of ProductFootprints are
specified in [[#api]].

Conceptually, the data type <{ProductFootprint}> is modeled as a multi-purpose
container for product-specific emission factors which is supported by
extensibility through [=Data Model Extensions=].

Data Model Extensions enable [=data owners=] to exchange additional information
related to a product with [=data recipients=]. The details are specified
in [[#dt-datamodelextension]] as well as [[!EXTENSIONS-GUIDANCE]], and [[!DATA-MODEL-EXTENSIONS]].

Each `ProductFootprint` can and should be updated over time, for instance to
incorporate new or refined data from [=data owners=] (see [[#lifecycle]]).


### Properties ### {#pf-properties}

A ProductFootprint has the following properties:

<figure id="pf-properties-table" dfn-type="element-attr" dfn-for="ProductFootprint">
  <table class="data">
    <thead>
      <tr>
        <th>Property
        <th>Type
        <th>Req
        <th>Specification
    <tbody>
      <tr>
        <td><dfn>id</dfn> : [=PfId=]
        <td>String
        <td>M
        <td>The product footprint identifier, See [[#dt-pfid]] for details.
      <tr>
        <td><dfn>specVersion</dfn>
        <td>String
        <td>M
        <td>
            The version of the ProductFootprint data specification with value <code>[VERSION]</code>.

            Advisement: Subsequent revisions will update this value according to [Semantic Versioning 2.0.0](https://semver.org/lang/en/).
      <tr>
        <td><dfn>precedingPfIds</dfn> : [=PfId=]
        <td>Array of Strings
        <td>O
        <td>
            If defined, MUST be non-empty set of preceding product footprint identifiers without duplicates.
            See [[#dt-pfid]] and [[#lifecycle-classification]] for details.
      <tr>
        <td><dfn>version</dfn>
        <td>Number
        <td>M
        <td>The version of the <{ProductFootprint}> with value an integer in the inclusive range of `0..2^31-1`.
      <tr>
        <td><dfn>created</dfn> : [=DateTime=]
        <td>String
        <td>M
        <td>A ProductFootprint MUST include the property `created` with value the timestamp of the creation of the ProductFootprint.
      <tr>
        <td><dfn>updated</dfn> : [=DateTime=]
        <td>String
        <td>O
        <td>A ProductFootprint SHOULD include the property `updated` with value the timestamp of the ProductFootprint update. A ProductFootprint MUST NOT include this property if an update has never been performed. The timestamp MUST be in UTC.
      <tr>
        <td><dfn>status</dfn>
        <td>String
        <td>M
        <td>
          Each ProductFootprint MUST include the property `status` with value one of the following values:

          : Active
          :: The default status of a product footprint is `Active`. A product
               footprint with <{ProductFootprint/status}> `Active` CAN be used
               by a [=data recipients=], e.g. for product footprint calculations.

          : Deprecated
          :: The product footprint is deprecated and SHOULD NOT be used for e.g. product footprint calculations by [=data recipients=].

          See [[#lifecycle]] for details.
      <tr>
        <td><dfn>statusComment</dfn>
        <td>String
        <td>O
        <td>
          If defined, a descriptive reasoning explaining the current status of the PCF, what was changed since the last version, etc. If the PCF was changed since a previous version, indicate all methodological and/or production process change(s) that occurred to result in the PCF change. For example, include the relevant change(s) from the list below:

          Methodological:
          - Access to new Emission Factor data (database, supplier-specific, company-specific)
          - Updated upstream data (i.e. upstream supplier updated their PCF based on methodology change)

          Production Process:
          - Change in process
          - Change in feedstock
          - Change from conventional to certified sustainable material
          - Change in energy source
          - Change in upstream supplier
          - Updated upstream data (i.e. upstream supplier updated their PCF based on process change)
        
          See [[#lifecycle]] for details.
      <tr>
        <td><dfn>validityPeriodStart</dfn> : [=DateTime=]
        <td>String
        <td>O
        <td>If defined, the start of the validity period of the ProductFootprint.
              The <dfn>validity period</dfn> is the time interval during which the ProductFootprint is declared as valid for use by a receiving [=data recipient=].

              The validity period is OPTIONAL defined by the properties <{ProductFootprint/validityPeriodStart}> (including) and <{ProductFootprint/validityPeriodEnd}> (excluding).

              If no validity period is specified, the ProductFootprint is valid for 3 years starting with <{CarbonFootprint/referencePeriodEnd}>.

              If a validity period is to be specified, then
              1. the value of <{ProductFootprint/validityPeriodStart}> MUST be defined with value greater than or equal to the value of <{CarbonFootprint/referencePeriodEnd}>.
              2. the value of <{ProductFootprint/validityPeriodEnd}> MUST be defined with value
                 1. strictly greater than <{ProductFootprint/validityPeriodStart}>, and
                 2. less than or equal to <{CarbonFootprint/referencePeriodEnd}> + 3 years.
      <tr>
        <td><dfn>validityPeriodEnd</dfn> : [=DateTime=]
        <td>String
        <td>O
        <td>The end (excluding) of the valid period of the ProductFootprint. See <{ProductFootprint/validityPeriodStart}> for further details.
      <tr>
        <td><dfn>companyName</dfn>
        <td>String
        <td>M
        <td>The name of the company that is the ProductFootprint Data Owner, with value a non-empty [=String=].
      <tr>
        <td><dfn>companyIds</dfn> : [=CompanyIdSet=]
        <td>Array
        <td>M
        <td>The non-empty set of Uniform Resource Names ([[!RFC8141|URN]]). Each value of this set is supposed to uniquely identify the ProductFootprint Data Owner. See [=CompanyIdSet=] for details.
      <tr>
        <td><dfn>productDescription</dfn>
        <td>String
        <td>M
        <td>The free-form description of the product, including any additional relevant information such as production technology, packaging, process, feedstock and technical parameters (e.g. dimensions). Products which are services (i.e. consulting) should include a short description of the service.
      <tr>
        <td><dfn>productIds</dfn> : [=ProductIdSet=]
        <td>Array
        <td>M
        <td>The non-empty set of [=ProductIds=] in [=URN=] format. Each of the values in the set is supposed to uniquely identify the product. See {#product-identifiers} for syntax and examples.
      <tr>
        <td><dfn>productClassifications</dfn>
        <td>Array of [=ProductClassification=]
        <td>O
        <td>
          The non-empty set of [=ProductClassifications=] in [=URN=] format. Each of the values in the set can classify the product as part of distinct groupings and categorizations. See {#product-identifiers}. 
          
          Advisement: Supersedes productCategoryCpc deprecated in version 2.3.
      <tr>
        <td><dfn>productCategoryCpc</dfn>
        <td>String
        <td>O
        <td>

          Advisement: DEPRECATED in 3.0. Superseded by <{ProductFootprint/productClassifications}>.

          The UN Central Product Classification (CPC) that the given product belongs to.
      <tr>
        <td><dfn>productNameCompany</dfn>
        <td>String
        <td>M
        <td>The non-empty trade name of the product.
      <tr>
        <td><dfn>comment</dfn>
        <td>String
        <td>O
        <td>

          Advisement: OPTIONAL in 3.0.

          Additional information related to the product footprint.

          Whereas the property <{ProductFootprint/productDescription}> contains product-level information, <{ProductFootprint/comment}> SHOULD be used for information and instructions related to the calculation of the footprint, or other information which informs the ability to interpret, to audit or to verify the Product Footprint.
      <tr>
        <td><dfn>pcf</dfn> : <{CarbonFootprint}>
        <td>Object
        <td>M
        <td>The carbon footprint of the given product with value conforming to the data type <{CarbonFootprint}>.
      <tr>
        <td><dfn>extensions</dfn> : <{DataModelExtension}>[]
        <td>Array
        <td>O
        <td>
          If defined, 1 or more data model extensions associated with the ProductFootprint.

          <{ProductFootprint/extensions}> MUST be encoded as a non-empty JSON Array of
          <{DataModelExtension}> JSON objects. See <{DataModelExtension}> for details.
  </table>
  <figcaption>Properties of data type ProductFootprint</figcaption>

</figure>


## Data Type: <dfn element>CarbonFootprint</dfn> ## {#dt-carbonfootprint}

A CarbonFootprint represents the carbon footprint of a product and related data in accordance with the [=PACT Methodology=].

### Scope of a CarbonFootprint ### {#dt-carbonfootprint-scope}

Each CarbonFootprint is scoped by
1. Time Period: the time period is defined by the properties <{CarbonFootprint/referencePeriodStart}> and <{CarbonFootprint/referencePeriodEnd}> (see [=PACT Methodology=] section 6.1.2.1)
2. Geography: further set by the properties <{CarbonFootprint/geographyRegionOrSubregion}>, <{CarbonFootprint/geographyCountry}>, and <{CarbonFootprint/geographyCountrySubdivision}> (see [=PACT Methodology=] section 6.1.2.2)

If a CarbonFootprint
1. Has geographical granularity `Global`, then the properties <{CarbonFootprint/geographyCountry}> and <{CarbonFootprint/geographyRegionOrSubregion}> and <{CarbonFootprint/geographyCountrySubdivision}> MUST be `undefined`;
2. Has a regional or sub-regional geographical granularity, then the property <{CarbonFootprint/geographyRegionOrSubregion}> MUST be `defined` and the properties <{CarbonFootprint/geographyCountry}> and <{CarbonFootprint/geographyCountrySubdivision}> MUST be `undefined`;
3. Has a country-specific geographical granularity, then property <{CarbonFootprint/geographyCountry}> MUST be `defined` AND the properties <{CarbonFootprint/geographyRegionOrSubregion}> and <{CarbonFootprint/geographyCountrySubdivision}> MUST be `undefined`;
4. Has a country subdivision-specific geographical granularity, then property <{CarbonFootprint/geographyCountrySubdivision}> MUST be `defined` AND the properties <{CarbonFootprint/geographyRegionOrSubregion}> and <{CarbonFootprint/geographyCountry}> MUST be `undefined`.


An overview of the relationship between the geographic scope and the definedness or undefinedness of properties is given in the following table:

<figure id="pdf-geographic-scopes-table">
  <table class="data">
    <thead>
      <tr>
        <th>Geographical Granularity / Level of aggregation
        <th>Property <{CarbonFootprint/geographyRegionOrSubregion}>
        <th>Property <{CarbonFootprint/geographyCountry}>
        <th>Property <{CarbonFootprint/geographyCountrySubdivision}>
    <tbody>
      <tr>
        <td>Global
        <td>`undefined`
        <td>`undefined`
        <td>`undefined`
      <tr>
        <td>Regional or Subregional
        <td>`defined`
        <td>`undefined`
        <td>`undefined`
      <tr>
        <td>Country
        <td>`undefined`
        <td>`defined`
        <td>`undefined`
      <tr>
        <td>Subdivision
        <td>`undefined`
        <td>`undefined`
        <td>`defined`
  </table>
  <figcaption>Geographic scope and definedness of CarbonFootprint properties</figcaption>

</figure>


### Properties ### {#dt-carbonfootprint-properties}

The properties of a CarbonFootprint are listed in the table below.

Advisement:
  The properties marked with `O*` are OPTIONAL only for reference periods
  before 2025, and for reference periods including the beginning of calendar
  year 2025 or later, the properties marked with `O*` MUST be defined.

<figure id="pf-carbonfootprint-properties-table" dfn-type="element-attr" dfn-for="CarbonFootprint">
  <table class="data">
    <thead>
      <tr>
        <th>Property
        <th>Type
        <th>Req
        <th>Specification
    <tbody>
      <tr>
        <td><dfn>declaredUnit</dfn> : {{DeclaredUnit}}
        <td>String
        <td>M
        <td>The unit of analysis of the product. See Data Type {{DeclaredUnit}} for further information.
      <tr>
        <td><dfn>unitaryProductAmount</dfn> : [=Decimal=]
        <td>String
        <td>M
        <td>The amount of <{CarbonFootprint/declaredUnit|Declared Units}> contained within the product to which the [[#dt-carbonfootprint|PCF]] is referring to. The value MUST be strictly greater than `0`.
      <tr>


        <td><dfn>productMassPerDeclaredUnit</dfn> : [=Decimal=]
        <td>String
        <td>O
        <td>

          Advisement: This property is optional in v2.3 but will be released in v3 as a mandatory attribute.

The mass (in kg) of the product per the provided <{CarbonFootprint/declaredUnit|declared unit}>, excluding packaging.
          For example, if the declared unit is `piece`, this attribute MUST be populated with the mass of one piece (aka unit) of product.
          If the declared unit is `liter`, this attribute SHOULD be populated with the mass of 1 liter of product (i.e. the density of the product).
          If the declared unit is `kilogram`, this attribute SHOULD by definition be populated with `1`.
          If the product mass is not relevant (i.e. PCF is for an energy (kWh, MJ), logistics (ton.km) or service product), this attribute SHOULD be populated with `0`.
      <tr>
        <td><dfn>pCfExcludingBiogenic</dfn> : [=Decimal=]
        <td>String
        <td>M
        <td>The product carbon footprint of the product <i>excluding</i> biogenic CO2 emissions. The value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kg of CO2 equivalent per declared unit` (`kgCO2e / declaredUnit`), expressed as a [=decimal=] equal to or greater than zero.
      <tr>
        <td><dfn>pCfIncludingBiogenic</dfn> : [=Decimal=]
        <td>String
        <td>O*
        <td>If present, the product carbon footprint of the product <i>including all</i> biogenic emissions (CO2 and otherwise). The value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kg of CO2 equivalent per declared unit` (`kgCO2e / declaredUnit`), expressed as a [=decimal=].

              Note: the value of this property can be less than `0` (zero).

      <tr>
        <td><dfn>fossilGhgEmissions</dfn> : [=Decimal=]
        <td>String
        <td>M
        <td>The emissions from fossil sources as a result of fuel combustion, from fugitive emissions, and from process emissions. The value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kg of CO2 equivalent per declared unit` (`kgCO2e / declaredUnit`), expressed as a [=decimal=] equal to or greater than zero.
      <tr>
        <td><dfn>fossilCarbonContent</dfn> : [=Decimal=]
        <td>String
        <td>M
        <td>The fossil carbon content of the product (mass of carbon). The value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kg Carbon per declared unit` (`kgC / declaredUnit`), expressed as a [=decimal=] equal to or greater than zero.
      <tr>
        <td><dfn>biogenicCarbonContent</dfn> : [=Decimal=]
        <td>String
        <td>M
        <td>The biogenic carbon content of the product (mass of carbon). The value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kg Carbon per declared unit` (`kgC / declaredUnit`), expressed as a [=decimal=] equal to or greater than zero.
      <tr>
        <td><dfn>dLucGhgEmissions</dfn> : [=Decimal=]
        <td>String
        <td>O*
        <td>If present, emissions resulting from recent (i.e., previous 20 years) carbon stock loss due to land conversion directly on the area of land under consideration. The value of this property MUST include direct land use change (dLUC) where available, otherwise statistical land use change (sLUC) can be used.
          The value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kg of CO2 equivalent per declared unit` (`kgCO2e / declaredUnit`), expressed as a [=decimal=] equal to or greater than zero.
          See [=PACT Methodology=] (Appendix B) for details.
      <tr>
        <td><dfn>landManagementGhgEmissions</dfn> : [=Decimal=]
        <td>String
        <td>O*
        <td>If present, GHG emissions and removals associated with land-management-related changes, including non-CO2 sources.
          The value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kg of CO2 equivalent per declared unit` (`kgCO2e / declaredUnit`), expressed as a [=decimal=].
      <tr>
        <td><dfn>otherBiogenicGhgEmissions</dfn> : [=Decimal=]
        <td>String
        <td>O*
        <td>If present, all other biogenic GHG emissions associated with product manufacturing and transport that are not included in dLUC (<{CarbonFootprint/dLucGhgEmissions}>), iLUC (<{CarbonFootprint/iLucGhgEmissions}>), and land management (<{CarbonFootprint/landManagementGhgEmissions}>).
          The value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kg of CO2 equivalent per declared unit` (`kgCO2e / declaredUnit`), expressed as a [=decimal=] equal to or greater than zero.
      <tr>
        <td><dfn>iLucGhgEmissions</dfn> : [=Decimal=]
        <td>String
        <td>O
        <td>If present, emissions resulting from recent (i.e., previous 20 years) carbon stock loss due to land conversion on land not owned or controlled by the company or in its supply chain, induced by change in demand for products produced or sourced by the company.
          The value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kg of CO2 equivalent per declared unit` (`kgCO2e / declaredUnit`), expressed as a [=decimal=] equal to or greater than zero.
          See [=PACT Methodology=] (Appendix B) for details.
      <tr>
        <td><dfn>biogenicCarbonWithdrawal</dfn> : [=Decimal=]
        <td>String
        <td>O*
        <td>If present, the Biogenic Carbon contained in the product converted to kilogram of CO2e. The value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kgCO2e / declaredUnit` expressed as a [=decimal=] equal to or <i>less than</i> zero.

      <tr>
        <td><dfn>aircraftGhgEmissions</dfn> : [=Decimal=]
        <td>String
        <td>O
        <td>If present, the GHG emissions resulting from aircraft engine usage for the transport of the product, excluding radiative forcing. The value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kg of CO2 equivalent per declared unit` (`kgCO2e / declaredUnit`), expressed as a [=decimal=] equal to or greater than zero.
      <tr>
        <td><dfn>characterizationFactors</dfn>
        <td>String
        <td>O
        <td>

          Advisement: DEPRECATED in 3.0. Superseded by <{CarbonFootprint/ipccCharacterizationFactorsSources}>.

          The IPCC version of the GWP characterization factors used in the calculation of the PCF (see [=PACT Methodology=] Section 3.2.2). In case several characterization factors are used, indicate the earliest version used in your calculations, disregarding supplier provided PCFs. The value MUST be one of the following:

          : `AR6`
          :: for the Sixth Assessment Report of the Intergovernmental Panel on Climate Change (IPCC)
          : `AR5`
          :: for the Fifth Assessment Report of the IPCC.
     <tr>
        <td><dfn>ipccCharacterizationFactorsSources</dfn>
        <td>Array of Strings
        <td>M
        <td>The characterization factors from one or more IPCC Assessment Reports used in the calculation of the PCF (see [=PACT Methodology=] Section 3.2.2).
          It MUST be a non-empty set of strings with the format `AR$VERSION$`, where `$VERSION$` stands for the
          IPCC report version number and MUST be an integer.

          Example values:
          <div class=example>["AR6"]</div>
          <div class=example>["AR5", "AR6"]</div>

          Per the Methodology the latest available characterization factor version shall be used, i.e., `["AR6"]`. In the event this is not possible, include the set of all characterization factors used.

          Advisement: Supersedes `characterizationFactors` deprecated in version 2.3.

      <tr>
        <td><dfn>crossSectoralStandards</dfn>
        <td>Array of Strings
        <td>M
        <td>The cross-sectoral standards applied for calculating or allocating [=GHG=] emissions.

          It MUST be a non-empty array and SHOULD contain only the following values without duplicates:

        : `ISO14067`
        :: for the ISO 14067 Standard, "Greenhouse gases — Carbon footprint of products — Requirements and guidelines for quantification"
        : `ISO14083`
        :: for the ISO 14083 Standard, "Greenhouse gases — Quantification and reporting of greenhouse gas emissions arising from transport chain operations"
        : `ISO14040-44`
        :: for the ISO 14040-44 Standard, "Environmental management — Life cycle assessment — Principles and framework"
        : `GHGP-Product`
        :: for the Greehouse Gas Protocol (GHGP) Product Standard
        : PEF
        :: for the EU Product Environmental Footprint Guide
        : `PACT-1.0`
        : `PACT-2.0`
        : `PACT-3.0`
        :: for a given version of the [=PACT Methodology=]. It is recommended to use the latest version of the Methodology.
        : PAS2050
        :: for the Publicly Available Specification (PAS) 2050, "Specification for the assessment of the life cycle greenhouse gas emissions of goods and services". The use of this standard is permitted but not recommended.

        The enumeration of standards above CAN evolve in future revisions. A host system MUST accept ProductFootprints from later revisions with `crossSectoralStandards` containing values that are not defined in this specification.

        Advisement: Supersedes `crossSectoralStandardsUsed` deprecated in version 2.3.
            
      <tr>
        <td><dfn>productOrSectorSpecificRules</dfn> : [=ProductOrSectorSpecificRuleSet=]
        <td>Array
        <td>O
        <td>The product-specific or sector-specific rules applied for calculating or allocating GHG emissions. If no product or sector specific rules were followed, this set MUST be empty.
      <tr>
        <td><dfn>biogenicAccountingMethodology</dfn>
        <td>String
        <td>O*
        <td>The standard followed to account for biogenic emissions and removals. If defined, the value SHOULD be one of the following:

          : `PEF`
          :: for the EU [Product Environmental Footprint Guide](https://ec.europa.eu/environment/archives/eussd/pdf/footprint/PEF%20methodology%20final%20draft.pdf)
          : `ISO`
          :: For the ISO 14067 standard
          : `GHGP`
          :: For the Greenhouse Gas Protocol (GHGP) Land sector and Removals Guidance
          : `Quantis`
          :: For the Quantis [Accounting for Natural Climate Solutions](https://quantis.com/report/accounting-for-natural-climate-solutions-guidance/) Guidance

          The enumeration of standards above will be evolved in future revisions. Account for this when implementing the validation of this property.
      <tr>
        <td><dfn>boundaryProcessesDescription</dfn>
        <td>String
        <td>O
        <td>

          Advisement: OPTIONAL in 3.0.

          The processes attributable to each lifecycle stage.

          Example text value:
          <div class=example>`Electricity consumption included as an input in the production phase`</div>
      <tr>
        <td><dfn>referencePeriodStart</dfn> : [=DateTime=]
        <td>String
        <td>M
        <td>The start (including) of the time boundary for which the PCF value
              is considered to be representative. Specifically, this start date
              represents the earliest date from which activity data was collected
              to include in the PCF calculation. 

              See the [=PACT Methodology=] section 6.1.2.1 for further details. 
              Can also be referred to as 'reporting period'.
      <tr>
        <td><dfn>referencePeriodEnd</dfn> : [=DateTime=]
        <td>String
        <td>M
        <td>The end (excluding) of the time boundary for which the PCF value is
              considered to be representative. Specifically, this end date
              represents the latest date from which activity data was collected
              to include in the PCF calculation. Can al

              See the [=PACT Methodology=] section 6.1.2.1 for further details. 
              Can also be referred to as 'reporting period'. 
      <tr>
        <td><dfn>geographyCountrySubdivision</dfn>
        <td>String
        <td>
        <td>If present, a ISO 3166-2 Subdivision Code. See [[#dt-carbonfootprint-scope]] for further details.

          Example value for the State of New York in the United States of America:
          <div class=example>`US-NY`</div>
          Example value for the department Yonne in France
          <div class=example>`FR-89`</div>
      <tr>
        <td><dfn>geographyCountry</dfn> : [=ISO3166CC=]
        <td>String
        <td>
        <td>If present, the value MUST conform to data type [=ISO3166CC=]. See [[#dt-carbonfootprint-scope]] for further details.

        Example value in case the geographic scope is France
        <div class=example>`FR`</div>
      <tr>
        <td><dfn>geographyRegionOrSubregion</dfn> : {{RegionOrSubregion}}
        <td>String
        <td>
        <td>If present, the value MUST conform to data type {{RegionOrSubregion}}. See [[#dt-carbonfootprint-scope]] for further details. Additionally, see the [=PACT Methodology=] Section 6.1.2.2.
      <tr>
        <td><dfn>secondaryEmissionFactorSources</dfn> : <{EmissionFactorDSSet}>
        <td>Array
        <td>O
        <td>If secondary data was used to calculate the <{CarbonFootprint}>, then it MUST include the property <{CarbonFootprint/secondaryEmissionFactorSources}> with value the emission factors used for the <{CarbonFootprint}> calculation.

        If no secondary data is used, this property MUST BE `undefined`.
      <tr>
        <td><dfn>exemptedEmissionsPercent</dfn>
        <td>[=Decimal=]
        <td>M
        <td>
          The percentage of emissions excluded from PCF, expressed as a decimal number. See [=PACT Methodology=].

          Advisement: [=Decimal=] in 3.0, was Number in 2.x
      <tr>
        <td><dfn>exemptedEmissionsDescription</dfn>
        <td>String
        <td>O
        <td>

          Advisement: OPTIONAL in 3.0.

          Rationale behind exclusion of specific PCF emissions, CAN be the empty string if no emissions were excluded.
      <tr>
        <td><dfn>packagingEmissionsIncluded</dfn>
        <td>Boolean
        <td>M
        <td>A boolean flag indicating whether packaging emissions are included in the PCF (<{CarbonFootprint/pCfExcludingBiogenic}>, <{CarbonFootprint/pCfIncludingBiogenic}>).
      <tr>
        <td><dfn>packagingGhgEmissions</dfn> : [=Decimal=]
        <td>String
        <td>O
        <td>
          Emissions resulting from the packaging of the product.
          If present, the value MUST be calculated per <{CarbonFootprint/declaredUnit|declared unit}> with unit `kg of CO2 equivalent per kilogram` (`kgCO2e / declared unit`), expressed as a [=decimal=] equal to or greater than zero.
          The value MUST NOT be defined if <{CarbonFootprint/packagingEmissionsIncluded}> is `false`.
      <tr>
        <td><dfn>allocationRulesDescription</dfn>
        <td>String
        <td>O
            <td>If present, a description of any allocation rules applied and the rationale explaining how the selected approach aligns with [=PACT Methodology=] rules (see Section 3.3.1.4).
      <tr>
        <td><dfn>uncertaintyAssessmentDescription</dfn>
        <td>String
        <td>O
            <td>If present, the results, key drivers, and a short qualitative description of the uncertainty assessment.
      <tr>
        <td><dfn>primaryDataShare</dfn>
        <td>[=Decimal=]
        <td>O*
        <td>
          The share of primary data in percent. See the [=PACT Methodology=] Sections 4.2.1 and 4.2.2, Appendix B.

          For reference periods ending before the beginning of year 2025, at least property <{CarbonFootprint/primaryDataShare}> or propery <{CarbonFootprint/dqi}> MUST be defined.

          For reference periods including the beginning of year 2025 or after, this property MUST be defined.

          Advisement: [=Decimal=] in 3.0, was Number in 2.x
      <tr>
        <td><dfn>dqi</dfn> : <{DataQualityIndicators}>
        <td>Object
        <td>O*
        <td>
          If present, the Data Quality Indicators (dqi) in accordance with the [=PACT Methodology=] Sections 4.2.1 and 4.2.3, Appendix B.

          For reference periods ending before the beginning of year 2025, at least property <{CarbonFootprint/primaryDataShare}> or propery <{CarbonFootprint/dqi}> MUST be defined.

          For reference periods including the beginning of year 2025 or after, this property MUST be defined.
      <tr>
        <td><dfn>assurance</dfn> : <{Assurance}>
        <td>Object
        <td>O
            <td>If present, the Assurance information in accordance with the [=PACT Methodology=].
  </table>
  <figcaption>Properties of data type CarbonFootprint</figcaption>

</figure>


## Data Type: <dfn element>DataQualityIndicators</dfn> ## {#dt-dataqualityindicators}

Data type `DataQualityIndicators` contains the quantitative data quality indicators in conformance with [=PACT Methodology=] Section 4.2.3 and Appendix B.

Each property is optional until the reference period includes the beginning of calendar year 2025, or later, when all properties MUST be defined.

Advisement: Starting version 3.0 the properties in DataQualityIndicators are typed [=Decimal=], instead of `Number`.

The following properties are defined for data type <{DataQualityIndicators}>:

<figure id="pf-dataqualityindicators-properties-table" dfn-type="element-attr" dfn-for="DataQualityIndicators">
  <table class="data">
    <thead>
      <tr>
        <th>Property
        <th>Type
        <th>Specification
    <tbody>
      <tr>
        <td><dfn>coveragePercent</dfn>
        <td>Decimal
        <td>
          Percentage of PCF included in the data quality assessment based on the `>5%` emissions threshold.
          
          Advisement: [=Decimal=] in 3.0, was Number in 2.x
      <tr>
        <td><dfn>technologicalDQR</dfn>
        <td>Decimal
        <td>
          Quantitative data quality rating (DQR) based on the data quality matrix (See [=PACT Methodology=] Table 9),
          scoring the technological representativeness of the sources used for PCF calculation based on
          weighted average of all inputs representing >5% of PCF emissions.

          The value MUST be a [=decimal=] between `1` and `3` including.

          Advisement: [=Decimal=] in 3.0, was Number in 2.x
      <tr>
        <td><dfn>temporalDQR</dfn>
        <td>Decimal
        <td>
          Quantitative data quality rating (DQR) based on the data quality matrix (Table 9),
          scoring the temporal representativeness of the sources used for PCF calculation based on
          weighted average of all inputs representing >5% of PCF emissions.

          The value MUST be between `1` and `3` inclusive.
          
          Advisement: [=Decimal=] in 3.0, was Number in 2.x
      <tr>
        <td><dfn>geographicalDQR</dfn>
        <td>Decimal
        <td>
          Quantitative data quality rating (DQR) based on the data quality matrix (Table 9),
          scoring the geographical representativeness of the sources used for PCF calculation
          based on weighted average of all inputs representing >5% of PCF emissions.

          The value MUST be between `1` and `3` inclusive.
          
          Advisement: [=Decimal=] in 3.0, was Number in 2.x
      <tr>
        <td><dfn>completenessDQR</dfn>
        <td>Decimal
        <td>
          Quantitative data quality rating (DQR) based on the data quality matrix (Table 9),
          scoring the completeness of the data collected for PCF calculation based on
          weighted average of all inputs representing >5% of PCF emissions.

          The value MUST be between `1` and `3` inclusive.
          
          Advisement: [=Decimal=] in 3.0, was Number in 2.x
      <tr>
        <td><dfn>reliabilityDQR</dfn>
        <td>Decimal
        <td>
          Quantitative data quality rating (DQR) based on the data quality matrix (Table 9),
          scoring the reliability of the data collected for PCF calculation based on
          weighted average of all inputs representing >5% of PCF emissions.

          The value MUST be between `1` and `3` inclusive.
          
          Advisement: [=Decimal=] in 3.0, was Number in 2.x
    </table>
  <figcaption>Properties of data type DataQualityIndicators</figcaption>
</figure>

<div class=example>
  Example value for the case that all DQIs are known but no coverage after exemption assessment performed:
  <pre highlight=json>
  {
    "technologicalDQR": "2.0",
    "temporalDQR": "2.0",
    "geographicalDQR": "2.0",
    "completenessDQR": "2.0",
    "reliabilityDQR": "2.0"
  }
  </pre>
</div>


## Data Type: <dfn element>Assurance</dfn> ## {#dt-assurance}

Data type `Assurance` contains the assurance in conformance with [=PACT Methodology=] chapter 5 and appendix B.

Advisement: the superfluous boolean property `assurance` has been REMOVED in version 3.0. The presence of the <{Assurance}> element indicates whether or not the <{CarbonFootprint}> has been assured in line with [=PACT Methodology=] requirements (section 5). 

The following properties are defined for data type <{Assurance}>:

<figure id="pf-assurance-properties-table" dfn-type="element-attr" dfn-for="Assurance">
  <table class="data">
    <thead>
      <tr>
        <th>Property
        <th>Type
        <th>Req
        <th>Specification
    <tbody>
      <tr>
        <td><dfn>coverage</dfn>
        <td>String
        <td>O
        <td>
          Level of granularity of the emissions data assured, with value equal to
          - `corporate level` for corporate level
          - `product line` for product line
          - `PCF system` for PCF System
          - `product level` for product level

          This property MAY be undefined only if the kind of assurance was not performed.
      <tr>
        <td><dfn>level</dfn>
        <td>String
        <td>O
        <td>
          Level of assurance applicable to the PCF, with value equal to
          - `limited` for limited assurance
          - `reasonable` for reasonable assurance

          This property MAY be undefined only if the kind of assurance was not performed.

      <tr>
        <td><dfn>boundary</dfn>
        <td>String
        <td>O
        <td>Boundary of the assurance, with value equal to
          - `Gate-to-Gate` for Gate-to-Gate
          - `Cradle-to-Gate` for Cradle-to-Gate.

          This property MAY be undefined only if the kind of assurance was not performed.
      <tr>
        <td><dfn>providerName</dfn>
        <td>String
        <td>O
        <td>The non-empty name of the independent third party engaged to undertake the assurance.

        Advisement: OPTIONAL in version 3.0.
      <tr>
        <td><dfn>completedAt</dfn> : [=DateTime=]
        <td>String
        <td>O
        <td>The date at which the assurance was completed. See data type [=DateTime=] for details.
      <tr>
        <td><dfn>standardName</dfn>
        <td>String
        <td>O
        <td>
          Name of the standard against which the PCF was assured.
      <tr>
        <td><dfn>comments</dfn>
        <td>String
        <td>O
        <td>
          Any additional comments that will clarify the interpretation of the assurance.

          This value of this property MAY be the empty string.
    </table>
  <figcaption>Properties of data type Assurance</figcaption>
</figure>

<div class=example>
  Example value for the case that 42% of the product's overall GHG emissions covered by the data quality assessment:
  <pre highlight=json>
  {
    "assurance": true,
    "coverage": "PCF system",
    "level": "limited"
    "boundary": "Cradle-to-Gate"
    "providerName": "My Auditor",
    "completedAt": "2022-12-08T14:47:32Z"
    "standardName": "ISO 14044"
  }
  </pre>
</div>


## Data Type: <dfn element>DataModelExtension</dfn> ## {#dt-datamodelextension}

Each data model extension MUST be a valid JSON object conforming with the
JSON Representation of Data Model Extensions
([§ 5. JSON Representation of a Data Model Extension](https://wbcsd.github.io/data-model-extensions/spec/#instantiation)).

See [[!DATA-MODEL-EXTENSIONS]] for technical details and [[!EXTENSIONS-GUIDANCE]] for data model extension guidance.


<div class=example>
Example imaginary Data Model Extension for encoding shipment-related data, encoded in JSON:

<pre highlight=json>
{
  "specVersion": "2.0.0",
  "dataSchema": "https://catalog.carbon-transparency.org/shipment/1.0.0/data-model.json",
  "data": {
    "shipmentId": "S1234567890",
    "consignmentId": "Cabc.def-ghi",
    "shipmentType": "PICKUP",
    "weight": 10,
    "transportChainElementId": "ABCDEFGHI"
  }
}
</pre>
</div>



## Data Type: <dfn enum>RegionOrSubregion</dfn> ## {#dt-regionorsubregion}

The data type `RegionOrSubregion` MUST be encoded as a [=String=] with value equal to one of the following values:

<dl dfn-type="enum-value" dfn-for="RegionOrSubregion">

: <dfn>Africa</dfn>
:: for the [=UN geographic region=] Africa

: <dfn>Americas</dfn>
:: for the [=UN geographic region=] Americas

: <dfn>Asia</dfn>
:: for the [=UN geographic region=] Asia

: <dfn>Europe</dfn>
:: for the [=UN geographic region=] Europe

: <dfn>Oceania</dfn>
:: for the [=UN geographic region=] Oceania

: <dfn>Australia and New Zealand</dfn>
:: for the [=UN geographic subregion=] Australia and New Zealand

: <dfn>Central Asia</dfn>
::  for the [=UN geographic subregion=] Central Asia

: <dfn>Eastern Asia</dfn>
:: for the [=UN geographic subregion=] Eastern Asia

: <dfn>Eastern Europe</dfn>
:: for the [=UN geographic subregion=] Eastern Europe

: <dfn>Latin America and the Caribbean</dfn>
:: for the [=UN geographic subregion=] Latin America and the Caribbean

: <dfn>Melanesia</dfn>
:: for the [=UN geographic subregion=] Melanesia

: <dfn>Micronesia</dfn>
:: for the [=UN geographic subregion=] Micronesia

: <dfn>Northern Africa</dfn>
:: for the [=UN geographic subregion=] Northern Africa

: <dfn>Northern America</dfn>
:: for the [=UN geographic subregion=] Northern America

: <dfn>Northern Europe</dfn>
::  for the [=UN geographic subregion=] Northern Europe

: <dfn>Polynesia</dfn>
:: for the [=UN geographic subregion=] Polynesia

: <dfn>South-eastern Asia</dfn>
:: for the [=UN geographic subregion=] South-eastern Asia

: <dfn>Southern Asia</dfn>
:: for the [=UN geographic subregion=] Southern Asia

: <dfn>Southern Europe</dfn>
:: for the [=UN geographic subregion=] Southern Europe

: <dfn>Sub-Saharan Africa</dfn>
:: for the [=UN geographic subregion=] Sub-Saharan Africa

: <dfn>Western Asia</dfn>
:: for the [=UN geographic subregion=] Western Asia

: <dfn>Western Europe</dfn>
:: for the [=UN geographic subregion=] Western Europe

</dl>


## Data Type: <dfn element>EmissionFactorDSSet</dfn> ## {#dt-emissionfactordataset}

A set of <{EmissionFactorDS|Emission Factor Data Sources}> of size 1 or larger.

### JSON Data Representation ### {#dt-emissionfactordataset-json}

As an array of objects, with each object conforming to the JSON representation of <{EmissionFactorDS}>.


## Data Type: <dfn element>EmissionFactorDS</dfn> ## {#dt-emissionfactords}

An EmissionFactorDS references emission factor databases (see [=PACT Methodology=] Section 4.1.3.2).

### Properties ### {#dt-emissionfactords-properties}

<dl dfn-type="element-attr" dfn-for="EmissionFactorDS">

: <dfn>name</dfn> (mandatory, data type: [=NonEmptyString=])
:: The non-empty name of the emission factor database.

: <dfn>version</dfn> (mandatory, data type: [=NonEmptyString=])
:: The non-empty version of the emission factor database.

</dl>

<div class=example>
Example encoding of a <{EmissionFactorDS}> in JSON:

```json
{
  "name": "ecoinvent",
  "version": "3.9.1"
}
```

</div>


### JSON Representation ### {#dt-emissionfactords-json}

Each <{EmissionFactorDS}> MUST be encoded as a JSON object.


## Data Type: <dfn element>ProductOrSectorSpecificRule</dfn> ## {#dt-productorsectorspecificrule}

A ProductOrSectorSpecificRule refers to a set of product or sector specific rules published by a specific operator and applied during product carbon footprint calculation.

### Properties ### {#dt-productorsectorspecificrule-properties}

<dl dfn-type="element-attr" dfn-for="ProductOrSectorSpecificRule">

: <dfn>operator</dfn> (mandatory, data type: {{ProductOrSectorSpecificRuleOperator}})
:: A ProductOrSectorSpecificRule MUST include the property `operator` with the value conforming to data type {{ProductOrSectorSpecificRuleOperator}}.

: <dfn>ruleNames</dfn> (mandatory, data type: [=NonEmptyStringVector=])
:: A ProductOrSectorSpecificRule MUST include the property `ruleNames` with value the non-empty set of rules applied from the specified <{ProductOrSectorSpecificRule/operator}>.

: <dfn>otherOperatorName</dfn> (optional, data type: [=NonEmptyString=])
::
    If the value of property <{ProductOrSectorSpecificRule/operator}> is `Other`, a <{ProductOrSectorSpecificRule}> MUST include the property `otherOperatorName` with value the name of the operator. In this case, the operator declared MUST NOT be included in the definition of {{ProductOrSectorSpecificRuleOperator}}.
    If the value of property operator is NOT Other, the property <{ProductOrSectorSpecificRule/otherOperatorName}> of a <{ProductOrSectorSpecificRule}> MUST be `undefined`.

</dl>

### JSON Representation ### {#dt-productorsectorspecificrule-json}

Each <{ProductOrSectorSpecificRule}> MUST be encoded as a JSON object.



## Data Type: <dfn>ProductOrSectorSpecificRuleSet</dfn> ## {#dt-productorsectorspecificruleset}

A set of ProductOrSectorSpecificRule of size 1 or larger.

### JSON Representation ### {#dt-productorsectorspecificruleset-json}

Each [=ProductOrSectorSpecificRuleSet=] MUST be encoded as an array of JSON objects, with each object conforming to [[#dt-productorsectorspecificrule-json]].




## Data Type: <dfn enum>ProductOrSectorSpecificRuleOperator</dfn> ## {#dt-productorsectorspecificruleoperator}

A ProductOrSectorSpecificRuleOperator is the enumeration of Product Category Rule (PCR) operators. Valid values are:

<dl dfn-type="enum-value" dfn-for="ProductOrSectorSpecificRuleOperator">

: <dfn>PEF</dfn>
:: for EU / <a href="https://ec.europa.eu/environment/archives/eussd/pdf/footprint/PEF%20methodology%20final%20draft.pdf">PEF</a> Methodology PCRs

: <dfn>EPD International</dfn>
:: for PCRs authored or published by [EPD International](https://www.environdec.com/)

: <dfn>Other</dfn>
:: for a PCR not published by the operators mentioned above

</dl>

### JSON Representation ### {#dt-productorsectorspecificruleoperator-json}

Each value is encoded as a JSON String.



## Data Type: <dfn>NonEmptyStringVector</dfn> ## {#dt-nonemptystringvector}

A list of [=NonEmptyString=] of length 1 or greater.

### JSON Representation ### {#dt-nonemptystringvector-json}

Each NonEmptyStringVector MUST be encoded as an array of [=NonEmptyStrings=].


## Data Type: <dfn enum>DeclaredUnit</dfn> ## {#dt-declaredunit}

DeclaredUnit is the enumeration of accepted declared units with values

<dl dfn-type="enum-value" dfn-for="DeclaredUnit">

: <dfn>liter</dfn>
:: for special SI Unit `litre` (see [[!SI-Unit]] Table 8)

: <dfn>kilogram</dfn>
:: for SI Base Unit `kilogram` (see [[!SI-Unit]])

: <dfn>cubic meter</dfn>
:: for cubic meter, the Derived Unit from SI Base Unit `metre`

: <dfn>kilowatt hour</dfn>
:: for kilowatt hour, the Derived Unit from special SI Unit `watt`

: <dfn>megajoule</dfn>
:: for megajoule, the Derived Unit from special SI Unit `joule`

: <dfn>ton kilometer</dfn>
:: for ton kilometer, the Derived Unit from SI Base Units `kilogram` and `metre`

: <dfn>square meter</dfn>
:: for square meter, the Derived Unit from SI Base Unit `metre`

: <dfn>piece</dfn>
:: for a piece, a unit of product. If this is unit is specified, {CarbonFootprint/productMassPerDeclaredUnit}> MUST to be provided as well.

</dl>


### JSON Representation ### {#dt-declaredunit-json}

The value of each {{DeclaredUnit}} MUST be encoded as a JSON String.


## Data Type: <dfn>NonEmptyString</dfn> ## {#dt-nonemptystring}

A String with 1 or more characters.

### JSON Representation ### {#dt-nonemptystring-json}

Each NonEmptyString MUST be encoded as a JSON String.



## Data Type: <dfn>CompanyIdSet</dfn> ## {#dt-companyidset}

A set of [=CompanyIds=] of length 1 or greater.



## Data Type: <dfn>CompanyId</dfn> ## {#dt-companyid}

Each CompanyId MUST be a [=URN=].

### Custom Company Ids (Company Codes) ### {#dt-companyid-custom}

If the [=data owner=] wishes to use a custom company code assigned to it by
a [=data recipient=] as a [=CompanyId=] value, the [=data owner=] SHOULD use the following format:

```
urn:pact:company:customcode:buyer-id:$custom-company-code$
```

where `$custom-company-code$` stands for the custom company code assigned by the [=data recipient=].

<div class=example>
A data owner got assigned the custom vendor code `4321` by a buyer, the value of the CompanyId is then:

`urn:pact:company:customcode:buyer-id:4321`.
</div>


If the [=data owner=] wishes to use its own custom company code known by
a [=data recipient=] as a [=CompanyId=] value, the [=data owner=] SHOULD use the following format:

```
urn:pact:company:customcode:supplier-id:$custom-company-code$
```

where `$custom-company-code$` stands for the custom company code set by the [=data recipient=].

<div class=example>
A data owner uses as custom vendor code `6789` which is known to a buyer, the value of the CompanyId is then:

`urn:pact:company:customcode:buyer-id:6789`.
</div>




## Data Type: <dfn>ProductIdSet</dfn> ## {#dt-productidset}

A set of [=ProductIds=] of size 1 or larger.

### JSON Representation ### {#dt-productidset-json}

Each ProductIdSet MUST be encoded as an array of strings.

## Data Type: <dfn>ProductId</dfn> ## {#dt-productid}

Each ProductId MUST be a [=URN=], see [[#product-identifiers]] for details and examples.

<div class=example>
```json
```
</div>

## Data Type: <dfn>ProductClassification</dfn> ## {#dt-productclassification}

A ProductClassification MUST be a [=URN=] conforming to the syntax described under [[#product-identifiers]].

<div class=example>
  31230 represents the class “Wood in chips or particles” in the UN Central Product Classification (CPC) code for the product:

  ```json
    "productClassifications": [
      "urn:pact:catalog.company.com:category-id:550010",
      "urn:cpc:0151"
    ]
    ```
</div>


## Data Type: <dfn>URN</dfn> ## {#dt-urn}

A String conforming to the [[!RFC8141|URN syntax]].

### JSON Representation ### {#dt-urn-json}

Each [=URN=] MUST be encoded as a JSON String.


## Data Type: <dfn>String</dfn> ## {#dt-string}

A regular UTF-8 String.

### JSON Data Representation ### {#dt-string-json}

Each [=String=] MUST be encoded as a JSON String.



## Data Type: <dfn>DateTime</dfn> ## {#dt-datetime}

Each DateTime MUST be a date and time string conforming to ISO 8601. The timezone MUST be UTC.

Example value for beginning of March, the year 2020, UTC:
<div class=example>
  `2020-03-01T00:00:00Z`
</div>


### JSON Representation ### {#dt-datetime-json}

Each [=DateTime=] MUST be encoded as a JSON String.



## Data Type: <dfn>ISO3166CC</dfn> ## {#dt-iso3166cc}

An ISO 3166-2 alpha-2 country code.

Example value for tue alpha-2 country code of the United States:
<div class=example>
  `US`
</div>

### JSON Representation ### {#dt-iso3166cc-json}

Each [=ISO3166CC=] MUST be encoded as a JSON String.


## Data Type: <dfn>Decimal</dfn> ## {#dt-decimal}

A dotted-decimal number.

Example values:
<div class=example>
    - `10`
    - `42.12`
    - `-182.84`
</div>

### JSON Representation ### {#dt-decimal-json}

Each Decimal MUST be encoded as a JSON String.



## Data Type: <dfn>PfId</dfn> ## {#dt-pfid}

A PfId MUST be a UUID v4 as specified in [[!RFC9562]].


### JSON Representation ### {#dt-pfid-json}

Each PfId MUST be encoded as a JSON String.

Example JSON string value:

<div class=example>
```json
"f4b1225a-bd44-4c8e-861d-079e4e1dfd69"
```
</div>
