<!-- 
Before publishing, make sure to: 
 - Add an entry to Changelog
 - Update the DATE below
 - STATUS can be LD|Draft|Consultation|Release
In addition, for publishing a release:
  Set STATUS Release
  Update VERSION major.minor.patch
  Update the Previous Version and TR links
-->
<pre class='metadata'>
Text Macro: DATE 20250327
Text Macro: VERSION 3.0.0
Text Macro: STATUS LD
Title: Technical Specifications for PCF Data Exchange
TR: https://wbcsd.github.io/tr/2024/data-exchange-protocol-20241024/
Previous Version: https://wbcsd.github.io/tr/2024/data-exchange-protocol-20240410/
Level: 1
Status: LD
Shortname: data-exchange-protocol
Max ToC Depth: 2
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

<!--
Advisement: This is the Draft Release of the PACT 3.0.0 Specifications, for consultation and feedback by the PACT Members. 
-->

Advisement: This document is a work in progress and should not be used for conformance testing. 
  Please refer to the [latest stable version of the Technical Specifications](https://wbcsd.github.io/tr/2024/data-exchange-protocol-20241024/) for this.

  For an overview of changes since the last version (2.3), see the [[#changelog]].
<!--
Advisement: This document will change heavily preparing for the 3.0 draft for consultation, ETA Mid-Feb.
  All feedback is welcome.
-->

This document contains the necessary technical foundation for the [=PACT Network=], an open and global network for emission data exchange.

The goal of this document is to enable the [=interoperable=] exchange of [=PCF|Product Carbon Footprints=] across [[#conformance|conforming]] [=host systems=].

The methodological foundation of the specification is the PACT Methodology Version 3.0, see [[!PACT-METHODOLOGY]].

## Status of This Document ## {#status}

Comments regarding this document are welcome. Please file issues directly on [GitHub](https://github.com/wbcsd/data-exchange-protocol/), or send them to [pact@wbcsd.org](mailto:pact@wbcsd.org).

This document was published by [Partnership for Carbon Transparency (PACT)](https://www.carbon-transparency.org/) after an update to the [[!PACT-METHODOLOGY|PACT Methodology]] was made.

The technical specifications within this document are the result of consensus processes by PACT members and the WBCSD.

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

For further information, please refer to the [PACT website](https://www.carbon-transparency.org) and the [PACT Pathfinder Network Vision Paper](https://wbcsd.sharepoint.com/:b:/s/ClimateEnergy/EXuphu_V4FZHqG1R8sr1mz8B5bo6bhhF0DBHnWDQq-_vCQ?e=Tae0eR).


## Disclaimer ## {#disclaimer}

While PACT encourages the implementation of the technical specifications by all entities to start creating a harmonized system, neither PACT, WBCSD, nor any other individuals who contributed to the development of this document assume responsibility for any consequences or damages resulting directly or indirectly from the use of this document.


## Acknowledgements ## {#acknowledgements}

WBCSD would like to thank all PACT members, WBCSD staff, and others who shared their detailed and thoughtful input and contributed actively to the development of this document.

PACT would also like to expressly thank the 40+ solutions which implemented V2 of the PACT Technical Specifications and became conformant during 2023 and 2024, resulting in significant learnings and feedback which is now incorporated in V3.


## License ## {#section-license}

Refer to the [LICENSE](https://docs.carbon-transparency.org/license) for use of this document. 

# Terminology # {#terminology}

: <dfn>Data Model Extension</dfn>
::
    A data model extension is a set of definitions that extends the data model of this document.

    The encoding of a data model extension in the data model is specified in [[#datamodelextension]]

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
:: A WBCSD-led group of companies and organizations working together to develop a global and open network for the secure peer-to-peer exchange of accurate, primary and verified product emissions data. See [www.carbon-transparency.org](www.carbon-transparency.org) for more information.

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

: <dfn data-export>Solution Provider</dfn>
:: An entity providing technical solutions to companies by implementing and offering [=host systems=].

: <dfn data-export>Solution</dfn>
:: Any PACT-conformant software host system is called a solution.

: <dfn>UN geographic region</dfn>, <dfn>UN geographic subregion</dfn>
:: See [https://unstats.un.org/unsd/methodology/m49/](https://unstats.un.org/unsd/methodology/m49/) for details.




# Conformance # {#conformance}

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words MAY, MUST, MUST NOT, SHALL, SHALL NOT, OPTIONAL, RECOMMENDED, REQUIRED, SHOULD, and SHOULD NOT in this document are to be interpreted as described in [[!RFC2119]] [[!RFC8174]] when, and only when, they appear in all capitals, as shown here.

A conforming [=host system=] is any algorithm realized as software and/or hardware that complies with the relevant normative statements in [[#api]].

A conforming requesting [=data recipient=] is any algorithm realized as software and/or hardware that complies with the relevant normative statements in [[#api]].



# Exchanging Footprints # {#exchanging-footprints}

Note: This chapter is non-normative.

Achieving transparency in carbon emissions at the product level is challenging due to the complexity of global supply chains. This specification focuses on enabling transparency through a peer-to-peer PCF data exchange by specifying necessary aspects for achieving interoperability, such as the [Data Model](#data-model) and [API](#api).

The PACT API supports two complementary methods for exchanging carbon footprint data, each designed for different use cases. 

1. **Synchronous Retrieval**: Provides immediate access to carbon footprint data through direct API calls. This approach is ideal for:

   * On-demand access to *already existing* PCFs
   * Integration with applications requiring real-time data access
   * Scenarios where the data recipient needs only to consume data (not receive updates)


2. **Asynchronous Exchange**: Enables event-based communication where PCF data can be requested, delivered, and updated over time. This approach is suited for:

    * Situations where a PCF may not be immediately available and needs time to be calculated
    * Workflows requiring notifications when new or updated PCF data becomes available
    * Complex supply chain scenarios where data may change over time


Both methods use the same underlying data model but differ in their communication patterns and implementation requirements. 

The following sections describe each exchange method in detail, including the specific API actions, communication flows, and implementation considerations.


## Synchronous Retrieval 

The synchronous part of the PACT API allows for immediate retrieval of PCFs. Refer to [[#action-listfootprints]] and [[#action-getfootprint]] for detailed request and response formats.


### Getting multiple PCFs

The `ListFootprints` action allows for directly retrieving multiple PCFs. Starting from version 3.0, host systems
must provide filtering on a minimum set of criteria. 

1. The data recipient authenticates with the data owner.
2. The data recipient calls the `/footprints` endpoint, optionally providing a filter with search criteria and a limit to obtain a list of PCFs. 
3. After validating the request, the data owner returns a 2xx status code and the list of <{ProductFootprint}> objects. On error the data owner returns a relevant HTTP error code. For details, see [[#api]]


### Getting a single PCF

A data-recipient can directly obtain a given PCF by its ID by calling `GetFootprint`.

1. The data recipient authenticates with the data owner.
2. The data recipient calls the `/footprints/{id}` endpoint, providing the PCF ID (in UUID format)
3. If found, the data owner returns the PCF in <{ProductFootprint}> and HTTP status code 200. If not found a 404 (Not found) status code will be returned. 


## Asynchronous Exchange ## {#business-cases-async-events}

Exchanging PCFs asynchronously requires **both** the [=data owner=] **and** the [=data recipient=] to run a PACT conformant host system, **both** sides being able to initiate communication to each other.


### Requesting a PCF

Generally, the data recipient sends a `RequestCreatedEvent` event to the data owner. The data owner will try to fullfil this request and, after some time, send the a `RequestFullfilledEvent` event back to the recipient.

1. The data recipient authenticates with the data owner.
2. The data recipient sends the `RequestCreatedEvent` event to the data owner, including criteria specifying which PCF it wants to receive, like product ID, reference period or geography.
3. The data owner validates the incoming event, directly returning a HTTP 2xx success code if OK, or a 4xx status code indicating  error. 
4. Asynchronously, the data owner will create a PCF or find an existing relevant PCF. 
5. The data owner will authenticate with the data recipient and send either a `RequestFullfilledEvent` back with the PCF or a `RequestRejectedEvent` if it can not produce the PCF.


### Sending an updated PCF

At any time after a data owner has sent a PCF to the data recipient, the data owner can send an update, for example because a PCF was updated or deprecated, or a new PCF was published, see [[#lifecycle]].

In this case the data owner sends a `PublishedEvent` to the data recipient.

1. The data owner authenticates with the data recipient and sends a `PublishedEvent` with the updated or created PCF.
1. The data recipient should validate this incoming event and directly return a status code indicating succesful receipt (HTTP code 2xx) or an error (HTTP 4xx or 5xx). 

Refer to [[#action-events]] for detailed request and response formats.



# Product Footprint Lifecycle # {#lifecycle}

## Introduction ## {#lifecycle-intro}

<div class=note>This section is non-normative</div>

The contents of a <{ProductFootprint}> can change over time. For instance when a [=data owner=] publishes an updated Product Footprint ("upstream Product Footprints") which goes into the calculation of another Product Footprint ("downstream Product Footprint").

Even without upstream changes, a downstream Product Footprint can undergo changes in its own right, for instance when calculation errors are discovered and fixed, or when secondary emission databases are updated.

This section defines how changes to Product Footprints shall be handled by [=data owners=] and communicated to [=data recipients=] through the <{ProductFootprint}> data model.

Advisement: Starting with version 3.0, any change to a Product Footprint will result in a new Product Footprint with a new ID. The previous Product Footprint will be marked as `Deprecated`. The properties `version`, `updated` and `statusComment` 
are now obsolete.

## Change Definition and Handling ## {#lifecycle-handling}

A change to a Product Footprint is defined as a change to one or more properties of a <{ProductFootprint}>, including a change of properties from being undefined to defined or vice-versa.

After creation of a <{ProductFootprint}> this footprint MUST NOT be changed, EXCEPT for changing its <{ProductFootprint/status}> property to `Deprecated`

A <{ProductFootprint}> with <{ProductFootprint/status}> `Deprecated` MUST NOT be changed anymore.

### Updating PCFs

Starting with version 3.0, a change to any part of the footprint MUST result in a new footprint with a new <{ProductFootprint/id}>. The old `id` SHOULD be added to the <{ProductFootprint/PrecedingPfIds}> list to be able to track back to the previous version. The old PCF MUST have its `status` set to `Deprecated`. 

### Deprecating PCFs

If a PCF becomes obsolete the `status` property of the PCF needs to be set to `Deprecated`. Note that this is the only occasion after creation that an already existing PCF will and MUST change. 

### Obsolete Properties

Starting with version 3.0, the following properties are now obsolete and have been removed from the <{ProductFootprint}>L:

  - `version`
  - `updated`
  - `statusComment`

## Validity Period ## {#validity-period}

The validity period is the time interval during which the 
ProductFootprint is declared as valid for use by a receiving [=data recipient=]. 

The validity period is OPTIONAL defined by the properties <{ProductFootprint/validityPeriodStart}> (including) and <{ProductFootprint/validityPeriodEnd}> (excluding).

If a validity period is specified, it is restricted to a time window between <{CarbonFootprint/referencePeriodEnd}> and <{CarbonFootprint/referencePeriodEnd}> + 3 years:

  - If specified, <{ProductFootprint/validityPeriodStart}> MUST be greater than or equal to  <{CarbonFootprint/referencePeriodEnd}>.

  - If <{ProductFootprint/validityPeriodEnd}> is specified it MUST be less than or equal to <{CarbonFootprint/referencePeriodEnd}> + 3 years.


If *no validity period* is specified, the ProductFootprint is valid for 
**3 years** starting with <{CarbonFootprint/referencePeriodEnd}>.





# Product Identification and Classification # {#product-identifiers}

<div class=note>Non-normative</div>

To exchange PCF data between organizations, it is necessary to identify the related product or material. Given [=data owners=] and [=data recipients=] do not always (or often) use the same identification schemes, commonly and uniquely identifying the same product is a challenge - especially at scale. Given this situation, organizations must perform laborious and manual “mapping” exercises to map their identifier(s) for a product to the identify their supplier can understand.

This specification describes how the product ID URN (Uniform Resource Name) should be constructed in cases where no formal namespace for a given product identifier is defined. 

This will not eliminate the need for a mapping process but will ease mapping identifiers with a common, easily understood structure. Further, this proposal ensures interoperability with industry-specific product identifiers.

We recognize there are existing relevant namespaces and corresponding URN syntax specifications. These can either be IANA-registered namespaces (like `urn:ISBN`) or widely used standards like `urn:gtin`. When product identification based on one or more of these standards is applicable, the corresponding namespaces should be used.

Similar to product identifiers, [product classifiers](#product-classification-urns) contain URNs, using well-known namespaces when applicable, or a custom `pact` namespace if needed.


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

    This is a non-exhaustive list of `$identifier-type$`. This set MAY be extended in minor versions of the standard release. Organizations may contact PACT to propose additional `$identifier-type$` for consideration to be added as recommended industry-agnostic identifiers. 

    Organizations and industry initiatives are encouraged to define the relevant `$identifier-type$` for products within their industry separately. 

### Examples

Below is a list of examples of <{ProductFootprint/productIds}> as used in the <{ProductFootprint}> data type clarifying the use of well-known and custom URN namespaces for identifying products. 

<table class="data">
<thead>
<tr>
  <td>Product ID type
  <td>Example
<tbody>
<tr>
  <td>
  Company-specific
  
  <td>
  Identifiers using the `pact` namespace, created by a given company for the purposes of uniquely identifying their products

  ```json
  ["urn:pact:sample.com:product-id:44055-9c05bc35-68f8"]
  ["urn:pact:sample-buyer.com:buyer-id:103403453"]
  ["urn:pact:sample-supplier.com:supplier-id:1234"]
  ```
<tr>
  <td>ISBN

  <td>
  Well known ISBN standard, see [iana.org](https://www.iana.org/assignments/urn-formal/isbn)

  ```json
  ["urn:isbn:978-951-0-18435-6"]
  ```
<tr>
  <td>GTIN (widely used)

  <td>
  GTIN is not an official IANA registered namespace, however in practice it is used to specify GTINs as a URN. See [gs1.org](https://www.gs1.org/standards/id-keys/gtin)

  ```json
  ["urn:gtin:4712345060507"]
  ```
<tr>
  <td>UUID

  <td>
  Globally Unique Identifiers. See [[RFC9562]]

  ```json
  ["urn:uuid:69585GB6-56T9-6958-E526-6FDGZJHU1326"]
  ```
<tr>
  <td>Combined

  <td>
  Combined example of a substance (Titan Dioxide of supplier Sigmaaldrich)

  ```json
  ["urn:pact:sigmaaldrich.com:supplier-id:14021",
  "urn:pact:cas.org:substance-number:13463-67-7",
  "urn:pact:iupac.org:substance-name:dioxotitanium",
  "urn:pact:inchi-trust.org:substance-id:1S,/2O.Ti",
  "urn:pact:inchi-trust.org:substance-key:
  GWEVSGVZZGPLCZ-UHFFFAOYSA-N"]
  ```
</table>


## Product Classification URNs ## {#product-classification-urns}

Similar to [product identifiers](#product-identifiers) any product classification MUST be a URN as specified in [[RFC8141]]: 

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

### Examples ### {#product-classification-examples}

<table class="data">
<thead>
<tr>
  <td>Description
  <td>Example
<tbody>
<tr>
  <td>CAS Registry Number

  <td>
  Unique identification number assigned to every chemical substance described in the open scientific literature See [cas.org](https://www.cas.org/cas-data/cas-registry)

  ```json
  ["urn:pact:cas.org:substance-number:13463-67-7"]
  ```
<tr>
  <td>InChI (International Chemical Identifier)

  <td>
  InChI is a standard identifier for chemical databases that facilitates effective information management across chemistry. See [inchi-trust.org](https://www.inchi-trust.org/)

  ```json
  ["urn:pact:inchi-trust.org:substance-id:$INCHI-ID$"]
  ```
<tr>
  <td>Custom category
  <td>

  ```json
  "urn:pact:catalog.company.com:category-id:550010"
  ```
<tr>
  <td>UN Central Product Classification

  <td>
  This is an international standard for 
  categorizing goods and services.
  (for wheat)

  ```json
  "urn:cpc:0151"
  ```
<tr>
  <td>UN Standard Products and Services Code

  <td>
  UNSPSC is a global classification system 
  for products and services, often used in procurement.
  (for desktop computers)
  ```json
  "urn:unspsc:43211507"
  ```
<tr>
  <td>ECLASS

  <td>
  ECLASS is a standard classification system for 
  products and services, widely used in industrial 
  and engineering contexts.

  ```json
  "urn:eclass:28070000"
  ```
<tr>
  <td>ISO
  
  <td>
  Used for identifying ISO standards, which include many technical standards for materials and products.

  ```json
  "urn:iso:std:iso:4217"
  ```
</table>

These namespaces allow systems and standards to consistently identify and categorize products, making them useful in a variety of domains like supply chain management, retail, industrial procurement, and publication. If you’re working with a specific product categorization system, you may find these URNs particularly relevant for classification or reference purposes.


# Data Model # {#data-model}


## Introduction ## {#data-model-intro}

This section specifies a data model for [[#productfootprint|product footprints]] conforming
with the [=PACT Methodology=] Version 3.

The overall data model is designed for interactions between [=data owners=] and
[=data recipients=], to enable
(i) interoperability,
(ii) comparability of and transparency over product footprints, or
(iii) the calculation of derived <{CarbonFootprint|CarbonFootprints}> from other <{CarbonFootprint|CarbonFootprints}>.

The data model consists of the following major data types:

1. <{ProductFootprint}>: contains information to identify a product,
    plus further information such as the <{CarbonFootprint}>
2. <{CarbonFootprint}>: contains information related to the carbon footprint
    of a product.
3. <{DataModelExtension}>: contains additional information beyond the data model
    specified in this document.

Additional uses of the data model are supported through the concept of
[=Data Model Extensions=]. These allow [=data owners=] to add
further information to a <{ProductFootprint}>.

## Validation

This specification defines two distinct validation layers that serve different purposes:

1. [**OpenAPI Schema Definition**](#openapi-schema) - The schema definition for the data model API specify the technical requirements for machine-to-machine communication and exchange of PCFs. Software implementations MUST adhere to these requirements for interoperability. 

2. [**PACT Methodology Reporting Rules**](#reporting-rules) - A set of business rules that guide what data should be included to properly follow carbon reporting practices. These rules indicate which properties are expected to be filled in according to the [=PACT Methodology=].

A conformant software implementation MUST adhere to the OpenAPI schema for all API methods and data objects.

Additionally, implementations CAN incorporate functionality to assist end-users with following the PACT Methodology reporting rules, such as by validating inputs or signaling missing information. This logic should be implemented in the end-user facing part of the application, while inter-machine communication is governed solely by the OpenAPI schema.


## OpenAPI Schema

The data model and API actions described here are formally defined in the [[!OpenAPI]] specification available at [https://docs.carbon-transparency.org/](https://docs.carbon-transparency.org/).

The OpenAPI schema serves two critical functions:

1. It defines the complete structure of the PACT data model, including all data types, properties, and their relationships.
2. It specifies the technical requirements for API compliance, including:

   * The minimum set of properties that MUST be provided  for valid API communication
   * Required data formats and value constraints
   * Valid request and response structures for each API endpoint

Implementations MUST conform to this schema to ensure interoperability when exchanging product footprints through the REST API. The schema should be considered the authoritative technical reference for all implementation decisions related to data structure and API communication.

### Basic Types

The following basic types are used in the data model:

<table class="data">
<thead>
<th>Type
<th>Description 
<tbody>
<tr>
  <td><code>string</code>
  <td> Any string of undetermined length, including the empty string ""

  ```json
  "Sample string"
  ```
<tr>
  <td><code>string&lt;uuid&gt;</code>
  <td> String representation of a UUID, see RFC4122

  ```json
  "{91715e5e-fd0b-4d1c-8fab-76290c46e6ed}"
  ```
<tr>
  <td><code>string&lt;urn&gt;</code>
  <td> String representation of a URN, see RFC8141 
  
  ```json
  "urn:gtin:5695872369587"
  ```
<tr>
  <td><code>string&lt;decimal&gt;</code>
  <td> Non-integer numbers in the data model MUST be represented as decimal strings. 

  ```json
  "12.3456",
  "-9876.5432102"
  "1.2345e+6"
  ```
<tr>
  <td><code>integer</code>
  <td>Non-fractional numbers SHOULD be represented as integers. 

  ```json
  123,
  -456
  ```
<tr>
  <td><code>string&lt;datetime&gt;</code>
  <td> Dates MUST be formatted according to [[!ISO8601-1]]

  ```json
  "2025-04-23T18:25:43.511Z"
  ```

<tr>
  <td><code>boolean</code>
  <td> Boolean flag: <code>true</code> or <code>false</code>

  ```json
  true
  ```

</table>

 ### Qualifiers
 
Types can have the following qualifiers. Any data object send to or from the API MUST to adhere to these for interoperability between [=host systems=].

<table class="data">
<thead>
<tr>
  <th>Qualifier
  <th>Description
<tbody>
<tr>
  <td><code>Required</code>
  <td>The property MUST be provided and MUST NOT be `null`.
<tr>
  <td><code>NonEmpty</code>
  <td>The `string` or `array` MUST have a length >= 1
<tr>
  <td><code>Unique</code>
  <td>All items in an `array` MUST be unique
</table>


## PACT Methodology Reporting Rules ## {#reporting-rules}

In addition to the technical requirements defined in the OpenAPI schema, the [=PACT Methodology=] defines a set of reporting expectations for carbon footprint data. 

These rules indicate which properties SHALL, SHOULD or MAY be provided in specific reporting contexts, even if they are technically optional in the API schema.
These reporting rules are expressed using the following notation:

Where applicable, the specification below also includes information on the *unit* 
of certain properties (e.g. *kgCO2e*: kilogram CO equivalent) and if 
values are expected to be negative or positive.
 
<table><tbody>
<tr><td>
SHALL
<td>
Value is required to report on
<tr><td style="white-space: nowrap">
BIO
<td>
Required if biogenic and land sector related emissions are applicable, 0 if not applicable, blank if unknown or unavailable
<tr><td style="white-space: nowrap">
BIO-2027
<td>
Required per 31/12/2027 if biogenic and land sector related emissions are applicable , 0 if not applicable, blank if unknown or unavalaible.
<tr><td style="white-space: nowrap">
CCU
<td>
Required if CCU applicable and data known and available, blank otherwise. 
<tr><td style="white-space: nowrap">
CCS
<td>
Required if CCS applicable and data known and available, blank otherwise.
<tr><td style="white-space: nowrap">
SHOULD
<td>
Value is recommended to report on, exceptions are possible.
<tr><td>
MAY
<td>Value is optional to report on
</table>

See [=PACT Methodology=] for more details.

## Undefined Properties

In a JSON object, a property is deemed undefined if it is either not present in the object or explicitly set to `null`. For example:

```json
{
  "property1": "value1",
  "property2": null
}
```

In this example, `property2` is considered undefined. 
Also, any property not present in the object, for example `property3` is also considered `undefined`.



<pre class=include>
path: data-model.generated.md
</pre>



# HTTP REST API # {#api}

## Introduction ## {#api-intro}

This section defines an [[!rfc9112|HTTP]]-based API for the [=interoperable=] exchange of [[#productfootprint|Product Footprint]] data between [=host systems=].

The scope of the HTTP API is minimal by design. Additional features will be added in future versions of this specification.



## <dfn>Host System</dfn> ## {#api-host-system}

A host system serves the needs of a single or multiple [=data owners=]. Additionally, a host system can also serve the needs of [=data recipients=] if it retrieves data from other host systems by calling their API.

In other words, any host system which implements the API endpoints as described in this specification can play 
the role of [=data owner=] as well as of [=data recipient=], thus mirroring real-world supply chains. See [[#exchanging-footprints]] for more details.

A [=host system=] MUST implement the following actions:

 - [Action Authenticate](#api-auth)
 - [Action ListFootprints](#action-listfootprints)
 - [Action GetFootprint](#action-getfootprint)
 - [Action Events](#action-events)

The host system MUST make footprints available to the data recipient through BOTH [=Action ListFootprints=] AND [=Action Events=]. 

A host system SHOULD implement access management to control what PCFs it accepts and makes available to which [=data recipients=].

A [=host system=] MUST offer its actions over HTTPS only. 

A [=host system=] MUST authenticate any client prior to using the above actions. 

A [=host system=] SHOULD offer an [=OpenId Provider Configuration Document=] for the client to obtain the token endpoint for [Action Authenticate](#api-auth).

A [=host system=] MUST offer all actions except [Action Authenticate](#api-auth) under the same Base URL, e.g. `https://api.example.org/`, or `https://example.org/pact-api/` Note that for version 3 these actions can be found under `$base-url$/3/...`

A [=host system=] MAY offer the [=OpenId Provider Configuration Document=] or [Action Authenticate](#api-auth) under a different URL (Auth Base Url): `$auth-base-url$/.well-known/openid-configuration` or `$auth-base-url$/auth/token`. See [[#api-auth]].



## Out of scope ## {#api-host-system-out-of-scope}

<div class=note>Non-normative</div>

This standard focuses on the necessary definitions to enable interoperable data exchange between data owners and data recipients. This is mediated through a host system which implements the HTTP REST API defined in this document.

Within the [=PACT=] Project, conforming host systems are called solutions.

Solutions add further functionality on top of this standard in order to enable meaningful and interoperable data exchanges.

The following section briefly describes some of the additional functionality which is beyond the scope of this document:

<ol type="a">
  <li>Footprint calculation according to the PACT Methodology</li>
  <li>Authentication and access management: the act of deciding and setting which product footprint may be accessed by each data recipient</li>
  <li>Credentials management: the overall functionality to generate access credentials for data recipients, to exchange these credentials with data recipients, to rotate or revoke such credentials, etc.</li>
  <li>Logging: creation and storage of access logs and audit trails related to data exchange, authentication processes, etc.</li>
</ol>

## Error Handling ## {#api-error-handling}

The actions [GetFootprint](#action-getfootprint), [ListFootprints](#action-listfootprints) and [Events](#action-events) MUST return an appropriate HTTP status code and MUST include a JSON <{Error}> object with information on the error.

Error responses are specified in detail such that data recipients can understand the cause of the error, and so that potentially host systems can act on and resolve errors automatically.

Error responses from [Action Authenticate](#api-auth) follow the OAuth specification [[!rfc6750]]. See [[#api-auth]]


## Authentication Flow ## {#api-auth}

The API requires authentication using the OAuth 2.0 client credentials flow. Clients must obtain an access token before making requests to protected endpoints.

[=Host systems=] MUST implement this action in conformance with [[!rfc6749]] Section 4.4.


### Obtaining an Access Token

Clients SHOULD retrieve the token endpoint dynamically via the OpenID Connect discovery mechanism. The OpenID configuration can  be found at:

```
$auth-base-url$/.well-known/openid-configuration
```

If provided by the host system, this document contains the `token_endpoint` to be used by the client. 

If no OpenID configuration is provided by the host system, clients MUST assume `$auth-base-url$/auth/token` to be the token endpoint.

After determining the token endpoint, clients MUST obtain an access token by making a request to:

```http
POST $token-endpoint$ 
```

with the following request parameters:

 * `grant_type`: Must be set to `client_credentials`.
 * `client_id`: The client’s unique identifier.
 * `client_secret`: The client’s secret key.

Example request:

```http
POST /auth/token HTTP/1.1
Host: id.example.com
Content-Type: application/x-www-form-urlencoded
Authorization: Basic {base64(client_id:client_secret)}

grant_type=client_credentials
```

### Token Response

A successful response returns an access token in the following format:

```json
{
  "access_token": "<token>",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

If the client cannot be authenticated, the [=host system=] MUST respond with a 400 or 401 status code, and provide details on the error:

```json
{
  "error": "invalid_client",
  "error_description": "Authentication failed"
}
```

For details and possible values for `error` see [[!rfc6749]] section 5.2

### Using the Access Token

Once obtained, the access token must be included in the Authorization header of API requests, following the OAuth 2.0 Bearer Token Usage standard (RFC 6750):

```http
GET <base-url>/3/<action> HTTP/1.1
Authorization: Bearer <access_token>
```

The host system MUST check the Access Token and return a 401 when it has expired or is invalid. 

Access tokens SHOULD expire. In this case, data recipients MUST retrieve a new [access token](#obtaining-an-access-token)
as described in this section.


<pre class=include>
path: rest-api.generated.md
</pre>


# Examples # {#api-examples}

<div class=note>Non-normative</div>

## Example Action ListFootprints ## {#api-action-list-example}


<div class="example">

Request:

```http
GET /3/footprints?limit=10 HTTP/2
host: api.example.org
authorization: Bearer [BearerToken]
```

Response:
 
```http
HTTP/1.1 200 OK
date: Mon, 23 May 2025 19:33:16 GMT
content-type: application/json
content-length: 1831
link: &lt;https://api.example.org/3/footprints?limit=10&amp;offset=10&gt;; rel="next"
```
<pre class=include-code>
path: examples/list-footprints-response.json
highlight: json
</pre>

Example response body when no footprints available: 

```http
{
  "data": []
}
```

</div>

## Example Action GetFootprint ## {#api-action-get-example}

<div class="example">

Request:

```http
GET /3/footprints/91715e5e-fd0b-4d1c-8fab-76290c46e6ed HTTP/2
host: api.example.org
authorization: Bearer [BearerToken]
```

Response:

```http
HTTP/1.1 200 OK
date: Mon, 23 May 2025 19:33:16 GMT
content-type: application/json
```
<pre class=include-code>
path: examples/get-footprint-response.json
highlight: json
</pre>

</div>

## Example Error Response ## {#api-error-response-example}

<div class=example>

Example request:

```http
GET /3/footprints/91715e5e-fd0b-4d1c-8fab-76290c46e6ed HTTP/2
host: api.example.org
authorization: Bearer [BearerToken]
```

Example response:

```http
HTTP/1.1 403 Forbidden
date: Mon, 23 May 2025 19:33:16 GMT
content-type: application/json
content-length: 44
```
<pre class=include-code>
path: examples/error-response-access-denied.json
highlight: json
</pre>

</div>

## Example Action Events ## {#api-action-events-example}

Example **ProductFootprint.RequestCreated**

<div class="example">

Request:

```http
POST /3/events HTTP/1.1
host: api.example.org
authorization: Bearer [BearerToken]
content-type: application/cloudevents+json; charset=UTF-8
```
```json
{
  "type": "org.wbcsd.pact.ProductFootprint.RequestCreated.3",
  "specversion": "1.0",
  "id": "848dcf00-2c18-400d-bcb8-11e45bbf7ebd",
  "source": "//api.recipient.org/3/events",
  "time": "2024-11-06T16:23:00Z",
  "data": {
      "productId": ["urn:gtin:4712345060507"],
      "geography": ["DE"],
      "comment": "Please provide current PCF value."
  }
}
```

Response:

```http
HTTP/1.1 200 OK
content-length: 0
```

</div>

Example **ProductFootprint.RequestFulfilled**

<div class="example">

Request:

```http
POST /3/events HTTP/1.1
host: api.recipient.org
authorization: Bearer [BearerToken]
content-type: application/cloudevents+json; charset=UTF-8
```
<pre class=include-code>
path: examples/pf-response-event.json
highlight: json
</pre>

Response: 

```http
HTTP/1.1 200 OK
content-length: 0
```

</div>



# Appendix A: Changelog # {#changelog}

## Version 3.0.0 (Apr 30, 2025) ## {#changelog-3.0.0}

Summary of major changes since version 2.3:

1. **API and Documentation Improvements**  
    - Description of API methods and responses is now generated from the OpenAPI specification
    - Simplified [Host system requirements](#api-host-system)
    - Simplified [Authentication section](#api-auth)
    - Added [Error handling](#api-error-handling) section
    - Added information on retry strategy for [RequestFulfilledEvent](#request-fulfilled-event), [RequestRejectedEvent](#request-rejected-event), [PublishedEvent](#published-event)
    - Clarity on [definition of change](#lifecycle-handling)

2. **Framework and Methodology Enhancements**
    - Simplified versioning (ADR-41) included in [[#lifecycle]]
    - Simplified filtering for Sync and Async API (ADR-42)
    - Common URN structure for product ids and classification id's (ADR-34)
    - Updated references to the PACT Framework 3.0
    - Added paragraph on [[#validity-period]] to [[#lifecycle]]

3. **Carbon Accounting Model Improvements**
    - Add Biogenic Emissions and Removals (ADR-45)
    - Include attributes for CCU (Carbon Capture and Utilization) (ADR-46)
    - Consistent typing of real numbers (ADR-39)
    - Additional units for service-related footprints (ADR-40)
    - Clarification of unit of measurement and product amount (ADR-36)

4. **Data Model Changes:**
    **Properties added:**
    - <{CarbonFootprint/declaredUnitOfMeasurement}>
    - <{CarbonFootprint/declaredUnitAmount}>
    - <{CarbonFootprint/pcfExcludingBiogenicUptake}>
    - <{CarbonFootprint/pcfIncludingBiogenicUptake}>
    - <{CarbonFootprint/biogenicNonCO2Emissions}>
    - <{CarbonFootprint/biogenicCO2Uptake}>
    - <{CarbonFootprint/landUseChangeGhgEmissions}>
    - <{CarbonFootprint/landCarbonLeakage}>
    - <{CarbonFootprint/landManagementBiogenicCO2Emissions}>
    - <{CarbonFootprint/landManagementBiogenicCO2Removals}>
    - <{CarbonFootprint/landManagementFossilGhgEmissions}>
    - <{CarbonFootprint/landAreaOccupation}>
    - <{CarbonFootprint/technologicalCO2CaptureOrigin}>
    - <{CarbonFootprint/technologicalCO2Removals}>
    - <{CarbonFootprint/ccsTechnologicalCO2CaptureIncluded}>
    - <{CarbonFootprint/ccsTechnologicalCO2Capture}>
    - <{CarbonFootprint/ccuCreditCertification}>
    - <{CarbonFootprint/ccuCalculationApproach}>
    - <{CarbonFootprint/ccuCarbonContent}>
    - <{CarbonFootprint/outboundLogisticsGhgEmissions}>
    - <{CarbonFootprint/ipccCharacterizationFactors}>
    - <{CarbonFootprint/recycledCarbonContent}>
    - <{CarbonFootprint/packagingBiogenicCarbonContent}>
    - <{CarbonFootprint/verification}>

    **Properties removed:**
    - `ProductFootprint/productCategoryCpc` (deprecated in 2.3, superseded by <{ProductFootprint/productClassifications}>)
    - `ProductFootprint/statusComment`
    - `CarbonFootprint/declaredUnit` (replaced by `declaredUnitOfMeasurement`)
    - `CarbonFootprint/UnitaryProductAmount` (replaced by <{CarbonFootprint/declaredUnitAmount}>)
    - `CarbonFootprint/pCfIncludingBiogenic` (superseded by <{CarbonFootprint/pcfIncludingBiogenicUptake}>)
    - `CarbonFootprint/pCfEncludingBiogenic` (superseded by <{CarbonFootprint/pcfExcludingBiogenicUptake}>)
    - `CarbonFootprint/dLucGhgEmissions`
    - `CarbonFootprint/iLucGhgEmissions`
    - `CarbonFootprint/landManagementGhgEmissions`
    - `CarbonFootprint/biogenicCarbonWithdrawal`
    - `CarbonFootprint/otherBiogenicGhgEmissions`
    - `CarbonFootprint/crossSectoralStandardsUsed` (deprecated in 2.3, replaced by `CarbonFootprint/crossSectoralStandards`)
    - `CarbonFootprint/characterizationFactors` (deprecated in 2.2, replaced by `CarbonFootprint/ipccCharacterizationFactors`)
    - `CarbonFootprint/uncertaintyAssessmentDescription`
    - `DataQualityIndicators/coveragePercent`
    - `DataQualityIndicators/reliabilityDQR`
    - `DataQualityIndicators/completenessDQR`

    **Properties and types renamed:**
    - `CarbonFootprint/assurance` renamed to <{CarbonFootprint/verification}>

    **Properties with changed optionality:**
    - Property <{CarbonFootprint/boundaryProcessesDescription}> now optional (ADR31)
    - Property <{CarbonFootprint/exemptedEmissionsDescription}> now optional (ADR31)
    - `Assurance/providername` now optional

    **Data type changes:**
    - Consistent Decimal typing for all fractional numbers (ADR39). The following fields changed from Number to Decimal:
        - `primaryDataShare`
        - `exemptedEmissionsPercent`
        - `technologicalDQR`
        - `geographicalDQR`
        - `temporalDQR`
    - DQR ratings `technologicalDQR`, `temporalDQR`, `geographicalDQR` now range between 1 and 5



## Version 2.3.0 (Oct 24, 2024) ## {#changelog-2.3.0}

Summary of changes:

1. Rebranding: Sunset the Pathfinder name, replacing "Pathfinder Framework" with "PACT Methodology" and "Pathfinder Network" with "PACT Network".

2. Product Identifiers:

   - Added chapter [[#product-identifiers]] including specification and examples for a common URN namespace syntax for <{ProductFootprint/productIds}> (ADR34)
   - Included URN namespace syntax for product classifications (ADR37)
   - Added optional property <{ProductFootprint/productClassifications}> (ADR37)
   - Advisement that property `ProductFootprint/productCategoryCpc` will be deprecated in version 3 (ADR37)

3. Terminology and Attribute Changes:

   - Replaced the term 'reporting period' with 'reference period' for consistency with the attributes <{CarbonFootprint/referencePeriodStart}> and <{CarbonFootprint/referencePeriodEnd}>
   - Revised <{ProductFootprint/productDescription}> to be more descriptive, following decision to keep attribute as mandatory
   - Indicated deprecation of `crossSectoralStandardsUsed` and introduction of <{CarbonFootprint/crossSectoralStandards}>, reflecting consensus reached on ADR32
   - Added advisement that `piece` will be added as a `DeclaredUnit` in v3
   - Added attribute <{CarbonFootprint/productMassPerDeclaredUnit}>, per consensus reached on ADR33
   - Clarified `ProductFootprint/statusComment` attribute to include descriptive reasoning behind a given change in status


## Version 2.2.1 (June 24, 2024) ## {#changelog-2.2.1}

Summary of changes:

1. **Documentation Improvements:**
    - Added diagram with visual representation of asynchronous event processing workflow
    - Fixed [[#api-action-list-example]], [[#api-action-events-example]], [[#api-action-get-example]], and [[#exchanging-footprints-async-events]] by removing spurious `geographicScope` object
    - Fixed <{CarbonFootprint/dqi}> value types in all examples
    - Fixed <{DataQualityIndicators}> by removing misleading link to `decimal`

2. **Definition Clarifications:**
    - Clarified <{CarbonFootprint/aircraftGhgEmissions}> definition to make it explicit that radiative forcing is excluded

## Version 2.2.0 (Apr 10, 2024) ## {#changelog-2.2.0}

Summary of changes:

1. **Documentation Improvements:**
    - Addition of the new [[#exchanging-footprintss]] chapter
    - Addition of missing examples in the [[#exchanging-footprints-async-events]] section
    - Fixed the incomplete `assurance` example and moved it to the appropriate section
    - Fixed the incorrect value of `pCfExcludingBiogenic` in all relevant examples
    - Removal of notes referring to the transition from v1 to v2

2. **API and Event Processing Updates:**
    - Updates to [=Action Events=] implementation requirement - changed from OPTIONAL to MANDATORY
    - Clarification of `PF Request Event` syntax, including the instruction that the `ProductFootprintFragment` should refer to one single product
    - Addition of a recommendation to include `ProductIds` in the PF Request Event request body
    - Addition of Examples of a PCF request and response Action Event flow
    - Addition of an Example for a ProductFootprintFragment indicating a query for a PCF via productId
    - Clarification of how to handle error codes in [=Action ListFootprints=] and [=Action GetFootprints=]
    - Fixed example 28's HTTP error code (from 401 to 400) in accordance with [[!rfc6749]]

3. **Data Model Changes:**
    - Deprecation of the `CarbonFootprint/characterizationFactors` property
    - Addition of a new `CarbonFootprint/ipccCharacterizationFactorsSources` property

4. **Future Version Advisements:**
    - Addition of advisement to <{CarbonFootprint/exemptedEmissionsPercent}> stating that the upper boundary will be removed in version 3
    - Addition of advisements to properties `ProductFootprint/productCategoryCpc`, <{ProductFootprint/comment}>, <{CarbonFootprint/boundaryProcessesDescription}>, and <{CarbonFootprint/exemptedEmissionsDescription}> stating that they will become OPTIONAL in version 3


## Version 2.1.0 (Dec 07, 2023) ## {#changelog-2.1.0}

This version introduces additional mandatory functionality:

1. A new authentication flow ([[#api-auth]]) is specified which allows discovery
    of token endpoint through an [=OpenId Provider Configuration Document=].
    The flow is backwards-compatible with the 2.0.x-series of authentication flow
    based on the `/auth/token` syntax.


## Version 2.0.1 (Oct 26, 2023) ## {#changelog-2.0.1}

Summary of changes:

1. **Data Model Corrections and Clarifications:**
    - Fixed definition discrepancies between the Pathfinder Framework Version 2 and the specification:
      - <{CarbonFootprint/boundaryProcessesDescription}>: Corrected from optional to mandatory
      - <{CarbonFootprint/primaryDataShare}>: Marked as `O*` instead of `O` to align with Framework
      - <{CarbonFootprint/dqi}>: Resolved discrepancy with Framework - updated to indicate at least one of `primaryDataShare` or `dqi` must be defined (not mutually exclusive)
    - Unit corrections:
      - <{CarbonFootprint/fossilCarbonContent}>: Changed unit from `kg of CO2e / declaredUnit` to `kg / declaredUnit` and further clarified as `kgC / declaredUunit`
      - <{CarbonFootprint/biogenicCarbonContent}>: Changed unit from `kg of CO2e / declaredUnit` to `kg / declaredUnit` and further clarified as `kgC / declaredUunit`
    - Value constraint corrections:
      - `CarbonFootprint/landManagementGhgEmissions`: Fixed incorrect definition as non-negative decimal
      - `CarbonFootprint/biogenicCarbonWithdrawal`: Fixed incorrect definition as non-negative decimal, clarified must be equal to `0` or less than `0`
    - Additional clarifications to:
      - `CarbonFootprint/fossilGhgEmissions`
      - `CarbonFootprint/pCfExcludingBiogenic`
      - `CarbonFootprint/pCfIncludingBiogenic`
      - `CarbonFootprint/biogenicCarbonWithdrawal`

2. **Assurance Data Type Updates:**
    - Documentation fix to `Assurance/coverage`: Changed from mandatory (`M`) to optional (`O`)
    - Added property `Assurance/assurance` in accordance with Framework

3. **API and Documentation Improvements:**
    - Clarified error responses for [Action Authenticate](#api-auth) endpoint with example error responses following [[!rfc6749]]
    - Added references to SI Units for data type `DeclaredUnit`
    - Clarified `filter` processing semantics in [[#action-listfootprints]] with new [[#filtering]] section
    - Fixed `referencePeriod` in <a href="#filtering">Filter Example</a> 
    - Fixed typo in <{CarbonFootprint/referencePeriodEnd}> definition
    - Clarified [=host system=] requirements for HTTP error status codes when events endpoint is not implemented
    - Clarified the [=PCF=] term definition
    - Fixed linking to semantic versioning document
    - Reworded <{CarbonFootprint/referencePeriodStart}> and <{CarbonFootprint/referencePeriodEnd}>
    - Minor documentation improvements to <{ProductFootprint/status}>
    - Added an advisement to `CarbonFootprint/biogenicAccountingMethodology`
    - Updated section [[#dataqualityindicators]] to reference Table 9 of the Pathfinder Framework
    - Fixed formatting of <{ProductFootprint/productDescription}> definition

## Version 2.0.0 (Feb 20, 2023) ## {#changelog-2.0.0}

Summary of the major changes and concepts added with this version:

1. update to Pathfinder Framework Version 2.0, including data model changes which are not backwards-compatible, including
    1. addition of data type <{DataQualityIndicators}> and `Assurance` to <{CarbonFootprint}>
2. event-based communication between [=host systems=] ([[#action-events]])
3. support for data model extensions ([[#datamodelextension]])
4. life cycle management of a <{ProductFootprint}> ([[#lifecycle]])

### Data Model Changes ### {#changelog-2.0.0-data-model}

Overview of the changes to the data model compared with the data model version 1.0.1:

- changes to data type <{ProductFootprint}>:
  - properties <{ProductFootprint/validityPeriodStart}> and <{ProductFootprint/validityPeriodEnd}>: added
  - life cycle properties <{ProductFootprint/precedingPfIds}>, <{ProductFootprint/status}> and `ProductFootprint/statusComment`: added
- addition of data type <{DataQualityIndicators}> to <{CarbonFootprint}> via property <{CarbonFootprint/dqi}>
- addition of data type `Assurance` to <{CarbonFootprint}> via property `CarbonFootprint/assurance`
-  changes to data type <{CarbonFootprint}>:
  - property `CarbonFootprint/characterizationFactors`: added
  - property `CarbonFootprint/exemptedEmissionsPercent`: added
  - property `CarbonFootprint/primaryDataShare`: was mandatory is now optional
  - property `CarbonFootprint/pCfExcludingBiogenic`: added
  - property `CarbonFootprint/pCfIncludingBiogenic`: added
  - property <{CarbonFootprint/fossilCarbonContent}>: added
  - property `CarbonFootprint/biogenicCarbonWithdrawal`: added
  - property `CarbonFootprint/biogenicAccountingMethodology`: added
  - property <{CarbonFootprint/packagingEmissionsIncluded}>: added
  - property <{CarbonFootprint/exemptedEmissionsDescription}>: added
  - property <{CarbonFootprint/packagingGhgEmissions}>: added
  - property `CarbonFootprint/uncertaintyAssessmentDescription`: added
  - property `reportingPeriodStart`: renamed to <{CarbonFootprint/referencePeriodStart}>
  - property `reportingPeriodEnd`: renamed to <{CarbonFootprint/referencePeriodEnd}>
  - property `emissionFactorSources`: renamed to <{CarbonFootprint/secondaryEmissionFactorSources}>
  - property <{CarbonFootprint/aircraftGhgEmissions}>: added
- changes to data type `BiogenicEmissions`:
  - all properties moved to <{CarbonFootprint}> and the data type removed fully, plus
  - property `landUseChangeGhgEmissions` substituted with properties `CarbonFootprint/iLucGhgEmissions` and `CarbonFootprint/dLucGhgEmissions`
  - property `landUseEmissions` renamed to `CarbonFootprint/landManagementGhgEmissions`
  - property `otherEmissions` renamed to `CarbonFootprint/otherBiogenicGhgEmissions`
- data type `CompanyId`: added, including instructions on custom company codes
- changes to data type `ProductId`: addition of instructions for CAS, InChi and custom URNs.

### API Changes ### {#changelog-2.0.0-api}

- [=Action ListFootprints=]:
    1. rename of HTTP query parameter `filter` to `$filter`
    2. introduce additional allowed `$filter` operators and properties:
        - Additional operators: `eq`, `lt`, `le`, `gt`, `and`, `any`
        - Additional properties: <{ProductFootprint/created}>, `ProductFootprint/updated`, `ProductFootprint/productCategoryCpc`, <{CarbonFootprint/geographyCountry}>, <{CarbonFootprint/referencePeriodStart}>, <{CarbonFootprint/referencePeriodEnd}>, <{ProductFootprint/companyIds}>, <{ProductFootprint/productIds}>.
    3. Addition of alternative [=Action ListFootprints=] response `HttpStatusCode` 202, and pull-based request/response semantics
    4. pagination is now mandatory. See [[#pagination]]

- [=Action Events=]: section [[#action-events]] added

## Version 1.0.1 ## {#changelog-1.0.1}

The following changes have been applied for version 1.0.1

1. Addition of data type `RegionOrSubregion`, cleaning up the definition of property <{CarbonFootprint/geographyRegionOrSubregion}>
2. Fix to the JSON representation specification in `crosssectoralstandardset-json`
3. Change to the minimum size of the set <{CarbonFootprint/productOrSectorSpecificRules}> from `0` to `1`, aligning with the overall specification.
4. Removal of unreferenced data type `Boolean` from the data model section
5. Rewording, simplified wording of chapter [[#api-auth]]
6. Addition of an authentication flow specification in chapter [[#api-auth]]
7. Improved wording of request parameter `Filter` in section [[#action-listfootprints]]
8. Improved wording in section [[#api-error-handling]], specifically
    - addition of error response definition
    - improved specification of the error response JSON representation
    - consolidated specification of overall error response representation as a HTTP Response
    - improvements to previous subsection "List of error codes", plus merging into overall section [[#api-error-handling]]
    - addition of list of example situations when an error response is returned
9. Addition of Section [[#api-error-response-example]]
10. Addition of term [=interoperable=] to section [[#terminology]], plus linking to in respective sections
11. Addition of Terms [=UN geographic region=] and [=UN geographic subregion=]
12. Introduction of a new property table layout in section [[#carbonfootprint]] and [[#productfootprint]]
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
  "OPENAPI": {
    "authors": [],
    "href": "https://spec.openapis.org/oas/v3.1.1.html",
    "title": "OpenAPI Specification v3.1.1",
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
  }
}
</pre>
