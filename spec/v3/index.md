<!-- 
Before publishing, make sure to: 
 - Add an entry to Changelog
 - Update the DATE below
 - STATUS can be Draft|Consultation|Release
In addition, for publishing a release:
  Set STATUS Release
  Update VERSION major.minor.patch
  Update the Previous Version and TR links
-->
<pre class='metadata'>
Text Macro: DATE 20241212
Text Macro: VERSION 3.0.0
Text Macro: STATUS Draft
Title: Technical Specifications for PCF Data Exchange
TR: https://wbcsd.github.io/tr/2024/data-exchange-protocol-20241024/
Previous Version: https://wbcsd.github.io/tr/2024/data-exchange-protocol-20240410/
Level: 1
Status: LD
Shortname: data-exchange-protocol
Mailing List: pact@wbcsd.org
Editor: Gertjan Schuurmans (WBCSD), https://www.wbcsd.org, schuurmans@wbcsd.org
Former Editor: Beth Hadley (WBCSD), https://www.wbcsd.org, hadley@wbcsd.org
Former Editor: Martin Pompéry (SINE Foundation), https://sine.foundation, martin@sine.foundation
Former Editor: Cecilia Valeri (WBCSD), https://www.wbcsd.org, valeri@wbcsd.org
Former Editor: Raimundo Henriques (SINE Foundation), https://sine.foundation, raimundo@sine.foundation
Abstract: This document specifies a data model for GHG emission data at product level based on the PACT Methodology (previously Pathfinder Framework) Version 3, and a protocol for interoperable exchange of GHG emission data at product level.
Markup Shorthands: markdown yes, idl yes, dfn yes
Boilerplate: omit copyright, omit conformance
Local Boilerplate: header yes
Metadata Include: This version off
</pre>

# Introduction # {#intro}

This document contains the necessary technical foundation for the [=PACT Network=], an open and global network for emission data exchange.

The goal of this document is to enable the [=interoperable=] exchange of [=PCF|Product Carbon Footprints=] across [[#conformance|conforming]] [=host systems=].

The methodological foundation of the specification is the PACT Methodology Version 3.0, see [[!PACT-METHODOLOGY]].

## Status of This Document ## {#status}

Comments regarding this document are welcome. Please file issues directly on [GitHub](https://github.com/wbcsd/data-exchange-protocol/), or send them to [pact@wbcsd.org](mailto:pact@wbcsd.org).

This document was published by [Partnership for Carbon Transparency (PACT)](https://www.carbon-transparency.com/) after an update to the [[!PACT-METHODOLOGY|PACT Methodology]]) was made.

The technical specifications within this document are the result of consent processes by PACT members and the WBCSD.

PACT recommends the wide deployment of this specification.


## Scope ## {#scope}

The scope of this document is to reach interoperability for product-level GHG emission data exchange through the definition of a data model ([[#data-model]]) based on the [=PACT Methodology=] Version 3.0 and the definition of a HTTP REST API ([[#api]]).


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

: PACT Methodology Version 3.0 (<dfn>PACT Methodology</dfn>)
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
As the [[!PACT-METHODOLOGY|PACT Methodology Version 3.0]] provides the methodological foundations for calculating product carbon footprints (PCFs),
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
            "productIds": ["urn:pact:company:customcode:buyer-id:4321"],
            "referencePeriodStart": "2023-01-01T00:00:00Z",
            "referencePeriodEnd": "2024-01-01T00:00:00Z"
          }
          ```
        </div>
    2. If the recipient is requesting a specific geography, it should include the geographic scope accordingly
        <div class="example">
          ```json
          {
            "productIds": ["urn:pact:company:customcode:buyer-id:4321"],
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

# Product Footprint Lifecycle # {#lifecycle}

## Introduction ## {#lifecycle-intro}

<div class=note>This section is non-normative</div>

The contents of a <{ProductFootprint|Product Footprints}> can change over time. For instance when a [=data owner=] publishes an updated Product Footprint ("upstream Product Footprints") which goes into the calculation of another Product Footprint ("downstream Product Footprint").

Even without upstream changes, a downstream Product Footprint can undergo changes in its own right, for instance when calculation errors are discovered and fixed, or when secondary emission databases are updated.

This section defines how changes to Product Footprints shall be handled by [=data owners=] and communicated to [=data recipients=] through the <{ProductFootprint}> data model.

For this, [=changes=] to ProductFootprint properties are defined and classified into [=minor change=] and [=major change=] ([[#lifecycle-classification]]). Depending on the change classification,

1. [=major changes=] must result in a new ProductFootprint ([[#lifecycle-major-changes]]) made available to its [=data recipients=],
1. [=minor changes=] result in either version updates ([[#lifecycle-minor-changes]]) or new ProductFootprint creation ([[#lifecycle-major-changes]])

In addition, if a Product Footprint is no longer valid, [=data owners=] can communicate this by applying a [=minor change=] through setting the <{ProductFootprint/status}> to `Deprecated`


## Change Definition and Classification ## {#lifecycle-classification}

A <dfn>change</dfn> to a <{ProductFootprint}> is defined as a change to one or more properties of a <{ProductFootprint}>, including a change of 1 or more properties from being undefined or to no longer being defined.

A <{ProductFootprint}> with <{ProductFootprint/status}> `Deprecated` MUST NOT be [=changed=].

There are 2 classes of changes to a <{ProductFootprint}>:

: <dfn>minor change</dfn>
::
    A [=minor change=] refers to a set of 1 or more [=changes=] to attributes to a <{ProductFootprint}>, including embedded data such as <{CarbonFootprint}>, etc.

    [=minor changes=] to a <{ProductFootprint}> SHOULD BE limited to correct errors, to incorporate changes in upstream data sources, or to incorporate changes in secondary data sources.

    A [=minor change=] is limited to the following <{CarbonFootprint}> properties:
      1. <{CarbonFootprint/pCfExcludingBiogenic}>, <{CarbonFootprint/pCfIncludingBiogenic}>,
         <{CarbonFootprint/fossilCarbonContent}>, <{CarbonFootprint/biogenicCarbonContent}>,
         <{CarbonFootprint/dLucGhgEmissions}>, <{CarbonFootprint/landManagementGhgEmissions}>,
         <{CarbonFootprint/otherBiogenicGhgEmissions}>, <{CarbonFootprint/iLucGhgEmissions}>,
         <{CarbonFootprint/biogenicCarbonWithdrawal}>, <{CarbonFootprint/aircraftGhgEmissions}>,
         <{CarbonFootprint/packagingEmissionsIncluded}>, <{CarbonFootprint/packagingGhgEmissions}>,
         <{CarbonFootprint/fossilGhgEmissions}>,
         <{CarbonFootprint/biogenicCarbonContent}>, <{CarbonFootprint/primaryDataShare}>,
         <{CarbonFootprint/secondaryEmissionFactorSources}>, <{CarbonFootprint/dqi}>,
         <{CarbonFootprint/primaryDataShare}> as a result of a change resulting from upstream ProductFootprints or an update to secondary data sources
      2. as a result of changes to the description properties
          <{CarbonFootprint/boundaryProcessesDescription}>, <{CarbonFootprint/allocationRulesDescription}>,
         <{CarbonFootprint/uncertaintyAssessmentDescription}>
      4. After a change to the assurance statement <{CarbonFootprint/assurance}> from being `undefined` to being defined

    A [=minor change=] MUST NOT change the <{ProductFootprint/id}> or the scope ([[#dt-carbonfootprint-scope]]) of the <{ProductFootprint}>.

: <dfn>major change</dfn>
::
    A [=major change=] refers to a set of 1 or more [=changes=] with 1 or more changes NOT conforming to the [=minor change=] definition.

    Additionally, a [=data owner=] CAN decide to handle a [=minor change=] as a [=major change=] (see [[#lifecycle-major-changes]] for further details).

<div class=example>
  Major change example: a [=data owner=] decides to publish Product Footprints with a sub-regional geographical granularity instead of a Product Footprint with scope `Global` ([[#dt-carbonfootprint-scope]]).

  The [=host system=] of the data owner then performs the following logical steps:

  1. deprecating the current Product Footprint ([[#lifecycle-minor-changes]]) by creating a new version with status set to `Deprecated`
  2. creating 1 or more new Product Footprints for each new geographical granularity ([[#lifecycle-major-changes]]),
  3. finally, making the new Product Footprints available to its [=data recipients=]

</div>

<div class=example>
  Minor change example: a [=data owner=] received an updated upstream Product Footprint which materially updates the <{CarbonFootprint/fossilGhgEmissions}> of one of its own Product Footprints.

  The [=host system=] of the data owner then performs the following logical steps:

  1. incorporating the <{CarbonFootprint/fossilGhgEmissions}> of the downstream Product Footprint into its Product Footprint
  2. creating a new version of the Product Footprint with the updated <{CarbonFootprint/fossilGhgEmissions}>
       by following the specification from [[#lifecycle-minor-changes]]
  3. finally, making the new Product Footprints available to its [=data recipients=]

</div>


## ProductFootprint version creation from minor changes ## {#lifecycle-minor-changes}

A [=minor change=] to a <{ProductFootprint}> MAY result in a new version of a <{ProductFootprint}>.

The [=data owner=] CAN represent a [=minor change=] to a <{ProductFootprint}> by creating 1 or more new <{ProductFootprint|ProductFootprints}> by following the specification from [[#lifecycle-major-changes]].

A version update to a <{ProductFootprint}> MUST be represented in the <{ProductFootprint}> by
1. incorporating the changes
2. incrementing <{ProductFootprint/version}> by 1 (or more)
3. setting <{ProductFootprint/updated}> to the time and date of the [=minor change=].
    If defined, <{ProductFootprint/updated}> MUST be strictly greater than the previous value of <{ProductFootprint/updated}>.
    Additionally, the value of <{ProductFootprint/updated}> MUST be strictly greater than the value of <{ProductFootprint/created}>.


## New ProductFootprint creation from major changes ## {#lifecycle-major-changes}

A [=Major change=] to 1 or more <{ProductFootprint|preceding ProductFootprints}> MUST result in

1. at least 1 new <{ProductFootprint}> being available to respective [=data recipients=]
2. for each of the preceding ProductFootprints, a new version being available to respective [=data recipients=] by
   1. following [[#lifecycle-minor-changes]]
   2. setting <{ProductFootprint/status}> to `Deprecated`

For each new ProductFootprint, the [=data owner=] MUST
1. make the necessary calculations for the new ProductFootprint
2. assign the new ProductFootprint a unique <{ProductFootprint/id}>
3. set <{ProductFootprint/updated}> to `undefined`
4. set <{ProductFootprint/precedingPfIds}> to the set of <{ProductFootprint/id}> of the 1 or more preceding ProductFootprints


# Product Identification and Classification # {#product-identifiers}

<div class=note>Non-normative</div>

To exchange PCF data between organizations, it is necessary to identify the related product or material. Given [=data owners=] and [=data recipients=] do not always (or often) use the same identification schemes, commonly and uniquely identifying the same product is a challenge - especially at scale. Given this situation, organizations must perform laborious and manual “mapping” exercises to map their identifier(s) for a product to the identify their supplier can understand.

This specification describes how the product ID URN (Uniform Resource Name) should be constructed in cases where no formal namespace for a given product identifier is defined. 

This will not eliminate the need for a mapping process but will ease mapping identifiers with a common, easily understood structure. Further, this proposal ensures interoperability with industry-specific product identifiers.

We recognize there are existing relevant namespaces and corresponding URN syntax specifications. These can either be IANA-registered namespaces (like `urn:ISBN`) or widely used standards like `urn:gtin`. When product identification based on one or more of these standards is applicable, the corresponding namespaces should be used.

Similar to product identifiers, product classifiers [=ProductClassifications=] contain URN's, using well-known namespaces when applicable, or a custom `pact` namespace if needed.


## Product Identifier URN’s ## {#product-identifier-urns}
Each ProductID MUST be a URN as specified in [[RFC8141]]. Accordingly, every URN conforms to the following syntax:

```
urn:namespace:namespace-specific-string
```

In determining which URN namespace and corresponding syntax to use, the data owner SHOULD follow the reasoning below:

1.	If an IANA-registered URN namespace exists and is applicable, this SHOULD be used. See [IANA Registered Namespaces](https://www.iana.org/assignments/urn-namespaces/urn-namespaces.xhtml) for existing specifications, like ISBN.

2.	If a widely used URN schema exists and is applicable, this SHOULD be used, for example GTIN product identifiers.

3.	If the data owner wishes to use a product identifier for which an existing URN specification does not exist, the data owner SHOULD use the following format:

    ```
    urn:pact:$domain-of-issuer$:$identifier-type$:$id$
    ```

    - `urn:pact`: is the fixed sub-string to identify the URN namespace. 

    - `$domain-of-issuer$` is the fully qualified domain name [[RFC1035]] of the organization issuing the identifier. Ideally the fully qualified domain points to the product specification. For example: `catalog.mycompany.com`

    - `$identifier-type$` defines the kind of product identifier being specified. This brings clarity to the recipient to understand what kind of identifier is provided. 

    - `$id$` is the actual id of the product within this context. This can be any string uniquely identifying the product.

    The following `$identifier-type$` values are recommended.

    <figure id="pdf-product-id-urn-entities">
    <table class="data">
    <thead>
      <tr>
        <td nowrap>`$identifier-type$`
        <td>Description
        <td>Notes
    <tbody>
      <tr>
        <td>`product-id`
        <td>Specifies a product id from a third-party organization, standard, etc. 
        <td>Use this identifier-type when no other, more specific one is applicable.
      <tr>
        <td>`buyer-id`
        <td>Specifies a product id created by the buyer, aka [=data recipient=].
        <td>This is the equivalent of "buyer-assigned" as referenced in Tech Specs V2.
      <tr>
        <td>`supplier-id`
        <td> Specifies a product id created by the supplier, aka [=data owner=].
        <td>This is the equivalent of "vendor-assigned" as referenced in Tech Specs V2.
    </table>
    </figure>

    This is a non-exhaustive list of `$identifier-type$`. This set MAY be extended in minor versions of the standard release. Organizations may contact PACT to propose additional `$identifier-type$` for consideration to be added as recommended industry-agnostic identifiers. 

    Organizations and industry initiatives are encouraged to define the relevant `$identifier-type$` for products within their industry separately. 

## Examples of Product Identifiers ## {#product-identifier-examples}

Below is a list of examples of <{ProductFootprint/productIds}> as used in the <{ProductFootprint}> data type clarifying the use of well-known and custom URN namespaces for identifying products. 

<figure id="product-id-examples">
<table class="data">
<thead>
  <tr>
    <td>Product ID type
    <td>Example
<tbody>
  <tr>
    <td>
    Company-specific
    
    Identifiers using the `pact` namespace, created by a given company for the purposes of uniquely identifying their products

    <td><div class=example>
    ```json
    ["urn:pact:sample.com:product-id:44055-9c05bc35-68f8"]
    ```</div>
    <div class=example>
    ```json
    ["urn:pact:sample-buyer.com:buyer-id:103403453"]
    ```</div>
    <div class=example>
    ```json
    ["urn:pact:sample-supplier.com:supplier-id:1234"]
    ```</div>
  <tr>
    <td>ISBN

    Well known ISBN standard, see [iana.org](https://www.iana.org/assignments/urn-formal/isbn)
    <td><div class=example>
    ```json
    ["urn:isbn:978-951-0-18435-6"]
    ```
  <tr>
    <td>GTIN (widely used)

    GTIN is not an official IANA registered namespace, however in practice it is used to specify GTINs as a URN. See [gs1.org](https://www.gs1.org/standards/id-keys/gtin)
    <td><div class=example>
    ```json
    ["urn:gtin:4712345060507"]
    ```
  <tr>
    <td>UUID

    Globally Unique Identifiers. See [[RFC9562]]
    <td><div class=example>
    ```json
    ["urn:uuid:69585GB6-56T9-6958-E526-6FDGZJHU1326"]
    ```
  <tr>
    <td>CAS Registry Number

    Unique identification number assigned to every chemical substance described in the open scientific literature See [cas.org](https://www.cas.org/cas-data/cas-registry)
    <td><div class=example>
    ```json
    ["urn:pact:cas.org:substance-number:13463-67-7"]
    ```
  <tr>
    <td>InChI (International Chemical Identifier)

    InChI is a standard identifier for chemical databases that facilitates effective information management across chemistry. See [inchi-trust.org](https://www.inchi-trust.org/)
    <td><div class=example>
    ```json
    ["urn:pact:inchi-trust.org:substance-id:$INCHI-ID$"]
    ```
  <tr>
    <td>Combined example of a substance

    Combined example of a substance (Titan Dioxide of supplier Sigmaaldrich)
    <td><div class=example>
    ```json
    ["urn:pact:sigmaaldrich.com:supplier-id:14021",
    "urn:pact:cas.org:substance-number:13463-67-7",
    "urn:pact:iupac.org:substance-name:dioxotitanium",
    "urn:pact:inchi-trust.org:substance-id:1S,/2O.Ti",
    "urn:pact:inchi-trust.org:substance-key:
    GWEVSGVZZGPLCZ-UHFFFAOYSA-N"]
    ```
</table>
</figure>


## Examples of Product Classifications ## {#product-classification-urns}

Similar to [=ProductIds=] a ProductClassification MUST be a [=URN=] as specified in [[RFC8141]]: 

```
urn:namespace:namespace-specific-string
```

In determining which URN namespace and corresponding syntax to use, the data owner SHOULD follow the reasoning below:

1.	If an IANA-registered URN namespace exists and is applicable, this SHOULD be used. See [IANA Registered Namespaces](https://www.iana.org/assignments/urn-namespaces/urn-namespaces.xhtml) for existing specifications. Example: 'urn:iso'

2.	If a widely used URN namespace exists and is applicable, this SHOULD be used.

3.	If the data owner wishes to use a product identifier for which an existing URN specification does not exist, the data owner SHOULD use the following format:

      `urn:pact:$domain-of-issuer$:$type$:$value$`

      - `urn:pact:` is the fixed sub-string to identify the URN Namespace. Based on feedback from the community we propose the use of **pact** as the recommended namespace. 

      - `$domain-of-issuer$` is the fully qualified domain name of the organization issuing the category identifier. The issuer of the code can be an organization, company or industry initiative. Example: `categories.mycompany.com`

      - `$type$` defines the kind of product category or classification being specified. This brings clarity to the recipient to understand what kind of classification is provided. 



## Product Classification Examples ## {#product-classification-examples}

<table class="data">
<thead>
<tr>
<td width="40%">Description
<td>Example
<tbody>
<tr>
  <td>Custom category

  <td><div class=example>
  ```json
  "urn:pact:catalog.company.com:category-id:550010"
  ```
  </div>
<tr>
  <td>UN Central Product Classification

  This is an international standard for 
  categorizing goods and services.
  <td><div class=example>
  (for wheat)
  ```json
  "urn:cpc:0151"
  ```
  </div>
<tr>
  <td>UN Standard Products and Services Code

  UNSPSC is a global classification system 
  for products and services, often used in procurement.
  <td><div class=example>
  (for desktop computers)
  ```json
  "urn:unspsc:43211507"
  ```
  </div>
<tr>
  <td>ECLASS

  ECLASS is a standard classification system for 
  products and services, widely used in industrial 
  and engineering contexts.
  <td><div class=example>
  ```json
  "urn:eclass:28070000"
  ```
  </div>
<tr>
  <td>ISO
  
  Used for identifying ISO standards, which include many technical standards for materials and products.

  <td><div class=example>
  ```json
  "urn:iso:std:iso:4217"
  ```
  </div>
</table>

These namespaces allow systems and standards to consistently identify and categorize products, making them useful in a variety of domains like supply chain management, retail, industrial procurement, and publication. If you’re working with a specific product categorization system, you may find these URNs particularly relevant for classification or reference purposes.
<!-- 
# Data Model # {#data-model}
-->
<pre class=include>
path: data-model.md
</pre>

<!--
# HTTP REST API # {#api}
-->
<pre class=include>
path: rest-api.md
</pre>

# Appendix A: License # {#license}

<pre class=include>
path: ../../LICENSE.md
</pre>

# Appendix B: Changelog # {#changelog}


## Version 3.0.0-20241212 (Dec 12, 2024) ## {#changelog-3.0.0}

Summary of changes:
1. Updated references to the upcoming PACT Framework 3.0 
2. Deprecation of property <{ProductFootprint/productCategoryCpc}> (ADR37)
3. Property <{ProductFootprint/comment}> now optional (ADR31)
4. Property <{CarbonFootprint/boundaryProcessesDescription}> now optional (ADR31)
5. Property <{CarbonFootprint/exemptedEmissionsDescription}> now optional (ADR31)
6. Deprecation of property <{CarbonFootprint/characterizationFactors}> (ADR28)
7. Removal of `crossSectoralStandardsUsed` which has been deprecated in 2.3 and is now superseeded by extensible crossSectoralStandards (ADR32).
8. Assurance/<{Assurance/providername}> now optional, after being mistakenly made mandatory in version 2.x
9. Consistent Decimal typing for all fractional numbers (ADR39). The data type of the following fields has been changed from Number to Decimal: `primaryDataShare`, `exemptedEmissionsPercent`, `coveragePercent`, `technologicalDQR`, `temporalDQR`, `geographicalDQR`, `completenessDQR`, `reliabilityDQR`


## Version 2.3.0 (Oct 24, 2024) ## {#changelog-2.3.0}

Release.

## Version 2.3.0-20241010 (October 10, 2024) ## {#changelog-2.3.0-20241008}
Summary of changes:
1. Sunsetting the Pathfinder name replacing Pathfinder Framework with 'PACT Methodology' and 'Pathfinder Network' with 'PACT Network'.
    Exceptions are technical id's for the Events (org.wbcsd.pathfinder.xxx) and mentions in the changelog.
2. Added chapter [[#product-identifiers]] including specification and examples for a common URN namespace syntax for <{ProductFootprint/productIds}> (ADR34)
3. Included URN namespace syntax for product classifications (ADR37)
4. Added optional property <{ProductFootprint/productClassifications}> (ADR37)
5. Advisement that property <{ProductFootprint/productCategoryCpc}> will be deprecated in version 3 (ADR37)

## Version 2.3.0-20240904 (September 4, 2024) ## {#changelog-2.3.0-20240904}
Summary of changes:
1. Replaced the term 'reporting period' with 'reference period' for consistency with the attributes <{CarbonFootprint/referencePeriodStart}> and <{CarbonFootprint/referencePeriodEnd}>.

## Version 2.3.0-20240625 (June 25, 2024) ## {#changelog-2.3.0-20240625}
Summary of changes:
1. Revision of <{ProductFootprint/productDescription}> to be more descriptive, following decision to keep attribute as mandatory
2. Indication of deprecation of `crossSectoralStandardsUsed` and introduction of <{CarbonFootprint/crossSectoralStandards}>, reflecting consensus reached on ADR32
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
2. Fix to the JSON representation specification in `crosssectoralstandardset-json`
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
