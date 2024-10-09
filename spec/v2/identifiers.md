# Product Identification and Classification # {#product-identification-classification}

<div class=note>Non-normative</div>

To exchange PCF data between organizations, it is necessary to identify the related product or material. Given [=data owners=] and [=data recipients=] do not always (or often) use the same identification schemes, commonly and uniquely identifying the same product is a challenge - especially at scale. Given this situation, organizations must perform laborious and manual “mapping” exercises to map their identifier(s) for a product to the identify their supplier can understand.

This specification describes how the product ID URN (Uniform Resource Name) should be constructed in cases where no formal namespace for a given product identifier is defined. 

This will not eliminate the need for a mapping process but will ease mapping identifiers with a common, easily understood structure. Further, this proposal ensures interoperability with industry-specific product identifiers.

We recognize there are existing relevant namespaces and corresponding URN syntax specifications. These can either be IANA-registered namespaces (like `urn:ISBN`) or widely used standards like `urn:gtin`. When product identification based on one or more of these standards is applicable, the corresponding namespaces should be used.

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

## Examples ## {#product-identifier-examples}

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
    ["urn:pact:cas.org:substance-id13463-67-7"]
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
