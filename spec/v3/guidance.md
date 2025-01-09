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
