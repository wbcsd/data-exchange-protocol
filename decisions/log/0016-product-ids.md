
# 16. Additional support for vendor and product codes (nee Company and Product Ids)

Date: 2022-11-10

## Status

Accepted

## Context

### Business Context

1. Companies (SCAs) use custom vendor codes to uniquely identity companies
   1. typically, buyers of goods assign a unique custom vendor code to each supplier. They then ask their suppliers to use this in due process, but especially to use custom company codes during emission data exchange   
2. Likewise, companies use custom product codes, which can either be defined by a supplier or a buyer (or both)
3. Additionally, SCAs asked for support of the following global product identification schemes:
   1. IUPAC InChI codes[^1]
   2. CAS number[^2]

### Current Technical Specification Situation

1. The [technical specification](../../spec/index.bs) allows for custom vendor and product codes.
2. But, the technical specification does **not** detail how to encode the schemes

Since the technical specification is lacking these details, companies must negotiate this technical detail with each of their buyers / suppliers, causing interoperability issues and increases transaction costs


## Decision

1. Custom vendor codes are included in the property `companyIds` of the `ProductFootprint` data model
2. Custom product codes are included in the property `productIds` of the `ProductFootprint` data model
3. Add to the technical specification details on how to encode
   1. custom vendor and product codes
   2. IUPAC codes and CAS numbers
4. Clarify within the technical specification: a host system can include custom vendor and product codes depending on who the requester (data recipient) is.

### Encoding Details

Example vendor code encodings:

1. A vendor got assigned the custom vendor code `4321` by a buyer:  `urn:pathfinder:company:customcode:buyer-assigned:4321`
2. A buyer got assigned a custom vendor code `6789` by a vendor:  `urn:pathfinder:company:customcode:vendor-assigned:6789`


Example product code encodings:

1. A vendor got assigned the custom vendor code `1234` by a buyer:  `urn:pathfinder:product:customcode:buyer-assigned:1234`
2. A buyer got assigned a custom vendor code `8765` by a vendor:  `urn:pathfinder:product:customcode:vendor-assigned:8765`


Example encoding of ethanol with the CAS Registry Number `64-17-5`:   `urn:pathfinder:product:id:cas:64-17-5`


Example encoding of Asprin with the IUPAC InChi Code `1S/C9H8O4/c1-6(10)13-8-5-3-2-4-7(8)9(11)12/h2-5H,1H3,(H,11,12)`:  `urn:pathfinder:product:id:iupac-inchi:1S%2FC9H8O4%2Fc1-6%2810%2913-8-5-3-2-4-7%288%299%2811%2912%2Fh2-5H%2C1H3%2C%28H%2C11%2C12%29`



## Consequences

1. Product and Vendor codes use the non-official URN namespace `pathfinder`
2. Custom vendor codes do not disclose in a unique way which *entity* assigned the custom product or vendor code; hence, custom product and vendors codes, as they are encoded, are not necessarily unique.
3. Technical specification must be updated accordingly.


[^1]: see https://www.inchi-trust.org/
[^2]: also see https://www.cas.org/cas-data/cas-registry