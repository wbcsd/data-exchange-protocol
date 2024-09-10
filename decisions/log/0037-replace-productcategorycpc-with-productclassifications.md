Date: 2024-09-10

 ## Status

 Proposed

The proposal is now in its final stages of revision, and following presentation to the PACT Tech WG September 11, a call for consensus will be conducted in the September 25 WG.

 ## Context

 This proposal is based on the working draft https://wbcsd.sharepoint.com/:w:/s/ClimateEnergy/ETiuwNrpFZpLvq6QLVA-lhIBlX5uYj-7UtsVgPAY1xBKjw which has been used to review and collect feedback from the community.

The working draft has resulted in different ADR's. ADR-0034 is the main one, proposing a URN format for productId's. This format could also be extended to product  *catogories* as well. That is being described in this ADR. 


## Proposal 

In ADR-0034 we propose a structured URN format for specifying product ID's. The `productIDs` attribute is intended to include ALL product identifiers that uniquely identify the product being sold (i.e. at the UPC / GTIN level). 

However, additional identifiers may be useful in helping to categorize or classify the product, which do not uniquely identify the product. These include for example the UN CPC code, but can also include all kind of other category identifiers. 

We believe that the format of such identifiers could likewise benefit from adopting the same URN format as proposed for the product ID's (ADR-0034), hence we propose the following:

- Deprecate `productCategoryCpc`, which is limited to *only* UN CPC codes.
- Introduce a new *optional* attribute, `productClassifications`, an *array* of URNs, where the URN format aligns to this proposal:

<br/>

    "productClassifications": [
        urn:pact:$fqdn-of-issuer$:$identifier-type$:$value$,
        ...
    ],

 - `urn:pact:` is the fixed sub-string to identify the URN Namespace. Based on feedback from the community we propose the use of **pact** as the recommended namespace. See below for considerations.

 - `$fqdn-of-issuer$` is the fully qualified domain name of the organization issuing the category identifier. The issuer of the code can be an organization, company or an initiative (e.g., UN, WBCSD, ISO). The fully qualified domain consists of top-level domain, domain, and sub-domain. Ideally the fully qualified domain points to the product specification. 

 - `$identifier-type$` defines the kind of product category identifier being specified. This brings clarity to the recipient to understand what kind of identifier is provided, is the identifier the buyer’s identifier, the supplier’s identifier, some standard third party identifier, etc.

For example:

    "productClassifications": [
      urn:pact:unstats.un.org:cpc21:31230,

    ],

Where 31230 represents the class “Wood in chips or particles” in the UN Central Product Classification (CPC) code for the product. 

## Consequences

- The attribute `productClassifications` can be added (including using CPC codes) without breaking backwards compatibility.
- The community should consider the value of `productCategoryCpc` with only CPC codes, where as these can also be included in the proposed generic URN format, together with other types of categories.
- Therefore there is an opportunity to remove productCategoryCpc as an attribute in v3.
