# 34. Proposal for a common URN structure for identifying products

Date: 2024-09-10

## Status

Proposed

## Context

The proposal is still in draft stage and will require significant review and revision from community to finalize, therefore we propose to keep teh proposal in word doc format for now to enable easier editing. Once finalized, we will update this ADR accordingly.

## Context

This proposal is based on the working draft https://wbcsd.sharepoint.com/:w:/s/ClimateEnergy/ETiuwNrpFZpLvq6QLVA-lhIBlX5uYj-7UtsVgPAY1xBKjw which has been used to review and collect feedback from the community.

The Product Carbon Footprint (PCF) is calculated for specific products or materials. To exchange PCF data between organizations, it is necessary to identify the related product or material. Given suppliers and customers do not always (or often) use the same identification schemes, commonly and uniquely identifying the same product is a painful challenge - especially at scale. Given this situation, organizations commonly must perform laborious and manual “mapping” exercises to map their identifier(s) for a product to the identify their supplier can understand.  
 

This proposal introduces to the PACT Technical Specification a recommended common structure for product identifiers, further specifying how the product ID URN (Uniform Resource Name) should be specified in cases where no formal namespace for a given product identifier is defined. This proposal does not eliminate the mapping process but aims to reduce the pain of mapping identifiers with a common, easily understood structure. Further, this proposal ensures interoperability with industry-specific product identifiers, and was originally proposed by Together for Sustainability. Special thanks to Bjoern Ebeling (TfS, Merck) who contributed substantially to authoring the original proposal. 

Specific problems this proposal addresses: 
 * Interoperability: Using a common structure for product identifier URNs will support interoperability between organizations, as well as between industry networks (Catena-X, TfS, GxD, etc.) A recommended common structure helps to reduce this confusion while still providing industry-specific flexibility. 
* Increase clarity and examples: Given the PACT Tech Specs provide significant flexibility regarding which company and product identifiers may be specified, additional examples are added which bring clarity regarding how to specify these identifiers 
* Future-proofing: while not mandatory, registering a common product footprint URN namespace with IANA will enable the structure to be widely communicated across the web.
 
Scope 
 * The scope of this proposal is limited to product identifiers, although we hypothesize introducing a common structure will be useful to additional identifiers, especially company identifiers. Learnings from this proposal will inform future proposals. 
 

## Proposal

The proposal consists of four recommendations:
 1. *A common URN Structure*: Introduction of a recommended common structure for the productID URN, when no relevant IANA namespace (and corresponding specification) is applicable.
 1. *Examples*: Introduces a set of examples for productID and companyID which help the community understand how to specify URNs across a number of examples and networks (TfS, Catena-X, etc.) 
 1. *IANA Registration*: Registration  registration of the pact URN namespace with IANA

## Technical Specification

## Part 1: Common URN Structure 
This proposal introduction of a recommended common structure for the productID URN, when no relevant IANA namespace (and corresponding specification) is relevant. 
We recognize there are a number of existing product identifiers which already have an existing relevant IANA namespace and corresponding URN format specification. When such a product identifier is used for PCF exchange, this corresponding specification should be used.  

We illustrate below with several examples the two “types” of product identifiers; this proposal only applies to product identifiers which do not already have a relevant IANA scheme and therefore have no recommended URN structure. 

### 1. Existing relevant IANA scheme for product identifier
We list below relevant examples of product identifiers which fall within this category. 

|Product Identifier|Scheme|Namespace Identifier|Example|Relevant specification|
|:----|:----|:----|:----|:----|
|ISBN|urn|ISBN|URN:ISBN:978-951-0-18435-6|https://www.iana.org/assignments/urn-formal/isbn|


Note: 
GTIN is not an official IANA registered namespace, however in practice it is used to specify GTINs as a URN. This was confirmed by experts at GS1.

|Product Identifier|Scheme|Namespace Identifier|Example|Relevant specification|
|:----|:----|:----|:----|:----|
|GTIN|urn|gtin|urn:gtin:4712345060507| https://www.gs1.org/standards/id-keys/gtin|


### 2. Product identifiers without an existing relevant IANA namespace
The below identifiers may be unique product identifiers or product classification / category identifiers, all of which help identify the product.

|Product Identifier|Description|Organization|Industry|
|:----|:----|:----|:----|
|Company-specific  (custom) identifiers|Identifiers which a given company creates for the purposes of uniquely identifying their products|Company-Specific|Industry-Agnostic|
|CAS Registry Number|Unique identification number assigned to every chemical substance described in the open scientific literature|Chemical Abstracts Service (CAS)|Chemical|
| |https://www.cas.org/cas-data/cas-registry | | |
|InChI (International Chemical Identifier)|InChI is a structure-based chemical identifier, developed by IUPAC and the InChI Trust. It is a standard identifier for chemical databases that facilitates effective information management across chemistry.|Inchi Trust|Chemical|
| |https://www.inchi-trust.org/ | | |
|UN Central Product Classification Code|The Central Product Classification (CPC) consists of a coherent and consistent classification structure for products (goods and services) based on a set of internationally agreed concepts, definitions, principles and classification rules.      |UNSTATS|Industry-Agnostic|
| |https://unstats.un.org/unsd/classifications/Econ/cpc | | |
|<Additional examples here>   | | | |


### 2. PACT Common Namespace Format
Additional specification to be included in the PACT technical specification and added to the ProductID Data Type:

Each productId MUST be a URN.

If the data owner (SCA) wishes to use a product identifier for which an existing URN specification exists, the relevant specification SHOULD be used. See https://www.iana.org/assignments/urn-namespaces/urn-namespaces.xhtml for existing specifications.

If the data owner (SCA) wishes to use a product identifier for which an existing URN specification does not exist, the data owner SHOULD use the following format: 

    urn:pact:$fqdn-of-issuer$:$entity-idtype$:$id$

> See [RFC8141](https://www.rfc-editor.org/rfc/rfc8141) for URN format details.

- `urn:pact:` is the fixed sub-string to identify the URN Namespace. Based on feedback from the community we propose the use of **pact** as the recommended namespace. See below for considerations.

- `$fqdn-of-issuer$` is the fully qualified domain name of the organization issuing the identifier. The issuer of the code can be a company or an initiative (e.g., WBCSD, TFS). The fully qualified domain consists of top-level domain, domain, and sub-domain. Ideally the fully qualified domain points to the product specification. 

- `$entity-idtype$` defines the kind of product identifier being specified. This brings clarity to the recipient to understand what kind of identifier is provided, is the identifier the buyer’s identifier, the supplier’s identifier, some standard third party identifier, etc.

The following `$entity-idtype$` are recommended. 

This is a non-exhaustive list of `$entity-idtype$` . PACT will maintain a set of general, industry-agnostic `$entity-idtype$` , as below. This set may be extended in minor versions of the standard release. Organizations may contact PACT to propose additional `$entity-idtype$` for consideration to be added as recommended industry-agnostic identifiers. Organizations (especially organizations initiatives) are encouraged to define the relevant `$entity-idtype$` for products within their industry separately. 

Table: PACT Set of recommended `$entity-idtype$`

|entity-idtype |Description      |Notes             |
|--------------|-----------------|------------------|
|`product-id`    | Specifies a product id from a third-party organization, standard, etc. |Use this entity-idtype when no other more specific one is applicable.|
|`category-id`   | Indicates a category as grouping of several substances or products|Issuer for the identifier, i.e. CAS.org|
|`buyer-id`      |Specifies a product id created by the buyer, aka “data recipient”|This is the equivalent of "buyer-assigned" as referenced in Tech Specs V2.|
|`supplier-id`   | Specifies a product id created by the supplier, aka “data owner”|This is the equivalent of "vendor-assigned" as referenced in Tech Specs V2|

#### Considerations Namespace to use

As a community, we will agree on an appropriate namespace, which we could then apply to register with IANA. The basic requirements of a URN namespace are:
 - unique and descriptive
 - not be easily confused with existing namespaces
 - short and memorable, ideally reflecting the name or purpose of the organization or entity

Typically, namespace identifiers either refer to the organization which defines the given namespace (such as “ieee”, “iso”), or refers to the identifier itself (“epc”, "uuid”, “isbn”, etc.)

After having gathered feedback on two options:
- **pfi**
  pfi could stand for “PACT Footprint Identification” or “Product Footprint Identification” (depending on community preference). The namespace would include all identifiers which facilitate the exchange of product (sustainability) footprint information
- **pact**
  PACT stands for “Partnership for Carbon Transparency” and would be a namespace to indicate all identifiers relevant for the industry-agnostic exchange of product carbon footprint information.

We have landed on **pact** as the recommended namespace option. R


### Part 2: Examples

The below examples are proposed for inclusion in the PACT Tech Specs
Product ID Examples

#### Ex 1: Custom Product Ids (Product Codes)
This example would replace https://wbcsd.github.io/data-exchange-protocol/v2/#dt-productid-custom

    urn:pact:buyerfqdn.com:buyer-id:$CUSTOM-PRODUCT-CODE$
    
    urn:pact:buyer.com:buyer-id:1234
>

    urn:pact:buyerfqdn.com:supplier-id:$CUSTOM-PRODUCT-CODE$
    
    urn:pact:supplier.com:supplier-id:1234

#### Ex 2: Product ID defined by TfS
TfS platform (i.e. SiGREEN) creates UUID credentials for the PCF. With the next release, there will 
be a UUID for any entity.

    urn:pfi:sigreen.siemens.com: component-identifier:4303F98A-785F-42CD-8DE0-0B79F34FCD40

#### Ex3: Product ID defined by Catena-X
Per the Catena-X specification, productID corresponds with Industry Core manufacturerPartId. 
See full details on the [PCF Specification](https://github.com/eclipse-tractusx/sldt-semantic-models/blob/main/io.catenax.pcf/7.0.0/Pcf.ttl) and
[PartTypeInformation](https://github.com/eclipse-tractusx/sldt-semantic-models/blob/main/io.catenax.part_type_information/1.0.0/PartTypeInformation.ttl)

Per Catena-X specification, manufacturerPartID is defined as the “Part ID as assigned by 
the manufacturer of the part. The part ID identifies the part in the manufacturer`s dataspace. 
The part ID references a specific version of a part. The version number must be included in 
the part ID if it is available. The part ID does not reference a specific instance of a part 
and must not be confused with the serial number."

This specification aligns with the PACT proposal. For example 

    urn:gtin:4712345060507
is a valid URN.

#### Ex 4: Product ID defined by registries like CAS
If the data owner (SCA) wishes to use a CAS Registry Number as a ProductId value, 
the data owner SHOULD use the following format:

    urn:pact:cas.org:substance-id:$CAS-REGISTRY-NUMBER$
    urn:pact:cas.org:category-id:$CAS-REGISTRY-NUMBER$

where `$CAS-REGISTRY-NUMBER$` stands for a CAS Registry Number.
Other Registries are for example:
https://pubchem.ncbi.nlm.nih.gov/compound/26042#section=Other-Identifiers

#### Ex 5: ProductId based on IUPAC InChi identifier or key
If the data owner (SCA) wishes to use a IUPAC InChi Code as a ProductId value, the data owner SHOULD use the following format:

    urn:pact:inchi-trust.org:substance-id:$INCHI-ID$
    urn:pact:inchi-trust.org:substance-key:$INCHI-KEY$


#### Ex 6: Product ID using a UUID

    urn:uuid:69585GB6-56T9-6958-E526-6FDGZJHU1326

##### Ex 7: Product ID using a GTIN

When GTIN is a relevant identifier for a given product (and therefore PCF), the appropriate identifier to share as part of the productIDs attribute will be a URN specifying the GTIN, and not the SGTIN. This is because a GTIN identifies a specific group of identical products (single SKU), while SGTIN identifies each unit of identical products using serial numbers. E.g. a light fixture has a GTIN, and to distinguish between two identical light fixtures, they must have their own SGTIN. Therefore the GTIN should be encoded in URN form, not an SGTIN.

    urn:gtin:4712345060507

Note that “gtin” is not an official registered namespace, however upon consultation with GS1 experts, we undrstood that in practicality "gtin” is used as a namespace for specifying gtin urns. In this case, GTIN is such an established identifier that GS1 explained if you get a URN that indicates the identifier is a GTIN, then treat it like a GTIN (as simple as that!) - therefore registering "gtin” with IANA in this case isn't necessary or relevant.

#### Ex8: Combined example of a substance (Titan Dioxide of supplier Sigmaaldrich)

    urn:pact:sigmaaldrich.com:supplier-id:14021
    urn:pact:cas.org:substance-number:13463-67-7
    urn:pact:iupac.org:substance-name:dioxotitanium
    urn:pact:inchi-trust.org:substance-id:1S/2O.Ti
    urn:pact:inchi-trust.org:substance-key:GWEVSGVZZGPLCZ-UHFFFAOYSA-N 

## Part 3: Optional IANA Registration
This proposal introduces the use of a URN namespace which is not officially registered with IANA (Internet Assigned Numbers Authority). 

To ensure that adopters of the specification can use the namespace uniquely and the namespace is formally managed, PACT COULD apply to officially register the URN namespace with IANA. 

The Internet Assigned Numbers Authority (IANA) is a key organization responsible for the global coordination of the Internet’s unique identifiers. IANA ensures the smooth operation and interoperability of the Internet by maintaining a central repository of unique identifiers used in Internet protocols and other standards.

However, there are a lot of URN namespaces in widespread use which have not been formally registered with IANA. GTIN is a prime example of that. After consulting GS1, the owner of GTIN, their feedback has been that, GTIN being a widely used identifier, they have never felt the practical need to formally register the namespace.

If the PACT community decides to apply, the process is free, although requires a rigorous application process which PACT Tech WG members will be requested to contribute to. Doing this in collaboration with a number of PACT’s closet partner initiatives (TfS, Catena-X, SFC, RMI, and Green x Digital) will strengthen the application.


## Consequences

- The existing recommended URN format for custom product codes, CAS, and InChi Codes as specified in the PACT Tech Specs must be revised.
- As the proposal is a recommended format (not a required format), technically it may be introduced already in v2.3 release as it does not break backwards compatibility necessarily. However as the proposal differs from the existing recommended formats, we believe it would be less disruptive to the community to include the v3 release.
- Community should consider the value of productCategoryCpc, as CPC code may be specified as a productID, and therefore there is an opportunity to remove productCategoryCpc as an attribute in v3. 

