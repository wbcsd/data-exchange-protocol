<pre class='metadata'>
Title: Technical Specifications for PCF Data Exchange
Text Macro: VERSION 2.3.0-20241008
Shortname: data-exchange-protocol
Level: 1
Status: LD
Mailing List: pact@wbcsd.org
Editor: Gertjan Schuurmans (WBCSD), https://www.wbcsd.org, schuurmans@wbcsd.org
Former Editor: Beth Hadley (WBCSD), https://www.wbcsd.org, hadley@wbcsd.org
Former Editor: Martin Pompéry (SINE Foundation), https://sine.foundation, martin@sine.foundation
Former Editor: Cecilia Valeri (WBCSD), https://www.wbcsd.org, valeri@wbcsd.org
Former Editor: Raimundo Henriques (SINE Foundation), https://sine.foundation, raimundo@sine.foundation
Abstract: This document specifies a data model for GHG emission data at product level based on the PACT Methodology (previously Pathfinder Framework) Version 2, and a protocol for interoperable exchange of GHG emission data at product level.
Markup Shorthands: markdown yes, idl yes, dfn yes
Boilerplate: omit copyright, omit conformance
Local Boilerplate: header yes
Local Boilerplate: computed-metadata yes
Metadata Include: This version off
</pre>

# Introduction # {#intro}

Advisement: This document is a work in progress and should not be used for conformance testing.
  Please refer to the [latest stable version of the Technical Specifications]([LATEST]) for conformance testing.
  All feedback is welcome.

This document contains the necessary technical foundation for the [=PACT Network=], an open and global network for emission data exchange.

The goal of this document is to enable the [=interoperable=] exchange of [=PCF|Product Carbon Footprints=] across [[#conformance|conforming]] [=host systems=].

The methodological foundation of the specification is the PACT Methodology Version 2.0 ([[!PACT-METHODOLOGY]]).

## Status of This Document ## {#status}

Comments regarding this document are welcome. Please file issues directly on [GitHub](https://github.com/wbcsd/data-exchange-protocol/), or send them to [pact@wbcsd.org](mailto:pact@wbcsd.org).

This document was published by [Partnership for Carbon Transparency (PACT)](https://www.carbon-transparency.com/) after an update to the [[!PACT-METHODOLOGY|PACT Methodology]]) was made.

The technical specifications within this document are the result of consent processes by PACT members and the WBCSD.

PACT recommends the wide deployment of this specification.


## Scope ## {#scope}

The scope of this document is to reach interoperability for product-level GHG emission data exchange through the definition of a data model ([[#data-model]]) based on the [=PACT Methodology=] Version 2.0 and the definition of a HTTP REST API ([[#api]]).


## Intended Audience ## {#audience}

This technical specification is for

- software developers who want to build software for the exchange of product footprints according to the [=PACT Methodology=];
- auditors and sustainability experts who want to understand the data semantics of product footprints or how they are exchanged between partners; and
- anyone that wants to understand more about the technological foundations of the PACT Network.


## About PACT and the PACT Network ## {#about-pact}

The PACT (previously Pathfinder) Network is a concept developed by PACT and powered by the World Business Council for Sustainable Development (WBCSD). PACT is working toward the vision of an open and global network of interoperable solutions for the secure peer-to-peer exchange of accurate, primary and verified product emissions data – across all industries and value chains.

For further information, please refer to the [PACT website](https://www.carbon-transparency.com) and the [PACT Pathfinder Network Vision Paper](https://wbcsd.sharepoint.com/:b:/s/ClimateEnergy/EXuphu_V4FZHqG1R8sr1mz8B5bo6bhhF0DBHnWDQq-_vCQ?e=Tae0eR).


## Disclaimer ## {#disclaimer}

While PACT encourages the implementation of the technical specifications by all entities to start creating a harmonized system, neither PACT, WBCSD, nor any other individuals who contributed to the development of this document assume responsibility for any consequences or damages resulting directly or indirectly from the use of this document.


## Acknowledgements ## {#acknowledgements}

WBCSD would like to thank all PACT members, WBCSD staff, and others who shared their detailed and thoughtful input and contributed actively to the development of this document.

WBCSD would also like to express special thanks to the companies participating in the pilot for testing the [=interoperable=] exchange of GHG emissions data across different solutions, as well as to those [=Solution Providers=] who have contributed to this document.


## License ## {#section-license}

The license can be found in [[#license]].


# Terminology # {#terminology}

: <dfn>Data Model Extension</dfn>
::
    A data model extension is a set of definitions that extends the data model of this document.

    The encoding of a data model extension in the data model is specified in [[#dt-datamodelextension]].

    See [[!DATA-MODEL-EXTENSIONS]] and [[!EXTENSIONS-GUIDANCE]] for further details.

: <dfn>Data recipient</dfn>
:: The company requesting and/or receiving [=PCF=] data from another company, using the technical means specified in this document.

: <dfn>Data owner</dfn>
:: The company exchanging PCF data with another company, using the technical means specified in this document.

: <dfn>interoperable</dfn>
:: The quality of being able to exchange data between [=host systems=] irrespective of the vendors of the host systems, without the need for translation or transformation of the data.

: Greenhouse Gas (emissions) (<dfn>GHG</dfn>)
:: Gaseous constituents of the atmosphere, both natural and anthropogenic, that absorb and emit radiation at specific wavelengths within the spectrum of infrared radiation emitted by the Earth’s surface, its atmosphere and clouds. GHGs include CDCO₂, Methane (CH4), Nitrous Oxide(N₂O), Hydrofluoro-Carbons (HFCs), Perfluorocarbons (PFCs) and Sulfur Hexafluoride (SF6).

: <dfn>OpenId Provider Configuration Document</dfn>
:: A `OpenId Provider Configuration Document` document provided in accordance with [[!OPENID-CONNECT]] Section 4

: Partnership for Carbon Transparency (<dfn>PACT</dfn>)
:: A WBCSD-led group of companies and organizations working together to develop a global and open network for the secure peer-to-peer exchange of accurate, primary and verified product emissions data. See [www.carbon-transparency.com](www.carbon-transparency.com) for more information.

: PACT Methodology Version 2.0 (<dfn>PACT Methodology</dfn>)
:: Guidance for the Accounting and Exchange of Product Life Cycle Emissions,
    building on existing standards and protocols, such as the GHG Protocol
    Product standard. Previously named PACT Framework. 
    See [[!PACT-METHODOLOGY]] for further details.

: <dfn>PACT Network</dfn>
:: An information network (previously Pathfinder Network) of and for companies to securely exchange environmental data with each other, with an initial focus on PCF data.

: Product Carbon Footprint (<dfn>PCF</dfn>)
:: The carbon (equivalent) emissions relating to a product. Products can be any kind of item exchanged between entities, including metric or volumetric quantities of a product.
     The <{ProductFootprint}> data model is a digital representation of a PCF in accordance with the [=PACT Methodology=].

: <dfn>Solution Provider</dfn>
:: An entity providing technical solutions to companies by implementing and offering [=host systems=].

: <dfn>UN geographic region</dfn>, <dfn>UN geographic subregion</dfn>
:: See [https://unstats.un.org/unsd/methodology/m49/](https://unstats.un.org/unsd/methodology/m49/) for details.




# Conformance # {#conformance}

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words MAY, MUST, MUST NOT, OPTIONAL, RECOMMENDED, REQUIRED, SHOULD, and SHOULD NOT in this document are to be interpreted as described in [[!RFC2119]] [[!RFC8174]] when, and only when, they appear in all capitals, as shown here.

A conforming [=host system=] is any algorithm realized as software and/or hardware that complies with the relevant normative statements in [[#api]].

A conforming requesting [=data recipient=] is any algorithm realized as software and/or hardware that complies with the relevant normative statements in [[#api]].


# Guidance and Business Cases # {#business-cases}

Note: This chapter is non-normative.

Due to the complexity and nature of global supply chains, achieving transparency in carbon emissions at the product level is a challenging task.
As the [[!PACT-METHODOLOGY|PACT Methodology Version 2.0]] provides the methodological foundations for calculating product carbon footprints (PCFs),
this specification focuses on enabling transparency through a peer-to-peer PCF data exchange by specifying necessary aspects for achieving interoperability, such as the [[#data-model|data model]] and [[#api|API]].

However, these two aspects can be combined in various ways to achieve different business objectives.

This chapter serves as a guidance to the technical specifications in general by providing examples for inter-company business cases related to the exchange of [=PCFs=].
The different business cases are explained in a structured way, with business objectives presented through the lenses of interoperable data exchange processes enabled by the
different aspects of this specification.

For now, this chapter focuses on asynchronous event processing. It will be expanded with additional business cases over time.


## Asynchronous Event Processing ## {#business-cases-async-events}

### The General Principles of Event Processing ### {#business-cases-async-events-principles}

1. A host system should strive to accept an event unless for the following reasons
    1. event processing is not support by the host system
    2. the syntax in the event is not supported (e.g. when the event failed “syntax checks” of the request host system)
2. Whenever a host system's `Event` endpoint returns an error response, no follow up response event (or error event) will be sent back to the original requester
3. The requested host system will attempt to always send a response event to the requesting host
    system, **but the requesting host system should not rely on this behavior and retry after an
    appropriate amount of time by sending another new request event.**

### Business Case 1: Requesting Product Footprints ### {#business-cases-async-events-1}

#### Context and Assumptions #### {#business-cases-async-events-1-context}

- This business case is triggered by a data recipient if they wish to access a Product Footprint <strong>they could not yet access through the `ListFootprints` API</strong>.
- The data recipient and data owner have a mutually agreed upon way to identify products.

#### Workflow #### {#business-cases-async-events-1-workflow}

A graphical representation of the workflow is given below. However, this flow is for illustrative
purposes only and does not replace or otherwise alter the text below the diagram.

Note: All requests to the `/events` endpoint require authentication (omitted from the diagram
below). See [[#api-auth]] for details.

<figure>
  <img src="diagrams/events.svg" height="100%" width="100%" >
  <figcaption>Event processing workflow.</figcaption>
</figure>

1. The data recipient sends a `ProductFootprintFragment`  to the `Events Endpoint` of the data owner. The data recipient should always include 1 or more product ids in property `productIds`. The data recipient should limit each fragment to exactly 1 specific product (e.g. a specific type of apple instead of all apples that somebody is offering)
    1. If the recipient is requesting a specific reference period, it should include the reference period accordingly
        <div class="example">
          ```json
          {
            "productIds": ["urn:pact:company:customcode:buyer-assigned:4321"],
            "referencePeriodStart": "2023-01-01T00:00:00Z",
            "referencePeriodEnd": "2024-01-01T00:00:00Z"
          }
          ```
        </div>
    2. If the recipient is requesting a specific geography, it should include the geographic scope accordingly
        <div class="example">
          ```json
          {
            "productIds": ["urn:pact:company:customcode:buyer-assigned:4321"],
            "geographyCountry": "FR"
          }
          ```
        </div>
    3. If the recipient has another need that is not covered above, the data recipient should
        express it as clearly as possible to the best of their ability and following the syntactic
        rules of the data model
        1. Note: it is possible that this request will not be commonly understood by the data owner's host system

#### Cases #### {#business-cases-async-events-1-cases}

- Case 0: The solution does not support this kind of processing
    - Either because the event processing does not exit at all, or the product footprint fragment as it is submitted by the data recipient is not supported by the requested host system
    - The `events` endpoint responds with HTTP error code `400` and with a body with error code `NotImplemented`
- Case 1: A PCF does not exist (yet) or a partially matching PCF exists
    - Accept the event (HTTP Code 200 returned by the events endpoint)
    - In case of a partial match, the data owner needs to decide whether to calculate the PCF(s) or not.
        - Note: the decision making and decision making protocol for this case is up to the discretion of each data owner
    - In case the data owner decided or needs to calculate the PCF and the calculation succeeded,
        - the host system makes the newly calculated footprints also available to the data recipient through `ListFootprints`
        - the host system of the data owner sends back the 1 or more product footprints in a single event to the data requester
    - In case the data owner decided to not make additional PCFs available
        - the host system responds listing the (partially) matching PCFs
    - If the product cannot be found or otherwise identified through the product footprint fragment
        - the host system of the data owner responds with a PF Response Error Event with code `NoSuchFootprint`
    - If the PCF calculation failed for other reasons
        - the host system SHOULD send **`PF Response Error Event`** with error code `InternalError`
- Case 2: The PCF(s) exists
    - The host system accepts the event (Code 200)
    - If the data recipient does not have access to the PCF yet
        - the data owner decides on making the PCF available or not
        - if the data owner made the matching PCF(s) available, their host system returns the PCFs to the data recipient
        - otherwise, the host system of the data owner responds with a error event with error code `AccessDenied`
    - If the data recipient has access to the PCF(s)
        - the data owner responds by sending
- Default / Backup Case:
    - The host systems accepts the event (Code 200)
    - The host system sends back a `PF Response Error Event` with code `BadRequest`


# Data Model # {#data-model}

This section specifies a data model for [[#dt-pf|product footprints]] conforming
with the [=PACT Methodology=] Version 2.

The data model consists of the following major data types:

1. <{ProductFootprint}>: contains information to identify a product,
    plus further information such as the <{CarbonFootprint}> (see [[#dt-pf]])
2. <{CarbonFootprint}>: contains information related to the carbon footprint
    of a product (see [[#dt-carbonfootprint]])
3. <{DataModelExtension}>: contains additional information beyond the data model
    specified in this document.

The overall data model is designed for interactions between [=data owners=] and
[=data recipients=], to enable
(i) interoperability,
(ii) comparability of and transparency over product footprints, or
(iii) the calculation of derived <{CarbonFootprint|CarbonFootprints}> from other <{CarbonFootprint|CarbonFootprints}>.

Additional uses of the data model are supported through the concept of
[=Data Model Extensions=]. These allow [=data owners=] to add
further information to a <{ProductFootprint}>.


## Data Type: <dfn element>ProductFootprint</dfn> ## {#dt-pf}

`ProductFootprint` is a data type which represents the carbon footprint
of a product under a specific scope ([[#dt-carbonfootprint-scope]])
and with values calculated in accordance with the [=PACT Methodology=].

The objective of a `ProductFootprint` is to provide interoperability between
the creator (the [=data owner=]) and the consumer (the [=data recipient=]) of
ProductFootprints. The details on the exchange of ProductFootprints are
specified in [[#api]].

Conceptually, the data type <{ProductFootprint}> is modeled as a multi-purpose
container for product-specific emissions factors which is supported by
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
        <td>The non-empty set of [=ProductIds=]. Each of the values in the set is supposed to uniquely identify the product. What constitutes a suitable product identifier depends on the product, the conventions, contracts, and agreements between the [=Data Owner=] and a [=Data Recipient=] and is out of the scope of this specification.
  <tr>
        <td><dfn>productCategoryCpc</dfn> : [=CpcCode=]
        <td>String
        <td>M
        <td>

          Advisement: This property will become OPTIONAL in version 3 of the Technical Specifications.

          The UN Central Product Classification (CPC) that the given product belongs to.
  <tr>
        <td><dfn>productNameCompany</dfn>
        <td>String
        <td>M
        <td>The non-empty trade name of the product.
  <tr>
        <td><dfn>comment</dfn>
        <td>String
        <td>M
        <td>

          Advisement: This property will become OPTIONAL in version 3 of the Technical Specifications.

          The additional information related to the product footprint.

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
        <td>M
        <td>

          Advisement: This property is DEPRECATED and only kept to ensure backwards-compatibility. It will be removed in version 3 of these Technical Specifications. It does not replace the (also mandatory) property <{CarbonFootprint/ipccCharacterizationFactorsSources}>.

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

          Advisement: Per the Methodology the latest available characterization factor version shall be used, i.e., `["AR6"]`. In the event this is not possible, include the set of all characterization factors used.
  <tr>
        <td><dfn>crossSectoralStandardsUsed</dfn> : [=CrossSectoralStandardSet=]
        <td>Array
        <td>M
        <td>

          Advisement: This property is DEPRECATED and only kept to ensure backwards-compatibility. It will be removed in version 3 of these Technical Specifications. It does not replace the (also mandatory) property <{CarbonFootprint/crossSectoralStandards}>.

          The cross-sectoral standards applied for calculating or allocating [=GHG=] emissions
  <tr>
        <td><dfn>crossSectoralStandards</dfn>
        <td>Array of Strings
        <td>M
        <td>The cross-sectoral standards applied for calculating or allocating [=GHG=] emissions.

          It MUST be a non-empty array and MUST contain only the following values without duplicates:

        : ISO14067
        :: for the ISO 14067 Standard, "Greenhouse gases — Carbon footprint of products — Requirements and guidelines for quantification"
        : ISO14083
        :: for the ISO 14083 Standard, "Greenhouse gases — Quantification and reporting of greenhouse gas emissions arising from transport chain operations"
        : ISO14040-44
        :: for the ISO 14040-44 Standard, "Environmental management — Life cycle assessment — Principles and framework"
        : GHGP Product
        :: for the Greehouse Gas Protocol (GHGP) Product Standard
        : PEF
        :: for the EU Product Environmental Footprint Guide
        : PACT Methodology `$VERSION$`
        :: for a given version of the [=PACT Methodology=], where `$VERSION$` is the version number (1.0, 2.0, 3.0, etc.). It is recommended to use the latest version of the Methodology.
        : PAS2050
        :: for the Publicly Available Specification (PAS) 2050, "Specification for the assessment of the life cycle greenhouse gas emissions of goods and services". The use of this standard is permitted but not recommended.

          Advisement:
            The enumeration of standards above CAN evolve in future revisions. A host system MUST accept ProductFootprints from later revisions with `crossSectoralStandards` containing values that are not defined in this specification.
  <tr>
        <td><dfn>productOrSectorSpecificRules</dfn> : [=ProductOrSectorSpecificRuleSet=]
        <td>Array
        <td>O
        <td>The product-specific or sector-specific rules applied for calculating or allocating GHG emissions. If no product or sector specific rules were followed, this set MUST be empty.
  <tr>
        <td><dfn>biogenicAccountingMethodology</dfn>
        <td>String
        <td>O*
        <td>The standard followed to account for biogenic emissions and removals. If defined, the value MUST be one of the following:

          : PEF
          :: for the EU [Product Environmental Footprint Guide](https://ec.europa.eu/environment/archives/eussd/pdf/footprint/PEF%20methodology%20final%20draft.pdf)
          : ISO
          :: For the ISO 14067 standard
          : GHGP
          :: For the Greenhouse Gas Protocol (GHGP) Land sector and Removals Guidance
          : Quantis
          :: For the Quantis [Accounting for Natural Climate Solutions](https://quantis.com/report/accounting-for-natural-climate-solutions-guidance/) Guidance

          Advisement: The enumeration of standards above will be evolved in future revisions. Account for this when implementing the validation of this property.
  <tr>
        <td><dfn>boundaryProcessesDescription</dfn>
        <td>String
        <td>M
        <td>

          Advisement: This property will become OPTIONAL in version 3 of the Technical Specifications.

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
        <td>Number
        <td>M
        <td>

            Advisement: The upper boundary of this property (currently `5`) will be removed in version 3 of the Technical Specifications.

            The Percentage of emissions excluded from PCF, expressed as a decimal number between `0.0` and `5` including. See [=PACT Methodology=].
  <tr>
        <td><dfn>exemptedEmissionsDescription</dfn>
        <td>String
        <td>M
        <td>

          Advisement: This property will become OPTIONAL in version 3 of the Technical Specifications.

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
        <td><dfn>primaryDataShare</dfn> : [=Percent=]
        <td>Number
        <td>O*
        <td>
          The share of primary data in percent. See the [=PACT Methodology=] Sections 4.2.1 and 4.2.2, Appendix B.

          For reference periods ending before the beginning of year 2025, at least property <{CarbonFootprint/primaryDataShare}> or propery <{CarbonFootprint/dqi}> MUST be defined.

          For reference periods including the beginning of year 2025 or after, this property MUST be defined.
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
        <td><dfn>coveragePercent</dfn> : [=Percent=]
        <td>Number
        <td>
          Percentage of PCF included in the data quality assessment based on the `>5%` emissions threshold.
  <tr>
        <td><dfn>technologicalDQR</dfn>
        <td>Number
        <td>
          Quantitative data quality rating (DQR) based on the data quality matrix (See [=PACT Methodology=] Table 9),
          scoring the technological representativeness of the sources used for PCF calculation based on
          weighted average of all inputs representing >5% of PCF emissions.

          The value MUST be a [=decimal=] between `1` and `3` including.
  <tr>
        <td><dfn>temporalDQR</dfn>
        <td>Number
        <td>
          Quantitative data quality rating (DQR) based on the data quality matrix (Table 9),
          scoring the temporal representativeness of the sources used for PCF calculation based on
          weighted average of all inputs representing >5% of PCF emissions.

          The value MUST be between `1` and `3` inclusive.
  <tr>
        <td><dfn>geographicalDQR</dfn>
        <td>Number
        <td>
          Quantitative data quality rating (DQR) based on the data quality matrix (Table 9),
          scoring the geographical representativeness of the sources used for PCF calculation
          based on weighted average of all inputs representing >5% of PCF emissions.

          The value MUST be between `1` and `3` inclusive.
  <tr>
        <td><dfn>completenessDQR</dfn>
        <td>Number
        <td>
          Quantitative data quality rating (DQR) based on the data quality matrix (Table 9),
          scoring the completeness of the data collected for PCF calculation based on
          weighted average of all inputs representing >5% of PCF emissions.

          The value MUST be between `1` and `3` inclusive.
  <tr>
        <td><dfn>reliabilityDQR</dfn>
        <td>Number
        <td>
          Quantitative data quality rating (DQR) based on the data quality matrix (Table 9),
          scoring the reliability of the data collected for PCF calculation based on
          weighted average of all inputs representing >5% of PCF emissions.

          The value MUST be between `1` and `3` inclusive.      
  </table>
  <figcaption>Properties of data type DataQualityIndicators</figcaption>
</figure>

<div class=example>
  Example value for the case that all DQIs are known but no coverage after exemption assessment performed:
  <pre highlight=json>
  {
    "technologicalDQR": 2.0,
    "temporalDQR": 2.0,
    "geographicalDQR": 2.0,
    "completenessDQR": 2.0,
    "reliabilityDQR": 2.0
  }
  </pre>
</div>


## Data Type: <dfn element>Assurance</dfn> ## {#dt-assurance}

Data type `Assurance` contains the assurance in conformance with [=PACT Methodology=] chapter 5 and appendix B.

The following properties are defined for data type <{Assurance}>

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
    <td><dfn>assurance</dfn>
    <td>Boolean
    <td>M
    <td>
      A boolean flag indicating whether the <{CarbonFootprint}> has been
      assured in line with [=PACT Methodology=] requirements (section 5).
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

    This property MAY be undefined only if the kind of assurance was not performed
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
    <td>M
    <td>The non-empty name of the independent third party engaged to undertake the assurance.

    Advisement: Given this property was incorrectly and unintentionally published in V2 of the Technical Specifications as Mandatory, it will be reverted to Optional in version 3 of the Technical Specifications.
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
  "dataSchema": "https://catalog.carbon-transparency.com/shipment/1.0.0/data-model.json",
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



## Data Type: <dfn enum>CrossSectoralStandard</dfn> ## {#dt-crosssectoralstandard}
Advisement: This data type is DEPRECATED and will be removed in version 3 of these Technical Specifications.

CrossSectoralStandard is the enumeration of accounting standards used for product carbon footprint calculation. Valid values are

<dl dfn-type="enum-value" dfn-for="CrossSectoralStandard">

: <dfn>GHG Protocol Product standard</dfn>
:: for the GHG Protocol Product standard

: <dfn>ISO Standard 14067</dfn>
:: for ISO Standard 14067

: <dfn>ISO Standard 14044</dfn>
:: for ISO Standard 14044

</dl>

### JSON Representation ### {#dt-crosssectoralstandard-json}

Each CrossSectoralStandard MUST be encoded as a JSON string.



## Data Type: <dfn>CrossSectoralStandardSet</dfn> ## {#dt-crosssectoralstandardset}

Advisement: This data type is DEPRECATED and will be removed in version 3 of these Technical Specifications.

A set of {{CrossSectoralStandard}} values.

### JSON Representation ### {#dt-crosssectoralstandardset-json}

As an array of strings, with each string conforming to the JSON representation of {{CrossSectoralStandard}}.


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


## Data Type: <dfn>CpcCode</dfn> ## {#dt-cpccode}

A CpCode represents a UN CPC Code version 2.1 value.

Example value of the CPC code for "wood in chips or particles":
<div class="example">`31230`</div>

### JSON Representation ### {#dt-cpccode-json}

Each CpcCode MUST be encoded as a JSON String.


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

Advisement: v3 will also include the following `DeclaredUnit`: <dfn>piece</dfn>, for a piece, a unit of product

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
urn:pact:company:customcode:buyer-assigned:$custom-company-code$
```

where `$custom-company-code$` stands for the custom company code assigned by the [=data recipient=].

<div class=example>
A data owner got assigned the custom vendor code `4321` by a buyer, the value of the CompanyId is then:

`urn:pact:company:customcode:buyer-assigned:4321`.
</div>


If the [=data owner=] wishes to use its own custom company code known by
a [=data recipient=] as a [=CompanyId=] value, the [=data owner=] SHOULD use the following format:

```
urn:pact:company:customcode:vendor-assigned:$custom-company-code$
```

where `$custom-company-code$` stands for the custom company code set by the [=data recipient=].

<div class=example>
A data owner uses as custom vendor code `6789` which is known to a buyer, the value of the CompanyId is then:

`urn:pact:company:customcode:vendor-assigned:6789`.
</div>




## Data Type: <dfn>ProductIdSet</dfn> ## {#dt-productidset}

A set of [=ProductIds=] of size 1 or larger.

### JSON Representation ### {#dt-productidset-json}

Each ProductIdSet MUST be encoded as an array of strings.

## Data Type: <dfn>ProductId</dfn> ## {#dt-productid}

Each ProductId MUST be a [=URN=], see [[#product-identification-classification]] for details and examples.

## Data Type: <dfn>URN</dfn> ## {#dt-urn}

A String conforming to the [[!RFC8141|URN syntax]].

### JSON Representation ### {#dt-urn-json}

Each [=URN=] MUST be encoded as a JSON String.


## Data Type: <dfn>String</dfn> ## {#dt-string}

A regular UTF-8 String.

### JSON Data Representation ### {#dt-string-json}

Each [=String=] MUST be encoded as a JSON String.



## Data Type: <dfn>Percent</dfn> ## {#dt-percent}

A Decimal number in the range of and including `0` and `100`.

Example values:
<div class=example>
    - `100`
    - `23.0`
    - `7.183924`
    - `0.0`
</div>

### JSON Representation ### {#dt-percent-json}

Each Percent MUST be encoded in IEEE-754 [double-precision floating-point format](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) as a JSON number.



## Data Type: <dfn element>StrictlyPositiveDecimal</dfn> ## {#dt-strictlypositivedecimal}

A positive, non-zero Decimal.

Example values:
<div class=example>
    - 0.123
    - 1000
    - 42.102340
</div>

### JSON Representation ### {#dt-strictlypositivedecimal-json}

See [[[#dt-decimal-json]]].



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

<pre class=include>
path: lifecycle.md
</pre>

<pre class=include>
path: identifiers.md
</pre>

<pre class=include>
path: rest-api.md
</pre>

# Appendix A: License # {#license}

<pre class=include>
path: LICENSE.md
</pre>

# Appendix B: Changelog # {#changelog}

## Version 2.3.0-20241008 (October 8, 2024) ## {#changelog-2.3.0-20241008}
Summary of changes:
1. Sunsetting the Pathfinder name replacing Pathfinder Framework with 'PACT Methodology' and 'Pathfinder Network' with 'PACT Network'.
    Exceptions are technical id's for the Events (org.wbcsd.pathfinder.xxx) and mentions in the changelog.
2. Added chapter [[#product-identification-classification]] including specification and examples for a common URN namespace syntax for <{ProductFootprint/ProductId}>, reflecting consensus reached on ADR34.

## Version 2.3.0-20240904 (September 4, 2024) ## {#changelog-2.3.0-20240904}
Summary of changes:
1. Replaced the term 'reporting period' with 'reference period' for consistency with the attributes <{CarbonFootprint/referencePeriodStart}> and <{CarbonFootprint/referencePeriodEnd}>.

## Version 2.3.0-20240625 (June 25, 2024) ## {#changelog-2.3.0-20240625}
Summary of changes:
1. Revision of <{ProductFootprint/productDescription}> to be more descriptive, following decision to keep attribute as mandatory
2. Indication of deprecation of <{CarbonFootprint/crossSectoralStandardsUsed}> and introduction of <{CarbonFootprint/crossSectoralStandards}>, reflecting consensus reached on ADR32
3. Addition of advisement that `piece` will be added as a `DeclaredUnit` in v3; addition of attribute <{CarbonFootprint/productMassPerDeclaredUnit}>, per consensus reached on ADR33.
4. Clarification added to <{ProductFootprint/statusComment}> attribute, per consensus reached in Methodology WG, to include descriptive reasoning behind a given change in status.
5. Update contact email, Editor, and Former Editors


## Version 2.2.1-20240624 (June 24, 2024) ## {#changelog-2.2.1-20240624}

Summary of changes:
1. add diagram with visual representation of asynchronous event processing workflow

## Version 2.2.1-20240513 (May 13, 2024) ## {#changelog-2.2.1-20240513}

Summary of changes:
1. fixed [[#api-action-list-example]], [[#api-action-events-example]],
    [[#api-action-get-example]], and [[#business-cases-async-events-1-workflow]] by removing spurious
    `geographicScope` object

## Version 2.2.1-20240507 (May 7, 2024) ## {#changelog-2.2.1-20240507}

Summary of changes:
1. fixed <{CarbonFootprint/dqi}> value types in all examples
2. clarification of <{DataQualityIndicators}> by removing misleading link to [=decimal=]

## Version 2.2.1-20240430 (Apr 30, 2024) ## {#changelog-2.2.1-20240430}

Summary of changes:

1. Clarification of <{CarbonFootprint/aircraftGhgEmissions}> definition to make it explicit that
    radiative forcing is excluded.

## Version 2.2.0 (Apr 10, 2024) ## {#changelog-2.2.0}

Release.

## Version 2.2.0-20240402 (Apr 02, 2024) ## {#changelog-2.2.0-20240402}

Summary of changes:

1. removal of notes referring to the transition from v1 to v2
2. fixed the incomplete `assurance` example and moved it to the appropriate section
3. addition of missing examples in the [[#business-cases-async-events-1-workflow]] section
4. addition of advisement to <{CarbonFootprint/exemptedEmissionsPercent}> stating that the upper boundary will be removed in version 3
5. clarification of how to handle error codes in [=ListResponseBody=] and [=GetResponseBody=]

## Version 2.2.0-20240327 (Mar 27, 2024) ## {#changelog-2.2.0-20240327}

Summary of changes:

1. addition of the new [[#business-cases]] chapter
2. clarification of [=PF Request Event=] syntax, including the instruction that the
    [=ProductFootprintFragment=] should refer to one single productm
3. addition of a recommendation to include [=ProductIds=] in the PF Request Event request body
4. fixed the incorrect the value of `pCfExcludingBiogenic` in all relevant examples
5. addition of advisements to properties <{ProductFootprint/productCategoryCpc}>,
    <{ProductFootprint/comment}>, <{CarbonFootprint/boundaryProcessesDescription}>, and
    <{CarbonFootprint/exemptedEmissionsDescription}> stating that they will become OPTIONAL in
    version 3

## Version 2.2.0-20240320 (Mar 20, 2024) ## {#changelog-2.2.0-20240320}

Summary of changes:

1. fixed example 28's HTTP error code (from 401 to 400) in accordance with [[!rfc6749]]

## Version 2.2.0-20240312 (Mar 12, 2024) ## {#changelog-2.2.0-20240312}

Summary of changes:

1. deprecation of the <{CarbonFootprint/characterizationFactors}> property
2. addition of a new <{CarbonFootprint/ipccCharacterizationFactorsSources}> property
3. updates to Action [=Action Events=] implementation requirement - changed from OPTIONAL to MANDATORY
4. addition of an Example for a ProductFootprintFragment indicating a query for a PCF via productId
5. addition of Examples of a PCF request and response Action Event flow

## Version 2.1.0 (Dec 07, 2023) ## {#changelog-2.1.0}

This version introduces additional mandatory functionality:

1. A new authentication flow ([[#api-auth]]) is specified which allows discovery
    of the [=AuthEndpoint=] through an [=OpenId Provider Configuration Document=].
    The flow is backwards-compatible with the 2.0.x-series of authentication flow
    based on the [=AuthSubpath=]`/auth/token` syntax.

## Version 2.0.1-20231026 (Oct 26, 2023) ## {#changelog-2.0.1-20231026}

Summary of changes:

1. clarification of the error responses of the [=Action Authenticate=] endpoint, plus addition of an example error response in line with [[!rfc6749]]

## Version 2.0.1-20230927 (Sep 27, 2023) ## {#changelog-2.0.1-20230927}

Summary of changes:

1. definition fixes to properties <{CarbonFootprint/primaryDataShare}> and <{CarbonFootprint/dqi}> to resolve a discrepancy with the latest version of the Pathfinder Framework:
    previously, the 2 properties were defined in a mutually-exclusive fashion (either one must be defined but *NOT* both) whereas the Pathfinder Framework Version 2.0 defines them as follows (Section 4.2.1, Page 39):
    ```Initially, companies shall calculate and report, as part of PCF data exchange, on at least one of the following metrics: [...]```
2. addition of references to SI Units to data type {{DeclaredUnit}}


## Version 2.0.1-20230720 (Jul 20, 2023) ## {#changelog-2.0.1-20230720}

Summary of changes:

1. clarification to specification of property <{CarbonFootprint/fossilGhgEmissions}>, <{CarbonFootprint/pCfExcludingBiogenic}>, <{CarbonFootprint/pCfIncludingBiogenic}>, and <{CarbonFootprint/biogenicCarbonWithdrawal}>
2. in addition, further clarification on the bounds of the property <{CarbonFootprint/biogenicCarbonWithdrawal}> which must be equal to `0` or less than `0`


## Version 2.0.1-20230629 (Jun 29, 2023) ## {#changelog-2.0.1-20230629}

Summary of changes:

1. clarify unit of properties <{CarbonFootprint/fossilCarbonContent}> and <{CarbonFootprint/biogenicCarbonContent}>: was declared as `kg / declaredUnit` and is now declared as `kgC / declaredUunit`


## Version 2.0.1-20230627 (Jun 27, 2023) ## {#changelog-2.0.1-20230627}

This version fixes 5 definition incorrectness

1. property <{CarbonFootprint/fossilCarbonContent}>: was incorrectly
    defined with unit `kg of CO2e / declaredUnit`. The unit is now defined as `kg / declaredUnit`
2. fix to the `referencePeriod` <a href=#example-filter-period>Filter Example</a>
3. fixed typo in the definition of <{CarbonFootprint/referencePeriodEnd}>
4. fixed definition of <{CarbonFootprint/landManagementGhgEmissions}>: previously, it was incorrectly defined as a non-negative decimal
5. fixed definition of <{CarbonFootprint/biogenicCarbonWithdrawal}>: previously, it was incorrectly defined as a non-negative decimal


In addition, this version:

1. clarifies in [[#api-action-list]] the semantics of the [=Filter=] processing being OPTIONAL by introducing section [[#api-action-list-filtering]]
2. clarifies that a [=host system=] must return HTTP error status codes if it does not implement the events endpoint (see [[#api-action-events]])
3. clarified the [=PCF=] term definition
4. fixed linking to semantic versioning document
5. reworded <{CarbonFootprint/referencePeriodStart}> and <{CarbonFootprint/referencePeriodEnd}>


## Version 2.0.1-20230522 (May 22, 2023) ## {#changelog-2.0.1-20230522}

This version fixes 1 definition incorrectness and includes 4 documentation improvements.

1. property <{CarbonFootprint/biogenicCarbonContent}>: was incorrectly
    defined with unit `kg of CO2e / declaredUnit`. The unit is now defined as `kg / declaredUnit`
2. property <{ProductFootprint/status}>: minor documentation improvements
3. Action [=Action ListFootprints=]: minor documentation improvements
4. property <{CarbonFootprint/biogenicAccountingMethodology}>: addition of an advisement
5. section [[#dt-dataqualityindicators]] is now referencing Table 9 of the Pathfinder Framework


## Version 2.0.1-20230314 (Mar 14, 2023) ## {#changelog-2.0.1-20230314}

This version fixes 2 discrepancies between the Pathfinder Framework
Version 2 and the data model in this specification.

1. property <{CarbonFootprint/boundaryProcessesDescription}>: was incorrectly
    defined as optional in v2.0.0, and this typo is now corrected such that
    the property is correctly marked as mandatory in accordance with the
    Pathfinder Framework Version 2
2. update to definition of property <{CarbonFootprint/primaryDataShare}>:
    it was marked as optional (`O`) and is now marked as `O*`. This update is
    in accordance with the Pathfinder Framework and the field's previous
    (v2.0.0) semantics; i.e. *no* semantical update to the specification
    whatsoever
3. formatting fix to the definition of property <{ProductFootprint/productDescription}>
4. Updates to data type <{Assurance}>:
    1. documentation fix to definition of property <{Assurance/coverage}>:
        was marked as mandatory (`M`) and is now marked as `O` in accordance with its definition and the Pathfinder Framework;
        i.e. *no* semantical update to the specification whatsoever
    2. addition of property <{Assurance/assurance}> in accordance with the Pathfinder Framework


## Version 2.0.0 (Feb 20, 2023) ## {#changelog-2.0.0}

Summary of the major changes and concepts added with this version:

1. update to Pathfinder Framework Version 2.0, including data model changes which are not backwards-compatible, including
    1. addition of data type <{DataQualityIndicators}> and <{Assurance}> to <{CarbonFootprint}>
2. event-based communication between [=host systems=] ([[#api-action-events]])
3. support for data model extensions ([[#dt-datamodelextension]])
4. life cycle management of a <{ProductFootprint}> ([[#lifecycle]])

### Data Model Changes ### {#changelog-2.0.0-data-model}

Overview of the changes to the data model compared with the data model version 1.0.1:

- changes to data type <{ProductFootprint}>:
  - properties <{ProductFootprint/validityPeriodStart}> and <{ProductFootprint/validityPeriodEnd}>: added
  - life cycle properties <{ProductFootprint/precedingPfIds}>, <{ProductFootprint/status}> and <{ProductFootprint/statusComment}>: added
- addition of data type <{DataQualityIndicators}> to <{CarbonFootprint}> via property <{CarbonFootprint/dqi}>
- addition of data type <{Assurance}> to <{CarbonFootprint}> via property <{CarbonFootprint/assurance}>
-  changes to data type <{CarbonFootprint}>:
  - property <{CarbonFootprint/characterizationFactors}>: added
  - property <{CarbonFootprint/exemptedEmissionsPercent}>: added
  - property <{CarbonFootprint/primaryDataShare}>: was mandatory is now optional
  - property <{CarbonFootprint/pCfExcludingBiogenic}>: added
  - property <{CarbonFootprint/pCfIncludingBiogenic}>: added
  - property <{CarbonFootprint/fossilCarbonContent}>: added
  - property <{CarbonFootprint/biogenicCarbonWithdrawal}>: added
  - property <{CarbonFootprint/biogenicAccountingMethodology}>: added
  - property <{CarbonFootprint/packagingEmissionsIncluded}>: added
  - property <{CarbonFootprint/exemptedEmissionsDescription}>: added
  - property <{CarbonFootprint/packagingGhgEmissions}: added
  - property <{CarbonFootprint/uncertaintyAssessmentDescription}>: added
  - property `reportingPeriodStart`: renamed to <{CarbonFootprint/referencePeriodStart}>
  - property `reportingPeriodEnd`: renamed to <{CarbonFootprint/referencePeriodEnd}>
  - property `emissionFactorSources`: renamed to <{CarbonFootprint/secondaryEmissionFactorSources}>
  - property <{CarbonFootprint/aircraftGhgEmissions}>: added
- changes to data type `BiogenicEmissions`:
  - all properties moved to <{CarbonFootprint}> and the data type removed fully, plus
  - property `landUseChangeGhgEmissions` substituted with properties <{CarbonFootprint/iLucGhgEmissions}> and <{CarbonFootprint/dLucGhgEmissions}>
  - property `landUseEmissions` renamed to <{CarbonFootprint/landManagementGhgEmissions}>
  - property `otherEmissions` renamed to <{CarbonFootprint/otherBiogenicGhgEmissions}>
- data type [=CompanyId=]: added, including instructions on custom company codes
- changes to data type [=ProductId=]: addition of instructions for CAS, InChi and custom URN's.

### API Changes ### {#changelog-2.0.0-api}

- [=Action ListFootprints=]:
    1. rename of [=filter=] HTTP query parameter `filter` to `$filter`
    2. introduce additional allowed `$filter` operators and properties:
        - Additional operators: `eq`, `lt`, `le`, `gt`, `and`, `any`
        - Additional properties: <{ProductFootprint/created}>, <{ProductFootprint/updated}>, <{ProductFootprint/productCategoryCpc}>, <{CarbonFootprint/geographyCountry}>, <{CarbonFootprint/referencePeriodStart}>, <{CarbonFootprint/referencePeriodEnd}>, <{ProductFootprint/companyIds}>, <{ProductFootprint/productIds}>.
    3. Addition of alternative [=Action ListFootprints=] response `HttpStatusCode` 202, and pull-based request/response semantics
    4. pagination is now mandatory. See [[#api-action-list-pagination]]

- [=Action Events=]: section [[#api-action-events]] added

## Version 1.0.1 ## {#changelog-1.0.1}

The following changes have been applied for version 1.0.1

1. Addition of data type {{RegionOrSubregion}}, cleaning up the definition of property <{CarbonFootprint/geographyRegionOrSubregion}>
2. Fix to the JSON representation specification in [[#dt-crosssectoralstandardset-json]]
3. Change to the minimum size of the set [[#dt-productorsectorspecificruleset]] from `0` to `1`, aligning with the overall specification.
4. Removal of unreferenced data type `Boolean` from the data model section
5. Rewording, simplified wording of chapter [[#api-action-auth]]
6. Addition of an authentication flow specification in chapter [[#api-auth]]
7. Improved wording of request parameter `Filter` in section [[#api-action-list-request]]
8. Improved wording in section [[#api-error-responses]], specifically
    - addition of [=error response=] definition
    - improved specification of the [=error response=] JSON representation
    - consolidated specification of overall [=error response=] representation as a HTTP Response
    - improvements to previous subsection "List of error codes", plus merging into overall section [[#api-error-responses]]
    - addition of list of example situations when an [=error response=] is returned
9. Addition of Section [[#api-error-response-example]]
10. Addition of term [=interoperable=] to section [[#terminology]], plus linking to in respective sections
11. Addition of Terms [=UN geographic region=] and [=UN geographic subregion=]
12. Introduction of a new property table layout in section [[#dt-carbonfootprint]] and [[#dt-pf]]
13. Removal of data types `PositiveDecimal`, `SpecVersionString`, `VersionInteger`


<pre class=biblio>
{
  "CE": {
    "authors": [],
    "href": "https://github.com/cloudevents/spec",
    "title": "Cloud Events Specification",
    "status": "LS",
    "publisher": "The Linux Foundation"
  },
  "CE-JSON": {
    "authors": [],
    "href": "https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/formats/json-format.md",
    "title": "JSON Event Format for CloudEvents - Version 1.0.2",
    "status": "LS",
    "publisher": "The Linux Foundation"
  },
  "CE-Structured-Content-Mode": {
    "authors": [],
    "href": "https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/http-protocol-binding.md#32-structured-content-mode",
    "title": "HTTP Protocol Binding for CloudEvents - Version 1.0.2",
    "status": "LS",
    "publisher": "The Linux Foundation"
  },
  "PACT-METHODOLOGY": {
    "authors": [],
    "href": "https://wbcsd.github.io/tr/2023/framework-20232601/framework.pdf",
    "title": "PACT Pathfinder Framework: Guidance for the Accounting and Exchange of Product Life Cycle Emissions (Version 2.0)",
    "status": "LS",
    "publisher": "WBCSD"
  },
  "DATA-MODEL-EXTENSIONS": {
    "authors": [],
    "href": "https://wbcsd.github.io/data-model-extensions/spec/",
    "title": "Technical Specification for Data Model Extensions",
    "status": "LS",
    "publisher": "WBCSD"
  },
  "EXTENSIONS-GUIDANCE": {
    "authors": [],
    "href": "https://wbcsd.github.io/data-model-extensions/guidance/",
    "title": "Guidance and Criteria Catalog for Pathfinder Data Model Extensions",
    "status": "LS",
    "publisher": "WBCSD"
  },
  "OPENID-CONNECT": {
    "authors": [],
    "href": "https://openid.net/specs/openid-connect-discovery-1_0.html",
    "title": "OpenID Connect Discovery 1.0 incorporating errata set 1"
  },
  "SI-Unit": {
    "authors": [ "Bureau International des Poids et Mesures" ],
    "href": "https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507",
    "title": "The International System of Units (SI) – 9th edition Version 2.01"
  }
}
</pre>
